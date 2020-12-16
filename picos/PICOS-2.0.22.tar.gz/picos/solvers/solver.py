# coding: utf-8

# ------------------------------------------------------------------------------
# Copyright (C) 2017-2019 Maximilian Stahlberg
#
# This file is part of PICOS.
#
# PICOS is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PICOS is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# ------------------------------------------------------------------------------

"""Backend for solver interface implementations."""

from __future__ import print_function

import os
import sys
import time
from contextlib import contextmanager

from ..apidoc import api_end, api_start
from ..compat import ABC, abstractmethod
from ..formatting import solver_box
from ..modeling.solution import Solution

_API_START = api_start(globals())
# -------------------------------


class SolverError(Exception):
    """Base class for solver-specific exceptions."""

    pass


class ProblemUpdateError(SolverError):
    """Changes to the problem could not be forward to the solver.

    Raised by implementations of ``_update_problem`` to signal to the method
    ``_load_problem`` that the problem needs to be re-imported.
    """

    pass


class OptionError(SolverError):
    """Base class for solver option related errors."""

    pass


class UnsupportedOptionError(OptionError):
    """The solver does not support an option.

    Raised by implementations of ``_solve`` to signal to the user that an option
    they specified is not supported by the solver or the requested sub-solver,
    or in conjunction with the given problem type or with another option. If the
    option is valid but not supported by PICOS, then NotImplementedError should
    be raised instead. The exception is only raised if the ``strictOptions``
    option is set, otherwise a warning is printed.
    """

    pass


# TODO: Handle conflicting options globally, instead of within solver
#       implementations. (Should not inherit from SolverError then.)
class ConflictingOptionsError(OptionError):
    """Two solver options are in conflict.

    Raised by implementations of ``_solve`` to signal to the user that two
    options they specified cannot be used in conjunction.
    """

    pass


# TODO: Handle dependent options globally, instead of within solver
#       implementations. (Should not inherit from SolverError then.)
class DependentOptionError(OptionError):
    """A solver option is invalid due to another option not being set.

    Raised by implementations of ``_solve`` to signal to the user that an option
    they specified needs another option to also be set.
    """

    pass


# TODO: Handle option value errors globally, instead of within solver
#       implementations. (Should not inherit from SolverError then.)
class OptionValueError(OptionError, ValueError):
    """A solver option has an invalid value.

    Raised by implementations of ``_solve`` to signal to the user that they have
    set an option to an invalid value.
    """

    pass


# TODO: Add a write function that interfaces the solver's export to file.
# TODO: Potentially make this inherit from Reformulation.
class Solver(ABC):
    """Base class for an interface to an optimization solver."""

    # --------------------------------------------------------------------------
    # Abstract class methods.
    # --------------------------------------------------------------------------

    @classmethod
    @abstractmethod
    def supports(cls, footprint):
        """Whether a type of problem, given by footprint, is supported.

        The default implementation ensures that all reformulations required by
        user's choice have been performed before the problem is handed to the
        solver. Solver implementations are thus required to incorporate it.
        """
        if footprint.options.dualize:
            return False

        return True

    @classmethod
    @abstractmethod
    def default_penalty(cls):
        """Report the default penalty for the solver.

        See :class:`~picos.Options` for the scale.
        """
        pass

    @classmethod
    @abstractmethod
    def test_availability(cls):
        """Raise an exception if the solver is not installed on the system.

        Checks whether the solver is installed on the system, and raises an
        appropriate exception (usually :exc:`ModuleNotFoundError` or
        :exc:`ImportError`) if not. Does not return anything.
        """
        pass

    @classmethod
    @abstractmethod
    def names(cls):
        """Returns a triple ``(name, display_name, long_display_name)``."""
        pass

    # --------------------------------------------------------------------------
    # __init__ and instance properties.
    # --------------------------------------------------------------------------

    def __init__(self, problem):
        """Instanciate a solver interface with an optimization problem.

        An exception is raised when the solver is not available on the user's
        platform. No exception is raised when the problem type is not supported
        as the problem is first imported when a solution is requested.

        Solver implementations are supposed to also implement :meth:`__init__`,
        but with ``problem`` as its only positional argument, and using
        :obj:`super` to provide fixed values for this method's additional
        parameters.

        :param problem: A PICOS optimization problem.
        :type problem: :class:`Problem <picos.Problem>`
        """
        # Make sure the solver is available.
        self.test_availability()

        # The external (PICOS) problem represenation.
        # HACK: Quick and dirty conversion to accept reformulations as input.
        from ..reforms import Reformulation
        from ..modeling import Problem
        if isinstance(problem, Reformulation):
            problem.successor = self
            self.predecessor  = problem
            self._ext = None
        else:
            assert isinstance(problem, Problem)
            self._ext = problem

        # The solver's internal problem representation, which the advanced user
        # may access at their own risk.
        self.int = None

        # The last optimization objective that was imported.
        self._knownObjective = None

        # The PICOS variables that are currently imported.
        self._knownVariables = set()

        # The PICOS constraints that are currently imported.
        self._knownConstraints = set()

    @property
    def ext(self):
        """The "external" (input) problem."""
        return self._ext if self._ext else self.predecessor.output

    @property
    def name(self):
        """Keyword string of the solver."""
        return self.names()[0]

    @property
    def display_name(self):
        """Short display name of the solver."""
        return self.names()[1]

    @property
    def long_display_name(self):
        """Long display name of the solver."""
        return self.names()[2]

    # --------------------------------------------------------------------------
    # Abstract instance methods.
    # --------------------------------------------------------------------------

    @abstractmethod
    def reset_problem(self):
        """Reset the solver's internal problem representation and related data.

        Method implementations are supposed to

        - set ``int`` to None (after performing any garbage collection), and
        - reset all additional problem metadata to the state it had after
          :meth:`__init__`, in particular the data stored for
          ``_update_problem``.

        Solver implementations should not call :meth:`reset_problem` directly,
        except from within :meth:`__init__` if this is convenient.

        The user may call this method at any time if they wish to solve the
        problem from scratch.
        """
        pass

    @abstractmethod
    def _import_problem(self):
        """Convert a PICOS problem to the solver's internal representation.

        Method implementations can assume to be run directly after either
        :meth:`__init__` or :meth:`reset_problem`, and before ``_solve``. The
        method is supposed to transform only the problem formulation itself;
        solver configuration options are passed inside ``_solve`` instead.
        """
        pass

    @abstractmethod
    def _update_problem(self):
        """Update the solver's internal problem representation, if possible.

        Method implementations should make use of ``_objective_has_changed``,
        ``_new_variables``, ``_removed_variables``, ``_new_constraints`` and
        ``_removed_constraints``. Note that you can use each of the latter four
        generators only once each update as they will update the sets of known
        variables and constraints, respectively.

        Method implementations may raise

        - :exc:`NotImplementedError`, if updates to the internal problem
          instance of the solver are not supported (not at all or just not by
          PICOS), or
        - :exc:`ProblemUpdateError`, if an update to the solver's internal
          problem instance is not possible for the particular set of changes in
          the problem formulation.

        In both cases, the user will receive a warning and the problem will be
        re-imported instead of updated. In the case of
        :exc:`ProblemUpdateError`, a reason should be given and will be included
        in the warning.

        Solver implementations should not call ``_update_problem`` directly, but
        instead call ``_load_problem``.
        """
        pass

    @abstractmethod
    def _solve(self):
        """Solve the problem and return the solution.

        Method implementations can assume to be run after ``_load_problem``,
        which attempts to run ``_update_problem`` and falls back to
        ``_import_problem``. The method is supposed to pass options to the
        solver, run it within the ``_stopwatch`` context, and return the
        solution. The solution object should be created via ``_make_solution``.

        An InappropriateSolverError should be raised if the solver (or its
        requested sub-solver) does not support the given problem type.

        :returns picos.modeling.Solution: The solution found by the solver.
        """
        pass

    # --------------------------------------------------------------------------
    # Non-abstract class methods.
    # --------------------------------------------------------------------------

    @classmethod
    def penalty(cls, options):
        """Report solver penalty given an :class:`~picos.Options` object."""
        return options["penalty_{}".format(cls.names()[0])]

    @classmethod
    def available(cls, verbose=False):
        """Whether the solver is properly installed on the system."""
        try:
            cls.test_availability()
            return True
        except Exception as e:
            if verbose:
                print(e)
            return False

    @classmethod
    def predict(cls, footprint):
        """Return the solver class.

        This mimics the behavior of
        :meth:`Reformulation.predict <picos.reforms.Reformulation>` so that
        solvers can be the last pipeline node in a reformulation strategy.
        """
        return cls

    # --------------------------------------------------------------------------
    # Non-abstract instance methods (except for __init__ and properties).
    # -------------------------------------------------------------------------

    def __str__(self):
        return "# wrapper around a " + self.display_name + " problem instance #"

    def reset(self):
        """A shorthand for :meth:`reset_problem`.

        This is defined for consistency with
        :meth:`Reformulation.reset <.reformulation.Reformulation.reset>`.
        """
        self.reset_problem()

    def external_problem(self):
        """Return the external (PICOS) problem represenation."""
        return self.ext

    def internal_problem(self):
        """Return the solver's internal problem represenation."""
        return self.int

    def verbosity(self):
        """Return the problem's current verbosity level."""
        return self.ext.options.verbosity

    def _verbosity_printer(self, minLevel, message=None):
        """Print a message if the verbosity level reaches a threshold.

        :returns: Whether messages are printed.
        """
        condition = self.ext.options.verbosity >= minLevel
        if condition and message is not None:
            print(message)
        return condition

    def _warn(self, message=None):
        """Print a warning message, if the verbosity level allows for it.

        :returns: Whether warning messages are printed.
        """
        return self._verbosity_printer(0, message)

    def _verbose(self, message=None):
        """Print an informative message, if the verbosity level allows for it.

        :returns: Whether informative messages are printed.
        """
        return self._verbosity_printer(1, message)

    def _debug(self, message=None):
        """Print a debug message, if the verbosity level allows for it.

        :returns: Whether debug messages are printed.
        """
        return self._verbosity_printer(2, message)

    def _handle_unsupported_option(self, option, customMessage=None):
        """Inform the user about an unsupported option.

        The manner depends on the ``strict_options`` option; either a warning is
        printed or an exception is raised.
        """
        assert option in self.ext.options, \
            "The option '{}' does not exist.".format(option)

        if self.ext.options[option] in (None, False):
            return

        if customMessage:
            message = customMessage
        else:
            message = "{} does not support the '{}' option." \
                .format(self.display_name, option)

        if self.ext.options.strict_options:
            raise UnsupportedOptionError(message)
        else:
            self._warn(message)

    def _handle_unsupported_options(self, *options):
        """Handle a number of unsupported options at once."""
        for option in options:
            self._handle_unsupported_option(option)

    def _handle_bad_option_value(self, option, reason=None):
        """Inform the user that they set an option to an invalid value."""
        assert option in self.ext.options, \
            "The option '{}' does not exist.".format(option)
        raise OptionValueError("Invalid value '{}' for option '{}'{}"
            .format(self.ext.options[option], option,
            ": {}".format(reason) if reason else "."))

    def _handle_continuous_nonconvex_error(self, error):
        """Raise a descriptive :exc:`ArithmeticError`."""
        raise ArithmeticError("{0} refuses the problem as (continuous) "
            "nonconvex even though PICOS ensures convexity of (continuous) "
            "problems given to {0}. The most likely cause is that some "
            "quadratic form is numerically on the verge of being semidefinite, "
            "with PICOS' and {0}'s judgement differing. You could try a slight "
            "perturbation of your data such that all quadratic forms become "
            "definite. The error produced by {0} reads: {1}".format(
            self.display_name, error))

    def _load_problem(self):
        """(Re-)import or update the solver's problem state for solving."""
        # Make sure the problem is supported.
        footprint = self.ext.footprint
        assert self.supports(footprint), \
            "PICOS gave {} an unsupported problem to load: {}".format(
                self.display_name, footprint)

        # Import or update the problem.
        if self.int is None:
            self._verbose("Building a {} problem instance."
                .format(self.display_name))
            self._import_problem()
        else:
            try:
                self._verbose("Updating the {} problem instance."
                    .format(self.display_name))
                self._update_problem()
            except (NotImplementedError, ProblemUpdateError) as error:
                if type(error) is NotImplementedError:
                    reason = "Not supported with {}.".format(self.display_name)
                else:
                    reason = str(error)
                    if reason == "":
                        reason = "Unknown reason."
                self._verbose("Update failed: {}".format(reason))
                self._verbose("Rebuilding the {} problem instance."
                    .format(self.display_name))
                self.reset_problem()
                self._import_problem()

        # Remember which objective and what constraints were imported.
        self._knownObjective = self.ext.objective
        self._knownVariables = set(self.ext.variables.values())
        self._knownConstraints = set(self.ext.constraints.values())

    def _objective_has_changed(self):
        """Check for an objective function change.

        :returns: Whether the optimization objective has changed since the last
            forward or update.
        """
        assert self._knownObjective is not None, \
            "_objective_has_changed may only be used inside _update_problem."

        objectiveChanged = self._knownObjective != self.ext.objective

        if objectiveChanged:
            self._knownObjective = self.ext.objective

        return objectiveChanged

    def _new_variables(self):
        """Check for new variables.

        Yields PICOS variables that were added to the external problem
        representation since the last import or update.

        Note that variables received from this method will also be added to the
        set of known variables, so you can only iterate once within each update.
        """
        for variable in self.ext.variables.values():
            if variable not in self._knownVariables:
                self._knownVariables.add(variable)
                yield variable

    def _removed_variables(self):
        """Check for removed variables.

        Yields PICOS variables that were removed from the external problem
        representation since the last import or update.

        Note that variables received from this method will also be removed from
        the set of known variables, so you can only iterate once within each
        update.
        """
        newVariables = set(self.ext.variables.values())
        for variable in self._knownVariables:
            if variable not in newVariables:
                yield variable
        self._knownVariables.intersection_update(newVariables)

    def _new_constraints(self):
        """Check for new constraints.

        Yields PICOS constraints that were added to the external problem
        representation since the last import or update.

        Note that constraints received from this method will also be added to
        the set of known constraints, so you can only iterate once within each
        update.
        """
        for constraint in self.ext.constraints.values():
            if constraint not in self._knownConstraints:
                self._knownConstraints.add(constraint)
                yield constraint

    def _removed_constraints(self):
        """Check for removed constraints.

        Yields PICOS constraints that were removed from the external problem
        representation since the last import or update.

        Note that constraints received from this method will also be removed
        from the set of known constraints, so you can only iterate once within
        each update.
        """
        newConstraints = set(self.ext.constraints.values())
        for constraint in self._knownConstraints:
            if constraint not in newConstraints:
                yield constraint
        self._knownConstraints.intersection_update(newConstraints)

    @contextmanager
    def _stopwatch(self):
        """Store the time spent within the context in ``timer``.

        Solver implementations should use this context around the call to the
        solution routine to measure its search time.
        """
        startTime = time.time()
        yield
        endTime = time.time()
        self.timer = endTime - startTime

    def _reset_stopwatch(self):
        """Reset the timer of the ``_stopwatch`` context manager."""
        self.timer = None

    def _make_solution(self, primals, duals, primalStatus, dualStatus,
            problemStatus, info={}, vectorizedPrimals=True):
        """Create a solution problem from within :meth:`_solve`.

        Note that the default value for ``vectorizedPrimals`` is :obj:`True`,
        unlike that of
        :meth:`Solution.__init__ <picos.modeling.Solution.__init__>`. This is
        because users are expected to create manual solutions from matrix data
        while solvers usually work with the vectorized variables.
        """
        from ..modeling import Solution
        from . import get_solver_name

        assert self.timer is not None, \
            "Solvers must measure search time via _stopwatch."

        return Solution(primals, duals, self.ext, get_solver_name(self),
            primalStatus, dualStatus, problemStatus, self.timer, info,
            vectorizedPrimals)

    def execute(self):
        """Solve the problem and return the solution.

        :returns picos.Solution or list(picos.Solution): A solution object or
            list thereof.
        """
        self._load_problem()
        self._reset_stopwatch()

        self._verbose("Starting solution search.")

        solution = self._solve()

        if isinstance(solution, list):
            assert all(isinstance(s, Solution) for s in solution)
        else:
            assert isinstance(solution, Solution)

        return solution

    @contextmanager
    def _header(self, subsolver=None):
        """Print both a header and a footer."""
        with solver_box(self.long_display_name, self.display_name,
                subsolver, self._verbose()):
            yield

    @contextmanager
    def _enforced_verbosity(self, noStdOutAt=0, noStdErrAt=-1):
        """Enfoce the user-specified verbosity within the context.

        :param int noStdOutAt: Don't print to stdout at or below this verbosity.
        :param int noStdErrAt: Don't print to stderr at or below this verbosity.
        """
        verbosity = self.ext.verbosity()

        if verbosity <= max(noStdOutAt, noStdErrAt):
            devNull = open(os.devnull, "w")

        if verbosity <= noStdOutAt:
            oldOut = sys.stdout
            sys.stdout = devNull

        if verbosity <= noStdErrAt:
            oldErr = sys.sdterr
            sys.stderr = devNull

        yield

        if verbosity <= noStdOutAt:
            sys.stdout = oldOut

        if verbosity <= noStdErrAt:
            sys.stderr = oldErr


# --------------------------------------
__all__ = api_end(_API_START, globals())

# coding: utf-8

# ------------------------------------------------------------------------------
# Copyright (C) 2018-2019 Maximilian Stahlberg
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

"""Implementation of :class:`ECOSSolver`."""

import cvxopt

from ..apidoc import api_end, api_start
from ..compat import assert_import_exists
from ..constraints import (AffineConstraint, ExpConeConstraint, RSOCConstraint,
                           SOCConstraint)
from ..expressions import AffineExpression, BinaryVariable, IntegerVariable
from ..modeling.footprint import Specification
from ..modeling.solution import (PS_FEASIBLE, PS_INFEASIBLE, PS_UNBOUNDED,
                                 PS_UNKNOWN, PS_UNSTABLE, SS_FAILURE,
                                 SS_INFEASIBLE, SS_OPTIMAL, SS_PREMATURE,
                                 SS_UNKNOWN)
from .solver import Solver

_API_START = api_start(globals())
# -------------------------------


class ECOSSolver(Solver):
    """Interface to the ECOS solver via its official Python interface."""

    SUPPORTED = Specification.compile(
        directions=Specification.ALL,
        objectives=[
            AffineExpression],
        variables=Specification.ALL,
        constraints=[
            AffineConstraint,
            SOCConstraint,
            RSOCConstraint,
            ExpConeConstraint])

    @classmethod
    def supports(cls, footprint):
        """Implement :meth:`~.solver.Solver.supports`."""
        if not Solver.supports(footprint):
            return False

        return footprint << cls.SUPPORTED

    @classmethod
    def default_penalty(cls):
        """Implement :meth:`~.solver.Solver.default_penalty`."""
        return 1.0  # Stable free/open source solver.

    @classmethod
    def test_availability(cls):
        """Implement :meth:`~.solver.Solver.test_availability`."""
        assert_import_exists("ecos")

    @classmethod
    def names(cls):
        """Implement :meth:`~.solver.Solver.names`."""
        return "ecos", "ECOS", "Embedded Conic Solver"

    def __init__(self, problem):
        """Initialize an ECOS solver interface.

        :param ~picos.Problem problem: The problem to be solved.
        """
        super(ECOSSolver, self).__init__(problem)

        self._numVars = 0
        """Total number of scalar variables passed to ECOS."""

        self._ecosVarOffset = {}
        """Maps a PICOS variable to its offset in the ECOS constraint matrix."""

        self._ecosConIndices = dict()
        """Maps a PICOS constraints to a range of ECOS constraint indices.

        Note that equality constraints use a different index space."""

        self._ecosModuleCache = None
        """A cached reference to the ECOS module."""

    def reset_problem(self):
        """Implement :meth:`~.solver.Solver.reset_problem`."""
        self.int = None

        self._numVars = 0
        self._ecosVarOffset.clear()
        self._ecosConIndices.clear()

        # self._objectiveOffset = 0.0

    @property
    def ecos(self):
        """Return the ECOS core module ecos.py.

        The module is obtained by ``import ecos`` up to ECOS 2.0.6 and by
        ``import ecos.ecos`` starting with ECOS 2.0.7.
        """
        if self._ecosModuleCache is None:
            import ecos
            if hasattr(ecos, "ecos"):
                self._ecosModuleCache = ecos.ecos
            else:
                self._ecosModuleCache = ecos
        return self._ecosModuleCache

    @property
    def array(self):
        """ECOS' array type."""
        return self.ecos.np.array

    @property
    def matrix(self):
        """ECOS' matrix type."""
        return self.ecos.sparse.csc_matrix

    def zeros(self, shape):
        """Create a zero array or a zero matrix, depending on ``shape``."""
        if isinstance(shape, int) or len(shape) == 1:
            return self.ecos.np.zeros(shape)
        else:
            return self.matrix(shape)

    def stack(self, *args):
        """Stack vectors or matrices, the latter vertically."""
        # In the case of matrices, stack vertically.
        if isinstance(args[0], self.ecos.sparse.base.spmatrix):
            for i in range(1, len(args)):
                assert isinstance(args[i], self.ecos.sparse.base.spmatrix)
            return self.ecos.sparse.vstack(args, format="csc")

        # In the case of arrays, append them.
        for i in range(len(args)):
            assert isinstance(args[i], self.ecos.np.ndarray)
        return self.ecos.np.hstack(args)

    def _affine_expression_to_G_and_h(self, expression):
        assert isinstance(expression, AffineExpression)

        length = len(expression)

        # Construct G.
        I, J, V = [], [], []
        for variable, coefficients in expression._coefs.items():
            ecosVarOffset = self._ecosVarOffset[variable]

            if not isinstance(coefficients, cvxopt.spmatrix):
                coefficients = cvxopt.sparse(coefficients)

            I.extend(coefficients.I)
            J.extend([ecosVarOffset + j for j in coefficients.J])
            V.extend(coefficients.V)
        G = self.matrix((V, (I, J)), (length, self._numVars))

        # Construct h.
        constant = expression._const
        if not isinstance(constant, cvxopt.matrix):
            constant = cvxopt.matrix(constant)
        h = self.array(constant, dtype=float).flatten()

        return G, h

    _Gh = _affine_expression_to_G_and_h

    def _import_variables(self):
        offset = 0
        for variable in self.ext.variables.values():
            dim = variable.dim

            # Mark integer variables.
            if isinstance(variable, (BinaryVariable, IntegerVariable)):
                ecosIndices = range(offset, offset + dim)

                if isinstance(variable, BinaryVariable):
                    self.int["bool_vars_idx"].extend(ecosIndices)
                else:
                    self.int["int_vars_idx"].extend(ecosIndices)

            # Register the variable.
            self._ecosVarOffset[variable] = offset
            offset += dim

            # Import bounds.
            bounds = variable.bound_constraint
            if bounds:
                self._import_affine_constraint(bounds)

        assert offset == self._numVars

    def _append_equality(self, A, b):
        offset = len(self.int["b"])
        length = len(b)

        self.int["A"] = self.stack(self.int["A"], A)
        self.int["b"] = self.stack(self.int["b"], b)

        return range(offset, offset + length)

    def _append_inequality(self, G, h, typecode):
        assert typecode in self.int["dims"]

        # Make sure constraints are appened in the proper order.
        if typecode == "l":
            assert len(self.int["dims"]["q"]) == 0 \
                and self.int["dims"]["e"] == 0
        elif typecode == "q":
            assert self.int["dims"]["e"] == 0

        offset = len(self.int["h"])
        length = len(h)

        self.int["G"] = self.stack(self.int["G"], G)
        self.int["h"] = self.stack(self.int["h"], h)

        if typecode == "q":
            self.int["dims"][typecode].append(length)
        elif typecode == "e":
            self.int["dims"][typecode] += 1
        else:
            self.int["dims"][typecode] += length

        return range(offset, offset + length)

    def _import_affine_constraint(self, constraint):
        assert isinstance(constraint, AffineConstraint)

        (G_smaller, h_smaller) = self._Gh(constraint.smaller)
        (G_greater, h_greater) = self._Gh(constraint.greater)
        G = G_smaller - G_greater
        h = h_greater - h_smaller

        if constraint.is_equality():
            return self._append_equality(G, h)
        else:
            return self._append_inequality(G, h, "l")

    def _import_socone_constraint(self, constraint):
        assert isinstance(constraint, SOCConstraint)

        (A, b) = self._Gh(constraint.ne)
        (c, d) = self._Gh(constraint.ub)

        return self._append_inequality(
            self.stack(-c, -A), self.stack(d, b), "q")

    def _import_rscone_constraint(self, constraint):
        assert isinstance(constraint, RSOCConstraint)

        (A,  b)  = self._Gh(constraint.ne)
        (c1, d1) = self._Gh(constraint.ub1)
        (c2, d2) = self._Gh(constraint.ub2)

        return self._append_inequality(
            self.stack(-(c1 + c2), -2.0*A, c2 - c1),
            self.stack(d1 + d2,     2.0*b, d1 - d2), "q")

    def _import_expcone_constraint(self, constraint):
        assert isinstance(constraint, ExpConeConstraint)

        (Gx, hx) = self._Gh(constraint.x)
        (Gy, hy) = self._Gh(constraint.y)
        (Gz, hz) = self._Gh(constraint.z)

        # ECOS' exponential cone is cl{(x,y,z) | exp(x/z) <= y/z, z > 0},
        # PICOS' is cl{(x,y,z) | x >= y*exp(z/y), y > 0}. Note that given y > 0
        # it is x >= y*exp(z/y) if and only if exp(z/y) <= x/y. Therefor we can
        # transform from our coordinates to theirs with the mapping
        # (x, y, z) ↦ (z, x, y). Further, G and h with G = (Gx, Gy, Gz) and
        # h = (hx, hy, hz) are such that G*X + h = (x, y, z) where X is the
        # row-vectorization of all variables. ECOS however expects G and h such
        # that h - G*X is constrained to be in the exponential cone.
        return self._append_inequality(
            -self.stack(Gz, Gx, Gy), self.stack(hz, hx, hy), "e")

    def _import_objective(self):
        direction, objective = self.ext.objective

        # ECOS does not support a constant offset.
        # self._objectiveOffset = objective._const[0]

        if direction != "find":
            # ECOS only supports minimization; flip the sign for maximization.
            sign = 1.0 if direction == "min" else -1.0

            # Import coefficients.
            for variable, coefficient in objective._coefs.items():
                for localIndex in range(variable.dim):
                    index = self._ecosVarOffset[variable] + localIndex
                    self.int["c"][index] = sign * coefficient[localIndex]

    def _import_problem(self):
        self._numVars = sum(var.dim for var in self.ext.variables.values())

        # ECOS' internal problem representation is stateless; a number of
        # vectors and matrices is supplied each time a search is started.
        # These vectors and matrices are thus stored in self.int.
        self.int = {
            # Objective function coefficients.
            "c": self.zeros(self._numVars),

            # Linear equality left hand side.
            "A": self.matrix((0, self._numVars)),

            # Linear equality right hand side.
            "b": self.array([]),

            # Conic inequality left hand side.
            "G": self.matrix((0, self._numVars)),

            # Conic inequality right hand side.
            "h": self.array([]),

            # Cone definition: Linear, second order, exponential dimensions.
            "dims": {"l": 0, "q": [], "e": 0},

            # Boolean variable indices.
            "bool_vars_idx": [],

            # Integer variable indices.
            "int_vars_idx": []
        }

        # NOTE: Constraints need to be append ordered by type.
        # TODO: Add fast constraints-by-type iterators to Problem.

        # Import variables with their bounds as affine constraints.
        self._import_variables()

        # Import affine constraints.
        for constraint in self.ext.constraints.values():
            if isinstance(constraint, AffineConstraint):
                self._ecosConIndices[constraint] = \
                    self._import_affine_constraint(constraint)

        # Import second order cone constraints.
        for constraint in self.ext.constraints.values():
            if isinstance(constraint, SOCConstraint):
                self._ecosConIndices[constraint] = \
                    self._import_socone_constraint(constraint)

        # Import rotated second order cone constraints.
        for constraint in self.ext.constraints.values():
            if isinstance(constraint, RSOCConstraint):
                self._ecosConIndices[constraint] = \
                    self._import_rscone_constraint(constraint)

        # Import exponential cone constraints.
        for constraint in self.ext.constraints.values():
            if isinstance(constraint, ExpConeConstraint):
                self._ecosConIndices[constraint] = \
                    self._import_expcone_constraint(constraint)

        # Make sure that no unsupported constraints are present.
        for constraint in self.ext.constraints.values():
            assert isinstance(constraint, (AffineConstraint, SOCConstraint,
                RSOCConstraint, ExpConeConstraint))

        # Set objective.
        self._import_objective()

    def _update_problem(self):
        raise NotImplementedError

    def _solve(self):
        ecosOptions = {}

        # verbosity
        beVerbose = self.verbosity() >= 1
        ecosOptions["verbose"]    = beVerbose
        ecosOptions["mi_verbose"] = beVerbose

        # rel_prim_fsb_tol, rel_dual_fsb_tol
        feasibilityTols = [tol for tol in (self.ext.options.rel_prim_fsb_tol,
                self.ext.options.rel_dual_fsb_tol) if tol is not None]
        if feasibilityTols:
            ecosOptions["feastol"] = min(feasibilityTols)

        # abs_ipm_opt_tol
        if self.ext.options.abs_ipm_opt_tol is not None:
            ecosOptions["abstol"] = self.ext.options.abs_ipm_opt_tol

        # rel_ipm_opt_tol
        if self.ext.options.rel_ipm_opt_tol is not None:
            ecosOptions["reltol"] = self.ext.options.rel_ipm_opt_tol

        # abs_bnb_opt_tol
        if self.ext.options.abs_bnb_opt_tol is not None:
            ecosOptions["mi_abs_eps"] = self.ext.options.abs_bnb_opt_tol

        # rel_bnb_opt_tol
        if self.ext.options.rel_bnb_opt_tol is not None:
            ecosOptions["mi_rel_eps"] = self.ext.options.rel_bnb_opt_tol

        # integrality_tol
        # HACK: ECOS_BB uses ECOS' "tolerance for feasibility condition for
        #       inaccurate solution" as the integrality tolerance.
        if self.ext.options.integrality_tol is not None:
            ecosOptions["feastol_inacc"] = self.ext.options.integrality_tol

        # max_iterations
        if self.ext.options.max_iterations is not None:
            ecosOptions["max_iters"]    = self.ext.options.max_iterations
            ecosOptions["mi_max_iters"] = self.ext.options.max_iterations

        # Handle unsupported options.
        self._handle_unsupported_options(
            "lp_root_method", "lp_node_method", "timelimit", "treememory",
            "max_fsb_nodes", "hotstart")

        # Assemble the solver input.
        arguments = {}
        arguments.update(self.int)
        arguments.update(ecosOptions)

        # Debug print the solver input.
        if self._debug():
            from pprint import pformat
            self._debug("Passing to ECOS:\n" + pformat(arguments))

        # Attempt to solve the problem.
        with self._header(), self._stopwatch():
            solution = self.ecos.solve(**arguments)

        # Debug print the solver output.
        if self._debug():
            from pprint import pformat
            self._debug("Recevied from ECOS:\n" + pformat(solution))

        # Retrieve primals.
        primals = {}
        if self.ext.options.primals is not False:
            for variable in self.ext.variables.values():
                offset = self._ecosVarOffset[variable]
                dim    = variable.dim
                value  = list(solution["x"][offset:offset + dim])
                primals[variable] = value

        # Retrieve duals.
        duals = {}
        if self.ext.options.duals is not False:
            for constraint in self.ext.constraints.values():
                dual    = None
                indices = self._ecosConIndices[constraint]

                if isinstance(constraint, AffineConstraint):
                    if constraint.is_equality():
                        dual = list(solution["y"][indices])
                    else:
                        dual = list(solution["z"][indices])
                elif isinstance(constraint, SOCConstraint):
                    dual     = solution["z"][indices]
                    dual     = list(dual)
                elif isinstance(constraint, RSOCConstraint):
                    dual     = solution["z"][indices]
                    dual[1:] = -dual[1:]
                    alpha    = dual[0] - dual[-1]
                    beta     = dual[0] + dual[-1]
                    z        = list(-2.0 * dual[1:-1])
                    dual     = [alpha, beta] + z
                elif isinstance(constraint, ExpConeConstraint):
                    zxy  = solution["z"][indices]
                    dual = [zxy[1], zxy[2], zxy[0]]
                else:
                    assert False, "Unexpected constraint type."

                if type(dual) is list:
                    if len(dual) == 1:
                        dual = float(dual[0])
                    else:
                        dual = cvxopt.matrix(dual, constraint.size)

                duals[constraint] = dual

        # # Retrieve objective value.
        # p = solution["info"]["pcost"]
        # d = solution["info"]["dcost"]
        #
        # if p is not None and d is not None:
        #     objectiveValue = 0.5 * (p + d)
        # elif p is not None:
        #     objectiveValue = p
        # elif d is not None:
        #     objectiveValue = d
        # else:
        #     objectiveValue = None
        #
        # if objectiveValue is not None:
        #     objectiveValue += self._objectiveOffset
        #
        #     if self.ext.objective.direction == "max":
        #         objectiveValue = -objectiveValue

        statusCode = solution["info"]["exitFlag"]
        if   statusCode == 0:  # optimal
            primalStatus   = SS_OPTIMAL
            dualStatus     = SS_OPTIMAL
            problemStatus  = PS_FEASIBLE
        elif statusCode == 10:  # inaccurate/optimal
            primalStatus   = SS_OPTIMAL
            dualStatus     = SS_OPTIMAL
            problemStatus  = PS_FEASIBLE
        elif statusCode == 1:  # primal infeasible
            primalStatus   = SS_INFEASIBLE
            dualStatus     = SS_UNKNOWN
            problemStatus  = PS_INFEASIBLE
        elif statusCode == 11:  # inaccurate/primal infeasible
            primalStatus   = SS_INFEASIBLE
            dualStatus     = SS_UNKNOWN
            problemStatus  = PS_INFEASIBLE
        elif statusCode == 2:  # dual infeasible
            primalStatus   = SS_UNKNOWN
            dualStatus     = SS_INFEASIBLE
            problemStatus  = PS_UNBOUNDED
        elif statusCode == 12:  # inaccurate/dual infeasible
            primalStatus   = SS_UNKNOWN
            dualStatus     = SS_INFEASIBLE
            problemStatus  = PS_UNBOUNDED
        elif statusCode == -1:  # iteration limit reached
            primalStatus   = SS_PREMATURE
            dualStatus     = SS_PREMATURE
            problemStatus  = PS_UNKNOWN
        elif statusCode == -2:  # search direction unreliable
            primalStatus   = SS_UNKNOWN
            dualStatus     = SS_UNKNOWN
            problemStatus  = PS_UNSTABLE
        elif statusCode == -3:  # numerically problematic
            primalStatus   = SS_UNKNOWN
            dualStatus     = SS_UNKNOWN
            problemStatus  = PS_UNSTABLE
        elif statusCode == -4:  # interrupted
            primalStatus   = SS_PREMATURE
            dualStatus     = SS_PREMATURE
            problemStatus  = PS_UNKNOWN
        elif statusCode == -7:  # solver error
            primalStatus   = SS_FAILURE
            dualStatus     = SS_FAILURE
            problemStatus  = PS_UNKNOWN
        else:
            primalStatus   = SS_UNKNOWN
            dualStatus     = SS_UNKNOWN
            problemStatus  = PS_UNKNOWN

        return self._make_solution(primals, duals, primalStatus, dualStatus,
            problemStatus, {"ecos_sol": solution})


# --------------------------------------
__all__ = api_end(_API_START, globals())

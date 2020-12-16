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

"""Linear matrix inequalities."""

from collections import namedtuple

from .. import glyphs
from ..apidoc import api_end, api_start
from ..caching import cached_property
from .constraint import Constraint, ConstraintConversion

_API_START = api_start(globals())
# -------------------------------


class LMIConstraint(Constraint):
    """Linear matrix inequality.

    An inequality with respect to the positive semidefinite cone, also known as
    a Linear Matrix Inequality (LMI) or an SDP constraint.
    """

    def __init__(self, lhs, relation, rhs, customString=None):
        """Construct a :class:`LMIConstraint`.

        :param ~picos.expressions.AffineExpression lhs:
            Left hand side expression.
        :param str relation:
            Constraint relation symbol.
        :param ~picos.expressions.AffineExpression rhs:
            Right hand side expression.
        :param str customString:
            Optional string description.
        """
        from ..expressions import (AffineExpression, HermitianVariable,
                                   SymmetricVariable)
        from ..expressions.vectorizations import (HermitianVectorization,
                                                  SymmetricVectorization)
        from ..expressions.data import cvxopt_equals

        required_type = self._required_type()

        assert isinstance(lhs, required_type)
        assert isinstance(rhs, required_type)
        assert relation in self.LE + self.GE

        if lhs.shape != rhs.shape:
            raise ValueError("Failed to form a constraint: "
                "Expressions have incompatible dimensions.")

        if lhs.shape[0] != lhs.shape[1]:
            raise ValueError("Failed to form a constraint: "
                "LMI expressions are not square.")

        self.lhs      = lhs
        self.rhs      = rhs
        self.relation = relation

        psd = self.psd
        if not psd.hermitian:
            needed = "symmetric" if required_type is AffineExpression \
                else "hermitian"

            raise ValueError("Failed to form a constraint: {} is not "
                "necessarily {}. Consider a constraint on {} instead."
                .format(psd, needed, glyphs.Tr("{}.hermitianized")(psd.string)))

        # Check if the constraint simply poses positive semidefiniteness on a
        # matrix variable, as certain solvers can handle this more efficiently
        # than a general linear matrix inequality.
        self.semidefVar = None
        if len(psd._coefs) == 1 and not psd._const:
            var, coef = list(psd._coefs.items())[0]

            # Don't accept any numeric deviation as we don't know the user's
            # tolerance settings.
            if isinstance(var, SymmetricVariable) and cvxopt_equals(
                    coef, SymmetricVectorization(psd.shape).identity,
                    tolerance=0.0):
                self.semidefVar = var
            elif isinstance(var, HermitianVariable) and cvxopt_equals(
                    coef, HermitianVectorization(psd.shape).identity,
                    tolerance=0.0):
                self.semidefVar = var

        super(LMIConstraint, self).__init__(
            self._get_type_term(), customString, printSize=True)

    def _get_type_term(self):
        return "LMI"

    def _required_type(self):
        from ..expressions import AffineExpression

        return AffineExpression

    @property
    def smaller(self):
        """The smaller-or-equal side expression."""
        return self.rhs if self.relation == self.GE else self.lhs

    @property
    def greater(self):
        """The greater-or-equal side expression."""
        return self.lhs if self.relation == self.GE else self.rhs

    @cached_property
    def psd(self):
        """The matrix expression posed to be positive semidefinite."""
        if self.relation == self.GE:
            return self.lhs - self.rhs
        else:
            return self.rhs - self.lhs

    @cached_property
    def nsd(self):
        """The matrix expression posed to be negative semidefinite."""
        if self.relation == self.GE:
            return self.rhs - self.lhs
        else:
            return self.lhs - self.rhs

    nnd = psd
    npd = nsd

    Subtype = namedtuple("Subtype", ("diag",))

    def _subtype(self):
        return self.Subtype(self.lhs.shape[0])

    @classmethod
    def _cost(cls, subtype):
        n = subtype.diag
        return n*(n + 1)//2

    def _expression_names(self):
        yield "lhs"
        yield "rhs"

    def _str(self):
        if self.relation == self.LE:
            return glyphs.psdle(self.lhs.string, self.rhs.string)
        else:
            return glyphs.psdge(self.lhs.string, self.rhs.string)

    def _get_size(self):
        return self.lhs.shape

    def _get_slack(self):
        return self.psd.value


class ComplexLMIConstraint(LMIConstraint):
    """Complex linear matrix inequality."""

    class RealConversion(ConstraintConversion):
        """Complex LMI to real LMI conversion."""

        @classmethod
        def predict(cls, subtype, options):
            """Implement :meth:`~.constraint.ConstraintConversion.predict`."""
            n = subtype.diag

            yield ("con", LMIConstraint.make_type(diag=2*n), 1)

        @classmethod
        def convert(cls, con, options):
            """Implement :meth:`~.constraint.ConstraintConversion.convert`."""
            from ..modeling import Problem

            P = Problem()
            Z = con.psd
            P.add_constraint((Z.real & -Z.imag) // (Z.imag & Z.real) >> 0)

            return P

        @classmethod
        def dual(cls, auxVarPrimals, auxConDuals, options):
            """Implement :meth:`~.constraint.ConstraintConversion.dual`."""
            assert len(auxConDuals) == 1

            auxConDual = auxConDuals[0]
            if auxConDual is None:
                return None
            else:
                assert auxConDual.size[0] == auxConDual.size[1]
                n = auxConDual.size[0] // 2
                assert 2*n == auxConDual.size[0]
                A = auxConDual[:n, :n]
                B = auxConDual[:n, n:]
                D = auxConDual[n:, n:]
                return (A + 1j*B) + (D + 1j*B).H

    def _get_type_term(self):
        return "Complex LMI"

    def _required_type(self):
        from ..expressions import ComplexAffineExpression

        return ComplexAffineExpression

    @classmethod
    def _cost(cls, subtype):
        return subtype.diag**2


# --------------------------------------
__all__ = api_end(_API_START, globals())

"""Some Gaphor specific updates to the canvas. This is done by setting the
correct properties on gaphas' modules.

Matrix
------
Small utility class wrapping cairo.Matrix. The `Matrix` class adds
state preservation capabilities.
"""

from __future__ import annotations

from typing import Callable, Optional, Set, Tuple

import cairo

from gaphas.state import observed, reversible_method


class Matrix:
    """Matrix wrapper. This version sends @observed messages on state changes.

    >>> Matrix()
    Matrix(1.0, 0.0, 0.0, 1.0, 0.0, 0.0)
    """

    def __init__(
        self,
        xx: float = 1.0,
        yx: float = 0.0,
        xy: float = 0.0,
        yy: float = 1.0,
        x0: float = 0.0,
        y0: float = 0.0,
        matrix: Optional[cairo.Matrix] = None,
    ) -> None:
        self._matrix = matrix or cairo.Matrix(xx, yx, xy, yy, x0, y0)
        self._handlers: Set[Callable[[Matrix], None]] = set()

    def add_handler(self, handler: Callable[[Matrix], None]) -> None:
        self._handlers.add(handler)

    def remove_handler(self, handler: Callable[[Matrix], None]) -> None:
        self._handlers.discard(handler)

    def notify(self) -> None:
        for handler in self._handlers:
            handler(self)

    @observed
    def invert(self) -> None:
        self._matrix.invert()
        self.notify()

    @observed
    def rotate(self, radians: float) -> None:
        self._matrix.rotate(radians)
        self.notify()

    @observed
    def scale(self, sx: float, sy: float) -> None:
        self._matrix.scale(sx, sy)
        self.notify()

    @observed
    def translate(self, tx: float, ty: float) -> None:
        self._matrix.translate(tx, ty)
        self.notify()

    @observed
    def set(
        self,
        xx: Optional[float] = None,
        yx: Optional[float] = None,
        xy: Optional[float] = None,
        yy: Optional[float] = None,
        x0: Optional[float] = None,
        y0: Optional[float] = None,
    ) -> None:
        updated = False
        m = self._matrix
        for name, val in (
            ("xx", xx),
            ("yx", yx),
            ("xy", xy),
            ("yy", yy),
            ("x0", x0),
            ("y0", y0),
        ):
            if val is not None and val != getattr(m, name):
                setattr(m, name, val)
                updated = True
        if updated:
            self.notify()

    # TODO: Make reversible
    reversible_method(invert, invert)
    reversible_method(rotate, rotate, {"radians": lambda radians: -radians})
    reversible_method(scale, scale, {"sx": lambda sx: 1 / sx, "sy": lambda sy: 1 / sy})
    reversible_method(
        translate, translate, {"tx": lambda tx: -tx, "ty": lambda ty: -ty}
    )

    def multiply(self, m: Matrix) -> Matrix:
        return Matrix(matrix=self._matrix.multiply(m._matrix))

    def transform_distance(self, dx: float, dy: float) -> Tuple[float, float]:
        return self._matrix.transform_distance(dx, dy)  # type: ignore[no-any-return]

    def transform_point(self, x: float, y: float) -> Tuple[float, float]:
        return self._matrix.transform_point(x, y)  # type: ignore[no-any-return]

    def inverse(self) -> Matrix:
        m = Matrix(matrix=cairo.Matrix(*self._matrix))  # type: ignore[misc]
        m.invert()
        return m

    def to_cairo(self) -> cairo.Matrix:
        return self._matrix

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Matrix):
            return bool(self._matrix == other._matrix)
        else:
            return False

    def __getitem__(self, val: int) -> float:
        return self._matrix[val]  # type: ignore[index,no-any-return]

    def __mul__(self, other: Matrix) -> Matrix:
        return Matrix(matrix=self._matrix * other._matrix)

    def __repr__(self) -> str:
        return f"Matrix{tuple(self._matrix)}"  # type: ignore[arg-type]

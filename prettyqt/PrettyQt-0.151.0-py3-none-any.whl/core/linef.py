from __future__ import annotations

from typing import Iterator, Literal, Union, Tuple

from qtpy import QtCore

from prettyqt import core


class LineF(QtCore.QLineF):
    def __repr__(self):
        return f"{type(self).__name__}({repr(self.get_p1())}, {repr(self.get_p1())})"

    def __reduce__(self):
        return self.__class__, (self.get_p1(), self.get_p1())

    def __reversed__(self):
        return LineF(self.get_p2(), self.get_p1())

    def __abs__(self) -> float:
        return self.length()

    def __iter__(self) -> Iterator[core.PointF]:
        yield self.get_p1()
        yield self.get_p2()

    def __getitem__(self, index: Literal[0, 1]) -> core.PointF:
        if index == 0:
            return self.get_p1()
        elif index == 1:
            return self.get_p2()
        else:
            raise KeyError(index)

    def __setitem__(
        self, index: Literal[0, 1], value: Union[QtCore.QPointF, Tuple[float, float]]
    ):
        if index == 0:
            self.set_p1(value)
        elif index == 1:
            self.set_p2(value)
        else:
            raise KeyError(index)

    def set_p1(self, point: Union[QtCore.QPointF, Tuple[float, float]]):
        if isinstance(point, tuple):
            point = core.PointF(*point)
        self.setP1(point)

    def get_p1(self) -> core.PointF:
        return core.PointF(self.p1())

    def set_p2(self, point: Union[QtCore.QPointF, Tuple[float, float]]):
        if isinstance(point, tuple):
            point = core.PointF(*point)
        self.setP2(point)

    def get_p2(self) -> core.PointF:
        return core.PointF(self.p2())

    def get_center(self) -> core.PointF:
        return core.PointF(self.center())

    def get_normal_vector(self) -> LineF:
        return LineF(self.normalVector())

    def get_unit_vector(self) -> LineF:
        return LineF(self.unitVector())

    def to_line(self) -> core.Line:
        return core.Line(self.toLine())


if __name__ == "__main__":
    line = LineF(core.Point(0, 0), core.Point(2, 2))
    print(repr(line))
    for p in line:
        print(p)

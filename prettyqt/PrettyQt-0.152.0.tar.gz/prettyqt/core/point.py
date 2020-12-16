from qtpy import QtCore


class Point(QtCore.QPoint):
    def __repr__(self):
        return f"{type(self).__name__}(x={self.x()}, y={self.y()})"

    def __getitem__(self, index) -> int:
        return (self.x(), self.y())[index]

    def __reduce__(self):
        return self.__class__, (self.x(), self.y())

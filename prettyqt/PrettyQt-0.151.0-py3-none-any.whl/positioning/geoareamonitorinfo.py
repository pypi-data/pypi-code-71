from qtpy import PYQT5, PYSIDE2

if PYQT5:
    from PyQt5 import QtPositioning
elif PYSIDE2:
    from PySide2 import QtPositioning

from prettyqt import core, positioning


class GeoAreaMonitorInfo(QtPositioning.QGeoAreaMonitorInfo):
    def __str__(self):
        return self.name()

    def __repr__(self):
        return f"{type(self).__name__}({self.name()!r})"

    def get_area(self) -> positioning.GeoShape:
        area = self.area()
        if isinstance(area, QtPositioning.QGeoCircle):
            return positioning.GeoCircle(area)
        elif isinstance(area, QtPositioning.QGeoRectangle):
            return positioning.GeoRectangle(area)
        elif isinstance(area, QtPositioning.QGeoPath):
            return positioning.GeoPath(area)
        elif isinstance(area, QtPositioning.QGeoPolygon):
            return positioning.GeoPolygon(area)
        elif isinstance(area, QtPositioning.QGeoShape):
            return positioning.GeoShape(area)
        else:
            raise RuntimeError()

    def get_expiration(self) -> core.DateTime:
        return core.DateTime(self.expiration())


if __name__ == "__main__":
    info = GeoAreaMonitorInfo("test")
    print(str(info))
    print(repr(info))

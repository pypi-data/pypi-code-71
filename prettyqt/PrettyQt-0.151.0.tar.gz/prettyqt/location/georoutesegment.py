from typing import List

from qtpy import QtLocation

from prettyqt import positioning, location


class GeoRouteSegment(QtLocation.QGeoRouteSegment):
    def __bool__(self):
        return self.isValid()

    def __abs__(self) -> float:
        return self.distance()

    def get_maneuver(self) -> location.GeoManeuver:
        return location.GeoManeuver(self.maneuver())

    def get_path(self) -> List[positioning.GeoCoordinate]:
        return [positioning.GeoCoordinate(i) for i in self.path()]


if __name__ == "__main__":
    segment = GeoRouteSegment()
    print(bool(segment))
    segment.setDistance(1)
    print(bool(segment))

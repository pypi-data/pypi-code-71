from qtpy import QtWidgets

from prettyqt import widgets, gui, constants
from prettyqt.utils import InvalidParamError


QtWidgets.QGraphicsPolygonItem.__bases__ = (widgets.AbstractGraphicsShapeItem,)


class GraphicsPolygonItem(QtWidgets.QGraphicsPolygonItem):
    def get_polygon(self) -> gui.PolygonF:
        return gui.PolygonF(self.polygon())

    def serialize_fields(self):
        return dict(polygon=self.get_polygon(), fill_rule=self.get_fill_rule())

    def set_fill_rule(self, rule: constants.FillRuleStr):
        if rule not in constants.FILL_RULE:
            raise InvalidParamError(rule, constants.FILL_RULE)
        self.setFillRule(constants.FILL_RULE[rule])

    def get_fill_rule(self) -> constants.FillRuleStr:
        return constants.FILL_RULE.inverse[self.fillRule()]

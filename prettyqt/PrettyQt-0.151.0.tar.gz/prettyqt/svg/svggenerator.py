from qtpy import QtSvg

from prettyqt import core, gui


QtSvg.QSvgGenerator.__bases__ = (gui.PaintDevice,)


class SvgGenerator(QtSvg.QSvgGenerator):
    def get_viewbox(self) -> core.Rect:
        return core.Rect(self.viewBox())

    def get_viewboxf(self) -> core.RectF:
        return core.RectF(self.viewBoxF())

    def get_size(self) -> core.Size:
        return core.Size(self.size())

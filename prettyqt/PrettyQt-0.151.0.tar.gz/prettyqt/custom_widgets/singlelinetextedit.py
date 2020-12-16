from typing import Optional

from qtpy import QtWidgets

from prettyqt import widgets


class SingleLineTextEdit(widgets.PlainTextEdit):
    def __init__(self, parent: Optional[QtWidgets.QWidget] = None):
        super().__init__(parent=parent)
        self.textChanged.connect(self._on_text_changed)
        font_metrics = self.get_font_metrics()
        self.row_height = font_metrics.lineSpacing()
        self.setFixedHeight(int(self.row_height * 1.5))
        self.set_size_policy(vertical="fixed")
        self.set_line_wrap_mode("none")
        self.set_scrollbar_policy("always_off")

    def _on_text_changed(self):
        text = self.text()
        with self.current_cursor() as c:
            pos = c.position()
            num_linebreaks = text.count("\n")
            with self.block_signals():
                self.set_text(text.replace("\n", ""))
            c.setPosition(pos - num_linebreaks)


if __name__ == "__main__":
    app = widgets.app()
    widget = SingleLineTextEdit()
    widget.show()
    app.main_loop()

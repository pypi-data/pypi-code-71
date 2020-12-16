import pathlib
from typing import Callable, Union

from qtpy import QtWebEngineWidgets

from prettyqt import core, widgets, webenginewidgets


QtWebEngineWidgets.QWebEngineView.__bases__ = (widgets.Widget,)


class WebEngineView(QtWebEngineWidgets.QWebEngineView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setPage(webenginewidgets.WebEnginePage(self))

    def set_url(self, url: Union[str, pathlib.Path]):
        """Set the url of the WebEngineView.

        Clears the view and loads the URL.

        Args:
            url: URL to set
        """
        if isinstance(url, pathlib.Path):
            url = core.Url.fromLocalFile(str(url))
        elif isinstance(url, str):
            url = core.Url(url)
        self.setUrl(url)

    def get_url(self) -> core.Url:
        return core.Url(self.url())

    def load_url(self, url: Union[str, pathlib.Path]):
        """Load the URL.

        Loads the specified url and displays it.

        Note: The view remains the same until enough data has arrived
        to display the new URL.

        Args:
            url: URL to load
        """
        if isinstance(url, pathlib.Path):
            url = core.Url.fromLocalFile(str(url))
        elif isinstance(url, str):
            url = core.Url(url)
        self.load(url)

    def set_zoom(self, zoom: float):
        """Set the zoom factor for the view.

        Valid values are within the range from 0.25 to 5.0. The default factor is 1.0.

        Args:
            zoom: Zoom factor
        """
        self.setZoomFactor(zoom)

    def find_text(
        self,
        string: str,
        backward: bool = False,
        case_sensitive: bool = False,
        callback: Callable[[bool], None] = None,
    ):
        """Find text in the current page.

        Finds the specified string, subString, in the page, using the given options.
        The findTextFinished() signal is emitted when a string search is completed.

        To clear the search highlight, just pass an empty string.

        The resultCallback must take a boolean parameter.
        It will be called with a value of true if the subString was found;
        otherwise the callback value will be false.

        Warning: It is guaranteed that the callback is always called,
        but it might be done during page destruction. When WebEnginePage is deleted,
        the callback is triggered with an invalid value and it is not safe to use
        the corresponding QWebEnginePage or QWebEngineView instance inside it.

        Args:
            string: string to search for
            backward: search backwards
            case_sensitive: case-sensitive search
            callback: result callback
        """
        if callback is None:

            def do_nothing(x):
                pass

            callback = do_nothing
        flag = QtWebEngineWidgets.QWebEnginePage.FindFlag()
        if case_sensitive:
            flag |= QtWebEngineWidgets.QWebEnginePage.FindCaseSensitively
        if backward:
            flag |= QtWebEngineWidgets.QWebEnginePage.FindBackward
        self.findText(string, flag, callback)


if __name__ == "__main__":
    from prettyqt import widgets

    app = widgets.app()
    path = "https://www.google.com"
    widget = WebEngineView()
    widget.set_url(path)
    widget.find_text("test", backward=True, case_sensitive=True, callback=None)
    widget.show()
    app.main_loop()

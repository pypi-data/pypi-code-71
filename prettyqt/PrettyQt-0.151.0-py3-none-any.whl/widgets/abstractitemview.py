import logging
from typing import Any, Generator, List, Optional, Literal

from qtpy import QtCore, QtWidgets

from prettyqt import constants, gui, widgets
from prettyqt.utils import bidict, InvalidParamError, helpers

logger = logging.getLogger(__name__)

TRIGGERS = bidict(
    none=QtWidgets.QAbstractItemView.NoEditTriggers,
    double_click=QtWidgets.QAbstractItemView.DoubleClicked,
    edit_key=QtWidgets.QAbstractItemView.EditKeyPressed,
)

SELECTION_BEHAVIOUR = bidict(
    rows=QtWidgets.QAbstractItemView.SelectRows,
    columns=QtWidgets.QAbstractItemView.SelectColumns,
    items=QtWidgets.QAbstractItemView.SelectItems,
)

SELECTION_BEHAVIOUR_STR = Literal["rows", "columns", "items"]

SELECTION_MODE = bidict(
    single=QtWidgets.QAbstractItemView.SingleSelection,
    extended=QtWidgets.QAbstractItemView.ExtendedSelection,
    multi=QtWidgets.QAbstractItemView.MultiSelection,
    none=QtWidgets.QAbstractItemView.NoSelection,
)

SELECTION_MODE_STR = Literal["single", "extended", "multi", "none"]

SCROLL_MODE = bidict(
    item=QtWidgets.QAbstractItemView.ScrollPerItem,
    pixel=QtWidgets.QAbstractItemView.ScrollPerPixel,
)

SCROLL_MODE_STR = Literal["item", "pixel"]

SCROLL_HINT = bidict(
    ensure_visible=QtWidgets.QAbstractItemView.EnsureVisible,
    position_at_top=QtWidgets.QAbstractItemView.PositionAtTop,
    position_at_bottom=QtWidgets.QAbstractItemView.PositionAtBottom,
    position_at_center=QtWidgets.QAbstractItemView.PositionAtCenter,
)

SCROLL_HINT_STR = Literal[
    "ensure_visible", "position_at_top", "position_at_bottom", "position_at_center"
]

QtWidgets.QAbstractItemView.__bases__ = (widgets.AbstractScrollArea,)


class AbstractItemView(QtWidgets.QAbstractItemView):
    def __len__(self) -> int:
        if self.model() is not None:
            return self.model().rowCount()
        return 0

    def selectAll(self):
        """Override, we dont want to selectAll for too many items bc of performance."""
        if self.model() is None:
            return None
        if self.model().rowCount() * self.model().columnCount() > 1_000_000:
            logger.warning("Too many cells to select.")
            return None
        super().selectAll()

    def set_model(self, model: Optional[QtCore.QAbstractItemModel]):
        """Delete old selection model explicitely, seems to help with memory usage."""
        old_model = self.model()
        old_sel_model = self.selectionModel()
        if old_model is not None or model is not None:
            self.setModel(model)
        # if old_model:
        #     old_model.deleteLater()
        #     del old_model
        if old_sel_model:
            old_sel_model.deleteLater()
            del old_sel_model

    def set_delegate(
        self,
        delegate: QtWidgets.QItemDelegate,
        column: Optional[int] = None,
        row: Optional[int] = None,
        persistent: bool = False,
    ):
        if column is not None:
            self.setItemDelegateForColumn(column, delegate)
            if persistent:
                model = self.model()
                for i in range(0, model.rowCount()):
                    self.openPersistentEditor(model.index(i, column))
        elif row is not None:
            self.setItemDelegateForRow(row, delegate)
            if persistent:
                model = self.model()
                for i in range(0, model.columnCount()):
                    self.openPersistentEditor(model.index(row, i))
        else:
            self.setItemDelegate(delegate)

    def toggle_select_all(self):
        """Select all items from list (deselect when all selected)."""
        if self.selectionModel() is None:
            return None
        if self.selectionModel().hasSelection():
            self.clearSelection()
        else:
            self.selectAll()

    def set_table_color(self, color: str):
        with self.edit_stylesheet() as ss:
            ss.QHeaderView.section.backgroundColor.setValue(color)

    def current_index(self) -> Optional[QtCore.QModelIndex]:
        if self.selectionModel() is None:
            return None
        return self.selectionModel().currentIndex()

    def current_data(self):
        if self.selectionModel() is None:
            return None
        idx = self.selectionModel().currentIndex()
        return idx.data(QtCore.Qt.UserRole)

    def current_row(self) -> Optional[int]:
        if self.selectionModel() is None:
            return None
        return self.selectionModel().currentIndex().row()

    def current_column(self) -> Optional[int]:
        if self.selectionModel() is None:
            return None
        return self.selectionModel().currentIndex().column()

    def selected_indexes(self) -> List[QtCore.QModelIndex]:
        """Returns list of selected indexes in first row."""
        indexes = (x for x in self.selectedIndexes() if x.column() == 0)
        return sorted(indexes, key=lambda x: x.row())

    def selected_names(self) -> Generator[Any, None, None]:
        """Returns generator yielding item names."""
        return (x.data(constants.NAME_ROLE) for x in self.selected_indexes())

    def selected_rows(self) -> Generator[int, None, None]:
        """Returns generator yielding row nums."""
        return (x.row() for x in self.selected_indexes())

    def selected_data(self) -> Generator[Any, None, None]:
        """Returns generator yielding selected userData."""
        return (x.data(constants.USER_ROLE) for x in self.selected_indexes())

    def setup_dragdrop_move(self):
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setDragDropMode(self.DragDrop)
        self.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.setDropIndicatorShown(True)

    def set_edit_triggers(self, *triggers: Optional[str]):
        items = ["none" if t is None else t for t in triggers]
        for item in items:
            if item not in TRIGGERS:
                raise InvalidParamError(item, TRIGGERS)
        flags = helpers.merge_flags(items, TRIGGERS)
        self.setEditTriggers(flags)

    def get_edit_triggers(self) -> List[str]:
        return [k for k, v in TRIGGERS.items() if v & self.editTriggers()]

    def set_selection_behaviour(self, behaviour: SELECTION_BEHAVIOUR_STR):
        """Set selection behaviour for given item view.

        Args:
            behaviour: selection behaviour to use

        Raises:
            InvalidParamError: behaviour does not exist
        """
        if behaviour not in SELECTION_BEHAVIOUR:
            raise InvalidParamError(behaviour, SELECTION_BEHAVIOUR)
        self.setSelectionBehavior(SELECTION_BEHAVIOUR[behaviour])

    def get_selection_behaviour(self) -> SELECTION_BEHAVIOUR_STR:
        """Return current selection behaviour.

        Returns:
            selection behaviour
        """
        return SELECTION_BEHAVIOUR.inverse[self.selectionBehavior()]

    def set_selection_mode(self, mode: Optional[SELECTION_MODE_STR]):
        """Set selection mode for given item view.

        Args:
            mode: selection mode to use

        Raises:
            InvalidParamError: mode does not exist
        """
        if mode is None:
            mode = "none"
        if mode not in SELECTION_MODE:
            raise InvalidParamError(mode, SELECTION_MODE)
        self.setSelectionMode(SELECTION_MODE[mode])

    def get_selection_mode(self) -> SELECTION_MODE_STR:
        """Return current selection mode.

        Returns:
            selection mode
        """
        return SELECTION_MODE.inverse[self.selectionMode()]

    def set_scroll_mode(self, mode: SCROLL_MODE_STR):
        """Set the scroll mode for both directions.

        Args:
            mode: mode to set

        Raises:
            InvalidParamError: invalid scroll mode
        """
        if mode not in SCROLL_MODE:
            raise InvalidParamError(mode, SCROLL_MODE)
        self.setHorizontalScrollMode(SCROLL_MODE[mode])
        self.setVerticalScrollMode(SCROLL_MODE[mode])

    def set_horizontal_scroll_mode(self, mode: SCROLL_MODE_STR):
        """Set the horizontal scroll mode.

        Args:
            mode: mode to set

        Raises:
            InvalidParamError: invalid scroll mode
        """
        if mode not in SCROLL_MODE:
            raise InvalidParamError(mode, SCROLL_MODE)
        self.setHorizontalScrollMode(SCROLL_MODE[mode])

    def set_vertical_scroll_mode(self, mode: SCROLL_MODE_STR):
        """Set the vertical scroll mode.

        Args:
            mode: mode to set

        Raises:
            InvalidParamError: invalid scroll mode
        """
        if mode not in SCROLL_MODE:
            raise InvalidParamError(mode, SCROLL_MODE)
        self.setVerticalScrollMode(SCROLL_MODE[mode])

    def num_selected(self) -> int:
        """Return amount of selected rows.

        Returns:
            amount of selected rows
        """
        if self.selectionModel() is None:
            return 0
        return len(self.selectionModel().selectedRows())

    def jump_to_column(self, col_num: int):
        """Make sure column at given index is visible.

        scrolls to column at given index

        Args:
            col_num: column to scroll to
        """
        if self.model() is None:
            return None
        idx = self.model().index(0, col_num)
        self.scrollTo(idx)

    def scroll_to_top(self):
        """Override to use abstractitemview-way of scrolling to top."""
        self.scrollToTop()

    def scroll_to_bottom(self):
        """Override to use abstractitemview-way of scrolling to bottom."""
        self.scrollToBottom()

    def select_last_row(self):
        idx = self.model().createIndex(self.model().rowCount() - 1, 0)
        self.setCurrentIndex(idx)

    def scroll_to(self, index, mode: SCROLL_HINT_STR = "ensure_visible"):
        if mode not in SCROLL_HINT:
            raise InvalidParamError(mode, SCROLL_HINT)
        self.scrollTo(index, SCROLL_HINT[mode])

    def highlight_when_inactive(self):
        """Highlight items when widget does not have focus."""
        p = gui.Palette()
        p.highlight_inactive()
        self.setPalette(p)

from qtpy import QtCore


class ModelIndex(QtCore.QModelIndex):
    def __getitem__(self, flag: int):
        return self.data(flag)

import sys

from PySide6.QtGui import QKeySequence, QShortcut, QClipboard
from PySide6.QtWidgets import QWidget, QTableWidget, QHeaderView, QAbstractItemView, QApplication, QVBoxLayout, \
    QTableWidgetItem


class TableTest(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["차종", "모델명", "업체명", "최종 결제금액"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.layout.addWidget(self.table)
        self.table.setRowCount(10)

        for i in range(0, 10):
            self.table.setItem(i, 0, QTableWidgetItem(f"차종{i}"))
            self.table.setItem(i, 1, QTableWidgetItem(f"모델{i}"))
            self.table.setItem(i, 2, QTableWidgetItem(f"업체{i}"))
            self.table.setItem(i, 3, QTableWidgetItem(f"금액{i}"))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = TableTest()
    window.show()

    sys.exit(app.exec())
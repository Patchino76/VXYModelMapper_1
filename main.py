from PySide6.QtCore import QUrl, QAbstractTableModel, Qt, QModelIndex, QTimer
from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine, qmlRegisterType
from PySide6.QtGui import QColor
from pathlib import Path
import sys
import os
from PySide6.QtCore import QObject, Property, Signal, Slot, QTimer, QPointF


class CustomModel( QAbstractTableModel ):

    dataChanged = Signal(list)

    def __init__( self, parent=None ):
        super().__init__( parent )

        self.column_count = 4
        self.row_count = 15
        self.data_list = [
            [ 19, 73, 16, 92 ],
            [ 68, 62, 58, 76 ],
            [ 115, 14, 111, 18 ],
            [ 153, 45, 165, 16 ],
            [ 217, 39, 207, 61 ],
            [ 265, 53, 255, 68 ],
            [ 302, 52, 312, 81 ],
            [ 360, 4, 364, 48 ],
            [ 419, 72, 416, 8 ],
            [ 458, 66, 466, 4 ],
            [ 502, 78, 515, 0 ],
            [ 558, 14, 553, 54 ],
            [ 616, 53, 606, 22 ],
            [ 657, 80, 661, 95 ],
            [ 700, 24, 704, 7 ]
        ]

    def rowCount( self, parent ):
        return len( self.data_list )

    def columnCount( self, parent ):
        return self.column_count

    def data( self, index, role ):
        if role == Qt.DisplayRole:
            return self.data_list[ index.row() ][ index.column() ]
        elif role == Qt.EditRole:
            return self.data_list[ index.row() ][ index.column() ]
        elif role == Qt.BackgroundRole:
            return QColor( Qt.white )
        

    def update_data(self):
        for i in range(len(self.data)):
            for j in range(self.columnCount(QModelIndex())):
                self.data[i][j] += 1
        self.dataChanged.emit(self.createIndex(0, 0), self.createIndex(self.rowCount(QModelIndex()) - 1,
                                                                        self.columnCount(QModelIndex()) - 1))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    my_model = CustomModel()

    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty("my_model", my_model)

    file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "main.qml")
    engine.load(QUrl.fromLocalFile(file))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())

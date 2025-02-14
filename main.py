import sys
from qtpy import QtWidgets

from ui.mainwindow import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)

window1 = QtWidgets.QMainWindow()
# titel van window
window1.setWindowTitle("Studierendenverwaltung")
# maak een button
button = QtWidgets.QPushButton(window1)
#
button.setText("hallo")
#laat button zien
button.show()
#ui_window = Ui_MainWindow()
#ui_window.setupUi(window1)
# laat window zien test
window1.show()
#exit programma en sluit window
sys.exit(app.exec_())

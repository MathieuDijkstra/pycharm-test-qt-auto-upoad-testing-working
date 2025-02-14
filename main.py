#
# ui converter voor het omzetten van ui bestanden naar py bestanden
#
import sys
from qtpy import QtWidgets
from ui_converter import convert_UI2PY  # Import the convert function

# Call the function to convert .ui files in 'ui1' folder
convert_UI2PY("ui1")

app = QtWidgets.QApplication(sys.argv)

window1 = QtWidgets.QMainWindow()
window1.setWindowTitle("Dit is de titel")

# Assuming 'form' is the file that contains Ui_Widget class
from ui1.form import Ui_Widget
# maak van Ui_Widget een instacie
Ui_window = Ui_Widget()
# teken de inhoud  van de ui in dit venster
Ui_window.setupUi(window1)
window1.show()

# Exit program and close window
sys.exit(app.exec_())

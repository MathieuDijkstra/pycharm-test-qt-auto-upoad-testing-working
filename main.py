#
# ui converter voor het omzetten van ui bestanden naar py bestanden
#
import sys
from qtpy import QtWidgets
from uiToPy_converter import uiToPy_converter  # Import the convert function

# Call the function to convert .ui files in 'ui1' folder
uiToPy_converter("ui1")
# QtWidgets.QApplication
#
#     This creates an application instance, which is required for any Qt-based GUI program.
#     It manages GUI control flow and event handling.
# The QApplication object manages the event loop and resources for the entire application, regardless of how many windows or widgets you have. Multiple windows can be created, but all of them will still share the same event loop and other application-level settings.
#
# When you create additional windows (such as QMainWindow), they are just different widgets or views that will be displayed by the same QApplication.
# Example with Two Windows
#
# You can create and show as many windows as you need while using just a single QApplication instance.
app = QtWidgets.QApplication(sys.argv)


# QtWidgets.QMainWindow()
#
#     This creates an instance of QMainWindow, which is a specialized widget for main windows in a Qt application.
#     A QMainWindow is a type of window that typically includes areas like:
#         Menu Bar
#         Toolbars
#         Status Bar
#         Central Widget (main area for content)
#
# window1 =
#
#     This assigns the QMainWindow object to the variable window1, which allows you to interact with and modify the window's properties later on.
window1 = QtWidgets.QMainWindow()
window1.setWindowTitle("Dit is de titel")

# Assuming 'form' is the file that contains Ui_Widget class
from ui1.form import Ui_Widget
# maak van Ui_Widget een instacie
Ui_window = Ui_Widget()
# teken de inhoud  van de ui in dit venster
Ui_window.setupUi(window1)

#events opvangen en aansturen:
# def on_pusButtonClicked():
#     print("push button clicked")
#     # togle check box object name: checkBox_prg
#     Ui_window.checkBox_prg.toggle()
# Ui_window.pushButton.clicked.connect(on_pusButtonClicked)

Ui_window.pushButton.clicked.connect(Ui_window.checkBox_prg.toggle)

# laat window zien
window1.show()

# Exit program and close window
sys.exit(app.exec_())

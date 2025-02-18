# #
# # ui converter voor het omzetten van ui bestanden naar py bestanden
# #
# import sys
# from qtpy import QtWidgets
# from uiToPy_converter import uiToPy_converter  # Import the convert function
#
# # Assuming 'form' is the file that contains Ui_Widget class
# from ui1.form import Ui_Widget
#
# # Call the function to convert .ui files in 'ui1' folder
# uiToPy_converter("ui1")
# # QtWidgets.QApplication
# #
# #     This creates an application instance, which is required for any Qt-based GUI program.
# #     It manages GUI control flow and event handling.
# # The QApplication object manages the event loop and resources for the entire application, regardless of how many windows or widgets you have. Multiple windows can be created, but all of them will still share the same event loop and other application-level settings.
# #
# # When you create additional windows (such as QMainWindow), they are just different widgets or views that will be displayed by the same QApplication.
# # Example with Two Windows
# #
# # You can create and show as many windows as you need while using just a single QApplication instance.
# app = QtWidgets.QApplication(sys.argv)
#
#
# # QtWidgets.QMainWindow()
# #
# #     This creates an instance of QMainWindow, which is a specialized widget for main windows in a Qt application.
# #     A QMainWindow is a type of window that typically includes areas like:
# #         Menu Bar
# #         Toolbars
# #         Status Bar
# #         Central Widget (main area for content)
# #
# # window1 =
# #
# #     This assigns the QMainWindow object to the variable window1, which allows you to interact with and modify the window's properties later on.
#
# #refactor window to a class erft alle eigenschappen die ook QtWidgets.QMainWindow heeft
# class MainWindow(QtWidgets.QMainWindow):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#
#         # Stel de titel van het venster in
#         self.setWindowTitle("Dit is de titel")
#
#         # Maak een instantie van Ui_Widget en sla deze op in self.ui
#         self.ui = Ui_Widget()
#
#         # Roep de setupUi-methode aan op de Ui_Widget instantie en geef self als parameter door
#         self.ui.setupUi(self)
#
#         # Verbind de knop met de checkbox-toggle functie
#         self.ui.pushButton.clicked.connect(self.ui.checkBox_prg.toggle)
#     # pass heb je alleen nodig als je een lege class hebt ( nu hebben we een functie er in dus kan hij weg
#     #pass
#
# #window1 = QtWidgets.QMainWindow() #class MainWindow(QtWidgets.QMainWindow): is deze regel
#
# window1 = MainWindow()
# # window1.setWindowTitle("Dit is de titel")
#
#
# # maak van Ui_Widget een instacie
# #Ui_window = Ui_Widget()
# # teken de inhoud  van de ui in dit venster
# #Ui_window.setupUi(window1)
#
# #events opvangen en aansturen:
# # def on_pusButtonClicked():
# #     print("push button clicked")
# #     # togle check box object name: checkBox_prg
# #     Ui_window.checkBox_prg.toggle()
# # Ui_window.pushButton.clicked.connect(on_pusButtonClicked)
#
# #Ui_window.pushButton.clicked.connect(Ui_window.checkBox_prg.toggle)
#
# # laat window zien
# window1.show()
#
# # Exit program and close window
# sys.exit(app.exec_())


#
# UI Converter en hoofdprogramma
# Dit programma converteert .ui-bestanden (van QT EDITOR ) om tezetten naar .py-bestanden en bouwt een hoofdvenster
# met een knop die een checkbox togglet. Het programma maakt gebruik van de Qt framework.
#
# Importeer de conversiefunctie die .ui-bestanden omzet naar .py-bestanden
from uiToPy_converter import uiToPy_converter  # Deze functie zorgt ervoor dat wijzigingen in de UI direct zichtbaar zijn
##
### oorspronkelijk programma
##
# Roep de functie aan om alle .ui-bestanden in de map 'ui1' te converteren naar .py-bestanden.
# Dit zorgt ervoor dat de meest recente UI-wijzigingen worden gebruikt.
uiToPy_converter("ui1")

# Import van het sys-module om toegang te krijgen tot argumenten en exit-functionaliteit
import sys
# Importeer QtWidgets uit qtpy voor het bouwen van de GUI
from qtpy import QtWidgets

# Importeer de Ui_Widget klasse die gegenereerd is vanuit het .ui-bestand (bijvoorbeeld form.ui)
# Het bestand form.py is het resultaat van de conversie en bevat de definitie van de UI.
# note! ui1 = de derectory,   form = form.py bestand in die derectory
# note import Ui_Widget is de class in form.py!
from ui1.form import Ui_Widget

# Maak een QApplication object aan.
# Dit object beheert de event loop, systeemresources en zorgt ervoor dat de GUI correct functioneert.
app = QtWidgets.QApplication(sys.argv)

# Definieer de MainWindow klasse, die erft van QtWidgets.QMainWindow.
# Dit zorgt ervoor dat we alle standaard functionaliteiten van een hoofdvenster van Qt erven.
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        # Roep de constructor van de ouderklasse aan om het hoofdvenster correct te initialiseren.
        super().__init__(parent)

        # Stel de titel van het venster in. Deze tekst verschijnt in de titelbalk van het venster.
        self.setWindowTitle("Dit is de titel")

        # Maak een instantie van de Ui_Widget klasse aan en bewaar deze in self.ui.
        # Deze instantie bevat alle widgets en layouts zoals gedefinieerd in het .ui bestand.
        self.ui = Ui_Widget()

        # Bouw de user interface in dit hoofdvenster.
        # De setupUi methode plaatst alle widgets en layouts in 'self', wat ons hoofdvenster is.
        self.ui.setupUi(self)

        # Verbind de clicked signal van de pushButton met de toggle methode van checkBox_prg.
        # Dit betekent dat wanneer de pushButton wordt aangeklikt, de checkbox van staat verandert.
        self.ui.pushButton.clicked.connect(self.ui.checkBox_prg.toggle)
        # stuur deze text naar dit lineEdit element
        self.ui.lineEdit.setText("!!!")
        #
        ## als er op
        #
        self.ui.buttonReadLine.clicked.connect(self.on_buttonReadLineClick)
    #
    # on click function
    #
    def on_buttonReadLineClick(self):
        print("op buttonReadLine geklikt invoer was:" +  self.ui.lineEdit.text() )



# Dit creëert ons hoofdvenster met de eerder gedefinieerde UI en functionaliteiten.
window1 = MainWindow()

# Toon het hoofdvenster op het scherm.
window1.show()

# Start de event loop van de applicatie.
# Deze loop zorgt ervoor dat het programma blijft draaien en reageert op gebruikersinteracties.
sys.exit(app.exec_())

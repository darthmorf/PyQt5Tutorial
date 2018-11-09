import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi # Import all PyQt5 Widgets

class MainWindow(QMainWindow): # Create a 'mainWindow' class that inherits from the PyQt equivalent
    def __init__(self, *args): 
        super().__init__(*args) # Pass the window arguments to the Qt Class - we don't need it
        loadUi("TestApp_MainUI.ui", self) # Load UI layout from file
        
        self.myButton.clicked.connect(lambda: self.updateLabelText("Button was clicked!"))
        self.openDialogButton.clicked.connect(lambda: self.openPopupDialog())
        self.show() # Show the window

    def updateLabelText(self, text):
        self.myLabel.setText(text)
        self.myButton.setText("I did stuff :D")

    def openPopupDialog(self):
        self.popupDialog = PopupDialog(self)

class PopupDialog(QDialog):
    def __init__(self, *args): 
        super().__init__(*args) 
        loadUi("TestApp_Dialog.ui", self) # Load UI layout from file
        self.setModal(True) # If a dialog is modal, it means you cannot interact with the main window while it is open
        self.show()

app = QApplication(sys.argv) # Create a PyQt app
mainWindow = MainWindow() # Initialise the MainWindow
sys.exit(app.exec_()) # Wait for the app to close, then close the program

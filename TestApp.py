import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * # Import all PyQt5 Widgets

class MainWindow(QMainWindow): # Create a 'mainWindow' class that inherits from the PyQt equivalent
    def __init__(self, *args): 
        super().__init__(*args) # Pass the window arguments to the Qt Class - we don't need it
        self.resize(500, 200) # Set the window size
        self.setWindowTitle("Hello Word")
        self.setWindowIcon(QIcon("icon.png"))

        self.label = QLabel("PyQt > tKinter!", self) # Create a new label element
        self.button = QPushButton("I do stuff :)", self) # Create a new button
        self.button.move(0, 50) # Move the button 50 pixels down
        self.button.clicked.connect(lambda: self.updateLabelText("Button was clicked!"))
        self.show() # Show the window

    def updateLabelText(self, text):
        self.label.setText(text)
        self.button.setText("I did stuff :D")


app = QApplication(sys.argv) # Create a PyQt app
mainWindow = MainWindow() # Initialise the MainWindow
sys.exit(app.exec_()) # Wait for the app to close, then close the program

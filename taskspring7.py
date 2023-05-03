from PyQt6.QtWidgets import (
QApplication, QMainWindow, QVBoxLayout, QLineEdit, 
QPushButton, QWidget, QGridLayout, QWidget
)
from functools import partial
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("gcd calculator")
        self.generallayout = QVBoxLayout()
        centralwidget = QWidget(self)
        centralwidget.setLayout(self.generallayout)
        self.setCentralWidget(centralwidget)
        self.createdisplay1()
        self.createdisplay2()
        self.createbuttons()

    def createbuttons(self):
        self.buttonmap = {}
        buttonslayout = QGridLayout()
        keyboard = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"],
            ["0", " "],
            ["calculate", "clear"], 
        ]

        for r, ks in enumerate(keyboard):
            for c, k in enumerate(ks):
                self.buttonmap[k] = QPushButton(k)
                self.buttonmap[k].setFixedSize(60, 30)
                buttonslayout.addWidget(self.buttonmap[k], r, c)

        self.generallayout.addLayout(buttonslayout)
  
    def createdisplay1(self):
        self.display1 = QLineEdit()
        self.display1.setFixedHeight(30)
        self.display1.setReadOnly(True)
        self.display1.setPlaceholderText("enter numbers")
        self.generallayout.addWidget(self.display1)

    def createdisplay2(self):
        self.display2 = QLineEdit()
        self.display2.setFixedHeight(30)
        self.display2.setReadOnly(True)
        self.display2.setPlaceholderText("gcd")
        self.generallayout.addWidget(self.display2)        
    
 
    def setdisplaytext1(self, text):
        self.display1.setText(text)
        self.display1.setFocus()
    
    def getdisplaytext1(self):
        return self.display1.text()
    
    def setdisplaytext2(self, text):
        self.display2.setText(text)
        self.display2.setFocus()
    
    def cleardisplay(self):
        self.setdisplaytext1("")
        self.setdisplaytext2("")
    

def findgcd(stroka):
    n = stroka.split()
    def funct(a, b):
        if a > b:
            t = a
            a = b
            b = t

        if a==0:
            return b
        else:
            return funct(b%a, a)
    
    result = str(funct(int(n[0]), int(n[1])))
    return result

class calculation:
    def __init__(self, gcd, view):
        self._gcd=gcd
        self._view = view
        self.connectbuttons()
    
    def solving(self):
        answer = self._gcd(self._view.getdisplaytext1())
        self._view.setdisplaytext2(answer)
    
    def enternumber(self, digit):
        number = self._view.getdisplaytext1()+digit
        self._view.setdisplaytext1(number)
 
    def connectbuttons(self):
        for k, b in self._view.buttonmap.items():
            if k not in {"calculate", "clear"}:
                b.clicked.connect(
                    partial(self.enternumber, k)
                )
        self._view.buttonmap["calculate"].clicked.connect(self.solving)
        self._view.buttonmap["clear"].clicked.connect(self._view.cleardisplay)



def main():
    app = QApplication([])
    window = Window()
    window.show()
    calculation(gcd=findgcd, view=window)
    sys.exit(app.exec())

if __name__=="__main__":
    main()

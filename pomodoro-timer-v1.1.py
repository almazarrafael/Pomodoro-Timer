from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from PyQt5.QtCore import *
import sys

timeStudy = 500
timeBreak = 500
numSec = 500
currentMode = "Study"

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(638, 297)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(20, 20, 421, 241))
        self.lcdNumber.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber.setProperty("intValue", 500)
        self.lcdNumber.setObjectName("lcdNumber")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(460, 20, 161, 241))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 60, 111, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 110, 111, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 160, 111, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 31, 16))
        self.label_3.setObjectName("label_3")
        self.spinBox = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox.setGeometry(QtCore.QRect(10, 30, 91, 21))
        self.spinBox.setMaximum(9999)
        self.spinBox.setProperty("value", 500)
        self.spinBox.setObjectName("spinBox")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(105, 35, 41, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(110, 120, 41, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(15, 95, 41, 16))
        self.label_6.setObjectName("label_6")
        self.spinBox_2 = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox_2.setGeometry(QtCore.QRect(15, 115, 91, 21))
        self.spinBox_2.setMaximum(9999)
        self.spinBox_2.setProperty("value", 500)
        self.spinBox_2.setObjectName("spinBox_2")
        self.checkBox = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox.setGeometry(QtCore.QRect(40, 180, 81, 17))
        self.checkBox.setObjectName("checkBox")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 55, 91, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(30, 140, 91, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.tabWidget.addTab(self.tab_2, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(25, 260, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 260, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 30, 47, 13))
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 638, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.startButton)
        self.pushButton_2.clicked.connect(self.stopButton)
        self.pushButton_3.clicked.connect(self.resetButton)
        self.pushButton_4.clicked.connect(self.changeMode)

        self.pushButton_5.clicked.connect(self.updateStudyTime)
        # self.pushButton_6.clicked.connect(self.updateBreakTime)

        self.timer = QTimer()
        self.timer.timeout.connect(self.updateLCD)

        self.url = QtCore.QUrl.fromLocalFile("./juntos.mp3")
        self.content = QtMultimedia.QMediaContent(self.url)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(self.content)
        self.pushButton_6.clicked.connect(self.play)

    def play(self):
        self.player.play()

    def changeMode(self):
        global timeStudy, timeBreak, currentMode
        if currentMode == "Study":
            currentMode = "Break"
            self.resetButton()
        else:
            currentMode = "Study"
            self.resetButton()
        self.label_2.setText(currentMode)

    def resetButton(self):
        global numSec, timeStudy, timeBreak
        self.label_7.setText("Paused")

        if currentMode == "Study":
            numSec = timeStudy
        else:
            numSec = timeBreak

        self.label_2.setText(currentMode)
        self.lcdNumber.display(numSec)

        self.stopButton()

    def updateStudyTime(self):
        global timeStudy, currentMode
        if self.label_7.text() == "Running..":
            return
        timeStudy = self.spinBox.value()
        currentMode = "Study"
        self.resetButton()

    def updateBreakTime(self):
        global timeBreak, currentMode
        if self.label_7.text() == "Running..":
            return
        timeBreak = self.spinBox_2.value()
        currentMode = "Break"
        self.resetButton()

    def startButton(self):
        self.timer.start(1000)
        self.label_7.setText("Running..")
        if currentMode == "Study":
            self.label_2.setText("Study")
        else:
            self.label_2.setText("Break")

    def stopButton(self):
        self.timer.stop()
        self.label_7.setText("Paused")

    def updateLCD(self):
        global numSec
        if numSec == 0:
            self.stopButton()
        self.lcdNumber.display(numSec)
        numSec -= 1

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pomodoro Timer - Rafael Almazar"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.pushButton_2.setText(_translate("MainWindow", "Stop"))
        self.pushButton_3.setText(_translate("MainWindow", "Reset"))
        self.pushButton_4.setText(_translate("MainWindow", "Change Mode"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Home"))
        self.label_3.setText(_translate("MainWindow", "Study:"))
        self.label_4.setText(_translate("MainWindow", "seconds"))
        self.label_5.setText(_translate("MainWindow", "seconds"))
        self.label_6.setText(_translate("MainWindow", "Break:"))
        self.checkBox.setText(_translate("MainWindow", "Alert Sound"))
        self.pushButton_5.setText(_translate("MainWindow", "Save and Reset"))
        self.pushButton_6.setText(_translate("MainWindow", "Save and Reset"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Settings"))
        self.label.setText(_translate("MainWindow", "Current Mode:"))
        self.label_2.setText(_translate("MainWindow", "Study"))
        self.label_7.setText(_translate("MainWindow", "Paused"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
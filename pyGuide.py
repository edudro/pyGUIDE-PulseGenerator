# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyGuide.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(787, 616)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 80, 721, 471))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setGeometry(QtCore.QRect(0, 60, 741, 251))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frame_3 = QtWidgets.QFrame(self.frame_5)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 741, 251))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame_3)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 721, 251))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber_2.setMidLineWidth(0)
        self.lcdNumber_2.setProperty("intValue", 20)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.verticalLayout.addWidget(self.lcdNumber_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.dial_2 = QtWidgets.QDial(self.horizontalLayoutWidget)
        self.dial_2.setMinimum(1)
        self.dial_2.setMaximum(50)
        self.dial_2.setSliderPosition(20)
        self.dial_2.setObjectName("dial_2")
        self.horizontalLayout.addWidget(self.dial_2)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 310, 721, 171))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(70, 20, 271, 121))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_5.setGeometry(QtCore.QRect(380, 20, 291, 121))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(100, 10, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(550, 30, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(670, 540, 71, 41))
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 787, 22))
        self.menubar.setObjectName("menubar")
        self.menuHome = QtWidgets.QMenu(self.menubar)
        self.menuHome.setObjectName("menuHome")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout_this_app = QtWidgets.QAction(MainWindow)
        self.actionAbout_this_app.setObjectName("actionAbout_this_app")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setText("")
        self.actionExport.setObjectName("actionExport")
        self.menuHome.addAction(self.actionAbout_this_app)
        self.menubar.addAction(self.menuHome.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dial_2.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_4.setText(_translate("MainWindow", "START"))
        self.pushButton_5.setText(_translate("MainWindow", "STOP"))
        self.label_3.setText(_translate("MainWindow", "Frequency"))
        self.label_5.setText(_translate("MainWindow", "Digitimer DS8R"))
        self.label_7.setText(_translate("MainWindow", "version 1.0"))
        self.menuHome.setTitle(_translate("MainWindow", "Home"))
        self.actionAbout_this_app.setText(_translate("MainWindow", "About this app"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))

    """
    UI functions
    """
    def setFrequency_Dial2(self, MainWindow):

        self.lcdNumber_2.display(self.dial_2.sliderPosition())

    def ChangeButton4Color(self):

        self.pushButton_5.setStyleSheet("")    #Reset button color
        self.pushButton_4.setStyleSheet("Background-color: green")

    def ChangeButton5Color(self):

        self.pushButton_4.setStyleSheet("")   #Reset button color
        self.pushButton_5.setStyleSheet("Background-color: red")

    """
    PyDAQmx functions
    """

    def GetPulseTrain(self):

        self.pulse_gene1 =  TrainGeneration.ContinuousPulseTrainGeneration(self.dial_2.sliderPosition()
                                                                           ,0.1, 
                                                                           "Dev1/ctr0", 
                                                                           reset=True)
        print("Pulse generator")

    def StartPulse(self):

        self.pulse_gene1.start()
        print("Start pulse")

    def StopPulse(self):

        self.pulse_gene1.stop()
        self.pulse_gene1.clear()
        print("Stop pulse")

if __name__ == "__main__":
    import sys
    import TrainGeneration


    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    """
    Dials
    """
    ui.dial_2.valueChanged.connect(ui.setFrequency_Dial2)


    """
    Buttons 4 and 5
    """
    ui.pushButton_4.clicked.connect(ui.GetPulseTrain)
    ui.pushButton_4.clicked.connect(ui.StartPulse)
    ui.pushButton_4.clicked.connect(ui.ChangeButton4Color)
    ui.pushButton_5.clicked.connect(ui.StopPulse)
    ui.pushButton_5.clicked.connect(ui.ChangeButton5Color)

    MainWindow.show()
    sys.exit(app.exec_())


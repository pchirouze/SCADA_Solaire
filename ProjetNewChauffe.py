# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProjetNewChauffe.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(747, 513)
        Dialog.setAutoFillBackground(True)
        Dialog.setStyleSheet("")
        self.label_T_ext = QtWidgets.QLabel(Dialog)
        self.label_T_ext.setGeometry(QtCore.QRect(450, 490, 121, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_T_ext.setFont(font)
        self.label_T_ext.setObjectName("label_T_ext")
        self.label_T_salon = QtWidgets.QLabel(Dialog)
        self.label_T_salon.setGeometry(QtCore.QRect(440, 470, 131, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_T_salon.setFont(font)
        self.label_T_salon.setStyleSheet("")
        self.label_T_salon.setTextFormat(QtCore.Qt.AutoText)
        self.label_T_salon.setScaledContents(True)
        self.label_T_salon.setObjectName("label_T_salon")
        self.label_synoptique = QtWidgets.QLabel(Dialog)
        self.label_synoptique.setGeometry(QtCore.QRect(0, 0, 747, 516))
        self.label_synoptique.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.label_synoptique.setStyleSheet("background-image: url(:/images/cuve.jpeg);\n"
"\n"
"")
        self.label_synoptique.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_synoptique.setLineWidth(1)
        self.label_synoptique.setText("")
        self.label_synoptique.setObjectName("label_synoptique")
        self.display_T_Salon = QtWidgets.QLabel(Dialog)
        self.display_T_Salon.setGeometry(QtCore.QRect(570, 470, 51, 21))
        self.display_T_Salon.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(209, 213, 231);")
        self.display_T_Salon.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.display_T_Salon.setAlignment(QtCore.Qt.AlignCenter)
        self.display_T_Salon.setObjectName("display_T_Salon")
        self.display_T_ext = QtWidgets.QLabel(Dialog)
        self.display_T_ext.setGeometry(QtCore.QRect(570, 490, 51, 21))
        self.display_T_ext.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(209, 213, 231);")
        self.display_T_ext.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.display_T_ext.setAlignment(QtCore.Qt.AlignCenter)
        self.display_T_ext.setObjectName("display_T_ext")
        self.display_T_pan_sol = QtWidgets.QLabel(Dialog)
        self.display_T_pan_sol.setGeometry(QtCore.QRect(650, 73, 51, 21))
        self.display_T_pan_sol.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(209, 213, 231);")
        self.display_T_pan_sol.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.display_T_pan_sol.setAlignment(QtCore.Qt.AlignCenter)
        self.display_T_pan_sol.setObjectName("display_T_pan_sol")
        self.display_T_cuve_h = QtWidgets.QLabel(Dialog)
        self.display_T_cuve_h.setGeometry(QtCore.QRect(390, 47, 51, 21))
        self.display_T_cuve_h.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(209, 213, 231);")
        self.display_T_cuve_h.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.display_T_cuve_h.setAlignment(QtCore.Qt.AlignCenter)
        self.display_T_cuve_h.setObjectName("display_T_cuve_h")
        self.display_T_cuve_m = QtWidgets.QLabel(Dialog)
        self.display_T_cuve_m.setGeometry(QtCore.QRect(390, 210, 51, 21))
        self.display_T_cuve_m.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(209, 213, 231);")
        self.display_T_cuve_m.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.display_T_cuve_m.setAlignment(QtCore.Qt.AlignCenter)
        self.display_T_cuve_m.setObjectName("display_T_cuve_m")
        self.display_T_cuve_b = QtWidgets.QLabel(Dialog)
        self.display_T_cuve_b.setGeometry(QtCore.QRect(390, 423, 51, 21))
        self.display_T_cuve_b.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(209, 213, 231);")
        self.display_T_cuve_b.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.display_T_cuve_b.setAlignment(QtCore.Qt.AlignCenter)
        self.display_T_cuve_b.setObjectName("display_T_cuve_b")
        self.display_T_v3v = QtWidgets.QLabel(Dialog)
        self.display_T_v3v.setGeometry(QtCore.QRect(170, 50, 51, 21))
        self.display_T_v3v.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(209, 213, 231);")
        self.display_T_v3v.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.display_T_v3v.setAlignment(QtCore.Qt.AlignCenter)
        self.display_T_v3v.setObjectName("display_T_v3v")
        self.display_T_ret_panel = QtWidgets.QLabel(Dialog)
        self.display_T_ret_panel.setGeometry(QtCore.QRect(570, 408, 51, 21))
        self.display_T_ret_panel.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(209, 213, 231);")
        self.display_T_ret_panel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.display_T_ret_panel.setAlignment(QtCore.Qt.AlignCenter)
        self.display_T_ret_panel.setObjectName("display_T_ret_panel")
        self.display_T_dep_panel = QtWidgets.QLabel(Dialog)
        self.display_T_dep_panel.setGeometry(QtCore.QRect(510, 345, 51, 21))
        self.display_T_dep_panel.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(209, 213, 231);")
        self.display_T_dep_panel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.display_T_dep_panel.setAlignment(QtCore.Qt.AlignCenter)
        self.display_T_dep_panel.setObjectName("display_T_dep_panel")
        self.progressBar_Pos_v3v = QtWidgets.QProgressBar(Dialog)
        self.progressBar_Pos_v3v.setGeometry(QtCore.QRect(240, 10, 118, 21))
        self.progressBar_Pos_v3v.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar_Pos_v3v.setAutoFillBackground(False)
        self.progressBar_Pos_v3v.setStyleSheet("background-color: rgb(204, 204, 204);\n"
"color: rgb(255, 0, 0);")
        self.progressBar_Pos_v3v.setProperty("value", 0)
        self.progressBar_Pos_v3v.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.progressBar_Pos_v3v.setTextVisible(True)
        self.progressBar_Pos_v3v.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar_Pos_v3v.setInvertedAppearance(False)
        self.progressBar_Pos_v3v.setObjectName("progressBar_Pos_v3v")
        self.display_P_solaire = QtWidgets.QLabel(Dialog)
        self.display_P_solaire.setGeometry(QtCore.QRect(650, 240, 61, 21))
        self.display_P_solaire.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(209, 213, 231);")
        self.display_P_solaire.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.display_P_solaire.setAlignment(QtCore.Qt.AlignCenter)
        self.display_P_solaire.setObjectName("display_P_solaire")
        self.display_E_solaire = QtWidgets.QLabel(Dialog)
        self.display_E_solaire.setGeometry(QtCore.QRect(640, 300, 81, 21))
        self.display_E_solaire.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(209, 213, 231);")
        self.display_E_solaire.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.display_E_solaire.setAlignment(QtCore.Qt.AlignCenter)
        self.display_E_solaire.setObjectName("display_E_solaire")
        self.display_E_HP_chauffage = QtWidgets.QLabel(Dialog)
        self.display_E_HP_chauffage.setGeometry(QtCore.QRect(360, 290, 111, 21))
        self.display_E_HP_chauffage.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(209, 213, 231);")
        self.display_E_HP_chauffage.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.display_E_HP_chauffage.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.display_E_HP_chauffage.setObjectName("display_E_HP_chauffage")
        self.Led_Pompe_Chauffage = QtWidgets.QLabel(Dialog)
        self.Led_Pompe_Chauffage.setGeometry(QtCore.QRect(220, 426, 15, 15))
        self.Led_Pompe_Chauffage.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.Led_Pompe_Chauffage.setFrameShape(QtWidgets.QFrame.Box)
        self.Led_Pompe_Chauffage.setText("")
        self.Led_Pompe_Chauffage.setObjectName("Led_Pompe_Chauffage")
        self.Led_Pompe_Solaire = QtWidgets.QLabel(Dialog)
        self.Led_Pompe_Solaire.setGeometry(QtCore.QRect(535, 412, 15, 15))
        self.Led_Pompe_Solaire.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.Led_Pompe_Solaire.setFrameShape(QtWidgets.QFrame.Box)
        self.Led_Pompe_Solaire.setText("")
        self.Led_Pompe_Solaire.setObjectName("Led_Pompe_Solaire")
        self.Led_thermoplongeur = QtWidgets.QLabel(Dialog)
        self.Led_thermoplongeur.setGeometry(QtCore.QRect(288, 262, 15, 15))
        self.Led_thermoplongeur.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.Led_thermoplongeur.setFrameShape(QtWidgets.QFrame.Box)
        self.Led_thermoplongeur.setText("")
        self.Led_thermoplongeur.setObjectName("Led_thermoplongeur")
        self.lineEdit_Consigne = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_Consigne.setGeometry(QtCore.QRect(570, 450, 51, 21))
        self.lineEdit_Consigne.setMouseTracking(True)
        self.lineEdit_Consigne.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_Consigne.setStyleSheet("background-color: rgb(185, 255, 199);")
        self.lineEdit_Consigne.setCursorPosition(6)
        self.lineEdit_Consigne.setObjectName("lineEdit_Consigne")
        self.pushButton_Cde_Chauffage = QtWidgets.QPushButton(Dialog)
        self.pushButton_Cde_Chauffage.setGeometry(QtCore.QRect(20, 480, 101, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Cde_Chauffage.setFont(font)
        self.pushButton_Cde_Chauffage.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_Cde_Chauffage.setObjectName("pushButton_Cde_Chauffage")
        self.label_Consigne = QtWidgets.QLabel(Dialog)
        self.label_Consigne.setGeometry(QtCore.QRect(460, 450, 101, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_Consigne.setFont(font)
        self.label_Consigne.setStyleSheet("")
        self.label_Consigne.setTextFormat(QtCore.Qt.AutoText)
        self.label_Consigne.setScaledContents(True)
        self.label_Consigne.setObjectName("label_Consigne")
        self.pushButton_Quit = QtWidgets.QPushButton(Dialog)
        self.pushButton_Quit.setGeometry(QtCore.QRect(650, 480, 80, 27))
        self.pushButton_Quit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_Quit.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_Quit.setObjectName("pushButton_Quit")
        self.label_etat_comm = QtWidgets.QLabel(Dialog)
        self.label_etat_comm.setGeometry(QtCore.QRect(30, 6, 201, 20))
        self.label_etat_comm.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_etat_comm.setMidLineWidth(2)
        self.label_etat_comm.setText("")
        self.label_etat_comm.setObjectName("label_etat_comm")
        self.Led_refresh_chauffage = QtWidgets.QLabel(Dialog)
        self.Led_refresh_chauffage.setGeometry(QtCore.QRect(10, 10, 15, 15))
        self.Led_refresh_chauffage.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.Led_refresh_chauffage.setFrameShape(QtWidgets.QFrame.Box)
        self.Led_refresh_chauffage.setText("")
        self.Led_refresh_chauffage.setObjectName("Led_refresh_chauffage")
        self.Led_refresh_solaire = QtWidgets.QLabel(Dialog)
        self.Led_refresh_solaire.setGeometry(QtCore.QRect(720, 10, 15, 15))
        self.Led_refresh_solaire.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.Led_refresh_solaire.setFrameShape(QtWidgets.QFrame.Box)
        self.Led_refresh_solaire.setText("")
        self.Led_refresh_solaire.setObjectName("Led_refresh_solaire")
        self.display_T_cons_eau = QtWidgets.QLabel(Dialog)
        self.display_T_cons_eau.setGeometry(QtCore.QRect(170, 30, 51, 21))
        self.display_T_cons_eau.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(185, 255, 199);")
        self.display_T_cons_eau.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.display_T_cons_eau.setAlignment(QtCore.Qt.AlignCenter)
        self.display_T_cons_eau.setObjectName("display_T_cons_eau")
        self.Display_I_Inst = QtWidgets.QLabel(Dialog)
        self.Display_I_Inst.setGeometry(QtCore.QRect(40, 30, 131, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Display_I_Inst.setFont(font)
        self.Display_I_Inst.setObjectName("Display_I_Inst")
        self.checkBox_Mode_Regul = QtWidgets.QCheckBox(Dialog)
        self.checkBox_Mode_Regul.setGeometry(QtCore.QRect(20, 460, 241, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_Mode_Regul.setFont(font)
        self.checkBox_Mode_Regul.setChecked(True)
        self.checkBox_Mode_Regul.setObjectName("checkBox_Mode_Regul")
        self.display_PA_compteurEDF = QtWidgets.QLabel(Dialog)
        self.display_PA_compteurEDF.setGeometry(QtCore.QRect(220, 490, 71, 21))
        self.display_PA_compteurEDF.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(209, 213, 231);")
        self.display_PA_compteurEDF.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.display_PA_compteurEDF.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.display_PA_compteurEDF.setObjectName("display_PA_compteurEDF")
        self.label_Consigne_2 = QtWidgets.QLabel(Dialog)
        self.label_Consigne_2.setGeometry(QtCore.QRect(130, 490, 91, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_Consigne_2.setFont(font)
        self.label_Consigne_2.setStyleSheet("")
        self.label_Consigne_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_Consigne_2.setScaledContents(True)
        self.label_Consigne_2.setObjectName("label_Consigne_2")
        self.Led_HeuresCreuses = QtWidgets.QLabel(Dialog)
        self.Led_HeuresCreuses.setGeometry(QtCore.QRect(390, 460, 16, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Led_HeuresCreuses.setFont(font)
        self.Led_HeuresCreuses.setStyleSheet("background-color: rgb(249, 255, 246);")
        self.Led_HeuresCreuses.setFrameShape(QtWidgets.QFrame.Box)
        self.Led_HeuresCreuses.setText("")
        self.Led_HeuresCreuses.setAlignment(QtCore.Qt.AlignCenter)
        self.Led_HeuresCreuses.setObjectName("Led_HeuresCreuses")
        self.label_Consigne_3 = QtWidgets.QLabel(Dialog)
        self.label_Consigne_3.setGeometry(QtCore.QRect(280, 460, 101, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_Consigne_3.setFont(font)
        self.label_Consigne_3.setStyleSheet("")
        self.label_Consigne_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_Consigne_3.setScaledContents(True)
        self.label_Consigne_3.setObjectName("label_Consigne_3")
        self.display_E_HC_chauffage = QtWidgets.QLabel(Dialog)
        self.display_E_HC_chauffage.setGeometry(QtCore.QRect(360, 310, 111, 21))
        self.display_E_HC_chauffage.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(209, 213, 231);")
        self.display_E_HC_chauffage.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.display_E_HC_chauffage.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.display_E_HC_chauffage.setObjectName("display_E_HC_chauffage")
        self.display_P_Chauffe = QtWidgets.QLabel(Dialog)
        self.display_P_Chauffe.setGeometry(QtCore.QRect(380, 240, 71, 21))
        self.display_P_Chauffe.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(209, 213, 231);")
        self.display_P_Chauffe.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.display_P_Chauffe.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.display_P_Chauffe.setObjectName("display_P_Chauffe")
        self.label_Consigne_4 = QtWidgets.QLabel(Dialog)
        self.label_Consigne_4.setGeometry(QtCore.QRect(300, 490, 91, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_Consigne_4.setFont(font)
        self.label_Consigne_4.setStyleSheet("")
        self.label_Consigne_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_Consigne_4.setScaledContents(True)
        self.label_Consigne_4.setObjectName("label_Consigne_4")
        self.display_I_Inst = QtWidgets.QLabel(Dialog)
        self.display_I_Inst.setGeometry(QtCore.QRect(390, 490, 51, 21))
        self.display_I_Inst.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(209, 213, 231);")
        self.display_I_Inst.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.display_I_Inst.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.display_I_Inst.setObjectName("display_I_Inst")
        self.label_synoptique.raise_()
        self.label_T_ext.raise_()
        self.label_T_salon.raise_()
        self.display_T_Salon.raise_()
        self.display_T_ext.raise_()
        self.display_T_pan_sol.raise_()
        self.display_T_cuve_h.raise_()
        self.display_T_cuve_m.raise_()
        self.display_T_cuve_b.raise_()
        self.display_T_v3v.raise_()
        self.display_T_ret_panel.raise_()
        self.display_T_dep_panel.raise_()
        self.progressBar_Pos_v3v.raise_()
        self.display_P_solaire.raise_()
        self.display_E_solaire.raise_()
        self.display_E_HP_chauffage.raise_()
        self.Led_Pompe_Chauffage.raise_()
        self.Led_Pompe_Solaire.raise_()
        self.Led_thermoplongeur.raise_()
        self.lineEdit_Consigne.raise_()
        self.pushButton_Cde_Chauffage.raise_()
        self.label_Consigne.raise_()
        self.pushButton_Quit.raise_()
        self.label_etat_comm.raise_()
        self.Led_refresh_chauffage.raise_()
        self.Led_refresh_solaire.raise_()
        self.display_T_cons_eau.raise_()
        self.Display_I_Inst.raise_()
        self.checkBox_Mode_Regul.raise_()
        self.display_PA_compteurEDF.raise_()
        self.label_Consigne_2.raise_()
        self.Led_HeuresCreuses.raise_()
        self.label_Consigne_3.raise_()
        self.display_E_HC_chauffage.raise_()
        self.display_P_Chauffe.raise_()
        self.label_Consigne_4.raise_()
        self.display_I_Inst.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Synoptique chauffage et solaire"))
        self.label_T_ext.setText(_translate("Dialog", "Température ext.  :"))
        self.label_T_salon.setText(_translate("Dialog", "Température salon  :"))
        self.display_T_Salon.setText(_translate("Dialog", "xx.x°C"))
        self.display_T_ext.setText(_translate("Dialog", "xx.x°C"))
        self.display_T_pan_sol.setText(_translate("Dialog", "xx.x°C"))
        self.display_T_cuve_h.setText(_translate("Dialog", "xx.x°C"))
        self.display_T_cuve_m.setText(_translate("Dialog", "xx.x°C"))
        self.display_T_cuve_b.setText(_translate("Dialog", "xx.x°C"))
        self.display_T_v3v.setText(_translate("Dialog", "xx.x°C"))
        self.display_T_ret_panel.setText(_translate("Dialog", "xx.x°C"))
        self.display_T_dep_panel.setText(_translate("Dialog", "xx.x°C"))
        self.progressBar_Pos_v3v.setFormat(_translate("Dialog", "%p%"))
        self.display_P_solaire.setText(_translate("Dialog", "xx.x kW"))
        self.display_E_solaire.setText(_translate("Dialog", "xx.x kWh/J"))
        self.display_E_HP_chauffage.setText(_translate("Dialog", "xx.x kWh"))
        self.lineEdit_Consigne.setText(_translate("Dialog", "19.5°C"))
        self.pushButton_Cde_Chauffage.setText(_translate("Dialog", "MARCHE"))
        self.label_Consigne.setText(_translate("Dialog", "Consigne salon  :"))
        self.pushButton_Quit.setText(_translate("Dialog", "Quitter"))
        self.display_T_cons_eau.setText(_translate("Dialog", "xx.x°C"))
        self.Display_I_Inst.setText(_translate("Dialog", "Consigne Temp Eau :"))
        self.checkBox_Mode_Regul.setText(_translate("Dialog", "Regul. uniquement sur Temp ext."))
        self.display_PA_compteurEDF.setText(_translate("Dialog", "xxxx VA"))
        self.label_Consigne_2.setText(_translate("Dialog", "PApp_Compt. :"))
        self.label_Consigne_3.setText(_translate("Dialog", "Heures Creuses : "))
        self.display_E_HC_chauffage.setText(_translate("Dialog", "xx.x kWh"))
        self.display_P_Chauffe.setText(_translate("Dialog", "xxxx.x kW"))
        self.label_Consigne_4.setText(_translate("Dialog", "PInst compt. :"))
        self.display_I_Inst.setText(_translate("Dialog", "xx A"))


import RessourceFile_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

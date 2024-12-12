#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2017 Patrice <patrice.chirouze@free.fr>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#------------------------------------------------------------------------------------------------------------------------------
# SI MODIFICATION INTERFACE GRAPHIQUE IL FAUT REGENERER LE CODE PYTHON A PARTIR DU CODE .UI VIA LA LIGNE DE COMMANDE SUIVANTE
#                pyuic5 ProjetNewChauffe.ui -x -o ProjetNewChauffe.py
#------------------------------------------------------------------------------------------------------------------------------

import json
from PyQt5.QtWidgets import *
import sys
import time
# --- importation du fichier de description GUI ---
from PyQt5.QtGui import *
from PyQt5.QtCore import * # inclut QTimer..
#from PyQt5 import uic
from ProjetNewChauffe import *
import paho.mqtt.client as mqtt


#DEBUG = True
DEBUG = False

# Avec broker MQTT mosquitto sur Raspberry PI 4
# MQTT_SERVER = '88.124.136.85'  # Accès remote IP box et redirection port routeur box (connexion ADSL)
MQTT_SERVER = '88.185.240.171'  # Accès remote IP box et redirection port routeur box (connexion fibre)
MQTT_PORT = 17100              # Accès remote IP box et redirection port routeur box
#MQTT_SERVER = '192.168.0.41'    # Accès local IP fixe Raspberry 
#MQTT_PORT = 1883                # Accès local IP fixe Raspberry

MQTT_USER = ''
MQTT_USER = ''
MQTT_PASSW = ''

# Variables globales
data_chauffage={}
data_solaire = {}
new_mes_chauffe = False
new_mes_solaire = False
connected = False

# Utiliser par MQTT (fonction avec callback si erreur)
def on_connect(self, client, userdata,rc):
    global connected
    connected = True
    print('Connecté')
    
    
def on_message(client, userdata, msg):
    global data_chauffage, data_solaire, new_mes_chauffe, new_mes_solaire
    if DEBUG: print(msg.topic, msg.payload)
    if msg.topic == '/regchauf/mesur':
        data_chauffage = json.loads(msg.payload)
        new_mes_chauffe = True
    if msg.topic == '/regsol/mesur':
        data_solaire = json.loads(msg.payload)
        new_mes_solaire = True

class myApp(QWidget, Ui_Dialog):

    def __init__(self, parent=None):
        global connected
        Ui_Dialog.__init__(self) # initialise le Qwidget principal
        QWidget.__init__(self)
        self.setupUi(parent) # Obligatoire
        self.clientmqtt = mqtt.Client()  # Herite de Client
        self.clientmqtt.username_pw_set(MQTT_USER,MQTT_PASSW)
        self.clientmqtt.on_connect = on_connect
        self.clientmqtt.on_message = on_message
        try:
            self.clientmqtt.connect(MQTT_SERVER, MQTT_PORT, 120) # Fonction bloquante
            self.clientmqtt.subscribe('/regchauf/mesur', 0)
            self.clientmqtt.subscribe('/regsol/mesur', 0)
        except:
            print('Pas de reseau')
            self.label_etat_comm.setText("Attente connexion réseau")
        self.lineEdit_Consigne.clearFocus()
        self.pushButton_Cde_Chauffage.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.counter = 0
        self.timer = QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.timerEvent)
        self.pushButton_Quit.released.connect(self.closeAppli)
        self.pushButton_Cde_Chauffage.released.connect(self.buttonStart_Chaufclicked)
        self.pushButton_Quit.released.connect(self.closeAppli)
        self.lineEdit_Consigne.returnPressed.connect(self.setpointChanged)
        self.lineEdit_Consigne.clearFocus()
        self.flagtimer = False
        self.once_time = False
        self.OneShot =False
        self.van_tm1 = 0


    def buttonStart_Chaufclicked(self):
        if data_chauffage['FNCT'][1] == 0:
            if self.checkBox_Mode_Regul.checkState():
                print('Cde start regulation T ext. uniquement')
                self.clientmqtt.publish('/regchauf/cde', '2')
            else:
                print('Cde start regulation T ext. et Consigne T ambiante')
                self.clientmqtt.publish('/regchauf/cde', '1')
        else:
            print('Cde stop')
            self.clientmqtt.publish('/regchauf/cde', '0')
        self.pushButton_Cde_Chauffage.clearFocus()
  
    def setpointChanged(self):
        if self.lineEdit_Consigne.text() != "":
            self.clientmqtt.publish('/regchauf/cons', str(self.lineEdit_Consigne.text()))
        self.lineEdit_Consigne.clearFocus()
    
    def closeAppli(self):
        self.clientmqtt.publish('/regchauf/send', 'stop')
        self.clientmqtt.publish('/regsol/send', 'stop')
        time.sleep(1)
        self.clientmqtt.disconnect()
        exit()
        
    def timerEvent(self):
        global connected, new_mes_chauffe, new_mes_solaire

        self.clientmqtt.loop()
        if connected :
            self.label_etat_comm.setText("Connecté MQTT: " + MQTT_SERVER)
            if self.once_time is False:
                self.clientmqtt.publish('/regchauf/send', 'start')
                self.clientmqtt.publish('/regsol/send', 'start')
                self.once_time = True
            if new_mes_chauffe is True: 
                self.Led_refresh_chauffage.setStyleSheet("background-color: rgb(255, 0, 0);")  
                if data_chauffage['FNCT'][1]== 0:
                   self.pushButton_Cde_Chauffage.setText("DEMARRER") 
                   self.pushButton_Cde_Chauffage.setStyleSheet("background-color: rgb(255, 0, 0);") 
                else :
                   self.pushButton_Cde_Chauffage.setText("ARRETER")
                   self.pushButton_Cde_Chauffage.setStyleSheet("background-color: rgb(0, 255, 0);") 
                if data_chauffage['CIRC'] == 0:
                   self.Led_Pompe_Chauffage.setStyleSheet("background-color: rgb(255, 0, 0);")
                else:
                    self.Led_Pompe_Chauffage.setStyleSheet("background-color: rgb(0, 255, 0);")
                if data_chauffage['ELEC']['PW'] == 0:
                    self.Led_thermoplongeur.setStyleSheet("background-color: rgb(255, 0, 0);")
                else:
                    self.Led_thermoplongeur.setStyleSheet("background-color: rgb(0, 255, 0);")
                self.display_T_cuve_m.setText("{0:.2f}°C".format(data_chauffage['TEMP']['Tcuv'])) 
                self.display_T_ext.setText("{0:.2f}°C".format(data_chauffage['TEMP']['Text'])) 
                self.display_T_Salon.setText("{0:.2f}°C".format(data_chauffage['TEMP']['Tint']))
                self.display_T_v3v.setText("{0:.2f}°C".format(data_chauffage['TEMP']['Tv3v'])) 
                self.P_elec_tot = data_chauffage['ELEC']['CHP'] + data_chauffage['ELEC']['CHC']
                self.display_PA_compteurEDF.setText("{:5} VA".format(data_chauffage['EDF']['PAPP']))
                self.display_P_Chauffe.setText("{0:4} W".format(int(data_chauffage['ELEC']['PW'])))
                self.display_I_Inst.setText("{:2} A".format(data_chauffage['EDF']['IINST'])) 
                if data_chauffage['EDF']['PTEC'] == 'HC..' :
                    self.Led_HeuresCreuses.setStyleSheet("background-color: rgb(0,255,0);")
                else :
                    self.Led_HeuresCreuses.setStyleSheet("background-color: rgb(249, 255, 246);")
                self.display_E_HP_chauffage.setText("E/j HP: {0:4.2f} kWh".format(data_chauffage['ELEC']['CHP']))
                self.display_E_HC_chauffage.setText("E/j HC: {0:4.2f} kWh".format(data_chauffage['ELEC']['CHC']))  
                self.progressBar_Pos_v3v.setValue(int(data_chauffage['VANN']))  
                self.display_T_cons_eau.setText("{0:.2f}°C".format(data_chauffage['CONS']))
                if self.lineEdit_Consigne.hasFocus() == False:
                    self.lineEdit_Consigne.setText("{0:.2f}°C".format(data_chauffage['FNCT'][0]))   
                    self.OneShot = True
                elif self.OneShot == True:
                    self.lineEdit_Consigne.setText("") 
                    self.OneShot = False  
                new_mes_chauffe = False
            else:
                self.Led_refresh_chauffage.setStyleSheet("background-color: rgb(0, 255, 0);")                       

            if new_mes_solaire :   
                self.Led_refresh_solaire.setStyleSheet("background-color: rgb(255, 0, 0);")    
                if data_solaire['PMP'] == 0:
                    self.Led_Pompe_Solaire.setStyleSheet("background-color: rgb(255, 0, 0);")
                else:
                    self.Led_Pompe_Solaire.setStyleSheet("background-color: rgb(0, 255, 0);")
                self.display_T_pan_sol.setText("{0:.2f}°C".format(data_solaire['Tcap']))
                self.display_T_dep_panel.setText("{0:.2f}°C".format(data_solaire['Taec']))
                self.display_T_ret_panel.setText("{0:.2f}°C".format(data_solaire['Trec']))      
                self.display_T_cuve_b.setText("{0:.2f}°C".format(data_solaire['Tcub']))  
                self.display_T_cuve_h.setText("{0:.2f}°C".format(data_solaire['Tcuh']))
                self.display_T_pan_sol.setText("{0:.2f}°C".format(data_solaire['Tcap']))   
                self.display_E_solaire.setText("{0:.2f} kWh/J".format(data_solaire['ENR']))    
                self.display_P_solaire.setText("{0:.2f} kW".format(data_solaire['PWR']))  
                new_mes_solaire = False
            else:
                self.Led_refresh_solaire.setStyleSheet("background-color: rgb(0, 255, 0);")  
        else:
            self.label_etat_comm.setText("Attente connexion à " + MQTT_SERVER)
            if DEBUG: print('Attente connexion à ' + MQTT_SERVER)

def main(args):
    app = QApplication(args) # crée l'objet application
    window = QDialog() # crée le Widget racine
    c = myApp(window) # Crée instance de la classe contenant le code de l'application
    window.show() # affiche la fenêtre QWidget
    ret = app.exec_() # lance l'exécution de l'application

if __name__ == '__main__':
#    sys.exit(main(sys.argv))
    main(sys.argv)
    

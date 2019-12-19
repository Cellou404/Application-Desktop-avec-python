# -*-Coding: utf-8

from mainWin import Ui_MainWindow
import addDialog
from editeDialog import Ui_Dialog

from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox, QWidget, QTableWidgetItem
from PyQt5 import QtGui
import sqlite3
import sys

connexion = sqlite3.connect('tableDB.db')
curs = connexion.cursor()
curs.execute(
    'CREATE TABLE IF NOT EXISTS information (Prenom TEXT, Nom TEXT, Age INT, Telephone TEXT, Datear DATE, Sommea INT, Sommeb INT, Sommet INT) ')


class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)

        self.title = "Gestion-Personnel"
        self.iconName = "Images/iconeMainWin.png"

        self.setupUi(self)
        # self.Load_Database()
        self.Load_Data()

        self.Init_Ui()

    def Init_Ui(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.show()
        self.pushButton_3.clicked.connect(self.Show_Add_Dialog)
        self.pushButton_suprimer.clicked.connect(self.Delete_Data)
        self.pushButton_suprimer.clicked.connect(self.Show_Delete_Warning)

    def Show_Add_Dialog(self):
        self.adding = AddDialog()
        self.adding.pushButton_enregistrer.clicked.connect(self.Add_Data)
        self.adding.pushButton_enregistrer.clicked.connect(self.Show_Added_Warning)
        self.adding.exec_()

    def Show_Added_Warning(self):
        msg = QMessageBox()
        msg.setWindowTitle("Alert")
        msg.setWindowIcon(QtGui.QIcon("Images/warning.png"))
        msg.setText("Enrégistrement éffectué avec succès !")
        msg.setIcon(QMessageBox.Information)

        x = msg.exec_()

    def Show_Delete_Warning(self):
        msg= QMessageBox()
        msg.setWindowIcon(QtGui.QIcon("Images/warning.png"))
        msg.setWindowTitle("Suppression")
        msg.setText("Suppression éffectuée avec succès !")
        msg.setIcon(QMessageBox.Critical)

        y = msg.exec_()

    def Add_Data(self):
        prenom = self.adding.lineEdit_prenom.text()
        nom = self.adding.lineEdit_nom.text()
        age = self.adding.lineEdit_age.text()
        tel = self.adding.lineEdit_tel.text()
        date = self.adding.lineEdit_date.text()
        sommeA = self.adding.lineEdit_somme_A.text()
        sommeB = self.adding.lineEdit_somme_B.text()

        try:
            curs.execute(
                'INSERT INTO information (Prenom, Nom, Age, Telephone, Datear, Sommea, Sommeb)VALUES(?,?,?,?,?,?,?)',
                (prenom, nom, age, tel, date, sommeA, sommeB))
            curs.execute('UPDATE information SET Sommet=Sommea+sommeb WHERE Prenom=prenom ')
            connexion.commit()
            print('Done !')
        # self.Load_Database()
        except Exception as error:
            print(error)

    def Delete_Data(self):
        content = 'SELECT * FROM information'
        result = curs.execute(content)
        for row in enumerate(result):
            if row[0] == self.tableWidget.currentRow():
                data = row[1]
                prenom = data[0]
                nom = data[1]
                age = data[2]
                tel = data[3]
                date = data[4]
                sommeA = data[5]
                sommeB = data[6]
                curs.execute(
                    "DELETE FROM information WHERE Prenom=? AND Nom=?AND Age=? AND Telephone=? AND Datear=? AND Sommea=? AND Sommeb=?",
                    (prenom, nom, age, tel, date, sommeA, sommeB))
                connexion.commit()
                self.Load_Database()

    def Load_Database(self):
        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(0)
        connexion = sqlite3.connect('tableDB.db')
        content = 'SELECT * FROM information'
        result = connexion.execute(content)
        for row_index, row_data in enumerate(result):
            self.tableWidget.insertRow(row_index)
            for colm_index, colm_data in enumerate(row_data):
                self.tableWidget.setItem(row_index, colm_index, QTableWidgetItem(str(colm_data)))
        connexion.close()
        self.label_4.setText("Total: " + str(self.tableWidget.rowCount()))
        return

    def Load_Data(self):
        self.pushButton_2.clicked.connect(self.Load_Database)

    def closeEvent(self, event):
        message = QMessageBox.question(self, "Fermeture", "êtres vous sûr de vouloir fermer la fenêtre", QMessageBox.No,
                                       QMessageBox.Yes)
        if message == QMessageBox.No:
            event.ignore()
        else:
            event.accept()


class AddDialog(QDialog, addDialog.Ui_Dialog):
    def __init__(self, parent=None):
        super(AddDialog, self).__init__(parent)

        self.setupUi(self)


class EditDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(EditDialog, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication([])
    win = MainApp()
    app.exec_()

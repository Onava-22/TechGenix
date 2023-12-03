from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt,QCoreApplication

from Vars import download_path,company_name,admuser,admkey,sql_db,sql_password,company_logo,aesthetic_banner,send_logo,user_logo,inbox_logo,personal_logo,department_logo,supervisor_logo,Supervisors

import mysql.connector as ms
import datetime as dttm
import csv

eid = None
print("System has been Booted Up.")

class Ui_MainWindow(object):

#Code to Prepare GUI
        
        def setupUi(self, MainWindow):
                
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(1200, 800)
                MainWindow.setMaximumSize(QtCore.QSize(1200, 800))
                MainWindow.setStyleSheet("")
                MainWindow.setWindowFlags(Qt.FramelessWindowHint)
                
                #Icon Setup
                
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(company_logo), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                MainWindow.setWindowIcon(icon)
                
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")

                self.r_window = QtWidgets.QStackedWidget(self.centralwidget)
                self.r_window.setEnabled(True)
                self.r_window.setGeometry(QtCore.QRect(340, 0, 861, 801))
                font = QtGui.QFont()
                font.setKerning(True)
                self.r_window.setFont(font)
                self.r_window.setStyleSheet("background-color:rgb(235, 242, 253)")
                self.r_window.setObjectName("r_window")

                self.r_aestheticpage = QtWidgets.QWidget()
                self.r_aestheticpage.setObjectName("r_aestheticpage")

                self.aesthetic_imglbl = QtWidgets.QLabel(self.r_aestheticpage)
                self.aesthetic_imglbl.setGeometry(QtCore.QRect(0, 0, 861, 801))
                self.aesthetic_imglbl.setText("")
                self.aesthetic_imglbl.setScaledContents(True)
                self.aesthetic_imglbl.setObjectName("aesthetic_imglbl")

                self.r_window.addWidget(self.r_aestheticpage)
                self.r_homepage = QtWidgets.QWidget()
                self.r_homepage.setObjectName("r_homepage")

                self.card_grpbox = QtWidgets.QGroupBox(self.r_homepage)
                self.card_grpbox.setGeometry(QtCore.QRect(180, 30, 501, 291))
                self.card_grpbox.setTitle("")
                self.card_grpbox.setObjectName("card_grpbox")

                self.cardbase_lbl2 = QtWidgets.QLabel(self.card_grpbox)
                self.cardbase_lbl2.setGeometry(QtCore.QRect(0, 0, 500, 271))
                self.cardbase_lbl2.setStyleSheet("border-style:outset;\n"
                "border-width:2px;\n"
                "border-color:black;\n"
                "border-radius: 30px;\n"
                "background-color: white;")
                self.cardbase_lbl2.setText("")
                self.cardbase_lbl2.setObjectName("cardbase_lbl2")

                self.cardbase_lbl1 = QtWidgets.QLabel(self.card_grpbox)
                self.cardbase_lbl1.setGeometry(QtCore.QRect(0, 230, 500, 61))
                self.cardbase_lbl1.setStyleSheet("color: rgb(255, 255, 255);\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-bottom-left-radius:30px;\n"
                "border-bottom-right-radius:30px;\n"
                "border-color:black;\n"
                "background-color: rgb(6,54,122);")
                self.cardbase_lbl1.setText("")
                self.cardbase_lbl1.setObjectName("cardbase_lbl1")

                self.cardlogo_imglbl = QtWidgets.QLabel(self.card_grpbox)
                self.cardlogo_imglbl.setGeometry(QtCore.QRect(30, 30, 121, 121))
                self.cardlogo_imglbl.setStyleSheet("border-style:outset;\n"
                "border-width:2px;\n"
                "border-color:black;")
                self.cardlogo_imglbl.setText("")
                self.cardlogo_imglbl.setScaledContents(True)
                self.cardlogo_imglbl.setObjectName("cardlogo_imglbl")

                self.cardjob_lbl = QtWidgets.QLabel(self.card_grpbox)
                self.cardjob_lbl.setGeometry(QtCore.QRect(173, 80, 61, 35))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.cardjob_lbl.setFont(font)
                self.cardjob_lbl.setStyleSheet("background-color: white;\n""color:black")
                self.cardjob_lbl.setObjectName("cardjob_lbl")

                self.cardcontact_txtlbl = QtWidgets.QLabel(self.card_grpbox)
                self.cardcontact_txtlbl.setGeometry(QtCore.QRect(240, 125, 225, 35))
                self.cardcontact_txtlbl.setMaximumSize(QtCore.QSize(16777215, 35))
                font = QtGui.QFont()
                font.setPointSize(7)
                self.cardcontact_txtlbl.setFont(font)
                self.cardcontact_txtlbl.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.cardcontact_txtlbl.setText("")
                self.cardcontact_txtlbl.setObjectName("cardcontact_txtlbl")

                self.cardmail_lbl = QtWidgets.QLabel(self.card_grpbox)
                self.cardmail_lbl.setGeometry(QtCore.QRect(173, 170, 61, 35))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.cardmail_lbl.setFont(font)
                self.cardmail_lbl.setStyleSheet("background-color: white;\n""color:black")
                self.cardmail_lbl.setObjectName("cardmail_lbl")

                self.cardcontact_lbl = QtWidgets.QLabel(self.card_grpbox)
                self.cardcontact_lbl.setGeometry(QtCore.QRect(173, 125, 61, 35))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.cardcontact_lbl.setFont(font)
                self.cardcontact_lbl.setStyleSheet("background-color: white;\n""color:black")
                self.cardcontact_lbl.setObjectName("cardcontact_lbl")

                self.cardname_lbl = QtWidgets.QLabel(self.card_grpbox)
                self.cardname_lbl.setGeometry(QtCore.QRect(173, 35, 61, 35))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.cardname_lbl.setFont(font)
                self.cardname_lbl.setStyleSheet("background-color: white;\n""color:black")
                self.cardname_lbl.setObjectName("cardname_lbl")

                self.cardjob_txt_lbl = QtWidgets.QLabel(self.card_grpbox)
                self.cardjob_txt_lbl.setGeometry(QtCore.QRect(240, 80, 225, 35))
                self.cardjob_txt_lbl.setMaximumSize(QtCore.QSize(16777215, 35))
                font = QtGui.QFont()
                font.setPointSize(7)
                self.cardjob_txt_lbl.setFont(font)
                self.cardjob_txt_lbl.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.cardjob_txt_lbl.setText("")
                self.cardjob_txt_lbl.setObjectName("cardjob_txt_lbl")

                self.cardname_txtlbl = QtWidgets.QLabel(self.card_grpbox)
                self.cardname_txtlbl.setGeometry(QtCore.QRect(240, 35, 225, 35))
                self.cardname_txtlbl.setMaximumSize(QtCore.QSize(16777215, 35))
                font = QtGui.QFont()
                font.setPointSize(7)
                self.cardname_txtlbl.setFont(font)
                self.cardname_txtlbl.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.cardname_txtlbl.setText("")
                self.cardname_txtlbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
                self.cardname_txtlbl.setObjectName("cardname_txtlbl")

                self.cardmail_txtlbl = QtWidgets.QLabel(self.card_grpbox)
                self.cardmail_txtlbl.setGeometry(QtCore.QRect(240, 170, 225, 35))
                self.cardmail_txtlbl.setMaximumSize(QtCore.QSize(16777215, 35))
                font = QtGui.QFont()
                font.setPointSize(7)
                self.cardmail_txtlbl.setFont(font)
                self.cardmail_txtlbl.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.cardmail_txtlbl.setText("")
                self.cardmail_txtlbl.setObjectName("cardmail_txtlbl")

                self.company_lbl_card = QtWidgets.QLabel(self.card_grpbox)
                self.company_lbl_card.setGeometry(QtCore.QRect(90, 250, 321, 20))
                font = QtGui.QFont()
                font.setPointSize(7)
                self.company_lbl_card.setFont(font)
                self.company_lbl_card.setStyleSheet("color: white;\n""background-color: rgb(6, 54, 122);")
                self.company_lbl_card.setAlignment(QtCore.Qt.AlignCenter)
                self.company_lbl_card.setObjectName("company_lbl_card")

                self.cardbase_lbl2.raise_()
                self.cardlogo_imglbl.raise_()
                self.cardjob_lbl.raise_()
                self.cardcontact_txtlbl.raise_()
                self.cardmail_lbl.raise_()
                self.cardcontact_lbl.raise_()
                self.cardname_lbl.raise_()
                self.cardjob_txt_lbl.raise_()
                self.cardname_txtlbl.raise_()
                self.cardmail_txtlbl.raise_()
                self.cardbase_lbl1.raise_()
                self.company_lbl_card.raise_()

                self.gridLayoutWidget_2 = QtWidgets.QWidget(self.r_homepage)
                self.gridLayoutWidget_2.setGeometry(QtCore.QRect(40, 370, 781, 391))
                self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
                self.persview_grid = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
                self.persview_grid.setContentsMargins(0, 0, 0, 0)
                self.persview_grid.setObjectName("persview_grid")

                self.address_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
                font = QtGui.QFont()
                font.setPointSize(9)
                self.address_lbl.setFont(font)
                self.address_lbl.setStyleSheet("background-color: ;\n"
                "background-color: rgb(235, 242, 253);\n"
                "color:black")
                self.address_lbl.setAlignment(QtCore.Qt.AlignCenter)
                self.address_lbl.setObjectName("address_lbl")

                self.persview_grid.addWidget(self.address_lbl, 0, 3, 1, 1)
                self.firstname_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
                font = QtGui.QFont()
                font.setPointSize(9)
                self.firstname_lbl.setFont(font)
                self.firstname_lbl.setStyleSheet("background-color: ;\n"
                "background-color: rgb(235, 242, 253);\n"
                "color:black")
                self.firstname_lbl.setAlignment(QtCore.Qt.AlignCenter)
                self.firstname_lbl.setObjectName("firstname_lbl")

                self.persview_grid.addWidget(self.firstname_lbl, 0, 0, 1, 1)
                self.lastname_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
                font = QtGui.QFont()
                font.setPointSize(9)
                self.lastname_lbl.setFont(font)
                self.lastname_lbl.setStyleSheet("background-color: ;\n"
                "background-color: rgb(235, 242, 253);\n"
                "color:black")
                self.lastname_lbl.setAlignment(QtCore.Qt.AlignCenter)
                self.lastname_lbl.setObjectName("lastname_lbl")

                self.persview_grid.addWidget(self.lastname_lbl, 2, 0, 1, 1)
                self.gender_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
                font = QtGui.QFont()
                font.setPointSize(9)
                self.gender_lbl.setFont(font)
                self.gender_lbl.setStyleSheet("background-color: ;\n"
                "background-color: rgb(235, 242, 253);\n"
                "color:black")
                self.gender_lbl.setAlignment(QtCore.Qt.AlignCenter)
                self.gender_lbl.setObjectName("gender_lbl")

                self.persview_grid.addWidget(self.gender_lbl, 3, 0, 1, 1)
                self.firstname_txtlbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
                self.firstname_txtlbl.setMaximumSize(QtCore.QSize(16777215, 35))
                font = QtGui.QFont()
                font.setPointSize(7)
                self.firstname_txtlbl.setFont(font)
                self.firstname_txtlbl.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.firstname_txtlbl.setText("")
                self.firstname_txtlbl.setObjectName("firstname_txtlbl")

                self.persview_grid.addWidget(self.firstname_txtlbl, 0, 1, 1, 1)
                self.address_txtlbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
                self.address_txtlbl.setMaximumSize(QtCore.QSize(16777215, 35))
                font = QtGui.QFont()
                font.setPointSize(7)
                self.address_txtlbl.setFont(font)
                self.address_txtlbl.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.address_txtlbl.setText("")
                self.address_txtlbl.setObjectName("address_txtlbl")

                self.persview_grid.addWidget(self.address_txtlbl, 0, 4, 1, 1)
                self.dob_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
                font = QtGui.QFont()
                font.setPointSize(9)
                self.dob_lbl.setFont(font)
                self.dob_lbl.setStyleSheet("background-color: ;\n"
                "background-color: rgb(235, 242, 253);\n"
                "color:black")
                self.dob_lbl.setAlignment(QtCore.Qt.AlignCenter)
                self.dob_lbl.setObjectName("dob_lbl")

                self.persview_grid.addWidget(self.dob_lbl, 4, 0, 1, 1)
                self.middlename_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
                font = QtGui.QFont()
                font.setPointSize(9)
                self.middlename_lbl.setFont(font)
                self.middlename_lbl.setStyleSheet("background-color: ;\n"
                "background-color: rgb(235, 242, 253);\n"
                "color:black")
                self.middlename_lbl.setAlignment(QtCore.Qt.AlignCenter)
                self.middlename_lbl.setObjectName("middlename_lbl")

                self.persview_grid.addWidget(self.middlename_lbl, 1, 0, 1, 1)
                spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
                self.persview_grid.addItem(spacerItem, 0, 2, 1, 1)
                self.city_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
                font = QtGui.QFont()
                font.setPointSize(9)
                self.city_lbl.setFont(font)
                self.city_lbl.setStyleSheet("background-color: ;\n"
                "background-color: rgb(235, 242, 253);\n"
                "color:black")
                self.city_lbl.setAlignment(QtCore.Qt.AlignCenter)
                self.city_lbl.setObjectName("city_lbl")

                self.persview_grid.addWidget(self.city_lbl, 1, 3, 1, 1)
                self.state_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
                font = QtGui.QFont()
                font.setPointSize(9)
                self.state_lbl.setFont(font)
                self.state_lbl.setStyleSheet("background-color: ;\n"
                "background-color: rgb(235, 242, 253);\n"
                "color:black")
                self.state_lbl.setAlignment(QtCore.Qt.AlignCenter)
                self.state_lbl.setObjectName("state_lbl")

                self.persview_grid.addWidget(self.state_lbl, 2, 3, 1, 1)
                self.zipcode_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
                font = QtGui.QFont()
                font.setPointSize(9)
                self.zipcode_lbl.setFont(font)
                self.zipcode_lbl.setStyleSheet("background-color: ;\n"
                "background-color: rgb(235, 242, 253);\n"
                "color:black")
                self.zipcode_lbl.setAlignment(QtCore.Qt.AlignCenter)
                self.zipcode_lbl.setObjectName("zipcode_lbl")

                self.persview_grid.addWidget(self.zipcode_lbl, 3, 3, 1, 1)
                self.contact_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
                font = QtGui.QFont()
                font.setPointSize(9)
                self.contact_lbl.setFont(font)
                self.contact_lbl.setStyleSheet("background-color: ;\n"
                "background-color: rgb(235, 242, 253);\n"
                "color:black")
                self.contact_lbl.setAlignment(QtCore.Qt.AlignCenter)
                self.contact_lbl.setObjectName("contact_lbl")

                self.persview_grid.addWidget(self.contact_lbl, 4, 3, 1, 1)
                self.middlename_txtlbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
                self.middlename_txtlbl.setMaximumSize(QtCore.QSize(16777215, 35))
                font = QtGui.QFont()
                font.setPointSize(7)
                self.middlename_txtlbl.setFont(font)
                self.middlename_txtlbl.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.middlename_txtlbl.setText("")
                self.middlename_txtlbl.setObjectName("middlename_txtlbl")

                self.persview_grid.addWidget(self.middlename_txtlbl, 1, 1, 1, 1)
                self.lastname_txtlbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
                self.lastname_txtlbl.setMaximumSize(QtCore.QSize(16777215, 35))
                font = QtGui.QFont()
                font.setPointSize(7)
                self.lastname_txtlbl.setFont(font)
                self.lastname_txtlbl.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.lastname_txtlbl.setText("")
                self.lastname_txtlbl.setObjectName("lastname_txtlbl")

                self.persview_grid.addWidget(self.lastname_txtlbl, 2, 1, 1, 1)
                self.gender_txtlbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
                self.gender_txtlbl.setMaximumSize(QtCore.QSize(16777215, 35))
                font = QtGui.QFont()
                font.setPointSize(7)
                self.gender_txtlbl.setFont(font)
                self.gender_txtlbl.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.gender_txtlbl.setText("")
                self.gender_txtlbl.setObjectName("gender_txtlbl")

                self.persview_grid.addWidget(self.gender_txtlbl, 3, 1, 1, 1)
                self.dob_txtlbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
                self.dob_txtlbl.setMaximumSize(QtCore.QSize(16777215, 35))
                font = QtGui.QFont()
                font.setPointSize(7)
                self.dob_txtlbl.setFont(font)
                self.dob_txtlbl.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.dob_txtlbl.setText("")
                self.dob_txtlbl.setObjectName("dob_txtlbl")

                self.persview_grid.addWidget(self.dob_txtlbl, 4, 1, 1, 1)
                self.city_txtlbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
                self.city_txtlbl.setMaximumSize(QtCore.QSize(16777215, 35))
                font = QtGui.QFont()
                font.setPointSize(7)
                self.city_txtlbl.setFont(font)
                self.city_txtlbl.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.city_txtlbl.setText("")
                self.city_txtlbl.setObjectName("city_txtlbl")

                self.persview_grid.addWidget(self.city_txtlbl, 1, 4, 1, 1)
                self.state_txtlbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
                self.state_txtlbl.setMaximumSize(QtCore.QSize(16777215, 35))
                font = QtGui.QFont()
                font.setPointSize(7)
                self.state_txtlbl.setFont(font)
                self.state_txtlbl.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.state_txtlbl.setText("")
                self.state_txtlbl.setObjectName("state_txtlbl")

                self.persview_grid.addWidget(self.state_txtlbl, 2, 4, 1, 1)
                self.contact_txtlbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
                self.contact_txtlbl.setMaximumSize(QtCore.QSize(16777215, 35))
                font = QtGui.QFont()
                font.setPointSize(7)
                self.contact_txtlbl.setFont(font)
                self.contact_txtlbl.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.contact_txtlbl.setText("")
                self.contact_txtlbl.setObjectName("contact_txtlbl")

                self.persview_grid.addWidget(self.contact_txtlbl, 4, 4, 1, 1)
                self.zipcode_txtlbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
                self.zipcode_txtlbl.setMaximumSize(QtCore.QSize(16777215, 35))
                font = QtGui.QFont()
                font.setPointSize(7)
                self.zipcode_txtlbl.setFont(font)
                self.zipcode_txtlbl.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.zipcode_txtlbl.setText("")
                self.zipcode_txtlbl.setObjectName("zipcode_txtlbl")

                self.persview_grid.addWidget(self.zipcode_txtlbl, 3, 4, 1, 1)
                self.persview_grid.setColumnStretch(0, 1)
                self.persview_grid.setColumnStretch(1, 5)
                self.persview_grid.setColumnStretch(2, 1)
                self.persview_grid.setColumnStretch(3, 1)
                self.persview_grid.setColumnStretch(4, 5)
                self.r_window.addWidget(self.r_homepage)
                self.r_perseditpage = QtWidgets.QWidget()
                self.r_perseditpage.setObjectName("r_perseditpage")

                self.gridLayoutWidget_5 = QtWidgets.QWidget(self.r_perseditpage)
                self.gridLayoutWidget_5.setGeometry(QtCore.QRect(40, 370, 781, 391))
                self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")

                self.editpers_gid = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
                self.editpers_gid.setContentsMargins(0, 0, 0, 0)
                self.editpers_gid.setObjectName("editpers_gid")

                self.editstate_lbl = QtWidgets.QLabel(self.gridLayoutWidget_5)
                font = QtGui.QFont()
                font.setPointSize(9)
                self.editstate_lbl.setFont(font)
                self.editstate_lbl.setStyleSheet("background-color: ;\n"
                "background-color: rgb(235, 242, 253);\n"
                "color:black")
                self.editstate_lbl.setAlignment(QtCore.Qt.AlignCenter)
                self.editstate_lbl.setObjectName("editstate_lbl")

                self.editpers_gid.addWidget(self.editstate_lbl, 2, 3, 1, 1)
                self.editfirstname_lineedit = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
                self.editfirstname_lineedit.setMinimumSize(QtCore.QSize(0, 30))
                self.editfirstname_lineedit.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.editfirstname_lineedit.setText("")
                self.editfirstname_lineedit.setObjectName("editfirstname_lineedit")

                self.editpers_gid.addWidget(self.editfirstname_lineedit, 0, 1, 1, 1)
                self.editfirstname_lbl = QtWidgets.QLabel(self.gridLayoutWidget_5)
                self.editfirstname_lbl.setMinimumSize(QtCore.QSize(0, 30))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.editfirstname_lbl.setFont(font)
                self.editfirstname_lbl.setStyleSheet("background-color: ;\n"
                "background-color: rgb(235, 242, 253);\n"
                "color:black")
                self.editfirstname_lbl.setAlignment(QtCore.Qt.AlignCenter)
                self.editfirstname_lbl.setObjectName("editfirstname_lbl")

                self.editpers_gid.addWidget(self.editfirstname_lbl, 0, 0, 1, 1)
                self.editlastname_lbl = QtWidgets.QLabel(self.gridLayoutWidget_5)
                font = QtGui.QFont()
                font.setPointSize(9)
                self.editlastname_lbl.setFont(font)
                self.editlastname_lbl.setStyleSheet("background-color: ;\n"
                "background-color: rgb(235, 242, 253);\n"
                "color:black")
                self.editlastname_lbl.setAlignment(QtCore.Qt.AlignCenter)
                self.editlastname_lbl.setObjectName("editlastname_lbl")

                self.editpers_gid.addWidget(self.editlastname_lbl, 2, 0, 1, 1)
                self.editzipcode_lbl = QtWidgets.QLabel(self.gridLayoutWidget_5)
                font = QtGui.QFont()
                font.setPointSize(9)
                self.editzipcode_lbl.setFont(font)
                self.editzipcode_lbl.setStyleSheet("background-color: ;\n"
                "background-color: rgb(235, 242, 253);\n"
                "color:black")
                self.editzipcode_lbl.setAlignment(QtCore.Qt.AlignCenter)
                self.editzipcode_lbl.setObjectName("editzipcode_lbl")

                self.editpers_gid.addWidget(self.editzipcode_lbl, 3, 3, 1, 1)
                self.editgender_lineedit = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
                self.editgender_lineedit.setMinimumSize(QtCore.QSize(0, 30))
                self.editgender_lineedit.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.editgender_lineedit.setObjectName("editgender_lineedit")

                self.editpers_gid.addWidget(self.editgender_lineedit, 3, 1, 1, 1)
                spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.editpers_gid.addItem(spacerItem1, 0, 2, 1, 1)
                self.editcontact_lbl = QtWidgets.QLabel(self.gridLayoutWidget_5)
                font = QtGui.QFont()
                font.setPointSize(9)
                self.editcontact_lbl.setFont(font)
                self.editcontact_lbl.setStyleSheet("background-color: ;\n"
                "background-color: rgb(235, 242, 253);\n"
                "color:black")
                self.editcontact_lbl.setAlignment(QtCore.Qt.AlignCenter)
                self.editcontact_lbl.setObjectName("editcontact_lbl")

                self.editpers_gid.addWidget(self.editcontact_lbl, 4, 3, 1, 1)
                self.editzipcode_lineedit = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
                self.editzipcode_lineedit.setMinimumSize(QtCore.QSize(0, 30))
                self.editzipcode_lineedit.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.editzipcode_lineedit.setObjectName("editzipcode_lineedit")

                self.editpers_gid.addWidget(self.editzipcode_lineedit, 3, 4, 1, 1)
                self.editaddress_lbl = QtWidgets.QLabel(self.gridLayoutWidget_5)
                font = QtGui.QFont()
                font.setPointSize(9)
                self.editaddress_lbl.setFont(font)
                self.editaddress_lbl.setStyleSheet("background-color: ;\n"
                "background-color: rgb(235, 242, 253);\n"
                "color:black")
                self.editaddress_lbl.setAlignment(QtCore.Qt.AlignCenter)
                self.editaddress_lbl.setObjectName("editaddress_lbl")

                self.editpers_gid.addWidget(self.editaddress_lbl, 0, 3, 1, 1)
                self.editdob_lbl = QtWidgets.QLabel(self.gridLayoutWidget_5)
                font = QtGui.QFont()
                font.setPointSize(9)
                self.editdob_lbl.setFont(font)
                self.editdob_lbl.setStyleSheet("background-color: ;\n"
                "background-color: rgb(235, 242, 253);\n"
                "color:black")
                self.editdob_lbl.setAlignment(QtCore.Qt.AlignCenter)
                self.editdob_lbl.setObjectName("editdob_lbl")

                self.editpers_gid.addWidget(self.editdob_lbl, 4, 0, 1, 1)
                self.editcontact_lineedit = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
                self.editcontact_lineedit.setMinimumSize(QtCore.QSize(0, 30))
                self.editcontact_lineedit.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.editcontact_lineedit.setObjectName("editcontact_lineedit")

                self.editpers_gid.addWidget(self.editcontact_lineedit, 4, 4, 1, 1)
                self.editmiddlename_lbl = QtWidgets.QLabel(self.gridLayoutWidget_5)
                font = QtGui.QFont()
                font.setPointSize(9)
                self.editmiddlename_lbl.setFont(font)
                self.editmiddlename_lbl.setStyleSheet("background-color: ;\n"
                "background-color: rgb(235, 242, 253);\n"
                "color:black")
                self.editmiddlename_lbl.setAlignment(QtCore.Qt.AlignCenter)
                self.editmiddlename_lbl.setObjectName("editmiddlename_lbl")

                self.editpers_gid.addWidget(self.editmiddlename_lbl, 1, 0, 1, 1)
                self.editcity_lbl = QtWidgets.QLabel(self.gridLayoutWidget_5)
                font = QtGui.QFont()
                font.setPointSize(9)
                self.editcity_lbl.setFont(font)
                self.editcity_lbl.setStyleSheet("background-color: ;\n"
                "background-color: rgb(235, 242, 253);\n"
                "color:black")
                self.editcity_lbl.setAlignment(QtCore.Qt.AlignCenter)
                self.editcity_lbl.setObjectName("editcity_lbl")

                self.editpers_gid.addWidget(self.editcity_lbl, 1, 3, 1, 1)
                self.editmiddlename_lineedit = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
                self.editmiddlename_lineedit.setMinimumSize(QtCore.QSize(0, 30))
                self.editmiddlename_lineedit.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.editmiddlename_lineedit.setObjectName("editmiddlename_lineedit")

                self.editpers_gid.addWidget(self.editmiddlename_lineedit, 1, 1, 1, 1)
                self.editgender_lbl = QtWidgets.QLabel(self.gridLayoutWidget_5)
                font = QtGui.QFont()
                font.setPointSize(9)
                self.editgender_lbl.setFont(font)
                self.editgender_lbl.setStyleSheet("background-color: ;\n"
                "background-color: rgb(235, 242, 253);\n"
                "color:black")
                self.editgender_lbl.setAlignment(QtCore.Qt.AlignCenter)
                self.editgender_lbl.setObjectName("editgender_lbl")

                self.editpers_gid.addWidget(self.editgender_lbl, 3, 0, 1, 1)
                self.editdob_lineedit = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
                self.editdob_lineedit.setMinimumSize(QtCore.QSize(0, 30))
                self.editdob_lineedit.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.editdob_lineedit.setObjectName("editdob_lineedit")

                self.editpers_gid.addWidget(self.editdob_lineedit, 4, 1, 1, 1)
                self.editlastname_lineedit = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
                self.editlastname_lineedit.setMinimumSize(QtCore.QSize(0, 30))
                self.editlastname_lineedit.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.editlastname_lineedit.setObjectName("editlastname_lineedit")

                self.editpers_gid.addWidget(self.editlastname_lineedit, 2, 1, 1, 1)
                self.editstate_lineedit = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
                self.editstate_lineedit.setMinimumSize(QtCore.QSize(0, 30))
                self.editstate_lineedit.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.editstate_lineedit.setObjectName("editstate_lineedit")

                self.editpers_gid.addWidget(self.editstate_lineedit, 2, 4, 1, 1)
                self.editcity_lineedit = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
                self.editcity_lineedit.setMinimumSize(QtCore.QSize(0, 30))
                self.editcity_lineedit.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.editcity_lineedit.setObjectName("editcity_lineedit")

                self.editpers_gid.addWidget(self.editcity_lineedit, 1, 4, 1, 1)
                self.editaddress_lineedit = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
                self.editaddress_lineedit.setMinimumSize(QtCore.QSize(0, 30))
                self.editaddress_lineedit.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.editaddress_lineedit.setObjectName("editaddress_lineedit")

                self.editpers_gid.addWidget(self.editaddress_lineedit, 0, 4, 1, 1)
                self.editpers_gid.setColumnStretch(0, 1)
                self.editpers_gid.setColumnStretch(1, 5)
                self.editpers_gid.setColumnStretch(2, 1)
                self.editpers_gid.setColumnStretch(3, 1)
                self.editpers_gid.setColumnStretch(4, 5)

                self.selectionbox_lbl = QtWidgets.QLabel(self.r_perseditpage)
                self.selectionbox_lbl.setGeometry(QtCore.QRect(40, 25, 781, 301))
                self.selectionbox_lbl.setStyleSheet("border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:30px;\n"
                "border-color:black;\n"
                "background-color: rgb(6, 54, 122);")
                self.selectionbox_lbl.setText("")
                self.selectionbox_lbl.setObjectName("selectionbox_lbl")

                self.gender_chkbox = QtWidgets.QCheckBox(self.r_perseditpage)
                self.gender_chkbox.setGeometry(QtCore.QRect(70, 258, 111, 20))
                self.gender_chkbox.setStyleSheet("color: white;\n""background-color: rgb(6, 54, 122);")
                self.gender_chkbox.setObjectName("gender_chkbox")

                self.address_chkbox = QtWidgets.QCheckBox(self.r_perseditpage)
                self.address_chkbox.setGeometry(QtCore.QRect(450, 180, 91, 20))
                self.address_chkbox.setStyleSheet("color: white;\n""background-color: rgb(6, 54, 122);")
                self.address_chkbox.setObjectName("address_chkbox")

                self.state_chkbox = QtWidgets.QCheckBox(self.r_perseditpage)
                self.state_chkbox.setGeometry(QtCore.QRect(450, 232, 91, 20))
                self.state_chkbox.setStyleSheet("color: white;\n""background-color: rgb(6, 54, 122);")
                self.state_chkbox.setObjectName("state_chkbox")

                self.zipcode_chkbox = QtWidgets.QCheckBox(self.r_perseditpage)
                self.zipcode_chkbox.setGeometry(QtCore.QRect(450, 258, 91, 20))
                self.zipcode_chkbox.setStyleSheet("color: white;\n""background-color: rgb(6, 54, 122);")
                self.zipcode_chkbox.setObjectName("zipcode_chkbox")

                self.city_chkbox = QtWidgets.QCheckBox(self.r_perseditpage)
                self.city_chkbox.setGeometry(QtCore.QRect(450, 206, 91, 20))
                self.city_chkbox.setStyleSheet("color: white;\n""background-color: rgb(6, 54, 122);")
                self.city_chkbox.setObjectName("city_chkbox")

                self.lastname_chkbox = QtWidgets.QCheckBox(self.r_perseditpage)
                self.lastname_chkbox.setGeometry(QtCore.QRect(70, 232, 111, 20))
                self.lastname_chkbox.setStyleSheet("color: white;\n""background-color: rgb(6, 54, 122);")
                self.lastname_chkbox.setObjectName("lastname_chkbox")

                self.middlename_chkbox = QtWidgets.QCheckBox(self.r_perseditpage)
                self.middlename_chkbox.setGeometry(QtCore.QRect(70, 206, 111, 20))
                self.middlename_chkbox.setStyleSheet("color: white;\n""background-color: rgb(6, 54, 122);")
                self.middlename_chkbox.setObjectName("middlename_chkbox")

                self.display_lbl = QtWidgets.QLabel(self.r_perseditpage)
                self.display_lbl.setGeometry(QtCore.QRect(60, 48, 741, 121))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.display_lbl.setFont(font)
                self.display_lbl.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:30px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.display_lbl.setAlignment(QtCore.Qt.AlignCenter)
                self.display_lbl.setObjectName("display_lbl")

                self.dob_chkbox = QtWidgets.QCheckBox(self.r_perseditpage)
                self.dob_chkbox.setGeometry(QtCore.QRect(70, 284, 111, 20))
                self.dob_chkbox.setStyleSheet("color: white;\n""background-color: rgb(6, 54, 122);")
                self.dob_chkbox.setObjectName("dob_chkbox")

                self.firstname_chkbox = QtWidgets.QCheckBox(self.r_perseditpage)
                self.firstname_chkbox.setGeometry(QtCore.QRect(70, 180, 111, 20))
                self.firstname_chkbox.setStyleSheet("color: white;\n""background-color: rgb(6, 54, 122);")
                self.firstname_chkbox.setCheckable(True)
                self.firstname_chkbox.setChecked(False)
                self.firstname_chkbox.setAutoRepeat(False)
                self.firstname_chkbox.setObjectName("firstname_chkbox")

                self.contact_chkbox = QtWidgets.QCheckBox(self.r_perseditpage)
                self.contact_chkbox.setGeometry(QtCore.QRect(450, 284, 91, 20))
                self.contact_chkbox.setStyleSheet("color: white;\n""background-color: rgb(6, 54, 122);")
                self.contact_chkbox.setObjectName("contact_chkbox")

                self.confirmchange_btn = QtWidgets.QPushButton(self.r_perseditpage)
                self.confirmchange_btn.setGeometry(QtCore.QRect(630, 260, 131, 41))
                self.confirmchange_btn.setStyleSheet("background-color:rgb(6, 54, 122);\n"
                "color:white;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:white")
                self.confirmchange_btn.setObjectName("confirmchange_btn")

                self.changestatus_txtlbl = QtWidgets.QLabel(self.r_perseditpage)
                self.changestatus_txtlbl.setGeometry(QtCore.QRect(600, 190, 191, 51))
                self.changestatus_txtlbl.setStyleSheet("color: white;\n""background-color: rgb(6, 54, 122);")
                self.changestatus_txtlbl.setAlignment(QtCore.Qt.AlignCenter)
                self.changestatus_txtlbl.setObjectName("changestatus_txtlbl")

                self.r_window.addWidget(self.r_perseditpage)
                self.r_depviewpage = QtWidgets.QWidget()
                self.r_depviewpage.setObjectName("r_depviewpage")

                self.dephead_txtlbl = QtWidgets.QLabel(self.r_depviewpage)
                self.dephead_txtlbl.setGeometry(QtCore.QRect(40, 30, 781, 101))
                font = QtGui.QFont()
                font.setFamily("Mongolian Baiti")
                font.setPointSize(15)
                self.dephead_txtlbl.setFont(font)
                self.dephead_txtlbl.setStyleSheet("color: white;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:50px;\n"
                "border-color:black;\n"
                "background-color: rgb(6, 54, 122);")
                self.dephead_txtlbl.setAlignment(QtCore.Qt.AlignCenter)
                self.dephead_txtlbl.setObjectName("dephead_txtlbl")

                self.dep_table = QtWidgets.QTableWidget(self.r_depviewpage)
                self.dep_table.setGeometry(QtCore.QRect(40, 160, 781, 601))
                self.dep_table.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.dep_table.setGridStyle(QtCore.Qt.DashDotLine)
                self.dep_table.setObjectName("dep_table")

                self.dep_table.setColumnCount(4)
                self.dep_table.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.dep_table.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.dep_table.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.dep_table.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.dep_table.setHorizontalHeaderItem(3, item)
                self.r_window.addWidget(self.r_depviewpage)
                self.r_inboxpage = QtWidgets.QWidget()
                self.r_inboxpage.setObjectName("r_inboxpage")

                self.inbox_txtlbl = QtWidgets.QLabel(self.r_inboxpage)
                self.inbox_txtlbl.setGeometry(QtCore.QRect(40, 30, 781, 101))
                font = QtGui.QFont()
                font.setFamily("Mongolian Baiti")
                font.setPointSize(15)
                self.inbox_txtlbl.setFont(font)
                self.inbox_txtlbl.setStyleSheet("color: white;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:50px;\n"
                "border-color:black;\n"
                "background-color: rgb(6, 54, 122);")
                self.inbox_txtlbl.setAlignment(QtCore.Qt.AlignCenter)
                self.inbox_txtlbl.setObjectName("inbox_txtlbl")

                self.inbox_table = QtWidgets.QTableWidget(self.r_inboxpage)
                self.inbox_table.setGeometry(QtCore.QRect(40, 160, 781, 601))
                self.inbox_table.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.inbox_table.setGridStyle(QtCore.Qt.DashDotLine)
                self.inbox_table.setObjectName("inbox_table")

                self.inbox_table.setColumnCount(3)
                self.inbox_table.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.inbox_table.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.inbox_table.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.inbox_table.setHorizontalHeaderItem(2, item)
                self.r_window.addWidget(self.r_inboxpage)
                self.r_sendpage = QtWidgets.QWidget()
                self.r_sendpage.setObjectName("r_sendpage")

                self.message_txtlbl = QtWidgets.QLabel(self.r_sendpage)
                self.message_txtlbl.setGeometry(QtCore.QRect(40, 30, 781, 101))
                font = QtGui.QFont()
                font.setFamily("Mongolian Baiti")
                font.setPointSize(15)
                self.message_txtlbl.setFont(font)
                self.message_txtlbl.setStyleSheet("color: white;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:50px;\n"
                "border-color:black;\n"
                "background-color: rgb(6, 54, 122);")
                self.message_txtlbl.setAlignment(QtCore.Qt.AlignCenter)
                self.message_txtlbl.setObjectName("message_txtlbl")

                self.to_combobox = QtWidgets.QComboBox(self.r_sendpage)
                self.to_combobox.setGeometry(QtCore.QRect(140, 180, 331, 31))
                self.to_combobox.setObjectName("to_combobox")
                self.to_combobox.addItem("")

                self.to_boxlbl = QtWidgets.QLabel(self.r_sendpage)
                self.to_boxlbl.setGeometry(QtCore.QRect(40, 160, 781, 71))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.to_boxlbl.setFont(font)
                self.to_boxlbl.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:30px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.to_boxlbl.setText("")
                self.to_boxlbl.setAlignment(QtCore.Qt.AlignCenter)
                self.to_boxlbl.setObjectName("to_boxlbl")

                self.to_txtlbl = QtWidgets.QLabel(self.r_sendpage)
                self.to_txtlbl.setGeometry(QtCore.QRect(70, 180, 61, 31))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.to_txtlbl.setFont(font)
                self.to_txtlbl.setStyleSheet("background-color: white;\n""color:black")
                self.to_txtlbl.setObjectName("to_txtlbl")

                self.sendmode_radiobtn = QtWidgets.QRadioButton(self.r_sendpage)
                self.sendmode_radiobtn.setGeometry(QtCore.QRect(530, 180, 95, 31))
                self.sendmode_radiobtn.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.sendmode_radiobtn.setChecked(True)
                self.sendmode_radiobtn.setObjectName("sendmode_radiobtn")

                self.sentmode_radiobtn = QtWidgets.QRadioButton(self.r_sendpage)
                self.sentmode_radiobtn.setGeometry(QtCore.QRect(660, 180, 121, 31))
                self.sentmode_radiobtn.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.sentmode_radiobtn.setObjectName("sentmode_radiobtn")

                self.sendmodes_stckwidget = QtWidgets.QStackedWidget(self.r_sendpage)
                self.sendmodes_stckwidget.setGeometry(QtCore.QRect(40, 260, 781, 501))
                self.sendmodes_stckwidget.setObjectName("sendmodes_stckwidget")

                self.sendmode = QtWidgets.QWidget()
                self.sendmode.setObjectName("sendmode")

                self.sendmsg_btn = QtWidgets.QPushButton(self.sendmode)
                self.sendmsg_btn.setGeometry(QtCore.QRect(660, 460, 93, 28))
                self.sendmsg_btn.setStyleSheet("color: white;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(6, 54, 122);")
                self.sendmsg_btn.setObjectName("sendmsg_btn")

                self.msgstatus_lbl = QtWidgets.QLabel(self.sendmode)
                self.msgstatus_lbl.setGeometry(QtCore.QRect(30, 460, 611, 16))
                self.msgstatus_lbl.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.msgstatus_lbl.setObjectName("msgstatus_lbl")

                self.message_txtedit = QtWidgets.QTextEdit(self.sendmode)
                self.message_txtedit.setGeometry(QtCore.QRect(30, 60, 721, 391))
                self.message_txtedit.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:1px;\n"
                "border-color:black;")
                self.message_txtedit.setObjectName("message_txtedit")

                self.msg_txtlbl = QtWidgets.QLabel(self.sendmode)
                self.msg_txtlbl.setGeometry(QtCore.QRect(30, 30, 61, 31))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.msg_txtlbl.setFont(font)
                self.msg_txtlbl.setStyleSheet("background-color: white;\n""color:black")
                self.msg_txtlbl.setObjectName("msg_txtlbl")

                self.message_boxlbl = QtWidgets.QLabel(self.sendmode)
                self.message_boxlbl.setGeometry(QtCore.QRect(0, 0, 781, 501))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.message_boxlbl.setFont(font)
                self.message_boxlbl.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:30px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.message_boxlbl.setText("")
                self.message_boxlbl.setAlignment(QtCore.Qt.AlignCenter)
                self.message_boxlbl.setObjectName("message_boxlbl")

                self.message_boxlbl.raise_()
                self.msg_txtlbl.raise_()
                self.sendmsg_btn.raise_()
                self.msgstatus_lbl.raise_()
                self.message_txtedit.raise_()

                self.sendmodes_stckwidget.addWidget(self.sendmode)
                self.sentmode = QtWidgets.QWidget()
                self.sentmode.setObjectName("sentmode")

                self.sent_table = QtWidgets.QTableWidget(self.sentmode)
                self.sent_table.setGeometry(QtCore.QRect(0, 0, 781, 501))
                self.sent_table.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.sent_table.setGridStyle(QtCore.Qt.DashDotLine)
                self.sent_table.setObjectName("sent_table")

                self.sent_table.setColumnCount(3)
                self.sent_table.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.sent_table.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.sent_table.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.sent_table.setHorizontalHeaderItem(2, item)
                self.sendmodes_stckwidget.addWidget(self.sentmode)

                self.message_txtlbl.raise_()
                self.to_boxlbl.raise_()
                self.to_combobox.raise_()
                self.to_txtlbl.raise_()
                self.sendmode_radiobtn.raise_()
                self.sentmode_radiobtn.raise_()
                self.sendmodes_stckwidget.raise_()

                self.r_window.addWidget(self.r_sendpage)
                self.r_supervisorpage = QtWidgets.QWidget()
                self.r_supervisorpage.setObjectName("r_supervisorpage")

                self.supervisor_txtlbl = QtWidgets.QLabel(self.r_supervisorpage)
                self.supervisor_txtlbl.setGeometry(QtCore.QRect(40, 30, 781, 101))
                font = QtGui.QFont()
                font.setFamily("Mongolian Baiti")
                font.setPointSize(15)
                self.supervisor_txtlbl.setFont(font)
                self.supervisor_txtlbl.setStyleSheet("color: white;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:50px;\n"
                "border-color:black;\n"
                "background-color: rgb(6, 54, 122);")
                self.supervisor_txtlbl.setAlignment(QtCore.Qt.AlignCenter)
                self.supervisor_txtlbl.setObjectName("supervisor_txtlbl")

                self.supervisor_table = QtWidgets.QTableWidget(self.r_supervisorpage)
                self.supervisor_table.setGeometry(QtCore.QRect(40, 160, 781, 601))
                self.supervisor_table.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.supervisor_table.setGridStyle(QtCore.Qt.DashDotLine)
                self.supervisor_table.setObjectName("supervisor_table")
                self.supervisor_table.setColumnCount(3)
                self.supervisor_table.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.supervisor_table.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.supervisor_table.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.supervisor_table.setHorizontalHeaderItem(2, item)

                self.r_window.addWidget(self.r_supervisorpage)
                self.r_admhomepage = QtWidgets.QWidget()
                self.r_admhomepage.setObjectName("r_admhomepage")

                self.adm_homehead_boxlbl = QtWidgets.QLabel(self.r_admhomepage)
                self.adm_homehead_boxlbl.setGeometry(QtCore.QRect(40, 27, 781, 181))
                self.adm_homehead_boxlbl.setStyleSheet("border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:80px;\n"
                "border-color:black;\n"
                "background-color: rgb(6, 54, 122);")
                self.adm_homehead_boxlbl.setText("")
                self.adm_homehead_boxlbl.setObjectName("adm_homehead_boxlbl")

                self.adm_homehead_txtlbl = QtWidgets.QLabel(self.r_admhomepage)
                self.adm_homehead_txtlbl.setGeometry(QtCore.QRect(60, 66, 741, 80))
                font = QtGui.QFont()
                font.setFamily("Mongolian Baiti")
                font.setPointSize(20)
                self.adm_homehead_txtlbl.setFont(font)
                self.adm_homehead_txtlbl.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:40px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.adm_homehead_txtlbl.setAlignment(QtCore.Qt.AlignCenter)
                self.adm_homehead_txtlbl.setObjectName("adm_homehead_txtlbl")

                self.adm_homehead_statuslbl = QtWidgets.QLabel(self.r_admhomepage)
                self.adm_homehead_statuslbl.setGeometry(QtCore.QRect(260, 170, 321, 10))
                font = QtGui.QFont()
                font.setPointSize(7)
                self.adm_homehead_statuslbl.setFont(font)
                self.adm_homehead_statuslbl.setStyleSheet("color: white;\n""background-color: rgb(6, 54, 122);")
                self.adm_homehead_statuslbl.setAlignment(QtCore.Qt.AlignCenter)
                self.adm_homehead_statuslbl.setObjectName("adm_homehead_statuslbl")

                self.countall_txtlbl = QtWidgets.QLabel(self.r_admhomepage)
                self.countall_txtlbl.setGeometry(QtCore.QRect(503, 273, 265, 35))
                self.countall_txtlbl.setMaximumSize(QtCore.QSize(16777215, 35))
                font = QtGui.QFont()
                font.setPointSize(7)
                self.countall_txtlbl.setFont(font)
                self.countall_txtlbl.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.countall_txtlbl.setText("")
                self.countall_txtlbl.setObjectName("countall_txtlbl")

                self.countmale_lbl = QtWidgets.QLabel(self.r_admhomepage)
                self.countmale_lbl.setGeometry(QtCore.QRect(370, 371, 127, 35))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.countmale_lbl.setFont(font)
                self.countmale_lbl.setStyleSheet("background-color: ;\n"
                "background-color: rgb(235, 242, 253);\n"
                "color:black")
                self.countmale_lbl.setAlignment(QtCore.Qt.AlignCenter)
                self.countmale_lbl.setObjectName("countmale_lbl")

                self.countall_lbl = QtWidgets.QLabel(self.r_admhomepage)
                self.countall_lbl.setGeometry(QtCore.QRect(370, 273, 127, 35))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.countall_lbl.setFont(font)
                self.countall_lbl.setStyleSheet("background-color: ;\n"
                "background-color: rgb(235, 242, 253);\n"
                "color:black")
                self.countall_lbl.setAlignment(QtCore.Qt.AlignCenter)
                self.countall_lbl.setObjectName("countall_lbl")

                self.countmale_txtlbl = QtWidgets.QLabel(self.r_admhomepage)
                self.countmale_txtlbl.setGeometry(QtCore.QRect(503, 371, 265, 35))
                self.countmale_txtlbl.setMaximumSize(QtCore.QSize(16777215, 35))
                font = QtGui.QFont()
                font.setPointSize(7)
                self.countmale_txtlbl.setFont(font)
                self.countmale_txtlbl.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.countmale_txtlbl.setText("")
                self.countmale_txtlbl.setObjectName("countmale_txtlbl")

                self.countfem_lbl = QtWidgets.QLabel(self.r_admhomepage)
                self.countfem_lbl.setGeometry(QtCore.QRect(370, 322, 127, 35))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.countfem_lbl.setFont(font)
                self.countfem_lbl.setStyleSheet("background-color: ;\n"
                "background-color: rgb(235, 242, 253);\n"
                "color:black")
                self.countfem_lbl.setAlignment(QtCore.Qt.AlignCenter)
                self.countfem_lbl.setObjectName("countfem_lbl")

                self.countfem_txtlbl = QtWidgets.QLabel(self.r_admhomepage)
                self.countfem_txtlbl.setGeometry(QtCore.QRect(503, 322, 265, 35))
                self.countfem_txtlbl.setMaximumSize(QtCore.QSize(16777215, 35))
                font = QtGui.QFont()
                font.setPointSize(7)
                self.countfem_txtlbl.setFont(font)
                self.countfem_txtlbl.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.countfem_txtlbl.setText("")
                self.countfem_txtlbl.setObjectName("countfem_txtlbl")

                self.countother_txtlbl = QtWidgets.QLabel(self.r_admhomepage)
                self.countother_txtlbl.setGeometry(QtCore.QRect(503, 420, 265, 35))
                self.countother_txtlbl.setMaximumSize(QtCore.QSize(16777215, 35))
                font = QtGui.QFont()
                font.setPointSize(7)
                self.countother_txtlbl.setFont(font)
                self.countother_txtlbl.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.countother_txtlbl.setText("")
                self.countother_txtlbl.setObjectName("countother_txtlbl")

                self.countother_lbl = QtWidgets.QLabel(self.r_admhomepage)
                self.countother_lbl.setGeometry(QtCore.QRect(370, 420, 127, 35))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.countother_lbl.setFont(font)
                self.countother_lbl.setStyleSheet("background-color: ;\n"
                "background-color: rgb(235, 242, 253);\n"
                "color:black")
                self.countother_lbl.setAlignment(QtCore.Qt.AlignCenter)
                self.countother_lbl.setObjectName("countother_lbl")

                self.adm_home_complogo = QtWidgets.QLabel(self.r_admhomepage)
                self.adm_home_complogo.setGeometry(QtCore.QRect(100, 250, 221, 221))
                self.adm_home_complogo.setStyleSheet("border-color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:1px;\n")
                self.adm_home_complogo.setText("")
                self.adm_home_complogo.setScaledContents(True)
                self.adm_home_complogo.setObjectName("adm_home_complogo")

                self.adm_home_boxlbl = QtWidgets.QLabel(self.r_admhomepage)
                self.adm_home_boxlbl.setGeometry(QtCore.QRect(80, 230, 261, 261))
                self.adm_home_boxlbl.setStyleSheet("border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:50px;\n"
                "border-color:black;\n"
                "background-color: rgb(6, 54, 122);")
                self.adm_home_boxlbl.setText("")
                self.adm_home_boxlbl.setObjectName("adm_home_boxlbl")

                self.selectionbox_lbl_9 = QtWidgets.QLabel(self.r_admhomepage)
                self.selectionbox_lbl_9.setGeometry(QtCore.QRect(40, 530, 781, 241))
                self.selectionbox_lbl_9.setStyleSheet("border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:80px;\n"
                "border-color:black;\n"
                "background-color: rgb(6, 54, 122);")
                self.selectionbox_lbl_9.setText("")
                self.selectionbox_lbl_9.setObjectName("selectionbox_lbl_9")

                self.display_lbl_7 = QtWidgets.QLabel(self.r_admhomepage)
                self.display_lbl_7.setGeometry(QtCore.QRect(60, 570, 741, 121))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.display_lbl_7.setFont(font)
                self.display_lbl_7.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:30px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.display_lbl_7.setAlignment(QtCore.Qt.AlignCenter)
                self.display_lbl_7.setObjectName("display_lbl_7")

                self.backup_btn = QtWidgets.QPushButton(self.r_admhomepage)
                self.backup_btn.setGeometry(QtCore.QRect(300, 710, 270, 40))
                self.backup_btn.setStyleSheet("color: rgb(0, 0, 127);\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.backup_btn.setObjectName("backup_btn")

                self.adm_homehead_boxlbl.raise_()
                self.adm_homehead_txtlbl.raise_()
                self.adm_homehead_statuslbl.raise_()
                self.adm_home_boxlbl.raise_()
                self.adm_home_complogo.raise_()
                self.selectionbox_lbl_9.raise_()
                self.display_lbl_7.raise_()
                self.backup_btn.raise_()
                self.countall_txtlbl.raise_()
                self.countmale_lbl.raise_()
                self.countall_lbl.raise_()
                self.countmale_txtlbl.raise_()
                self.countfem_lbl.raise_()
                self.countfem_txtlbl.raise_()
                self.countother_txtlbl.raise_()
                self.countother_lbl.raise_()

                self.r_window.addWidget(self.r_admhomepage)
                self.r_admquerypage = QtWidgets.QWidget()
                self.r_admquerypage.setObjectName("r_admquerypage")

                self.adm_queryhead_txtlbl = QtWidgets.QLabel(self.r_admquerypage)
                self.adm_queryhead_txtlbl.setGeometry(QtCore.QRect(40, 30, 781, 101))
                font = QtGui.QFont()
                font.setFamily("Mongolian Baiti")
                font.setPointSize(15)
                self.adm_queryhead_txtlbl.setFont(font)
                self.adm_queryhead_txtlbl.setStyleSheet("color: white;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:50px;\n"
                "border-color:black;\n"
                "background-color: rgb(6, 54, 122);")
                self.adm_queryhead_txtlbl.setAlignment(QtCore.Qt.AlignCenter)
                self.adm_queryhead_txtlbl.setObjectName("adm_queryhead_txtlbl")

                self.adm_query_boxlbl = QtWidgets.QLabel(self.r_admquerypage)
                self.adm_query_boxlbl.setGeometry(QtCore.QRect(40, 160, 781, 141))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.adm_query_boxlbl.setFont(font)
                self.adm_query_boxlbl.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:30px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.adm_query_boxlbl.setText("")
                self.adm_query_boxlbl.setAlignment(QtCore.Qt.AlignCenter)
                self.adm_query_boxlbl.setObjectName("adm_query_boxlbl")

                self.adm_query_txtlbl = QtWidgets.QLabel(self.r_admquerypage)
                self.adm_query_txtlbl.setGeometry(QtCore.QRect(60, 180, 51, 31))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.adm_query_txtlbl.setFont(font)
                self.adm_query_txtlbl.setStyleSheet("background-color: white;\n""color:black")
                self.adm_query_txtlbl.setObjectName("adm_query_txtlbl")

                self.adm_query_txtedit = QtWidgets.QTextEdit(self.r_admquerypage)
                self.adm_query_txtedit.setGeometry(QtCore.QRect(120, 180, 671, 80))
                self.adm_query_txtedit.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:1px;\n"
                "border-color:black;")
                self.adm_query_txtedit.setObjectName("adm_query_txtedit")

                self.adm_querydisp_table = QtWidgets.QTableWidget(self.r_admquerypage)
                self.adm_querydisp_table.setGeometry(QtCore.QRect(40, 330, 781, 431))
                self.adm_querydisp_table.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.adm_querydisp_table.setGridStyle(QtCore.Qt.DashDotLine)
                self.adm_querydisp_table.setObjectName("adm_querydisp_table")
                self.adm_querydisp_table.setColumnCount(0)
                self.adm_querydisp_table.setRowCount(0)

                self.adm_query_status_txtlbl = QtWidgets.QLabel(self.r_admquerypage)
                self.adm_query_status_txtlbl.setGeometry(QtCore.QRect(60, 270, 241, 16))
                self.adm_query_status_txtlbl.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.adm_query_status_txtlbl.setObjectName("adm_query_status_txtlbl")

                self.adm_query_confirm_btn = QtWidgets.QPushButton(self.r_admquerypage)
                self.adm_query_confirm_btn.setGeometry(QtCore.QRect(688, 270, 101, 20))
                self.adm_query_confirm_btn.setStyleSheet("color: white;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(6, 54, 122);")
                self.adm_query_confirm_btn.setObjectName("adm_query_confirm_btn")

                self.adm_query_download_btn = QtWidgets.QPushButton(self.r_admquerypage)
                self.adm_query_download_btn.setGeometry(QtCore.QRect(580, 270, 102, 20))
                self.adm_query_download_btn.setStyleSheet("color: white;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(6, 54, 122);")
                self.adm_query_download_btn.setObjectName("adm_query_download_btn")

                self.adm_filename_txtlbl = QtWidgets.QLabel(self.r_admquerypage)
                self.adm_filename_txtlbl.setGeometry(QtCore.QRect(333, 269, 71, 20))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.adm_filename_txtlbl.setFont(font)
                self.adm_filename_txtlbl.setStyleSheet("background-color: white;\n""color:black")
                self.adm_filename_txtlbl.setObjectName("adm_filename_txtlbl")

                self.adm_filename_lineedit = QtWidgets.QLineEdit(self.r_admquerypage)
                self.adm_filename_lineedit.setGeometry(QtCore.QRect(408, 270, 161, 20))
                self.adm_filename_lineedit.setMinimumSize(QtCore.QSize(0, 10))
                self.adm_filename_lineedit.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.adm_filename_lineedit.setObjectName("adm_filename_lineedit")

                self.r_window.addWidget(self.r_admquerypage)
                self.r_updatepage = QtWidgets.QWidget()
                self.r_updatepage.setObjectName("r_updatepage")

                self.adm_update_status_txtlbl = QtWidgets.QLabel(self.r_updatepage)
                self.adm_update_status_txtlbl.setGeometry(QtCore.QRect(60, 270, 611, 16))
                self.adm_update_status_txtlbl.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.adm_update_status_txtlbl.setObjectName("adm_update_status_txtlbl")

                self.adm_update_confirm_btn = QtWidgets.QPushButton(self.r_updatepage)
                self.adm_update_confirm_btn.setGeometry(QtCore.QRect(688, 270, 101, 20))
                self.adm_update_confirm_btn.setStyleSheet("color: white;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(6, 54, 122);")
                self.adm_update_confirm_btn.setObjectName("adm_update_confirm_btn")

                self.adm_update_boxlbl = QtWidgets.QLabel(self.r_updatepage)
                self.adm_update_boxlbl.setGeometry(QtCore.QRect(40, 160, 781, 141))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.adm_update_boxlbl.setFont(font)
                self.adm_update_boxlbl.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:30px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.adm_update_boxlbl.setText("")
                self.adm_update_boxlbl.setAlignment(QtCore.Qt.AlignCenter)
                self.adm_update_boxlbl.setObjectName("adm_update_boxlbl")

                self.adm_updatehead_txtlbl = QtWidgets.QLabel(self.r_updatepage)
                self.adm_updatehead_txtlbl.setGeometry(QtCore.QRect(40, 30, 781, 101))
                font = QtGui.QFont()
                font.setFamily("Mongolian Baiti")
                font.setPointSize(15)
                self.adm_updatehead_txtlbl.setFont(font)
                self.adm_updatehead_txtlbl.setStyleSheet("color: white;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:50px;\n"
                "border-color:black;\n"
                "background-color: rgb(6, 54, 122);")
                self.adm_updatehead_txtlbl.setAlignment(QtCore.Qt.AlignCenter)
                self.adm_updatehead_txtlbl.setObjectName("adm_updatehead_txtlbl")

                self.adm_update_txtedit = QtWidgets.QTextEdit(self.r_updatepage)
                self.adm_update_txtedit.setGeometry(QtCore.QRect(120, 180, 671, 80))
                self.adm_update_txtedit.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:1px;\n"
                "border-color:black;")
                self.adm_update_txtedit.setObjectName("adm_update_txtedit")

                self.adm_update_txtlbl = QtWidgets.QLabel(self.r_updatepage)
                self.adm_update_txtlbl.setGeometry(QtCore.QRect(60, 180, 51, 51))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.adm_update_txtlbl.setFont(font)
                self.adm_update_txtlbl.setStyleSheet("background-color: white;\n""color:black")
                self.adm_update_txtlbl.setObjectName("adm_update_txtlbl")

                self.adm_updatehistory_boxlbl = QtWidgets.QLabel(self.r_updatepage)
                self.adm_updatehistory_boxlbl.setGeometry(QtCore.QRect(40, 330, 781, 431))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.adm_updatehistory_boxlbl.setFont(font)
                self.adm_updatehistory_boxlbl.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:30px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.adm_updatehistory_boxlbl.setText("")
                self.adm_updatehistory_boxlbl.setAlignment(QtCore.Qt.AlignCenter)
                self.adm_updatehistory_boxlbl.setObjectName("adm_updatehistory_boxlbl")

                self.adm_historysubhead_txtlbl = QtWidgets.QLabel(self.r_updatepage)
                self.adm_historysubhead_txtlbl.setGeometry(QtCore.QRect(60, 350, 741, 61))
                self.adm_historysubhead_txtlbl.setStyleSheet("border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:30px;\n"
                "border-color:black;\n"
                "background-color: rgb(6, 54, 122);\n"
                "color:rgb(255, 255, 255)")
                self.adm_historysubhead_txtlbl.setAlignment(QtCore.Qt.AlignCenter)
                self.adm_historysubhead_txtlbl.setObjectName("adm_historysubhead_txtlbl")

                self.adm_historydisp_table = QtWidgets.QTableWidget(self.r_updatepage)
                self.adm_historydisp_table.setGeometry(QtCore.QRect(80, 450, 701, 271))
                self.adm_historydisp_table.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.adm_historydisp_table.setGridStyle(QtCore.Qt.DashDotLine)
                self.adm_historydisp_table.setObjectName("adm_historydisp_table")
                self.adm_historydisp_table.setColumnCount(1)
                self.adm_historydisp_table.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.adm_historydisp_table.setHorizontalHeaderItem(0, item)
                self.adm_historydisp_table.horizontalHeader().setDefaultSectionSize(675)

                self.adm_update_boxlbl.raise_()
                self.adm_updatehead_txtlbl.raise_()
                self.adm_update_txtedit.raise_()
                self.adm_update_txtlbl.raise_()
                self.adm_update_status_txtlbl.raise_()
                self.adm_update_confirm_btn.raise_()
                self.adm_updatehistory_boxlbl.raise_()
                self.adm_historysubhead_txtlbl.raise_()
                self.adm_historydisp_table.raise_()

                self.r_window.addWidget(self.r_updatepage)
                self.r_admannouncepage = QtWidgets.QWidget()
                self.r_admannouncepage.setObjectName("r_admannouncepage")

                self.adm_annto_combobox = QtWidgets.QComboBox(self.r_admannouncepage)
                self.adm_annto_combobox.setGeometry(QtCore.QRect(140, 180, 331, 31))
                self.adm_annto_combobox.setObjectName("adm_annto_combobox")
                self.adm_annto_combobox.addItem("")

                self.adm_ann_boxlbl = QtWidgets.QLabel(self.r_admannouncepage)
                self.adm_ann_boxlbl.setGeometry(QtCore.QRect(40, 160, 781, 71))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.adm_ann_boxlbl.setFont(font)
                self.adm_ann_boxlbl.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:30px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.adm_ann_boxlbl.setText("")
                self.adm_ann_boxlbl.setAlignment(QtCore.Qt.AlignCenter)
                self.adm_ann_boxlbl.setObjectName("adm_ann_boxlbl")

                self.adm_announcehead_txtlbl = QtWidgets.QLabel(self.r_admannouncepage)
                self.adm_announcehead_txtlbl.setGeometry(QtCore.QRect(40, 30, 781, 101))
                font = QtGui.QFont()
                font.setFamily("Mongolian Baiti")
                font.setPointSize(15)
                self.adm_announcehead_txtlbl.setFont(font)
                self.adm_announcehead_txtlbl.setStyleSheet("color: white;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:50px;\n"
                "border-color:black;\n"
                "background-color: rgb(6, 54, 122);")
                self.adm_announcehead_txtlbl.setAlignment(QtCore.Qt.AlignCenter)
                self.adm_announcehead_txtlbl.setObjectName("adm_announcehead_txtlbl")

                self.adm_sentmode_radiobtn = QtWidgets.QRadioButton(self.r_admannouncepage)
                self.adm_sentmode_radiobtn.setGeometry(QtCore.QRect(660, 180, 121, 31))
                self.adm_sentmode_radiobtn.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.adm_sentmode_radiobtn.setObjectName("adm_sentmode_radiobtn")

                self.adm_annto_txtlbl = QtWidgets.QLabel(self.r_admannouncepage)
                self.adm_annto_txtlbl.setGeometry(QtCore.QRect(70, 180, 61, 31))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.adm_annto_txtlbl.setFont(font)
                self.adm_annto_txtlbl.setStyleSheet("background-color: white;\n""color:black")
                self.adm_annto_txtlbl.setObjectName("adm_annto_txtlbl")

                self.adm_sendmode_radiobtn = QtWidgets.QRadioButton(self.r_admannouncepage)
                self.adm_sendmode_radiobtn.setGeometry(QtCore.QRect(530, 180, 95, 31))
                self.adm_sendmode_radiobtn.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.adm_sendmode_radiobtn.setChecked(True)
                self.adm_sendmode_radiobtn.setObjectName("adm_sendmode_radiobtn")

                self.adm_annsentsend_stckwdgt = QtWidgets.QStackedWidget(self.r_admannouncepage)
                self.adm_annsentsend_stckwdgt.setGeometry(QtCore.QRect(40, 260, 781, 501))
                self.adm_annsentsend_stckwdgt.setObjectName("adm_annsentsend_stckwdgt")

                self.adm_sendann_page = QtWidgets.QWidget()
                self.adm_sendann_page.setObjectName("adm_sendann_page")

                self.adm_ann_boxlbl_2 = QtWidgets.QLabel(self.adm_sendann_page)
                self.adm_ann_boxlbl_2.setGeometry(QtCore.QRect(0, 0, 781, 501))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.adm_ann_boxlbl_2.setFont(font)
                self.adm_ann_boxlbl_2.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:30px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.adm_ann_boxlbl_2.setText("")
                self.adm_ann_boxlbl_2.setAlignment(QtCore.Qt.AlignCenter)
                self.adm_ann_boxlbl_2.setObjectName("adm_ann_boxlbl_2")

                self.adm_ann_txtlbl = QtWidgets.QLabel(self.adm_sendann_page)
                self.adm_ann_txtlbl.setGeometry(QtCore.QRect(30, 30, 111, 31))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.adm_ann_txtlbl.setFont(font)
                self.adm_ann_txtlbl.setStyleSheet("background-color: white;\n""color:black")
                self.adm_ann_txtlbl.setObjectName("adm_ann_txtlbl")

                self.adm_sendann_btn = QtWidgets.QPushButton(self.adm_sendann_page)
                self.adm_sendann_btn.setGeometry(QtCore.QRect(660, 460, 93, 28))
                self.adm_sendann_btn.setStyleSheet("color: white;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(6, 54, 122);")
                self.adm_sendann_btn.setObjectName("adm_sendann_btn")

                self.adm_ann_txtedit = QtWidgets.QTextEdit(self.adm_sendann_page)
                self.adm_ann_txtedit.setGeometry(QtCore.QRect(30, 60, 721, 391))
                self.adm_ann_txtedit.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:1px;\n"
                "border-color:black;")
                self.adm_ann_txtedit.setObjectName("adm_ann_txtedit")

                self.adm_annstatus_txtlbl = QtWidgets.QLabel(self.adm_sendann_page)
                self.adm_annstatus_txtlbl.setGeometry(QtCore.QRect(30, 460, 611, 16))
                self.adm_annstatus_txtlbl.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.adm_annstatus_txtlbl.setObjectName("adm_annstatus_txtlbl")

                self.adm_annsentsend_stckwdgt.addWidget(self.adm_sendann_page)
                self.adm_sentann_page = QtWidgets.QWidget()
                self.adm_sentann_page.setObjectName("adm_sentann_page")
                self.adm_sentann_table = QtWidgets.QTableWidget(self.adm_sentann_page)
                self.adm_sentann_table.setGeometry(QtCore.QRect(0, 0, 781, 501))
                self.adm_sentann_table.setStyleSheet("color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.adm_sentann_table.setGridStyle(QtCore.Qt.DashDotLine)
                self.adm_sentann_table.setObjectName("adm_sentann_table")
                self.adm_sentann_table.setColumnCount(3)
                self.adm_sentann_table.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.adm_sentann_table.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.adm_sentann_table.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.adm_sentann_table.setHorizontalHeaderItem(2, item)

                self.adm_annsentsend_stckwdgt.addWidget(self.adm_sentann_page)
                self.adm_ann_boxlbl.raise_()
                self.adm_announcehead_txtlbl.raise_()
                self.adm_sentmode_radiobtn.raise_()
                self.adm_annto_txtlbl.raise_()
                self.adm_sendmode_radiobtn.raise_()
                self.adm_annto_combobox.raise_()
                self.adm_annsentsend_stckwdgt.raise_()

                self.r_window.addWidget(self.r_admannouncepage)

                self.l_window = QtWidgets.QStackedWidget(self.centralwidget)
                self.l_window.setGeometry(QtCore.QRect(0, 0, 341, 801))
                self.l_window.setStyleSheet("background-color: rgb(6, 54, 122)")
                self.l_window.setObjectName("l_window")

                self.l_loginpage = QtWidgets.QWidget()
                self.l_loginpage.setObjectName("l_loginpage")

                self.logo_imglbl = QtWidgets.QLabel(self.l_loginpage)
                self.logo_imglbl.setGeometry(QtCore.QRect(20, 100, 301, 301))
                self.logo_imglbl.setStyleSheet("border-color: black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:1px;\n")
                self.logo_imglbl.setText("")
                self.logo_imglbl.setScaledContents(True)
                self.logo_imglbl.setObjectName("logo_imglbl")

                self.layoutWidget = QtWidgets.QWidget(self.l_loginpage)
                self.layoutWidget.setGeometry(QtCore.QRect(10, 410, 321, 91))
                self.layoutWidget.setObjectName("layoutWidget")

                self.input_grid = QtWidgets.QGridLayout(self.layoutWidget)
                self.input_grid.setContentsMargins(0, 0, 0, 0)
                self.input_grid.setObjectName("input_grid")

                self.key_lineinp = QtWidgets.QLineEdit(self.layoutWidget)
                self.key_lineinp.setStyleSheet("border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "background-color:white")
                self.key_lineinp.setObjectName("key_lineinp")
                self.key_lineinp.setEchoMode(QtWidgets.QLineEdit.Password)

                self.input_grid.addWidget(self.key_lineinp, 1, 1, 1, 1)

                self.user_lineinp = QtWidgets.QLineEdit(self.layoutWidget)
                self.user_lineinp.setStyleSheet("border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "background-color:white")
                self.user_lineinp.setText("")
                self.user_lineinp.setObjectName("user_lineinp")
                self.input_grid.addWidget(self.user_lineinp, 0, 1, 1, 1)

                self.key_lbl = QtWidgets.QLabel(self.layoutWidget)
                self.key_lbl.setStyleSheet("background-color: transparent;\n""color:white")
                self.key_lbl.setObjectName("key_lbl")
                self.input_grid.addWidget(self.key_lbl, 1, 0, 1, 1)

                self.user_lbl = QtWidgets.QLabel(self.layoutWidget)
                self.user_lbl.setStyleSheet("background-color: transparent;\n""color:white")
                self.user_lbl.setObjectName("user_lbl")
                self.input_grid.addWidget(self.user_lbl, 0, 0, 1, 1)

                self.company_lbl = QtWidgets.QLabel(self.l_loginpage)
                self.company_lbl.setGeometry(QtCore.QRect(0, 780, 321, 20))
                font = QtGui.QFont()
                font.setPointSize(7)
                self.company_lbl.setFont(font)
                self.company_lbl.setStyleSheet("color: white")
                self.company_lbl.setAlignment(QtCore.Qt.AlignCenter)
                self.company_lbl.setObjectName("company_lbl")

                self.verticalLayoutWidget = QtWidgets.QWidget(self.l_loginpage)
                self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 510, 321, 81))
                self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
                self.confirmstatusgrid = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)

                self.confirmstatusgrid.setContentsMargins(0, 0, 0, 0)
                self.confirmstatusgrid.setObjectName("confirmstatusgrid")

                self.confirm_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
                self.confirm_btn.setStyleSheet("background-color:white;\n"
                "color:black;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black")
                self.confirm_btn.setObjectName("confirm_btn")
                self.confirmstatusgrid.addWidget(self.confirm_btn)

                self.status = QtWidgets.QLabel(self.verticalLayoutWidget)
                self.status.setStyleSheet("background-color: transparent;\n"
                "color:white")
                self.status.setAlignment(QtCore.Qt.AlignCenter)
                self.status.setObjectName("status")
                self.confirmstatusgrid.addWidget(self.status)

                self.Quit_btn = QtWidgets.QPushButton(self.l_loginpage)
                self.Quit_btn.setGeometry(QtCore.QRect(40, 740, 261, 31))
                self.Quit_btn.setStyleSheet("color: rgb(0, 0, 127);\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.Quit_btn.setObjectName("Quit_btn")

                self.l_window.addWidget(self.l_loginpage)

                self.l_employeetab = QtWidgets.QWidget()
                self.l_employeetab.setObjectName("l_employeetab")

                self.gridLayoutWidget = QtWidgets.QWidget(self.l_employeetab)
                self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 321, 72))
                self.gridLayoutWidget.setObjectName("gridLayoutWidget")

                self.curuser_grid = QtWidgets.QGridLayout(self.gridLayoutWidget)
                self.curuser_grid.setContentsMargins(0, 0, 0, 0)
                self.curuser_grid.setObjectName("curuser_grid")

                self.user_img = QtWidgets.QLabel(self.gridLayoutWidget)
                self.user_img.setMaximumSize(QtCore.QSize(70, 70))
                self.user_img.setText("")
                self.user_img.setScaledContents(True)
                self.user_img.setObjectName("user_img")
                self.curuser_grid.addWidget(self.user_img, 0, 0, 2, 1)

                self.lname_lbl = QtWidgets.QLabel(self.gridLayoutWidget)
                self.lname_lbl.setMaximumSize(QtCore.QSize(16777215, 35))
                font = QtGui.QFont()
                font.setPointSize(7)
                self.lname_lbl.setFont(font)
                self.lname_lbl.setStyleSheet("color: white")
                self.lname_lbl.setText("")
                self.lname_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
                self.lname_lbl.setObjectName("lname_lbl")
                self.curuser_grid.addWidget(self.lname_lbl, 0, 2, 1, 1)

                self.lmail_lbl = QtWidgets.QLabel(self.gridLayoutWidget)
                self.lmail_lbl.setMaximumSize(QtCore.QSize(16777215, 35))
                font = QtGui.QFont()
                font.setPointSize(7)
                self.lmail_lbl.setFont(font)
                self.lmail_lbl.setStyleSheet("color: white")
                self.lmail_lbl.setText("")
                self.lmail_lbl.setObjectName("lmail_lbl")
                self.curuser_grid.addWidget(self.lmail_lbl, 1, 2, 1, 1)

                spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                
                self.curuser_grid.addItem(spacerItem2, 0, 1, 1, 1)
                self.curuser_grid.setColumnStretch(0, 20)
                self.curuser_grid.setColumnStretch(1, 2)
                self.curuser_grid.setColumnStretch(2, 60)

                self.gridLayoutWidget_3 = QtWidgets.QWidget(self.l_employeetab)
                self.gridLayoutWidget_3.setGeometry(QtCore.QRect(30, 130, 281, 326))
                self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")

                self.features_grid = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
                self.features_grid.setContentsMargins(0, 0, 0, 0)
                self.features_grid.setObjectName("features_grid")

                self.inbox_btn = QtWidgets.QPushButton(self.gridLayoutWidget_3)
                self.inbox_btn.setMinimumSize(QtCore.QSize(0, 30))
                self.inbox_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:white")
                self.inbox_btn.setObjectName("inbox_btn")
                self.features_grid.addWidget(self.inbox_btn, 5, 2, 1, 1)

                spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.features_grid.addItem(spacerItem3, 6, 2, 1, 1)

                self.personal_img = QtWidgets.QLabel(self.gridLayoutWidget_3)
                self.personal_img.setMinimumSize(QtCore.QSize(50, 50))
                self.personal_img.setMaximumSize(QtCore.QSize(50, 50))
                self.personal_img.setText("")
                self.personal_img.setScaledContents(True)
                self.personal_img.setObjectName("personal_img")
                self.features_grid.addWidget(self.personal_img, 0, 0, 2, 1)

                spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.features_grid.addItem(spacerItem4, 8, 2, 1, 1)

                self.supervisor_btn = QtWidgets.QPushButton(self.gridLayoutWidget_3)
                self.supervisor_btn.setMinimumSize(QtCore.QSize(0, 30))
                self.supervisor_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:white")
                self.supervisor_btn.setObjectName("supervisor_btn")
                self.features_grid.addWidget(self.supervisor_btn, 9, 2, 1, 1)
                
                spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.features_grid.addItem(spacerItem5, 0, 1, 1, 1)
                
                self.inbox_img = QtWidgets.QLabel(self.gridLayoutWidget_3)
                self.inbox_img.setMinimumSize(QtCore.QSize(50, 50))
                self.inbox_img.setMaximumSize(QtCore.QSize(50, 50))
                self.inbox_img.setText("")          
                self.inbox_img.setScaledContents(True)
                self.inbox_img.setObjectName("inbox_img")
                self.features_grid.addWidget(self.inbox_img, 5, 0, 1, 1)
                
                self.department_btn = QtWidgets.QPushButton(self.gridLayoutWidget_3)
                self.department_btn.setMinimumSize(QtCore.QSize(0, 30))
                self.department_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:white")
                self.department_btn.setObjectName("department_btn")
                self.features_grid.addWidget(self.department_btn, 3, 2, 1, 1)
                
                spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.features_grid.addItem(spacerItem6, 2, 2, 1, 1)
                
                self.supervisor_img = QtWidgets.QLabel(self.gridLayoutWidget_3)
                self.supervisor_img.setMinimumSize(QtCore.QSize(50, 50))
                self.supervisor_img.setMaximumSize(QtCore.QSize(50, 50))
                self.supervisor_img.setText("")
                self.supervisor_img.setScaledContents(True)
                self.supervisor_img.setObjectName("supervisor_img")
                self.features_grid.addWidget(self.supervisor_img, 9, 0, 1, 1)
                
                spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.features_grid.addItem(spacerItem7, 4, 2, 1, 1)
                
                self.department_img = QtWidgets.QLabel(self.gridLayoutWidget_3)
                self.department_img.setMinimumSize(QtCore.QSize(50, 50))
                self.department_img.setMaximumSize(QtCore.QSize(50, 50))
                self.department_img.setText("")
                self.department_img.setScaledContents(True)
                self.department_img.setObjectName("department_img")
                self.features_grid.addWidget(self.department_img, 3, 0, 1, 1)
                
                self.personal_btn = QtWidgets.QPushButton(self.gridLayoutWidget_3)
                self.personal_btn.setMinimumSize(QtCore.QSize(0, 30))
                self.personal_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:white")
                self.personal_btn.setObjectName("personal_btn")
                self.features_grid.addWidget(self.personal_btn, 0, 2, 2, 1)
                
                self.send_btn = QtWidgets.QPushButton(self.gridLayoutWidget_3)
                self.send_btn.setMinimumSize(QtCore.QSize(0, 30))
                self.send_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:white")
                self.send_btn.setObjectName("send_btn")
                self.features_grid.addWidget(self.send_btn, 7, 2, 1, 1)
                
                self.send_img = QtWidgets.QLabel(self.gridLayoutWidget_3)
                self.send_img.setMinimumSize(QtCore.QSize(50, 50))
                self.send_img.setMaximumSize(QtCore.QSize(50, 50))
                self.send_img.setText("")
                self.send_img.setScaledContents(True)
                self.send_img.setObjectName("send_img")
                self.features_grid.addWidget(self.send_img, 7, 0, 1, 1)
                
                self.features_grid.setColumnStretch(0, 20)
                self.features_grid.setColumnStretch(1, 1)
                self.features_grid.setColumnStretch(2, 60)
                
                self.signout_btn = QtWidgets.QPushButton(self.l_employeetab)
                self.signout_btn.setGeometry(QtCore.QRect(40, 740, 261, 31))
                self.signout_btn.setStyleSheet("color: rgb(0, 0, 127);\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.signout_btn.setObjectName("signout_btn")
                
                self.company_lbl_empgui = QtWidgets.QLabel(self.l_employeetab)
                self.company_lbl_empgui.setGeometry(QtCore.QRect(0, 780, 321, 20))
                font = QtGui.QFont()
                font.setPointSize(7)
                self.company_lbl_empgui.setFont(font)
                self.company_lbl_empgui.setStyleSheet("color: white")
                self.company_lbl_empgui.setAlignment(QtCore.Qt.AlignCenter)
                self.company_lbl_empgui.setObjectName("company_lbl_empgui")
                
                self.home_btn = QtWidgets.QPushButton(self.l_employeetab)
                self.home_btn.setGeometry(QtCore.QRect(40, 699, 261, 31))
                self.home_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:white")
                self.home_btn.setObjectName("home_btn")
                
                self.l_window.addWidget(self.l_employeetab)
                
                self.l_admintab = QtWidgets.QWidget()
                self.l_admintab.setObjectName("l_admintab")
                
                self.gridLayoutWidget_4 = QtWidgets.QWidget(self.l_admintab)
                self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 20, 321, 72))
                self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
                
                self.curuser_grid_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
                self.curuser_grid_2.setContentsMargins(0, 0, 0, 0)
                self.curuser_grid_2.setObjectName("curuser_grid_2")
                
                self.ladmin_imglbl = QtWidgets.QLabel(self.gridLayoutWidget_4)
                self.ladmin_imglbl.setMaximumSize(QtCore.QSize(70, 70))
                self.ladmin_imglbl.setText("")
                self.ladmin_imglbl.setScaledContents(True)
                self.ladmin_imglbl.setObjectName("ladmin_imglbl")
                self.curuser_grid_2.addWidget(self.ladmin_imglbl, 0, 0, 2, 1)
                
                self.lname_lbl_adm = QtWidgets.QLabel(self.gridLayoutWidget_4)
                self.lname_lbl_adm.setMaximumSize(QtCore.QSize(16777215, 35))
                font = QtGui.QFont()
                font.setPointSize(7)
                self.lname_lbl_adm.setFont(font)
                self.lname_lbl_adm.setStyleSheet("color: white")
                self.lname_lbl_adm.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
                self.lname_lbl_adm.setObjectName("lname_lbl_adm")
                self.curuser_grid_2.addWidget(self.lname_lbl_adm, 0, 2, 1, 1)
                
                self.lmail_lbl_adm = QtWidgets.QLabel(self.gridLayoutWidget_4)
                self.lmail_lbl_adm.setMaximumSize(QtCore.QSize(16777215, 35))
                font = QtGui.QFont()
                font.setPointSize(7)
                self.lmail_lbl_adm.setFont(font)
                self.lmail_lbl_adm.setStyleSheet("color: white")
                self.lmail_lbl_adm.setObjectName("lmail_lbl_adm")
                self.curuser_grid_2.addWidget(self.lmail_lbl_adm, 1, 2, 1, 1)
                
                spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.curuser_grid_2.addItem(spacerItem8, 0, 1, 1, 1)
                self.curuser_grid_2.setColumnStretch(0, 20)
                self.curuser_grid_2.setColumnStretch(1, 2)
                self.curuser_grid_2.setColumnStretch(2, 60)
                
                self.gridLayoutWidget_6 = QtWidgets.QWidget(self.l_admintab)
                self.gridLayoutWidget_6.setGeometry(QtCore.QRect(30, 130, 281, 191))
                self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
                
                self.features_grid_adm = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
                self.features_grid_adm.setContentsMargins(0, 0, 0, 0)
                self.features_grid_adm.setObjectName("features_grid_adm")
                
                spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.features_grid_adm.addItem(spacerItem9, 2, 2, 1, 1)
                
                self.l_announcementimage = QtWidgets.QLabel(self.gridLayoutWidget_6)
                self.l_announcementimage.setMinimumSize(QtCore.QSize(50, 50))
                self.l_announcementimage.setMaximumSize(QtCore.QSize(50, 50))
                self.l_announcementimage.setText("")
                self.l_announcementimage.setScaledContents(True)
                self.l_announcementimage.setObjectName("l_announcementimage")
                self.features_grid_adm.addWidget(self.l_announcementimage, 5, 0, 1, 1)
                
                self.l_announcementbtn = QtWidgets.QPushButton(self.gridLayoutWidget_6)
                self.l_announcementbtn.setMinimumSize(QtCore.QSize(0, 30))
                self.l_announcementbtn.setStyleSheet("color: rgb(255, 255, 255);\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:white")
                self.l_announcementbtn.setObjectName("l_announcementbtn")
                self.features_grid_adm.addWidget(self.l_announcementbtn, 5, 2, 1, 1)
                
                spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.features_grid_adm.addItem(spacerItem10, 0, 1, 1, 1)
                
                self.l_queryimg = QtWidgets.QLabel(self.gridLayoutWidget_6)
                self.l_queryimg.setMinimumSize(QtCore.QSize(50, 50))
                self.l_queryimg.setMaximumSize(QtCore.QSize(50, 50))
                self.l_queryimg.setText("")
                self.l_queryimg.setScaledContents(True)
                self.l_queryimg.setObjectName("l_queryimg")
                self.features_grid_adm.addWidget(self.l_queryimg, 0, 0, 2, 1)
                
                self.l_querybtn = QtWidgets.QPushButton(self.gridLayoutWidget_6)
                self.l_querybtn.setMinimumSize(QtCore.QSize(0, 30))
                self.l_querybtn.setStyleSheet("color: rgb(255, 255, 255);\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:white")
                self.l_querybtn.setObjectName("l_querybtn")
                self.features_grid_adm.addWidget(self.l_querybtn, 0, 2, 2, 1)
                
                spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.features_grid_adm.addItem(spacerItem11, 4, 2, 1, 1)
                
                self.l_updatebtn = QtWidgets.QPushButton(self.gridLayoutWidget_6)
                self.l_updatebtn.setMinimumSize(QtCore.QSize(0, 30))
                self.l_updatebtn.setStyleSheet("color: rgb(255, 255, 255);\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:white")
                self.l_updatebtn.setObjectName("l_updatebtn")
                self.features_grid_adm.addWidget(self.l_updatebtn, 3, 2, 1, 1)
                
                self.l_updateimage = QtWidgets.QLabel(self.gridLayoutWidget_6)
                self.l_updateimage.setMinimumSize(QtCore.QSize(50, 50))
                self.l_updateimage.setMaximumSize(QtCore.QSize(50, 50))
                self.l_updateimage.setText("")
                self.l_updateimage.setScaledContents(True)
                self.l_updateimage.setObjectName("l_updateimage")
                self.features_grid_adm.addWidget(self.l_updateimage, 3, 0, 1, 1)
                
                self.features_grid_adm.setColumnStretch(0, 20)
                self.features_grid_adm.setColumnStretch(1, 1)
                self.features_grid_adm.setColumnStretch(2, 60)
                self.features_grid_adm.setRowStretch(0, 10)
                
                self.adm_home_btn = QtWidgets.QPushButton(self.l_admintab)
                self.adm_home_btn.setGeometry(QtCore.QRect(40, 699, 261, 31))
                self.adm_home_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:white")
                self.adm_home_btn.setObjectName("adm_home_btn")
                
                self.adm_signout_btn = QtWidgets.QPushButton(self.l_admintab)
                self.adm_signout_btn.setGeometry(QtCore.QRect(40, 740, 261, 31))
                self.adm_signout_btn.setStyleSheet("color: rgb(0, 0, 127);\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.adm_signout_btn.setObjectName("adm_signout_btn")
                
                self.company_lbl_empgui_3 = QtWidgets.QLabel(self.l_admintab)
                self.company_lbl_empgui_3.setGeometry(QtCore.QRect(0, 780, 321, 20))
                font = QtGui.QFont()
                font.setPointSize(7)
                self.company_lbl_empgui_3.setFont(font)
                self.company_lbl_empgui_3.setStyleSheet("color: white")
                self.company_lbl_empgui_3.setAlignment(QtCore.Qt.AlignCenter)
                self.company_lbl_empgui_3.setObjectName("company_lbl_empgui_3")
                
                self.l_window.addWidget(self.l_admintab)
                MainWindow.setCentralWidget(self.centralwidget)

                self.retranslateUi(MainWindow)
                self.r_window.setCurrentIndex(0)
                self.sendmodes_stckwidget.setCurrentIndex(0)
                self.adm_annsentsend_stckwdgt.setCurrentIndex(0)
                self.l_window.setCurrentIndex(0)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

                #Setting up PixMaps

                self.logo_imglbl.setPixmap(QtGui.QPixmap(company_logo))
                self.aesthetic_imglbl.setPixmap(QtGui.QPixmap(aesthetic_banner))
                self.cardlogo_imglbl.setPixmap(QtGui.QPixmap(company_logo))
                self.user_img.setPixmap(QtGui.QPixmap(user_logo))
                self.personal_img.setPixmap(QtGui.QPixmap(personal_logo))
                self.department_img.setPixmap(QtGui.QPixmap(department_logo))
                self.inbox_img.setPixmap(QtGui.QPixmap(inbox_logo))
                self.send_img.setPixmap(QtGui.QPixmap(send_logo))
                self.supervisor_img.setPixmap(QtGui.QPixmap(supervisor_logo))
                self.adm_home_complogo.setPixmap(QtGui.QPixmap(company_logo))
                self.ladmin_imglbl.setPixmap(QtGui.QPixmap(user_logo))
                self.l_queryimg.setPixmap(QtGui.QPixmap(personal_logo))
                self.l_updateimage.setPixmap(QtGui.QPixmap(department_logo))
                self.l_announcementimage.setPixmap(QtGui.QPixmap(department_logo))

                #Buttons Connection to Defined Functions

                self.confirm_btn.clicked.connect(self.check)
                self.personal_btn.clicked.connect(self.openpersonal)
                self.confirmchange_btn.clicked.connect(self.changepersonal)
                self.department_btn.clicked.connect(self.opendepartment)
                self.inbox_btn.clicked.connect(self.openinbox)
                self.send_btn.clicked.connect(self.opensend)
                self.sendmode_radiobtn.clicked.connect(self.opensendmode)
                self.sendmsg_btn.clicked.connect(self.sendmsg)
                self.sentmode_radiobtn.clicked.connect(self.opensentmode)
                self.supervisor_btn.clicked.connect(self.opensupervisor)
                self.home_btn.clicked.connect(self.openemphome)
                self.signout_btn.clicked.connect(self.signout)
                self.backup_btn.clicked.connect(self.backuptables)
                self.l_querybtn.clicked.connect(self.openquery)
                self.adm_query_confirm_btn.clicked.connect(self.execquery)
                self.adm_query_download_btn.clicked.connect(self.downloadtable)
                self.l_updatebtn.clicked.connect(self.openupdate)
                self.adm_update_confirm_btn.clicked.connect(self.makeupdate)
                self.adm_sentmode_radiobtn.clicked.connect(self.openadmsentmode)
                self.adm_sendmode_radiobtn.clicked.connect(self.openadmsendmode)
                self.adm_sendann_btn.clicked.connect(self.sendann)
                self.Quit_btn.clicked.connect(self.quitsystem)
                self.Quit_btn.clicked.connect(QCoreApplication.instance().quit)
                self.l_announcementbtn.clicked.connect(self.openannouncement)
                self.adm_home_btn.clicked.connect(self.openadmhome)
                self.adm_signout_btn.clicked.connect(self.admsignout)

        def retranslateUi(self, MainWindow):
                
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.cardjob_lbl.setText(_translate("MainWindow", "Job:"))
                self.cardmail_lbl.setText(_translate("MainWindow", "Mail:"))
                self.cardcontact_lbl.setText(_translate("MainWindow", "Contact:"))
                self.cardname_lbl.setText(_translate("MainWindow", "Name:"))
                self.company_lbl_card.setText(_translate("MainWindow", "TechGenix Solutions Pvt. Ltd.   Contact: 011-XXXX-XXXX"))
                self.address_lbl.setText(_translate("MainWindow", "Address:"))
                self.firstname_lbl.setText(_translate("MainWindow", "First Name:"))
                self.lastname_lbl.setText(_translate("MainWindow", "Last Name:"))
                self.gender_lbl.setText(_translate("MainWindow", "Gender:"))
                self.dob_lbl.setText(_translate("MainWindow", "DOB:"))
                self.middlename_lbl.setText(_translate("MainWindow", "Middle Name:"))
                self.city_lbl.setText(_translate("MainWindow", "City:"))
                self.state_lbl.setText(_translate("MainWindow", "State:"))
                self.zipcode_lbl.setText(_translate("MainWindow", "Zip Code:"))
                self.contact_lbl.setText(_translate("MainWindow", "Contact:"))
                self.editstate_lbl.setText(_translate("MainWindow", "State:"))
                self.editfirstname_lbl.setText(_translate("MainWindow", "First Name:"))
                self.editlastname_lbl.setText(_translate("MainWindow", "Last Name:"))
                self.editzipcode_lbl.setText(_translate("MainWindow", "Zip Code:"))
                self.editcontact_lbl.setText(_translate("MainWindow", "Contact:"))
                self.editaddress_lbl.setText(_translate("MainWindow", "Address:"))
                self.editdob_lbl.setText(_translate("MainWindow", "DOB:"))
                self.editmiddlename_lbl.setText(_translate("MainWindow", "Middle Name:"))
                self.editcity_lbl.setText(_translate("MainWindow", "City:"))
                self.editgender_lbl.setText(_translate("MainWindow", "Gender:"))
                self.gender_chkbox.setText(_translate("MainWindow", "Gender"))
                self.address_chkbox.setText(_translate("MainWindow", "Address"))
                self.state_chkbox.setText(_translate("MainWindow", "State"))
                self.zipcode_chkbox.setText(_translate("MainWindow", "Zip Code"))
                self.city_chkbox.setText(_translate("MainWindow", "City"))
                self.lastname_chkbox.setText(_translate("MainWindow", "Last Name"))
                self.middlename_chkbox.setText(_translate("MainWindow", "Middle Name"))
                self.display_lbl.setText(_translate("MainWindow", "Select the Checkboxes for the categories where changes are to be made\n"
                "\n"
                "Format for Address: House_No.-St.Type-St.Name\n"
                "Format for Date Of Birth: YYYY-MM-DD"))
                self.dob_chkbox.setText(_translate("MainWindow", "Date Of Birth"))
                self.firstname_chkbox.setText(_translate("MainWindow", "First Name"))
                self.contact_chkbox.setText(_translate("MainWindow", "Contact"))
                self.confirmchange_btn.setText(_translate("MainWindow", "Confirm Changes"))
                self.confirmchange_btn.setShortcut(_translate("MainWindow", "Return"))
                self.changestatus_txtlbl.setText(_translate("MainWindow", "Click Confirm to Apply Changes"))
                self.dephead_txtlbl.setText(_translate("MainWindow", "Department Name Here"))
                item = self.dep_table.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "Name"))
                item = self.dep_table.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "Gender"))
                item = self.dep_table.horizontalHeaderItem(2)
                item.setText(_translate("MainWindow", "Job"))
                item = self.dep_table.horizontalHeaderItem(3)
                item.setText(_translate("MainWindow", "Mail"))
                self.inbox_txtlbl.setText(_translate("MainWindow", "INBOX"))
                item = self.inbox_table.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "Time"))
                item = self.inbox_table.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "Recieved From"))
                item = self.inbox_table.horizontalHeaderItem(2)
                item.setText(_translate("MainWindow", "Message"))
                self.message_txtlbl.setText(_translate("MainWindow", "Message Colleagues"))
                self.to_combobox.setItemText(0, _translate("MainWindow", "Select Recipient"))
                self.to_txtlbl.setText(_translate("MainWindow", "To:"))
                self.sendmode_radiobtn.setText(_translate("MainWindow", "Send Mode"))
                self.sendmode_radiobtn.setShortcut(_translate("MainWindow", "Q"))
                self.sentmode_radiobtn.setText(_translate("MainWindow", "View Sent Mode"))
                self.sentmode_radiobtn.setShortcut(_translate("MainWindow", "W"))
                self.sendmsg_btn.setText(_translate("MainWindow", "Send"))
                self.msgstatus_lbl.setText(_translate("MainWindow", "Choose Recipient. Type Message. Press Send."))
                self.msg_txtlbl.setText(_translate("MainWindow", "Message:"))
                item = self.sent_table.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "Time"))
                item = self.sent_table.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "Sent to"))
                item = self.sent_table.horizontalHeaderItem(2)
                item.setText(_translate("MainWindow", "Message"))
                self.supervisor_txtlbl.setText(_translate("MainWindow", "SUPERVISORS"))
                item = self.supervisor_table.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "Name"))
                item = self.supervisor_table.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "Department"))
                item = self.supervisor_table.horizontalHeaderItem(2)
                item.setText(_translate("MainWindow", "Mail"))
                self.adm_homehead_txtlbl.setText(_translate("MainWindow", "ADMIN PANEL"))
                self.adm_homehead_statuslbl.setText(_translate("MainWindow", "Welcome, ADMIN"))
                self.countmale_lbl.setText(_translate("MainWindow", "Male Employees:"))
                self.countall_lbl.setText(_translate("MainWindow", "No of Employees:"))
                self.countfem_lbl.setText(_translate("MainWindow", "Female Employees:"))
                self.countother_lbl.setText(_translate("MainWindow", "Other Employees:"))
                self.display_lbl_7.setText(_translate("MainWindow", "Click the Backup Button to get all the System Databases in a .csv in the Downloads Folder.\n"
                "\n"
                "Go To Query, Type and Custom Query, Type a Name and Click Download\n"
                "to obtain a custom .csv in the Downloads Folder\n"
                "\n"
                "Tables: Employee, UserKeys, Messages, Details, Updates"))
                self.backup_btn.setText(_translate("MainWindow", "Backup"))
                self.backup_btn.setShortcut(_translate("MainWindow","Return"))
                self.adm_queryhead_txtlbl.setText(_translate("MainWindow", "QUERY MODE"))
                self.adm_query_txtlbl.setText(_translate("MainWindow", "Query:"))
                self.adm_query_status_txtlbl.setText(_translate("MainWindow", "Type Query without (;). Press Confirm."))
                self.adm_query_confirm_btn.setText(_translate("MainWindow", "Confirm"))
                self.adm_query_confirm_btn.setShortcut(_translate("MainWindow","Return"))
                self.adm_query_download_btn.setText(_translate("MainWindow", "Download"))
                self.adm_query_download_btn.setShortcut(_translate("MainWindow", "Ctrl+S"))
                self.adm_filename_txtlbl.setText(_translate("MainWindow", "File Name:"))
                self.adm_filename_lineedit.setText(_translate("MainWindow", "Table"))
                self.adm_update_status_txtlbl.setText(_translate("MainWindow", "Type Update Query without (;). Press Confirm."))
                self.adm_update_confirm_btn.setText(_translate("MainWindow", "Confirm"))
                self.adm_updatehead_txtlbl.setText(_translate("MainWindow", "UPDATE MODE"))
                self.adm_update_txtlbl.setText(_translate("MainWindow", "Update\n""Query:"))
                self.adm_historysubhead_txtlbl.setText(_translate("MainWindow", "HISTORY"))
                item = self.adm_historydisp_table.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "Update Query"))
                self.adm_annto_combobox.setItemText(0, _translate("MainWindow", "All Employees"))
                self.adm_announcehead_txtlbl.setText(_translate("MainWindow", "ANNOUNCEMENTS"))
                self.adm_sentmode_radiobtn.setText(_translate("MainWindow", "View Sent Mode"))
                self.adm_sentmode_radiobtn.setShortcut(_translate("MainWindow", "W"))
                self.adm_annto_txtlbl.setText(_translate("MainWindow", "To:"))
                self.adm_sendmode_radiobtn.setText(_translate("MainWindow", "Send Mode"))
                self.adm_sendmode_radiobtn.setShortcut(_translate("MainWindow", "Q"))
                self.adm_ann_txtlbl.setText(_translate("MainWindow", "Announcement:"))
                self.adm_sendann_btn.setText(_translate("MainWindow", "Send"))
                self.adm_sendann_btn.setShortcut(_translate("MainWindow","Return"))
                self.adm_annstatus_txtlbl.setText(_translate("MainWindow", "Choose Recipient. Type Message. Press Send."))
                item = self.adm_sentann_table.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "Time"))
                item = self.adm_sentann_table.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "Sent to"))
                item = self.adm_sentann_table.horizontalHeaderItem(2)
                item.setText(_translate("MainWindow", "Message"))
                self.key_lbl.setText(_translate("MainWindow", "Passkey:"))
                self.user_lbl.setText(_translate("MainWindow", "Username:"))
                self.company_lbl.setText(_translate("MainWindow", "TechGenix Solutions Pvt. Ltd.   Contact: 011-XXXX-XXXX"))
                self.confirm_btn.setText(_translate("MainWindow", "\n""Confirm\n"""))
                self.confirm_btn.setShortcut(_translate("MainWindow", "Return"))
                self.status.setText(_translate("MainWindow", "Enter your details above..."))
                self.Quit_btn.setText(_translate("MainWindow", "Quit"))
                self.Quit_btn.setShortcut(_translate("MainWindow", "Esc"))
                self.inbox_btn.setText(_translate("MainWindow", "View Inbox"))
                self.inbox_btn.setShortcut(_translate("MainWindow", "3"))
                self.supervisor_btn.setText(_translate("MainWindow", "View Supervisors"))
                self.supervisor_btn.setShortcut(_translate("MainWindow", "5"))
                self.department_btn.setText(_translate("MainWindow", "View Department Details"))
                self.department_btn.setShortcut(_translate("MainWindow", "2"))
                self.personal_btn.setText(_translate("MainWindow", "Edit Personal Details"))
                self.personal_btn.setShortcut(_translate("MainWindow", "1"))
                self.send_btn.setText(_translate("MainWindow", "Send Messages"))
                self.send_btn.setShortcut(_translate("MainWindow", "4"))
                self.signout_btn.setText(_translate("MainWindow", "Sign Out"))
                self.signout_btn.setShortcut(_translate("MainWindow", "Esc"))
                self.company_lbl_empgui.setText(_translate("MainWindow", "TechGenix Solutions Pvt. Ltd.   Contact: 011-XXXX-XXXX"))
                self.home_btn.setText(_translate("MainWindow", "Home"))
                self.home_btn.setShortcut(_translate("MainWindow", "`"))
                self.lname_lbl_adm.setText(_translate("MainWindow", "ADMIN"))
                self.lmail_lbl_adm.setText(_translate("MainWindow", "admin.solutions@techgenix.com"))
                self.l_announcementbtn.setText(_translate("MainWindow", "Announcements"))
                self.l_announcementbtn.setShortcut(_translate("MainWindow", "3"))
                self.l_querybtn.setText(_translate("MainWindow", "Query Mode"))
                self.l_querybtn.setShortcut(_translate("MainWindow", "1"))
                self.l_updatebtn.setText(_translate("MainWindow", "Update Mode"))
                self.l_updatebtn.setShortcut(_translate("MainWindow", "2"))
                self.adm_home_btn.setText(_translate("MainWindow", "Home"))
                self.adm_home_btn.setShortcut(_translate("MainWindow","`"))
                self.adm_signout_btn.setText(_translate("MainWindow", "Sign Out"))
                self.adm_signout_btn.setShortcut(_translate("MainWindow", "Esc"))
                self.company_lbl_empgui_3.setText(_translate("MainWindow", "TechGenix Solutions Pvt. Ltd.   Contact: 011-XXXX-XXXX"))


#Code Blocks to Check User and Define Basic Vars

        def check(self):
                global user,key,eid
                con=ms.connect(host='localhost',user='root',password=sql_password,database=sql_db)
                cur=con.cursor()
                user=self.user_lineinp.text()
                key=self.key_lineinp.text()
                auth=0
                cur.execute('select * from UserKeys')
                userkeys=cur.fetchall()
                con.close()
                for i in userkeys:
                        if i[1]==user and i[2]==key:
                                eid=i[0]
                                auth=1
                                break
                if auth==0:
                        if user==admuser and key==admkey:
                                print('An ADMIN has Accessed the System.')
                                con=ms.connect(host='localhost',user='root',password=sql_password,database=sql_db)
                                cur=con.cursor()
                                cur.execute("Select Gender,Count(*) from Employee GROUP BY Gender")
                                db=cur.fetchall()
                                con.close()
                                for i in db:
                                        if i[0]=='M':
                                                cn_m=i[1]
                                        elif i[0]=='F':
                                                cn_f=i[1]
                                        else:
                                                cn_o=i[1]
                                self.countall_txtlbl.setText(str(cn_f+cn_m+cn_o))
                                self.countmale_txtlbl.setText(str(cn_m))
                                self.countfem_txtlbl.setText(str(cn_f))
                                self.countother_txtlbl.setText(str(cn_o))
                                self.r_window.setCurrentWidget(self.r_admhomepage)
                                self.l_window.setCurrentWidget(self.l_admintab)
                        else:
                                print('Access has been denied:\n','Username:',self.user_lineinp.text(),'\n','PassKey:',self.key_lineinp.text())
                                self.status.setStyleSheet("color:rgb(255, 0, 0)")
                                self.status.setText("Incorrect Username or Passkey")
                        
                else:
                        self.defineemp()
                        print('Employee',eid,fn,'has Accessed the System.')
                        self.r_window.setCurrentWidget(self.r_homepage) 
                        self.l_window.setCurrentWidget(self.l_employeetab)        

        def defineemp(self):
                global fn,mn,ln,dob,g,dep,job,un,pk,mail,cn,adr,ct,st,zp
                con=ms.connect(host='localhost',user='root',password=sql_password,database=sql_db)
                cur=con.cursor()
                cur.execute("select * from Employee")
                db=cur.fetchall()
                for i in db:
                        if i[0]==eid:
                                fn=i[1]
                                mn=i[2]
                                ln=i[3]
                                dob=i[4]
                                g=i[5]
                                dep=i[6]
                                job=i[7]
                cur.execute("select * from Userkeys")
                db=cur.fetchall()
                for i in db:
                        if i[0]==eid:
                                un=i[1]
                                pk=i[2]
                                mail=i[3]
                                cn=i[4]
                cur.execute("select * from Details")
                db=cur.fetchall()
                for i in db:
                        if i[0]==eid:
                                adr=i[1]
                                ct=i[2]
                                st=i[3]
                                zp=i[4]
                con.close()
                if mn=="NULL":
                        self.lname_lbl.setText(fn+' '+ln)
                else:
                        self.lname_lbl.setText(fn+' '+mn+' '+ln)
                self.firstname_txtlbl.setText(fn)
                if mn== "NULL":
                        self.cardname_txtlbl.setText(fn+' '+ln)
                else:
                        self.cardname_txtlbl.setText(fn+' '+mn+' '+ln)
                self.middlename_txtlbl.setText(mn)
                self.lastname_txtlbl.setText(ln)
                self.dob_txtlbl.setText(str(dob))
                self.gender_txtlbl.setText(g)
                self.cardjob_txt_lbl.setText(job)
                self.cardcontact_txtlbl.setText(str(cn))
                self.contact_txtlbl.setText(str(cn))
                self.lmail_lbl.setText(mail)
                self.cardmail_txtlbl.setText(mail)
                self.address_txtlbl.setText(adr)
                self.city_txtlbl.setText(ct)
                self.state_txtlbl.setText(st)
                self.zipcode_txtlbl.setText(zp)

#Code Blocks for Employee Access Panels

        def openemphome(self):
                self.r_window.setCurrentWidget(self.r_homepage)

        def openpersonal(self):
                self.changestatus_txtlbl.setText('Select and Change')
                self.editfirstname_lineedit.setText(fn)
                self.editmiddlename_lineedit.setText(mn)
                self.editlastname_lineedit.setText(ln)
                self.editgender_lineedit.setText(g)
                self.editdob_lineedit.setText(str(dob))
                self.editaddress_lineedit.setText(adr)
                self.editcity_lineedit.setText(ct)
                self.editstate_lineedit.setText(st)
                self.editzipcode_lineedit.setText(zp)
                self.editcontact_lineedit.setText(str(cn))
                self.changestatus_txtlbl.setStyleSheet("color: white;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:50px;\n"
                "border-color:black;\n"
                "background-color: rgb(6, 54, 122);")
                self.changestatus_txtlbl.setText("Select & Confirm")
                self.r_window.setCurrentWidget(self.r_perseditpage)

        def changepersonal(self):
                try:
                        con=ms.connect(host='localhost',user='root',password=sql_password,database=sql_db)
                        cur=con.cursor()
                        if self.firstname_chkbox.checkState():
                                ch = self.editfirstname_lineedit.text()
                                cur.execute(f"UPDATE Employee SET First_Name = '{ch}' where Employee_ID = {eid}")
                                con.commit()
                        if self.middlename_chkbox.checkState():
                                ch=self.editmiddlename_lineedit.text()
                                cur.execute(f"UPDATE Employee SET Middle_Name = '{ch}' where Employee_ID = {eid}")
                                con.commit()
                        if self.lastname_chkbox.checkState():
                                ch=self.editlastname_lineedit.text()
                                cur.execute(f"UPDATE Employee SET Last_Name = '{ch}' where Employee_ID = {eid}")
                                con.commit()
                        if self.gender_chkbox.checkState():
                                ch = self.editgender_lineedit.text()
                                cur.execute(f"UPDATE Employee SET Gender = '{ch}' where Employee_ID = {eid}")
                                con.commit()
                        if self.dob_chkbox.checkState():
                                ch = self.editdob_lineedit.text()
                                cur.execute(f"UPDATE Employee SET DOB = '{ch}' where Employee_ID = {eid}")
                                con.commit()
                        if self.address_chkbox.checkState():
                                ch = self.editaddress_lineedit.text()
                                cur.execute(f"UPDATE Details SET Address = '{ch}' where Employee_ID = {eid}")
                                con.commit()
                        if self.city_chkbox.checkState():
                                ch = self.editcity_lineedit.text()
                                cur.execute(f"UPDATE Details SET City = '{ch}' where Employee_ID = {eid}")
                                con.commit()
                        if self.state_chkbox.checkState():
                                ch = self.editstate_lineedit.text()
                                cur.execute(f"UPDATE Details SET State = '{ch}' where Employee_ID = {eid}")
                                con.commit()
                        if self.zipcode_chkbox.checkState():
                                ch = self.editzipcode_lineedit.text()
                                cur.execute(f"UPDATE Details SET Zipcode = '{ch}' where Employee_ID = {eid}")
                                con.commit()
                        if self.contact_chkbox.checkState():
                                ch = self.editcontact_lineedit.text()
                                cur.execute(f"UPDATE Userkeys SET Contact = {int(ch)} where Employee_ID = {eid}")
                                con.commit()
                        self.defineemp()
                        self.r_window.setCurrentWidget(self.r_homepage)
                        self.l_window.setCurrentWidget(self.l_employeetab)
                except:
                        self.changestatus_txtlbl.setStyleSheet("color: red;\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:50px;\n"
                "border-color:black;\n"
                "background-color: rgb(6, 54, 122);")
                        self.changestatus_txtlbl.setText("Error Occured.")
                        self.defineemp()

        def opendepartment(self):
                self.dephead_txtlbl.setText(dep)
                self.dep_table.setRowCount(10)
                con=ms.connect(host='localhost',user='root',password=sql_password,database=sql_db)
                cur=con.cursor()
                cur.execute(f"select * from Employee where Department ='{dep}'")
                db=cur.fetchall()
                self.dep_table.setRowCount(len(db))
                row=0
                for i in db:
                        if i[2]=="NULL":
                                self.dep_table.setItem(row,0,QtWidgets.QTableWidgetItem(i[1]+' '+i[3]))
                        else:
                                self.dep_table.setItem(row,0,QtWidgets.QTableWidgetItem(i[1]+' '+i[2]+' '+i[3]))
                        self.dep_table.setItem(row,1,QtWidgets.QTableWidgetItem(i[5]))
                        self.dep_table.setItem(row,2,QtWidgets.QTableWidgetItem(i[7]))
                        cur.execute("select * from userkeys")
                        db2=cur.fetchall()
                        for j in db2:
                                if j[0]==i[0]:
                                        self.dep_table.setItem(row,3,QtWidgets.QTableWidgetItem(j[3]))
                        row+=1
                con.close()
                self.r_window.setCurrentWidget(self.r_depviewpage)

        def openinbox(self):
                con=ms.connect(host='localhost',user='root',password=sql_password,database=sql_db)
                cur=con.cursor()
                cur.execute(f"select * from Messages where Reciever='{mail}' OR Reciever='All Employees'")
                db=cur.fetchall()
                con.close()
                self.inbox_table.setRowCount(len(db))
                row=0
                for i in db:
                        self.inbox_table.setItem(row,0,QtWidgets.QTableWidgetItem(str(i[2])))
                        self.inbox_table.setItem(row,1,QtWidgets.QTableWidgetItem(i[0]))
                        self.inbox_table.setItem(row,2,QtWidgets.QTableWidgetItem(i[3]))
                        row+=1
                self.r_window.setCurrentWidget(self.r_inboxpage)

        def opensend(self):
                con=ms.connect(host='localhost',user='root',password=sql_password,database=sql_db)
                cur=con.cursor()
                cur.execute("select Mail from UserKeys")
                db=cur.fetchall()
                for i in db:
                        self.to_combobox.addItem(i[0])
                cur.execute(f"select * from messages where sender='{mail}'")
                db=cur.fetchall()
                con.close()
                self.sent_table.setRowCount(len(db))
                row=0
                for i in db:
                        self.sent_table.setItem(row,0,QtWidgets.QTableWidgetItem(str(i[2])))
                        self.sent_table.setItem(row,1,QtWidgets.QTableWidgetItem(i[1]))
                        self.sent_table.setItem(row,2,QtWidgets.QTableWidgetItem(i[3]))
                        row+=1                               
                self.message_txtedit.setText("")
                self.msgstatus_lbl.setStyleSheet("color:rgb(0, 0, 0);\n""background-color: white")
                self.msgstatus_lbl.setText("Choose Recipient. Type Message. Press Send.") 
                self.r_window.setCurrentWidget(self.r_sendpage)

        def opensendmode(self):
                
                self.msgstatus_lbl.setStyleSheet("color:rgb(0, 0, 0);\n""background-color: white")
                self.msgstatus_lbl.setText("Choose Recipient. Type Message. Press Send.")
                self.sendmodes_stckwidget.setCurrentWidget(self.sendmode)
        
        def opensentmode(self):
                con=ms.connect(host='localhost',user='root',password=sql_password,database=sql_db)
                cur=con.cursor()                
                cur.execute(f"select * from messages where sender='{mail}'")
                db=cur.fetchall()
                con.close()
                self.sent_table.setRowCount(len(db))
                row=0
                for i in db:
                        self.sent_table.setItem(row,0,QtWidgets.QTableWidgetItem(str(i[2])))
                        self.sent_table.setItem(row,1,QtWidgets.QTableWidgetItem(i[1]))
                        self.sent_table.setItem(row,2,QtWidgets.QTableWidgetItem(i[3]))
                        row+=1     
                self.sendmodes_stckwidget.setCurrentWidget(self.sentmode)

        def sendmsg(self):
                con=ms.connect(host='localhost',user='root',password=sql_password,database=sql_db)
                cur=con.cursor()
                rcvr=self.to_combobox.currentText()
                time=str(dttm.datetime.now())[:-7:]
                msg=self.message_txtedit.toPlainText().replace("'","''")
                if rcvr=="Select Recipient":
                        self.msgstatus_lbl.setStyleSheet("color:rgb(255, 0, 0);\n""background-color: white")
                        self.msgstatus_lbl.setText("Please select a Valid Recipient.")
                else:
                        cur.execute(f"insert into Messages (Sender,Reciever,Time,Message) Values('{mail}','{rcvr}','{time}','{msg}')")
                        con.commit()
                        con.close()
                        self.message_txtedit.setText("")
                        self.msgstatus_lbl.setStyleSheet("color:rgb(0, 255, 0);\n""background-color: white")
                        self.msgstatus_lbl.setText("Message sent successfully.")
        
        def opensupervisor(self):
                con=ms.connect(host='localhost',user='root',password=sql_password,database=sql_db)
                cur=con.cursor()
                cur.execute("select * from Employee where Job like '%Supervisor'")
                db=cur.fetchall()
                self.supervisor_table.setRowCount(len(db))
                row=0
                for i in db:
                        if i[7] in Supervisors:
                                if i[2]=="NULL":
                                        self.supervisor_table.setItem(row,0,QtWidgets.QTableWidgetItem(i[1]+' '+i[3]))
                                else:
                                        self.supervisor_table.setItem(row,0,QtWidgets.QTableWidgetItem(i[1]+' '+i[2]+' '+i[3]))
                                self.supervisor_table.setItem(row,1,QtWidgets.QTableWidgetItem(i[6]))
                                cur.execute("select * from userkeys")
                                db2=cur.fetchall()
                                for j in db2:
                                        if j[0]==i[0]:
                                                self.supervisor_table.setItem(row,2,QtWidgets.QTableWidgetItem(j[3]))
                                row+=1
                con.close()
                self.r_window.setCurrentWidget(self.r_supervisorpage)

#Code Blocks For ADMIN Access Panels

        def openadmhome(self):
                self.backup_btn.setStyleSheet("color: rgb(0, 0, 127);\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.backup_btn.setText("Backup.")
                self.r_window.setCurrentWidget(self.r_admhomepage)

        def backuptables(self):
                con=ms.connect(host='localhost',user='root',password=sql_password,database=sql_db)
                cur=con.cursor()
                cur.execute('select * from Employee')
                db=cur.fetchall()
                with open (rf'{download_path}\Employee.csv', mode='w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([desc[0] for desc in cur.description])  # Write header row
                        writer.writerows(db)  # Write data rows
                cur.execute('select * from Userkeys')
                db=cur.fetchall()
                with open (rf'{download_path}\Userkeys.csv', mode='w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([desc[0] for desc in cur.description])  # Write header row
                        writer.writerows(db)  # Write data rows
                cur.execute('select * from Details')
                db=cur.fetchall()
                with open (rf'{download_path}\Details.csv', mode='w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([desc[0] for desc in cur.description])  # Write header row
                        writer.writerows(db)  # Write data rows
                cur.execute('select * from Messages')
                db=cur.fetchall()
                with open (rf'{download_path}\Messages.csv', mode='w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([desc[0] for desc in cur.description])  # Write header row
                        writer.writerows(db)  # Write data rows
                cur.execute('select * from Updates')
                db=cur.fetchall()
                with open (rf'{download_path}\Updates.csv', mode='w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([desc[0] for desc in cur.description])  # Write header row
                        writer.writerows(db)  # Write data rows
                con.close()
                self.backup_btn.setStyleSheet("color: rgb(0, 255, 0);\n"
                "border-style:outset;\n"
                "border-width:2px;\n"
                "border-radius:10px;\n"
                "border-color:black;\n"
                "background-color: rgb(255, 255, 255);")
                self.backup_btn.setText("Backup Completed")
                
        def openquery(self):
                self.r_window.setCurrentWidget(self.r_admquerypage)
        
        def execquery(self):
                try:
                        self.adm_querydisp_table.clear()
                        con=ms.connect(host='localhost',user='root',password=sql_password,database=sql_db)
                        cur=con.cursor()
                        query=self.adm_query_txtedit.toPlainText().replace("'","''")
                        cur.execute(query)
                        db=cur.fetchall()
                        nclmns=cur.description
                        clmns=[i[0] for i in cur.description]
                        self.adm_querydisp_table.setColumnCount(len(clmns))
                        self.adm_querydisp_table.setHorizontalHeaderLabels(clmns)
                        self.adm_querydisp_table.setRowCount(len(db))
                        row=0
                        clmn=0
                        for i in db:
                                while clmn!=len(clmns):
                                        if isinstance(i[clmn],dttm.date) or type(i[clmn])==type(1):
                                                self.adm_querydisp_table.setItem(row,clmn,QtWidgets.QTableWidgetItem(str(i[clmn])))
                                        else:
                                                self.adm_querydisp_table.setItem(row,clmn,QtWidgets.QTableWidgetItem(i[clmn]))
                                        clmn+=1
                                row+=1
                                clmn=0
                        con.close()
                        self.adm_query_status_txtlbl.setStyleSheet('color: rgb(0,0,0);\n''background-color: white')
                        self.adm_query_status_txtlbl.setText("Type Query without (;)")
                        
                except:
                        self.adm_query_status_txtlbl.setStyleSheet('color: rgb(255,0,0);\n''background-color: white')
                        self.adm_query_status_txtlbl.setText('Error in Query.')         

        def downloadtable(self):
                try:
                        con=ms.connect(host='localhost',user='root',password=sql_password,database=sql_db)
                        cur=con.cursor()
                        query=self.adm_query_txtedit.toPlainText()
                        cur.execute(query)
                        db=cur.fetchall()
                        csv_file = self.adm_filename_lineedit.text()+'.csv'
                        with open (rf'{download_path}\{csv_file}', mode='w', newline='') as file:
                                writer = csv.writer(file)
                                writer.writerow([desc[0] for desc in cur.description])  # Write header row
                                writer.writerows(db)  # Write data rows
                        con.close()
                        self.adm_query_status_txtlbl.setStyleSheet('color: rgb(0,255,0);\n''background-color: white')
                        self.adm_query_status_txtlbl.setText('File Downloaded.')
                except:
                        self.adm_query_status_txtlbl.setStyleSheet('color: rgb(255,0,0);\n''background-color: white')
                        self.adm_query_status_txtlbl.setText('Error in Query.')

        def openupdate(self):
                try:
                        con=ms.connect(host='localhost',user='root',password=sql_password,database=sql_db)
                        cur=con.cursor()
                        cur.execute("select * from Updates")
                        db=cur.fetchall()
                        self.adm_historydisp_table.setRowCount(len(db))
                        row=0
                        for i in db:
                                self.adm_historydisp_table.setItem(row,0,QtWidgets.QTableWidgetItem(i[0]))
                                row+=1
                except:
                        pass
                self.adm_update_status_txtlbl.setText("Type Update Query without (;). Press Confirm.")
                self.r_window.setCurrentWidget(self.r_updatepage)
        
        def makeupdate(self):
                try:
                        con=ms.connect(host='localhost',user='root',password=sql_password,database=sql_db)
                        cur=con.cursor()
                        query=self.adm_update_txtedit.toPlainText()
                        cur.execute(query)
                        con.commit()
                        cur.execute(f"insert into Updates values('{query.replace("'","''")}')")
                        con.commit()
                        con.close()
                        self.openupdate()
                        self.adm_update_txtedit.setText("")
                        self.adm_update_status_txtlbl.setStyleSheet("background-color: rgb(255, 255, 255);\n""color: green")
                        self.adm_update_status_txtlbl.setText("Update Successful.")
                except:
                        self.adm_update_status_txtlbl.setStyleSheet("background-color: rgb(255, 255, 255);\n""color: red")
                        self.adm_update_status_txtlbl.setText("Error Occured.")

        def openannouncement(self):
                con=ms.connect(host='localhost',user='root',password=sql_password,database=sql_db)
                cur=con.cursor()
                cur.execute("select Mail from UserKeys")
                db=cur.fetchall()
                for i in db:
                        self.adm_annto_combobox.addItem(i[0])
                self.adm_annstatus_txtlbl.setStyleSheet("color:rgb(0,0,0);\n""background-color: white")
                self.adm_annstatus_txtlbl.setText('Choose Recipient. Type Message. Press Send.')
                self.r_window.setCurrentWidget(self.r_admannouncepage)
        
        def openadmsendmode(self):
                self.adm_annstatus_txtlbl.setStyleSheet("color:rgb(0,0,0);\n""background-color: white")
                self.adm_annstatus_txtlbl.setText('Choose Recipient. Type Message. Press Send.')
                self.adm_annsentsend_stckwdgt.setCurrentWidget(self.adm_sendann_page)

        def openadmsentmode(self):
                con=ms.connect(host='localhost',user='root',password=sql_password,database=sql_db)
                cur=con.cursor()
                cur.execute(f"select * from Messages where Sender='admin.solutions@{company_name.lower()}.com'")
                db=cur.fetchall()
                con.close()
                self.adm_sentann_table.setRowCount(len(db))
                row=0
                for i in db:
                        self.adm_sentann_table.setItem(row,0,QtWidgets.QTableWidgetItem(str(i[2])))
                        self.adm_sentann_table.setItem(row,1,QtWidgets.QTableWidgetItem(i[1]))
                        self.adm_sentann_table.setItem(row,2,QtWidgets.QTableWidgetItem(i[3]))
                        row+=1
                
                self.adm_annsentsend_stckwdgt.setCurrentWidget(self.adm_sentann_page)
                
        def sendann(self):
                con=ms.connect(host='localhost',user='root',password=sql_password,database=sql_db)
                cur=con.cursor()
                time=str(dttm.datetime.now())[:-7:]
                ann=self.adm_ann_txtedit.toPlainText().replace("'","''")
                rcvr=self.adm_annto_combobox.currentText()
                cur.execute(f"insert into Messages (Sender,Reciever,Time,Message) Values('admin.solutions@{company_name.lower()}.com','{rcvr}','{time}','{ann}')")    
                con.commit()
                con.close()
                self.adm_ann_txtedit.setText("")
                self.adm_annstatus_txtlbl.setStyleSheet("color:rgb(0,255,0);\n""background-color: white")
                self.adm_annstatus_txtlbl.setText('Announcement Made Successfully.')
                
#Code Blocks to Exit GUIs

        def signout(self):
                print("Employee",eid,fn,'has Signed Out of the System.')
                self.key_lineinp.setText("")
                self.user_lineinp.setText("")
                self.status.setStyleSheet("color:rgb(255, 255, 255)")
                self.status.setText("Enter your details above...")
                self.r_window.setCurrentWidget(self.r_aestheticpage)
                self.l_window.setCurrentWidget(self.l_loginpage)

        def admsignout(self):
                print("ADMIN has Signed Out of the System.")
                self.key_lineinp.setText("")
                self.user_lineinp.setText("")
                self.status.setStyleSheet("color:rgb(255, 255, 255)")
                self.status.setText("Enter your details above...")
                self.r_window.setCurrentWidget(self.r_aestheticpage)
                self.l_window.setCurrentWidget(self.l_loginpage)
        
        def quitsystem(self):
                print("System has been Shut Down.")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    MainWindow.setGeometry(
        QtWidgets.QStyle.alignedRect(
            QtCore.Qt.LeftToRight,
            QtCore.Qt.AlignCenter,
            MainWindow.size(),
            QtWidgets.QApplication.primaryScreen().availableGeometry(),
        )
    )
    sys.exit(app.exec_())

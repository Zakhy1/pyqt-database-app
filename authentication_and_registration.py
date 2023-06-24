import sqlite3

from PyQt5 import QtWidgets

import auth
import register
import terms_of_use


class AuthWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.auth = auth.Ui_Form()
        self.auth.setupUi(self)
        self.setWindowModality(2)
        self.reg = Register()

        # Основные обработчики
        self.validate_flag = False
        self.auth.pushButton.clicked.connect(self.checkPass)
        self.auth.pushButton_2.clicked.connect(self.registration)

    def checkPass(self):
        login = self.auth.lineEdit.text()
        password = self.auth.lineEdit_2.text()
        try:
            con = sqlite3.connect('database.db')
            cursor = con.cursor()

            cursor.execute(f"""
                SELECT login, password FROM users
                WHERE login = '{login}' and password = '{password}'
                """)

            if cursor.fetchone():
                self.validate_flag = True
                self.close()
            else:
                self.auth.label_3.setText("Такого пользователя не существует")
            con.close()
        except sqlite3.Error as error:
            print(error)

    def registration(self):
        self.reg.show()

    def closeEvent(self, value):
        if not self.validate_flag:
            raise SystemExit


class Register(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.register = register.Ui_Form()
        self.register.setupUi(self)
        self.setWindowModality(2)

        self.validate_flag = False
        self.register.pushButton.clicked.connect(self.show_terms_of_use)
        self.register.pushButton_2.clicked.connect(self.registerValidation)

    def show_terms_of_use(self):
        self.terms = Terms()
        self.terms.show()

    def registerValidation(self):
        login = self.register.lineEdit.text()
        name = self.register.lineEdit_4.text()
        password = self.register.lineEdit_2.text()
        rep_password = self.register.lineEdit_3.text()
        checkbox = self.register.checkBox
        try:
            con = sqlite3.connect('database.db')
            cursor = con.cursor()
            cursor.execute(f"""SELECT * FROM USERS WHERE login = '{login}'""")

            if password != rep_password:
                self.register.label_4.setText('Пароли не совпадают')
            elif len(login) < 3:
                self.register.label_4.setText('Ваш логин слишком короткий')
            elif len(password) < 5:
                self.register.label_4.setText('Пароль слишком короткий')
            elif len(name) < 2:
                self.register.label_4.setText('Ваше имя слишком короткое')
            elif not checkbox.isChecked():
                self.register.label_5.setText('Вы должны согласиться для регистрации')
            if cursor.fetchone():
                self.register.label_4.setText('Такой пользователь существует')
            elif password == rep_password and len(login) > 3 and len(name) > 2 and len(password) > 5 and \
                    checkbox.isChecked() and cursor.fetchone() is None:
                cursor.execute(f"""
                                INSERT INTO USERS (name, login, password)
                                VALUES ('{name}', '{login}', '{password}') 
                                """)
                self.register.label_4.setText('Вы успешно зарегистрированы')
                con.commit()
                cursor.close()
                con.close()
        except sqlite3.Error as error:
            print(error)


class Terms(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.terms = terms_of_use.Ui_Form()
        self.terms.setupUi(self)
        self.setWindowModality(2)

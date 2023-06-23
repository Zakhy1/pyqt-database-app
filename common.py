from PyQt5 import QtWidgets

import add_user_form
import simple_add
import delete_form
import add_product
import add_sale_form

from DataBaseAdapter import DataBaseAdapter


class AddSimple(QtWidgets.QWidget):
    def __init__(self, table, parent=None):
        super().__init__(parent)
        self.table = table
        self.add_category = simple_add.Ui_Form()
        self.add_category.setupUi(self)
        self.setWindowModality(2)

        self.add_category.pushButton.clicked.connect(self.validate)

    def validate(self):
        name = self.add_category.lineEdit.text()
        db = DataBaseAdapter("database.db")
        unique_flag = db.check_unique(self.table, name)

        if len(name) < 3:
            self.add_category.label_4.setText("Название слишком короткое")
        if not unique_flag:
            self.add_category.label_4.setText("Такая запись уже существует")
        elif len(name) > 3 and unique_flag:
            db.insert(self.table, [["name", name]])
            self.add_category.label_4.setText("запись добавлена")


class AddSaleForm(QtWidgets.QWidget):
    def __init__(self, table: str, parent=None):
        super().__init__(parent)
        self.table = table
        self.add_sale_form = add_sale_form.Ui_Form()
        self.add_sale_form.setupUi(self)
        self.setWindowModality(2)

        self.get_combo_boxes()
        self.add_sale_form.pushButton.clicked.connect(self.submit)

    def get_combo_boxes(self):
        db = DataBaseAdapter("database.db")
        users = db.get_names("users")
        products = db.get_names("products")

        user_combo = self.add_sale_form.comboBox
        product_combo = self.add_sale_form.comboBox_2

        user_combo.addItems(users)
        product_combo.addItems(products)

        user_combo.setCurrentIndex(0)
        product_combo.setCurrentIndex(0)

    def submit(self):
        db = DataBaseAdapter("database.db")
        user = self.add_sale_form.comboBox.currentIndex()
        product = self.add_sale_form.comboBox.currentIndex()

        db.insert("sales", [["user", user + 1], ["product", product + 1]])
        self.add_sale_form.label_4.setText("Поздравляю, вы продали!")


class AddProductForm(QtWidgets.QWidget):
    def __init__(self, table: str, parent=None):
        super().__init__(parent)
        self.table = table
        self.add_product_form = add_product.Ui_Form()
        self.add_product_form.setupUi(self)
        self.setWindowModality(2)

        self.get_combo_boxes()
        self.add_product_form.pushButton.clicked.connect(self.validate)

    def get_combo_boxes(self):
        db = DataBaseAdapter("database.db")
        categories = db.get_names("category")
        providers = db.get_names("providers")

        category_combo = self.add_product_form.comboBox
        provider_combo = self.add_product_form.comboBox_2

        category_combo.addItems(categories)
        provider_combo.addItems(providers)

        category_combo.setCurrentIndex(0)
        provider_combo.setCurrentIndex(0)

    def validate(self):
        name = self.add_product_form.lineEdit.text()
        price = int(self.add_product_form.spinBox_2.text())
        category_id = self.add_product_form.comboBox.currentIndex()
        provider_id = self.add_product_form.comboBox_2.currentIndex()
        count = int(self.add_product_form.spinBox.text())
        db = DataBaseAdapter("database.db")
        name_unique_flag = db.check_unique("products", name, "name")

        if len(name) < 3:
            self.add_product_form.label_4.setText("Слишком короткое название товара")
        if price < 1:
            self.add_product_form.label_4.setText("Товары у нас не бесплатные")
        if not name_unique_flag:
            self.add_product_form.label_4.setText("Данный товар уже существует")

        elif len(name) > 3 and price > 1 and name_unique_flag:
            db.insert(self.table, [["name", name], ["price", str(price)],
                                   ["category", str(category_id+1)], ["provider", str(provider_id+1)],
                                   ["count", str(count)]])
            self.add_product_form.label_4.setText("Товар добавлен")


class AddUserForm(QtWidgets.QWidget):
    def __init__(self, table: str, parent=None):
        super().__init__(parent)
        self.table = table
        self.add_user = add_user_form.Ui_Form()
        self.add_user.setupUi(self)
        self.setWindowModality(2)

        self.add_user.pushButton.clicked.connect(self.validate)

    def validate(self):
        db = DataBaseAdapter("database.db")

        name = self.add_user.lineEdit.text()
        login = self.add_user.lineEdit_2.text()
        password = self.add_user.lineEdit_3.text()

        user_unique_flag = db.check_unique("users", login, "login")

        if len(name) < 2:
            self.add_user.label_4.setText("Имя должно быть длиннее 2 символов")
        if len(login) < 2:
            self.add_user.label_4.setText("Логин должен быть длиннее 2 символов")
        if len(password) <= 5:
            self.add_user.label_4.setText("Пароль должен быть нормальный!")
        if not user_unique_flag:
            self.add_user.label_4.setText("Такой пользователь существует")

        elif len(name) > 2 and len(login) > 2 and len(password) > 5 and user_unique_flag:
            db.insert(self.table, [["name", name], ["login", login], ["password", password]])
            self.add_user.label_4.setText("Пользователь добавлен")


class DeleteForm(QtWidgets.QWidget):
    def __init__(self, table: str, parent=None):
        super().__init__(parent)
        self.table = table
        self.delete_form = delete_form.Ui_Form()
        self.delete_form.setupUi(self)
        self.setWindowModality(2)

        self.delete_form.pushButton.clicked.connect(self.validate)

    def validate(self):
        db = DataBaseAdapter("database.db")
        pk = int(self.delete_form.lineEdit.text())

        if pk:
            exist_flag = db.check_exist(self.table, pk)
            if not exist_flag:
                self.delete_form.label_2.setText("Записи с таким ID не существует")
            else:
                db.delete(self.table, pk)
                self.delete_form.label_2.setText("Удаление прошло успешно")
        else:
            self.delete_form.label_2.setText("Поле не должно быть пустым")

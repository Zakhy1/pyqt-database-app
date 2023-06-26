import sys
import sqlite3

from authentication_and_registration import AuthWindow
from common import AddSimple, DeleteForm, AddProductForm, AddUserForm, AddSaleForm
from main_window import *
from table_model import TableModel
from DataBaseAdapter import DataBaseAdapter


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.interface = Ui_MainWindow()
        self.interface.setupUi(self)

        # модальные окна

        self.interface.toolButton.clicked.connect(self.refresh_tables)
        # Кнопки в категориях
        self.interface.pushButton_6.clicked.connect(self.add_category)
        self.interface.pushButton_5.clicked.connect(self.delete_category)
        # self.interface.pushButton_4.clicked.connect(self.edit_category)
        self.interface.pushButton_28.clicked.connect(self.extract_categories)
        # Кнопки в поставщиках
        self.interface.pushButton_32.clicked.connect(self.add_provider)
        self.interface.pushButton_27.clicked.connect(self.delete_provider)
        # self.interface.pushButton_27.clicked.connect(self.edit_provider)
        self.interface.pushButton_36.clicked.connect(self.extract_providers)
        # Кнопки в товарах
        self.interface.pushButton_39.clicked.connect(self.add_product)
        self.interface.pushButton_38.clicked.connect(self.delete_product)
        # self.interface.pushButton_32.clicked.connect(self.edit_product)
        self.interface.pushButton_37.clicked.connect(self.extract_products)
        # Кнопки в продажах
        self.interface.pushButton_14.clicked.connect(self.add_sale)
        self.interface.pushButton_9.clicked.connect(self.delete_sale)
        # self.interface.pushButton_9.clicked.connect(self.edit_sale)
        self.interface.pushButton_41.clicked.connect(self.extract_sales)
        # Кнопки в сотрудниках
        self.interface.pushButton_12.clicked.connect(self.add_user)
        self.interface.pushButton_13.clicked.connect(self.delete_user)
        # self.interface.pushButton_12.clicked.connect(self.edit_user)
        self.interface.pushButton_40.clicked.connect(self.extract_users)

        # Таблицы
        self.product_table = self.interface.tableView
        self.category_table = self.interface.tableView_2
        self.sales_table = self.interface.tableView_3
        self.user_table = self.interface.tableView_4
        self.provider_table = self.interface.tableView_9

        self.refresh_tables()

    # Методы CRUD
    def refresh_tables(self):
        try:
            con = sqlite3.connect('database.db')
            cursor = con.cursor()

            # Таблица пользователей
            cursor.execute("SELECT id, login, password FROM USERS")
            data = cursor.fetchall()

            self.user_model = TableModel(data)
            user_table_labels = ["ID", 'Имя', 'Логин']
            self.user_model.setHorizontalHeaderLabels(user_table_labels)
            self.user_table.setModel(self.user_model)
            self.user_table.resizeColumnsToContents()

            # Таблица продаж
            cursor.execute("SELECT sales.id, users.name, products.name, time "
                           "FROM sales "
                           "JOIN users ON sales.user = users.id JOIN products ON sales.product = products.id")
            data = cursor.fetchall()

            self.sales_model = TableModel(data)
            sales_model_labels = ["ID", "Пользователь",
                                  "Товар", "Время продажи"]
            self.sales_model.setHorizontalHeaderLabels(sales_model_labels)
            self.sales_table.setModel(self.sales_model)
            self.sales_table.resizeColumnsToContents()

            # Таблица товаров
            cursor.execute("SELECT products.id, products.name, category.name, price, providers.name, count "
                           "FROM products "
                           "JOIN category ON category.id = products.category "
                           "JOIN providers ON providers.id = products.provider")
            data = cursor.fetchall()

            self.product_model = TableModel(data)
            product_model_labels = ["ID", "Наименование", "Категория",
                                    "Цена", "Производитель", "Количество"]
            self.product_model.setHorizontalHeaderLabels(product_model_labels)
            self.product_table.setModel(self.product_model)
            self.product_table.resizeColumnsToContents()

            # Таблица поставщиков
            cursor.execute("SELECT id, name FROM providers")
            data = cursor.fetchall()

            self.provider_model = TableModel(data)
            provider_model_labels = ["ID", "Наименование поставщика"]
            self.provider_model.setHorizontalHeaderLabels(provider_model_labels)
            self.provider_table.setModel(self.provider_model)
            self.provider_table.resizeColumnsToContents()

            # Таблица категорий
            cursor.execute("SELECT id, name FROM category")
            data = cursor.fetchall()

            self.category_model = TableModel(data)
            category_model_labels = ["ID", "Наименование категории"]
            self.category_model.setHorizontalHeaderLabels(category_model_labels)
            self.category_table.setModel(self.category_model)
            self.category_table.resizeColumnsToContents()
            con.close()
        except sqlite3.Error as error:
            print(error)

    # Методы CRUD
    # Категории
    def add_category(self):
        self.add_category_modal = AddSimple("category")
        self.add_category_modal.show()

    def delete_category(self):
        self.delete_category_modal = DeleteForm("category")
        self.delete_category_modal.show()

    # def edit_category(self):
    #     pass

    @staticmethod
    def extract_categories():
        db = DataBaseAdapter("database.db")
        db.extract("category")

    # Поставщики
    def add_provider(self):
        self.add_provider_modal = AddSimple("providers")
        self.add_provider_modal.show()

    def delete_provider(self):
        self.delete_provider_modal = DeleteForm("providers")
        self.delete_provider_modal.show()

    # def edit_provider(self):
    #     pass

    @staticmethod
    def extract_providers():
        db = DataBaseAdapter("database.db")
        db.extract("providers")

    # Товары
    def add_product(self):
        self.add_product = AddProductForm("products")
        self.add_product.show()

    def delete_product(self):
        self.delete_product_modal = DeleteForm("products")
        self.delete_product_modal.show()

    # def edit_product(self):
    #     pass

    @staticmethod
    def extract_products():
        db = DataBaseAdapter("database.db")
        db.extract("products")

    # Продажи
    def add_sale(self):
        self.add_sale_modal = AddSaleForm("sales")
        self.add_sale_modal.show()

    def delete_sale(self):
        self.delete_sale_modal = DeleteForm("sales")
        self.delete_sale_modal.show()

    # def edit_sale(self):
    #     pass

    @staticmethod
    def extract_sales():
        db = DataBaseAdapter("database.db")
        db.extract("sales")

    # Пользователи
    def add_user(self):
        self.add_user_modal = AddUserForm("users")
        self.add_user_modal.show()

    def delete_user(self):
        self.delete_user_modal = DeleteForm("users")
        self.delete_user_modal.show()

    # def edit_user(self):
    #     pass

    @staticmethod
    def extract_users():
        db = DataBaseAdapter("database.db")
        db.extract("users")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    auth = AuthWindow()
    myapp = MainWindow()
    myapp.show()
    auth.show()
    sys.exit(app.exec_())
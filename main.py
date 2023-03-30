import sys
from des_Login_Form import *
from style_login_form import *
from psycopg2 import connect
import hashlib
import string
#Добавить кнопку посмотреть у поля ввода пароля(Вместо точек показывает пароль)

class LoginWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = UiLoginForm()
        self.ui.setupUi(self)
        self.ui.sign_up_push_button.setStyleSheet(sign_up_button_style)
        self.ui.sign_in_push_button.clicked.connect(self.sign_in)
        self.ui.sign_up_push_button.clicked.connect(self.sign_up)
        self.ui.error_label.setStyleSheet(error_label_register_style)
        self.connection = connect(
            user="postgres",
            password="445467qwe",
            host="127.0.0.1",
            port="5432",
            database="MusicApp"
        )
        self.cursor = self.connection.cursor()

    def sign_in(self):
        line_edit_login = self.ui.login_line_edit.text()
        line_edit_password = self.ui.password_line_edit.text()
        if not line_edit_login.split():
            self.error_handler('Неверный логин', self.ui.login_line_edit)
        else:
            self.ui.login_line_edit.setStyleSheet(main_style_line_edit)
        if not line_edit_password.split():
            self.error_handler('Неверный пароль', self.ui.password_line_edit)
            return
        else:
            self.ui.password_line_edit.setStyleSheet(main_style_line_edit)

        self.cursor.execute('SELECT login, password FROM users WHERE login = %s',
                            (self.ui.login_line_edit.text(), ))
        select_res = self.cursor.fetchall()
        if select_res:
            self.ui.login_line_edit.setStyleSheet(main_style_line_edit)
            user_password = select_res[0][1]
            if user_password == line_edit_password:
                print('Вы вошли')
            else:
                self.error_handler('Неверный пароль', self.ui.password_line_edit)
        else:
            self.error_handler('Неверный логин', self.ui.login_line_edit)

    def error_handler(self, error_text: str, obj: QtWidgets.QLineEdit):
        obj.setStyleSheet(error_line_edit_register_style) #Переданному line_edit присваиваются стили ошибки(Красная рамка)
        self.ui.error_label.setText(error_text)

    def sign_up(self):
        #Создается и показывается новое окно
        self.sign_up_window = SignUpWindow(connection=self.connection,
                                           login_line_edit=self.ui.login_line_edit.text().strip())
        self.sign_up_window.show()
        self.hide()


class SignUpWindow(QtWidgets.QWidget):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent)
        self.ui = UiSignUpForm()
        self.ui.setupUi(self)
        self.ui.sign_up_register_push_button.clicked.connect(self.sign_up_reg)
        self.ui.login_register_line_edit.setText(kwargs['login_line_edit'])
        self.connection = kwargs['connection']
        self.cursor = self.connection.cursor()
        self.ui.error_label.setStyleSheet(error_label_register_style)

    def sign_up_reg(self):
        user_login = self.ui.login_register_line_edit.text().strip()
        user_email = self.ui.email_register_line_edit.text().strip()
        user_phone = self.ui.phone_line_edit.text().strip()
        user_password = self.ui.password_line_edit.text().strip()

        if self.check_data('Данный логин уже занят', 'login',
                           self.ui.login_register_line_edit):
            return
        if self.check_data('Данный Email привязан к другому аккаунту',
                           'email', self.ui.email_register_line_edit):
            return
        if self.check_data('Данный номер телефона привязан к другому аккаунту',
                           'phone_number', self.ui.phone_line_edit):
            return

        #Проверка корректности введенных пользователем данных
        #Проверка логина
        if len(user_login) < 4:
            self.error_handler('Логин должен содержать больше 3 символов',
                               self.ui.login_register_line_edit)
            return
        elif len(list(filter(lambda i: i in string.ascii_letters, user_login))) < 1:
            self.error_handler('Логин должен содержать хотя бы 1 букву',
                               self.ui.login_register_line_edit)
            return
        else:
            self.ui.login_register_line_edit.setStyleSheet(main_style_line_edit)
        #Проверка Email
        if '@' not in user_email:
            self.error_handler('Введите корректный email',
                               self.ui.email_register_line_edit)
            return
        elif user_email.split('@')[1] not in ['mail.ru', 'gmail.com']:
            self.error_handler('Введите корректный email',
                               self.ui.email_register_line_edit)
            return
        else:
            self.ui.email_register_line_edit.setStyleSheet(main_style_line_edit)
        #Проверка пароля
        if len(user_password) < 6:
            self.error_handler('Пароль должен содержать 6 и более символов',
                               self.ui.password_line_edit)
            return
        else:
            self.ui.password_line_edit.setStyleSheet(main_style_line_edit)
        #Проверка телефона
        if not user_phone:
            user_phone = None
        elif len(user_phone) != 11:
            self.error_handler('Введите корректный номер телефона',
                               self.ui.phone_line_edit)
            return
        else:
            self.ui.phone_line_edit.setStyleSheet(main_style_line_edit)

        self.cursor.execute('INSERT INTO users (email, password, login) VALUES(%s, %s, %s)',
                            (user_email, hashlib.md5(user_password.encode()).hexdigest(), user_login))
        self.connection.commit()

    def error_handler(self, error_text: str, obj: QtWidgets.QLineEdit):
        obj.setStyleSheet(error_line_edit_register_style) #Переданному line_edit присваиваются стили ошибки(Красная рамка)
        self.ui.error_label.setText(error_text)

    def check_data(self, error_desc: str, column_name: str, obj_line_edit: QtWidgets.QLineEdit) -> bool:
        self.cursor.execute(f'SELECT {column_name} FROM users WHERE {column_name} = %s', (obj_line_edit.text().strip(),))
        checker = self.cursor.fetchone()
        if checker: #Если запрос к базе вернет кортеж, то поле в базе существует
            self.error_handler(error_desc, obj_line_edit)
            return True
        else:
            obj_line_edit.setStyleSheet(main_style_line_edit)
            return False


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    app.setStyleSheet(main_style)

    mywin = LoginWindow()
    mywin.show()
    app.exec()

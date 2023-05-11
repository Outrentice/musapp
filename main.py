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

        self.cursor.execute('SELECT login, password, id FROM users WHERE login = %s',
                            (self.ui.login_line_edit.text(), ))
        select_res = self.cursor.fetchall()
        if select_res:
            self.ui.login_line_edit.setStyleSheet(main_style_line_edit)
            user_password = select_res[0][1]
            if user_password == hashlib.md5(line_edit_password.encode()).hexdigest():
                self.show_main_window(select_res[0][2])
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

    def show_main_window(self, user_id):
        self.user_profile_window = UserProfileWindow(connection=self.connection, user_id=user_id)
        self.user_profile_window.show()
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

        self.user_profile_window = UserProfileWindow(connection=self.connection)
        self.user_profile_window.show()
        self.hide()

    def error_handler(self, error_text: str, obj: QtWidgets.QLineEdit):
        obj.setStyleSheet(error_line_edit_register_style) #Переданному line_edit присваиваются стили ошибки(Красная рамка)
        self.ui.error_label.setText(error_text)

    def check_data(self, error_desc: str, column_name: str, obj_line_edit: QtWidgets.QLineEdit) -> bool:
        self.cursor.execute(f'SELECT {column_name} FROM users WHERE {column_name} = %s', (obj_line_edit.text().strip(),))
        checker = self.cursor.fetchone()
        print(checker)
        if checker: #Если запрос к базе вернет кортеж, то поле в базе существует
            self.error_handler(error_desc, obj_line_edit)
            return True
        else:
            obj_line_edit.setStyleSheet(main_style_line_edit)
            return False


class UserProfileWindow(QtWidgets.QWidget):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent)
        self.ui = UiUserProfile()
        self.ui.setupUi(self)

        self.connection = kwargs['connection']
        self.user_id = kwargs['user_id']
        self.cursor = self.connection.cursor()

        self.ui.playlist1_into_scroll.clicked.connect(self.click_button_playlist)
        self.ui.pushButton.clicked.connect(self.window_create_playlist)

        self.set_user_data()

    def create_playlist_button(self):
        name_playlist = self.dialog_create_playlist.lineEdit.text().strip()

        if name_playlist:
            self.cursor.execute('SELECT playlist_name FROM playlist WHERE playlist_name = %s', (name_playlist, ))
            check_unique_name = self.cursor.fetchone()

            if not check_unique_name:
                self.cursor.execute('INSERT INTO playlist (playlist_name, user_id) VALUES (%s, %s)', (name_playlist, self.user_id))
                self.connection.commit()
                self.dialog_window.close()

                if self.ui.horizontalLayout_playlist.count() < 3:
                    new_playlist = QtWidgets.QPushButton()
                    new_playlist.setMinimumSize(QtCore.QSize(150, 150))
                    new_playlist.setMaximumSize(QtCore.QSize(150, 150))
                    new_playlist.setStyleSheet("border: 1px solid black; border-radius: 7%;"
                                               "background-color: rgb(89, 114, 93);")
                    new_playlist.setObjectName(name_playlist + '_into_main')
                    new_playlist.setText(name_playlist)
                    self.ui.horizontalLayout_playlist.addWidget(new_playlist)
            else:
                self.error_handler('Плейлист существует',
                                   self.dialog_create_playlist.lineEdit)

    def window_create_playlist(self):
        self.dialog_window = QtWidgets.QDialog()
        self.dialog_create_playlist = UiCreatePlaylist()
        self.dialog_create_playlist.setupUi(self.dialog_window)

        self.dialog_create_playlist.pushButton_Create.clicked.connect(self.create_playlist_button)

        self.dialog_window.exec()

    def set_user_data(self):
        self.cursor.execute('SELECT * FROM users WHERE id = %s', (self.user_id, ))
        user_data = self.cursor.fetchone()
        self.ui.username.setText('username: ' + user_data[3])

        self.cursor.execute('SELECT * FROM playlist WHERE user_id = %s', (self.user_id,))
        playlists_data = self.cursor.fetchall()

        self.ui.playlist1_into_scroll.setText(playlists_data[0][1])
        self.ui.playlist1_into_main.setText(playlists_data[0][1])

        for playlist in playlists_data[1:]:
            count_main = self.ui.horizontalLayout_playlist.count()

            new_playlist = QtWidgets.QPushButton()
            new_playlist.setMinimumSize(QtCore.QSize(150, 150))
            new_playlist.setMaximumSize(QtCore.QSize(150, 150))
            new_playlist.setStyleSheet("border: 1px solid black; border-radius: 7%;" 
                                       "background-color: rgb(62, 79, 65);")
            new_playlist.setObjectName(playlist[1] + '_into_scroll')
            new_playlist.setText(playlist[1])

            self.ui.verticalLayout_in_scroll.addWidget(new_playlist)

            if count_main < 3:
                new_playlist.setStyleSheet("border: 1px solid black; border-radius: 7%;"
                                           "background-color: rgb(89, 114, 93);")
                new_playlist.setObjectName(playlist[1] + '_into_main')
                self.ui.horizontalLayout_playlist.addWidget(new_playlist)

    def click_button_playlist(self):
        print('Привет')

    def error_handler(self, error_text: str, obj: QtWidgets.QLineEdit):
        obj.setStyleSheet(error_line_edit_register_style) #Переданному line_edit присваиваются стили ошибки(Красная рамка)
        self.dialog_create_playlist.error_label.setText(error_text)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    app.setStyleSheet(main_style)

    mywin = LoginWindow()
    mywin.show()
    app.exec()

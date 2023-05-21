import os
import sys
from typing import Union

from PIL import Image, ImageDraw
from mutagen.mp3 import MP3

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
        self.playlists = []
        self.user_id = kwargs['user_id']
        self.cursor = self.connection.cursor()

        self.ui.playlist1_into_scroll.clicked.connect(self.click_button_playlist)
        self.ui.playlist1_into_main.clicked.connect(self.click_button_playlist)
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

                new_playlist = self.create_button_playlist(name_playlist, 'rgb(62, 79, 65)')
                self.ui.verticalLayout_in_scroll.addWidget(new_playlist)
                self.playlists.append(new_playlist)

                if self.ui.horizontalLayout_playlist.count() < 3:
                    new_playlist = self.create_button_playlist(name_playlist, 'rgb(89, 114, 93)')
                    self.ui.horizontalLayout_playlist.addWidget(new_playlist)
            else:
                self.error_handler('Плейлист существует',
                                   self.dialog_create_playlist.lineEdit)

    def create_button_playlist(self, name_playlist, back_color):
        new_playlist = QtWidgets.QPushButton()
        new_playlist.setMinimumSize(QtCore.QSize(150, 150))
        new_playlist.setMaximumSize(QtCore.QSize(150, 150))
        new_playlist.setStyleSheet("border: 1px solid black; border-radius: 7%;"
                                   f"background-color: {back_color};")
        new_playlist.setObjectName(name_playlist + '_into_main')
        new_playlist.setText(name_playlist)

        new_playlist.clicked.connect(self.click_button_playlist)

        return new_playlist

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

        self.cursor.execute('SELECT * FROM playlist WHERE user_id = %s AND track_id IS NULL', (self.user_id, ))
        playlists_data = self.cursor.fetchall()

        if playlists_data:
            self.ui.playlist1_into_scroll.setText(playlists_data[0][1])
            self.ui.playlist1_into_main.setText(playlists_data[0][1])

            self.playlists.append(self.ui.verticalLayout_in_scroll.itemAt(0).widget())

            for playlist in playlists_data[1:]:
                count_main = self.ui.horizontalLayout_playlist.count()

                new_playlist = QtWidgets.QPushButton()
                new_playlist.setMinimumSize(QtCore.QSize(150, 150))
                new_playlist.setMaximumSize(QtCore.QSize(150, 150))
                new_playlist.setStyleSheet("border: 1px solid black; border-radius: 7%;" 
                                           "background-color: rgb(62, 79, 65);")
                new_playlist.setObjectName(playlist[1] + '_into_scroll')
                new_playlist.setText(playlist[1])
                new_playlist.clicked.connect(self.click_button_playlist)

                self.ui.verticalLayout_in_scroll.addWidget(new_playlist)

                self.playlists.append(new_playlist)

                if count_main < 3:
                    new_playlist_main = QtWidgets.QPushButton()
                    new_playlist_main.setStyleSheet("border: 1px solid black; border-radius: 7%;"
                                               "background-color: rgb(89, 114, 93);")
                    new_playlist_main.setMinimumSize(QtCore.QSize(150, 150))
                    new_playlist_main.setMaximumSize(QtCore.QSize(150, 150))
                    new_playlist_main.setObjectName(playlist[1] + '_into_main')
                    new_playlist_main.setText(playlist[1])
                    print(playlist[1])

                    new_playlist_main.clicked.connect(self.click_button_playlist)

                    self.ui.horizontalLayout_playlist.addWidget(new_playlist_main)

            # self.playlists = [self.ui.verticalLayout_in_scroll.itemAt(i).widget()
                              # for i in range(self.ui.verticalLayout_in_scroll.count())]
        else:
            self.ui.playlist1_into_main.deleteLater()
            self.ui.playlist1_into_scroll.deleteLater()

    def click_button_playlist(self):
        self.playlist_window = PlaylistWindow(connection=self.connection, user_id=self.user_id,
                                              playlist_name=QtWidgets.QApplication.instance().sender().text(),
                                              scroll_layout=self.playlists, profile_window=self)
        self.playlist_window.show()
        self.hide()

    def error_handler(self, error_text: str, obj: QtWidgets.QLineEdit):
        obj.setStyleSheet(error_line_edit_register_style) #Переданному line_edit присваиваются стили ошибки(Красная рамка)
        self.dialog_create_playlist.error_label.setText(error_text)


class PlaylistWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent)
        self.ui = UiPlaylistView()
        self.ui.setupUi(self)

        self.connection = kwargs['connection']
        self.cursor = self.connection.cursor()

        self.playlists = kwargs['scroll_layout']
        self.ui.verticalLayout_in_scroll.itemAt(0).widget().deleteLater()
        [self.ui.verticalLayout_in_scroll.addWidget(button) for button in self.playlists]

        self.user_id = kwargs['user_id']
        self.playlist_name = kwargs['playlist_name']
        self.main_window = kwargs['profile_window']

        self.ui.back_button.clicked.connect(self.show_main_window)
        self.ui.add_track_button.clicked.connect(self.add_track)

        self.set_playlist_data()

    def show_main_window(self):
        [self.main_window.ui.verticalLayout_in_scroll.addWidget(widget) for widget in self.playlists]
        self.main_window.show()
        self.hide()

    def get_name_image(self):
        self.file_path_img, _ = QtWidgets.QFileDialog.getOpenFileName(self.dialog_window, "Open File", ".", "Image files (*.png, *.jpg)")

        if self.file_path_img:
            im = Image.open(self.file_path_img)
            width, height = im.size

            if width > 1920 and height > 1080:
                self.dialog_add_track.upload_cover_photo.setStyleSheet(error_line_edit_register_style)
                self.file_path_img = None
            else:
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("icons/upload_done-icon.svg"))
                self.dialog_add_track.upload_cover_photo.setIcon(icon)

                self.dialog_add_track.upload_cover_photo.setStyleSheet(main_style)
                self.dialog_add_track.upload_cover_photo.clicked.disconnect()

    def get_name_mp3(self):
        self.file_path_mp3, _ = QtWidgets.QFileDialog.getOpenFileName(self.dialog_window,
                                                                      "Open File", ".", "Audio Files (*.mp3)")

        if self.file_path_mp3:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icons/upload_done-icon.svg"))
            self.dialog_add_track.upload_track.setIcon(icon)

            self.dialog_add_track.upload_track.setStyleSheet(main_style)
            self.dialog_add_track.upload_track.clicked.disconnect()

    def upload(self, executor: str, track_name: str, file_path: str) -> str:  # Проверка есть ли трек с таким именем
        if file_path:
            extension = 'mp3' if file_path.split("/")[-1].rsplit(".", 1)[-1] == 'mp3' else 'jpg'
            path = f'Tracks/{executor}/{track_name}/{track_name}.{extension}'

            with open(file_path, 'rb') as file:
                file_data = file.read()

            if not os.path.exists(f'Tracks/{executor}'):
                os.mkdir(f'Tracks/{executor}')

            if not os.path.exists(f'Tracks/{executor}/{track_name}'):
                os.mkdir(f'Tracks/{executor}/{track_name}')
            elif os.path.exists(path):
                return path

            with open(path, 'wb') as file:
                file.write(file_data)

            if extension == 'jpg':
                im = Image.open(path)
                im = self.add_corners(im, im.size[0] // 10)

                path = f'Tracks/{executor}/{track_name}/{track_name}.png'
                im.save(path)
                os.remove(f'Tracks/{executor}/{track_name}/{track_name}.{extension}')

            return path

    @staticmethod
    def add_corners(im, rad):
        circle = Image.new('L', (rad * 2, rad * 2), 0)
        draw = ImageDraw.Draw(circle)
        draw.ellipse((0, 0, rad * 2 - 1, rad * 2 - 1), fill=255)
        alpha = Image.new('L', im.size, 255)
        w, h = im.size
        alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
        alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
        alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
        alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
        im.putalpha(alpha)
        return im

    def click_add_track_button(self):
        track_name = self.dialog_add_track.lineEdit.text().strip()
        executor = self.dialog_add_track.lineEdit_2.text().strip()

        if not self.error_handler(track_name, self.dialog_add_track.lineEdit) and not \
                self.error_handler(executor, self.dialog_add_track.lineEdit_2):
            if self.__dict__.get('file_path_mp3'):
                mp3_path = self.upload(executor, track_name, self.file_path_mp3)
            elif os.path.exists(f'Tracks/{executor}/{track_name}/{track_name}.mp3'):
                mp3_path = f'Tracks/{executor}/{track_name}/{track_name}.mp3'
            else:
                self.dialog_add_track.upload_track.setStyleSheet(error_line_edit_register_style)
                return

            self.dialog_add_track.upload_track.setStyleSheet(main_style)

            if self.__dict__.get('file_path_img'):
                cover_path = self.upload(executor, track_name, self.file_path_img)
            elif os.path.exists(f'Tracks/{executor}/{track_name}/{track_name}.png'):
                cover_path = f'Tracks/{executor}/{track_name}/{track_name}.png'
            else:
                cover_path = 'Tracks/Covers/defaulf.jpg'

            audio = MP3(mp3_path)

            duration = int(audio.info.length)
            duration = str(duration // 60) + ':' + str(duration % 60)

            if not (int(duration.split(':')[0]) // 10):
                duration = '0' + duration
            if not (int(duration.split(':')[1]) // 10):
                duration = duration.split(':')
                duration = duration[0] + ':' + '0' + duration[1]

            self.cursor.execute('SELECT id FROM performers WHERE performer_name = %s', (executor,))
            id_executor = self.cursor.fetchone()

            if not id_executor:
                self.cursor.execute('INSERT INTO performers (performer_name) VALUES (%s)', (executor, ))
                self.connection.commit()

                self.cursor.execute('SELECT lastval()')
                id_executor = self.cursor.fetchone()

            self.cursor.execute('SELECT id, cover_photo FROM track_list'                               
                                ' WHERE track_name = %s AND duration = %s AND performers_id = %s',
                                (track_name, duration, id_executor))
            track_id = self.cursor.fetchone()

            if not track_id:
                self.cursor.execute('INSERT INTO track_list (track_name, duration, performers_id, mp3, cover_photo)'
                                    ' VALUES (%s, %s, %s, %s, %s)',
                                    (track_name, duration, id_executor,
                                     f'Tracks/{executor}/{track_name}/{track_name}.mp3', cover_path))
                self.connection.commit()

                self.cursor.execute('SELECT lastval()')
                track_id = self.cursor.fetchone()
            else:
                if track_id[1] == 'Tracks/Covers/defaulf.jpg' and cover_path != 'Tracks/Covers/defaulf.jpg':
                    self.cursor.execute('UPDATE track_list SET cover_photo = %s WHERE id = %s',
                                        (cover_path, track_id[0]))
                    self.connection.commit()

                    for i in range(self.ui.verticalLayout_2.count()):
                        if self.ui.verticalLayout_2.itemAt(i).itemAt(2).itemAt(0).widget().text() == track_name and\
                                self.ui.verticalLayout_2.itemAt(i).itemAt(2).itemAt(1).widget().text() == executor:
                            self.ui.verticalLayout_2.itemAt(i).itemAt(1).widget().setPixmap(QtGui.QPixmap(cover_path))
                            self.ui.verticalLayout_2.itemAt(i).itemAt(1).widget().setScaledContents(True)

                track_id = track_id[0]
            self.cursor.execute('INSERT INTO playlist (playlist_name, user_id, track_id) VALUES (%s, %s, %s)',
                                (self.playlist_name, self.user_id, track_id))
            self.connection.commit()

            self.dialog_window.close()

            self.cursor.execute('SELECT login FROM users WHERE id = %s', (self.user_id,))
            add_user = self.cursor.fetchone()[0]

            count_track = self.ui.verticalLayout_2.count()
            if count_track == 5:
                for i in range(count_track):
                    if self.ui.verticalLayout_2.itemAt(i).itemAt(3).widget().text() == 'add: owner':
                        self.ui.verticalLayout_2.itemAt(i).itemAt(1).widget().setPixmap(QtGui.QPixmap(cover_path))
                        self.ui.verticalLayout_2.itemAt(i).itemAt(1).widget().setScaledContents(True)
                        self.ui.verticalLayout_2.itemAt(i).itemAt(2).itemAt(0).widget().setText(track_name)
                        self.ui.verticalLayout_2.itemAt(i).itemAt(2).itemAt(1).widget().setText(executor)
                        self.ui.verticalLayout_2.itemAt(i).itemAt(3).widget().setText('add: ' + add_user)
                        self.ui.verticalLayout_2.itemAt(i).itemAt(4).widget().setText(duration)
                        break
                    elif i == 4 and self.ui.verticalLayout_2.itemAt(i).itemAt(3).widget().text() != 'add: owner':
                        self.add_track_in_scroll(cover_path, track_name, executor, add_user, duration)
            else:
                self.add_track_in_scroll(cover_path, track_name, executor, add_user, duration)

    def add_track(self):
        self.dialog_window = QtWidgets.QDialog()
        self.dialog_add_track = UiAddTrack()
        self.dialog_add_track.setupUi(self.dialog_window)

        self.dialog_add_track.upload_track.clicked.connect(self.get_name_mp3)
        self.dialog_add_track.upload_cover_photo.clicked.connect(self.get_name_image)
        self.dialog_add_track.add.clicked.connect(self.click_add_track_button)

        self.dialog_window.exec()

    def set_playlist_data(self):
        self.cursor.execute('SELECT playlist_name, track_name, duration, cover_photo, mp3, performer_name'
                            ' FROM playlist LEFT JOIN track_list ON track_id=track_list.id'
                            ' LEFT JOIN performers ON track_list.performers_id=performers.id'
                            ' WHERE playlist_name = %s AND user_id = %s AND track_id IS NOT NULL',
                            (self.playlist_name, self.user_id))
        playlist_data = self.cursor.fetchall()

        self.ui.playlist_name.setText(self.playlist_name)

        if playlist_data:
            self.cursor.execute('SELECT login FROM users WHERE id = %s', (self.user_id,))
            add_user = self.cursor.fetchone()[0]

            for i in range(len(playlist_data)):
                if i < 5 and playlist_data[i]:
                    self.ui.verticalLayout_2.itemAt(i).itemAt(1).widget().setPixmap(QtGui.QPixmap(playlist_data[i][3]))
                    self.ui.verticalLayout_2.itemAt(i).itemAt(1).widget().setScaledContents(True)
                    self.ui.verticalLayout_2.itemAt(i).itemAt(2).itemAt(0).widget().setText(playlist_data[i][1])
                    self.ui.verticalLayout_2.itemAt(i).itemAt(2).itemAt(1).widget().setText(playlist_data[i][5])
                    self.ui.verticalLayout_2.itemAt(i).itemAt(3).widget().setText('add: ' + add_user)
                    self.ui.verticalLayout_2.itemAt(i).itemAt(4).widget().setText(playlist_data[i][2])
                else:
                    self.add_track_in_scroll(playlist_data[i][3], playlist_data[i][1],
                                             playlist_data[i][5], add_user, playlist_data[i][2])
    def add_track_in_scroll(self, path_to_cover: str, track_name: str, executor: str, add_user: str, duration: str ):
        horizontalLayout_4 = QtWidgets.QHBoxLayout()
        horizontalLayout_4.setObjectName("horizontalLayout_4")

        playButton_1 = QtWidgets.QPushButton(self.ui.scrollAreaWidgetContents)
        playButton_1.setMinimumSize(QtCore.QSize(24, 24))
        playButton_1.setMaximumSize(QtCore.QSize(24, 24))
        playButton_1.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        playButton_1.setStyleSheet("border: 1.5px solid black; border-radius: 12%;")
        playButton_1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/play-icon.svg"))
        playButton_1.setIcon(icon)
        playButton_1.setIconSize(QtCore.QSize(12, 12))
        playButton_1.setCheckable(False)
        playButton_1.setFlat(False)
        playButton_1.setObjectName("playButton_1")

        horizontalLayout_4.addWidget(playButton_1)

        track1_image = QtWidgets.QLabel(self.ui.scrollAreaWidgetContents)
        track1_image.setMaximumSize(QtCore.QSize(0, 30))
        track1_image.setMaximumSize(QtCore.QSize(30, 30))
        track1_image.setStyleSheet("border: 1px solid black; border-radius: 8px;")
        track1_image.setPixmap(QtGui.QPixmap(path_to_cover))
        track1_image.setScaledContents(True)
        track1_image.setObjectName("track1_image")

        horizontalLayout_4.addWidget(track1_image)

        verticalLayout_5 = QtWidgets.QVBoxLayout()
        verticalLayout_5.setSpacing(0)
        verticalLayout_5.setObjectName("verticalLayout_5")

        TrackName1 = QtWidgets.QLabel(self.ui.scrollAreaWidgetContents)
        TrackName1.setMinimumSize(QtCore.QSize(0, 15))
        TrackName1.setMaximumSize(QtCore.QSize(250, 15))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        # font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        TrackName1.setFont(font)
        TrackName1.setStyleSheet("color: rgb(255, 255, 255);")
        TrackName1.setObjectName("TrackName1")
        TrackName1.setText(track_name)

        verticalLayout_5.addWidget(TrackName1)

        ArtistName1 = QtWidgets.QLabel(self.ui.scrollAreaWidgetContents)
        ArtistName1.setMinimumSize(QtCore.QSize(0, 15))
        ArtistName1.setMaximumSize(QtCore.QSize(250, 15))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        ArtistName1.setFont(font)
        ArtistName1.setStyleSheet(" color: rgb(152, 152, 152);")
        ArtistName1.setObjectName("ArtistName1")
        ArtistName1.setText(executor)

        verticalLayout_5.addWidget(ArtistName1)
        horizontalLayout_4.addLayout(verticalLayout_5)

        add_label1 = QtWidgets.QLabel(self.ui.scrollAreaWidgetContents)
        add_label1.setMinimumSize(QtCore.QSize(0, 31))
        add_label1.setMaximumSize(QtCore.QSize(16777215, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        add_label1.setFont(font)
        add_label1.setStyleSheet("")
        add_label1.setObjectName("add_label1")
        add_label1.setText('add: ' + add_user)

        horizontalLayout_4.addWidget(add_label1)

        track_time1 = QtWidgets.QLabel(self.ui.scrollAreaWidgetContents)
        track_time1.setMinimumSize(QtCore.QSize(0, 31))
        track_time1.setMaximumSize(QtCore.QSize(51, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        track_time1.setFont(font)
        track_time1.setStyleSheet("")
        track_time1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        track_time1.setObjectName("track_time1")
        track_time1.setText(duration)

        horizontalLayout_4.addWidget(track_time1)

        delete_button1 = QtWidgets.QPushButton(self.ui.scrollAreaWidgetContents)
        delete_button1.setMinimumSize(QtCore.QSize(31, 31))
        delete_button1.setMaximumSize(QtCore.QSize(31, 16777215))
        delete_button1.setStyleSheet("")
        delete_button1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/delete-svgrepo-com.svg"))
        delete_button1.setIcon(icon1)
        delete_button1.setIconSize(QtCore.QSize(24, 24))
        delete_button1.setObjectName("delete_button1")

        horizontalLayout_4.addWidget(delete_button1)

        self.ui.verticalLayout_2.addLayout(horizontalLayout_4)

    @staticmethod
    def error_handler(text: str, obj: QtWidgets.QLineEdit):
        if text:
            obj.setStyleSheet(main_style_line_edit)
            return False

        obj.setStyleSheet(error_line_edit_register_style) #Переданному line_edit присваиваются стили ошибки(Красная рамка)
        return True


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    app.setStyleSheet(main_style)

    mywin = LoginWindow()
    mywin.show()
    app.exec()

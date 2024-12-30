from time import sleep


class User:
    def __init__(self, name, pwd, age):
        self.nickname = name
        self.password = hash(pwd)
        self.age = age

    def __repr__(self):
        return self.nickname

    def __eq__(self, other):
        return self.nickname == other.nickname


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __repr__(self):
        return self.title

    def __eq__(self, other):
        return self.title == other.title

    def play(self):
        for sec in range(self.time_now + 1, self.duration + 1, 1):
            print(sec, end=' ')
            sleep(0.5)
        print('Конец видео')


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def __contains__(self, item):
        return any(item == video.title for video in self.videos)

    def log_in(self, nickname, password):
        for user in self.users:
            if all([user.nickname == nickname, user.password == hash(password)]):
                self.current_user = user
                break

    def register(self, nickname, password, age):
        new_user = User(nickname, password, age)
        if new_user in self.users:
            print(f'Пользователь {nickname} уже существует')
        else:
            self.users.append(new_user)
        self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        self.videos += [video for video in videos if video not in self.videos]

    def get_videos(self, search_word):
        return [video for video in self.videos if str.lower(search_word) in str.lower(video.title)]

    def watch_video(self, title):
        if self.current_user is None:
            print('Войдите в аккаунт чтобы смотреть видео')
        elif title in self:
            if self.current_user.age < 18:
                print('Вам нет 18 лет, пожалуйста покиньте страницу')
            else:
                self.get_videos(title)[0].play()


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
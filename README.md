# Документацию по использованию программы
## Для корректной работы программы требуется следующее:
- Браузер (рекомендуется **Chrome**)
- Python версии 3.10 и новее
- Любой компилятор подходящий для языка Python (рекомендуется PyCharm)
- Наличие библиотек os и playwright в проекте компилятора
## Установка
Ниже приведена инструкция для установки всех необходимых библиотек:
- Чтобы установить библиотеки нужно открыть терминал в компиляторе и ввести следующие команды:
  - pip install **playwright** (библиотека производящая все процессы тестирования)
  - pip install **os** (данная библиотека нужна для создания папки, в случае ее отсутствия, а так же сохранять в данную папку)
  - pip install **pytest** (Библиотека для запуска программы)
 ## Запуск программы
 Откройте в компиляторе файл **main_test.py**. Откройте терминал и введите команду pytest tests/main_test.py. После чего проверьте папку output на наличие скриншотов
 ## Возникновение ошибок
 Если возникла ошибка, которая сообщает о превышении времени ожидания ответа, то попробуйте перезапустить программу. Время, за которое выполняется тест, всегда разное и может превышать 30 секунд, после которых программа сама прекращает свою работу

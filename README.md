## Тестовое задание для Digift

### Задача
Имеется последовательность цифр не начинающаяся с 0 (строка).

Имеется «словарь» ставящий в соответствие каждой цифре и некоторым парам цифр букву латинского алфавита от A до Z 
таким образом что букве «A» соответствует цифра «1» а буква «Z» будет соответствовать паре цифр «27».
Необходимо разработать алгоритм, который сосчитает число комбинаций, которыми исходная «строка» может быть 
разложена по «словарю».
Примеры:
* «1234» - ответ 3 («1»-«2»-«3»-«4»; «12»-«3»-«4»; «1»-«23»-«4»)
* «10101» - ответ 1
* «54321» - ответ 2 («5»-«4»-«3»-«2»-«1»;«5»-«4»-«3»-«21»)

### Решение
Метод осуществляющий подсчёт `get_count` находит в `./src/getCount.py`

Происходит рекурсивный обход строки, формирующий все возможные комбинаций разложения строки на комбинаций, 
после чего подсчитывается количество этих комбинаций.

Рекурсия - зло, которое стремительно потребляет память при работе, при этом одни и те же коминации проверяются 
по несколько раз в разных ветках рекурсии, но более эффективное решение быстро придумать не получилось


### Установка окружения
Из корня репозитория запустить
```
python -m venv ./.venv
pip install -r requirements.txt
```

### Запуск тестов
Из корня репозитория запустить
```pytest ./tests```

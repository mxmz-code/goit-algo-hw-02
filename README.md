# goit-algo-hw-02

## Опис проєкту

Цей проєкт демонструє роботу з основними структурами даних у Python через три завдання:

1. **Система обробки заявок** – імітація черги обробки заявок.
2. **Перевірка на паліндром** – визначення, чи є рядок паліндромом.
3. **Перевірка симетричності дужок** – перевірка виразу на правильність розставлених дужок.

## Структура папок

```
goit-algo-hw-02/
│
├── main.py               # Головний файл для запуску програми
├── tasks/
│   ├── task1.py          # Завдання 1: Система обробки заявок
│   ├── task2.py          # Завдання 2: Перевірка на паліндром
│   └── task3.py          # Завдання 3: Перевірка симетричності дужок
│
├── modules/
│   ├── ui_utils.py       # Утиліти для інтерфейсу користувача
│   ├── logger.py         # Логування дій користувача
│   └── language.py       # Модуль для перекладу інтерфейсу
│
└── README.md             # Опис проєкту
```

## Інструкція зі встановлення

1. **Склонуйте репозиторій**:

    ```bash
    git clone https://github.com/yourusername/goit-algo-hw-02.git
    cd goit-algo-hw-02
    ```

2. **Створіть та активуйте віртуальне середовище**:

    ```bash
    python -m venv venv
    source venv/bin/activate       # Для Linux та macOS
    .\venv\Scripts\activate     # Для Windows
    ```

3. **Встановіть залежності**:

    ```bash
    pip install -r requirements.txt
    ```

## Як запустити програму

Запустіть головний файл **main.py**:

```bash
python main.py
```

## Інструкція з використання

### Головне меню

При запуску програми з'явиться головне меню, де можна вибрати одне із завдань:

- `[1]` Виконати завдання 1 (Обробка заявок)
- `[2]` Виконати завдання 2 (Перевірка на паліндром)
- `[3]` Виконати завдання 3 (Перевірка дужок)
- `[q]` Вихід

### Завдання 1: Система обробки заявок

Команди:
- `[g]` Створити заявку
- `[p]` Обробити заявку
- `[s]` Статус черги

### Завдання 2: Перевірка на паліндром

Команди:
- `[1]` Ввести текст для перевірки
- `[2]` Показати приклади паліндромів
- `[3]` Згенерувати випадковий рядок

### Завдання 3: Перевірка симетричності дужок

Команди:
- `[1]` Ввести вираз для перевірки
- `[2]` Згенерувати та перевірити 5 випадкових виразів

## Приклади виконання

### Завдання 1

```
🔹 [g] Створити заявку
🔹 [p] Обробити заявку
🔹 [s] Статус черги
🔹 [q] Вихід

Введіть команду: g
✅ Заявку створено: request-1234
```

### Завдання 2

```
🔹 [1] Ввести текст для перевірки
🔹 [2] Показати приклади паліндромів
🔹 [3] Згенерувати випадковий рядок

Введіть команду: 1
Введіть рядок для перевірки: radar
✅ Це паліндром
```

### Завдання 3

```
🔹 [1] Ввести вираз для перевірки
🔹 [2] Згенерувати та перевірити 5 випадкових виразів

Введіть команду: 1
Введіть вираз для перевірки: ( [ { } ] )
✅ Симетрично
```

## Ліцензія

Цей проєкт ліцензовано під ліцензією MIT.

## Контакти

Для зворотного зв'язку не звертайтесь.
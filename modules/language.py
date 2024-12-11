import json

# Словник для зберігання перекладів
translations = {
    "en": {
        # Main
        "main_menu": "Main Menu",
        "task1": "Execute Task 1 (Request Processing)",
        "task2": "Execute Task 2 (Palindrome Check)",
        "task3": "Execute Task 3 (Bracket Check)",
        "exit": "Exit",
        "enter_command": "Enter a command",
        "goodbye": "Thank you for using the program! Goodbye!",
        "welcome": "Welcome to the program!",
        "topic": "Topic: Basic Data Structures (goit-algo-hw-02)",
        "lets_go": "Let's go!",
        "unknown_command": "Unknown command. Please try again.",
        "press_enter": "Press Enter to continue...",
        "change_language": "Change language",
        "stack": "Stack",
        "stack_explanation": "Stack content (shows the sequence of unmatched brackets):",

        # Task 1
        "create_request": "Create a request",
        "process_request": "Process a request",
        "queue_status": "Queue status",
        "request_created": "Request created",
        "processing_request": "Processing request",
        "request_processed": "Request processed",
        "queue_full": "The queue is full. Cannot add a new request.",
        "queue_empty": "The queue is empty. No requests to process.",
        "current_queue": "Current queue:",

        # Task 2
        "enter_text": "Enter a string to check",
        "palindrome": "This is a palindrome",
        "not_palindrome": "This is not a palindrome",
        "empty_input": "Input cannot be empty!",
        "show_examples": "Show examples of palindromes",
        "generate_random": "Generate a random string",
        "palindrome_examples": "Examples of palindromes:",
        "random_string": "Generated random string",

        # Task 3
        "checking_expression": "Checking expression",
        "balanced": "Balanced",
        "not_balanced": "Not balanced",
        "input_expression": "Enter an expression to check",
        "checking_random_expressions": "Checking 5 random expressions...",
        "generate_random_expressions": "Generate and check 5 random expressions",
        "at_position": "at position",
        "doesnt_match": "doesn't match",
        "not_closed": "not closed",
        "no_brackets": "No brackets found in the expression"
    },
    "uk": {
        # Main
        "main_menu": "Головне меню",
        "task1": "Виконати завдання 1 (Обробка заявок)",
        "task2": "Виконати завдання 2 (Перевірка на паліндром)",
        "task3": "Виконати завдання 3 (Перевірка дужок)",
        "exit": "Вихід",
        "enter_command": "Введіть команду",
        "goodbye": "Дякуємо за використання програми! До зустрічі!",
        "welcome": "Ласкаво просимо до програми!",
        "topic": "Тема: Основні структури даних (goit-algo-hw-02)",
        "lets_go": "Поїхали!",
        "unknown_command": "Невідома команда. Спробуйте ще раз.",
        "press_enter": "Натисніть Enter для продовження...",
        "change_language": "Змінити мову",
        "stack": "Стек",
        "stack_explanation": "Вміст стеку (показує послідовність непарних дужок):",

        # Task 1
        "create_request": "Створити заявку",
        "process_request": "Обробити заявку",
        "queue_status": "Статус черги",
        "request_created": "Заявку створено",
        "processing_request": "Обробка заявки",
        "request_processed": "Заявку оброблено",
        "queue_full": "Черга переповнена. Неможливо додати нову заявку.",
        "queue_empty": "Черга порожня. Немає заявок для обробки.",
        "current_queue": "Поточна черга:",

        # Task 2
        "enter_text": "Введіть рядок для перевірки",
        "palindrome": "Це паліндром",
        "not_palindrome": "Це не паліндром",
        "empty_input": "Введення не може бути порожнім!",
        "show_examples": "Показати приклади паліндромів",
        "generate_random": "Згенерувати випадковий рядок",
        "palindrome_examples": "Приклади паліндромів:",
        "random_string": "Згенерований випадковий рядок",

        # Task 3
        "checking_expression": "Перевірка виразу",
        "balanced": "Симетрично",
        "not_balanced": "Несиметрично",
        "input_expression": "Введіть вираз для перевірки",
        "checking_random_expressions": "Перевірка 5 випадкових виразів...",
        "generate_random_expressions": "Згенерувати та перевірити 5 випадкових виразів",
        "at_position": "на позиції",
        "doesnt_match": "не відповідає",
        "not_closed": "не закрито",
        "no_brackets": "У виразі не знайдено дужок"
    }
}

def translate(key, lang="en"):
    """Перекладає текст за ключем відповідно до вибраної мови."""
    return translations.get(lang, translations["en"]).get(key, key)

def set_language():
    """Дозволяє користувачу вибрати мову інтерфейсу."""
    print("🌐 Виберіть мову / Choose a language:")
    print("[1] English")
    print("[2] Українська")
    choice = input("📝 Enter choice (1 or 2): ").strip()

    if choice == '2':
        return "uk"
    return "en"

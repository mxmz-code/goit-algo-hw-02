from modules.ui_utils import clear_screen, print_banner, pause
from modules.language import translate, set_language
from modules.logger import log_action
import random
from colorama import init, Fore, Style

# Инициализация colorama
init(autoreset=True)

def explain_stack(stack, language):
    """Функция для объяснения содержимого стека."""
    if not stack:
        return ""
    explanation = f"\n{translate('stack_explanation', language)}\n"
    for char, pos in stack:
        explanation += f"  {Fore.CYAN}'{char}'{Style.RESET_ALL} {translate('at_position', language)} {pos}\n"
    return explanation

def is_balanced(expression, language):
    """Перевіряє, чи є дужки у виразі симетричними з підсвіткою помилкових дужок і візуалізацією стека."""
    if not any(char in '()[]{}<>' for char in expression):
        return f"{Fore.YELLOW}⚠️ {translate('no_brackets', language)}"

    stack = []
    brackets = {')': '(', ']': '[', '}': '{', '>': '<'}
    expression_list = list(expression)

    for i, char in enumerate(expression_list):
        if char in '([{<':
            stack.append((char, i))
        elif char in ')]}>':
            if not stack:
                expression_list[i] = f"{Fore.RED}{char}{Style.RESET_ALL}"
                return f"{Fore.RED}❌ {translate('not_balanced', language)} {translate('at_position', language)} {i}: '{char}'\n{explain_stack(stack, language)}"
            top, pos = stack.pop()
            if top != brackets[char]:
                expression_list[i] = f"{Fore.RED}{char}{Style.RESET_ALL}"
                expression_list[pos] = f"{Fore.RED}{top}{Style.RESET_ALL}"
                return f"{Fore.RED}❌ {translate('not_balanced', language)} {translate('at_position', language)} {i}: '{char}' {translate('doesnt_match', language)} '{top}'\n{explain_stack(stack, language)}"

    if stack:
        for _, pos in stack:
            expression_list[pos] = f"{Fore.RED}{expression_list[pos]}{Style.RESET_ALL}"
        return f"{Fore.RED}❌ {translate('not_balanced', language)} {translate('not_closed', language)}\n{explain_stack(stack, language)}"

    return f"{Fore.GREEN}✅ {translate('balanced', language)}"

def generate_random_expression(symmetrical=False):
    """Генерує випадковий вираз з дужками для перевірки. Якщо symmetrical=True, генерує симетричний вираз."""
    if symmetrical:
        length = random.randint(3, 7)
        half = ''.join(random.choice('([{<') for _ in range(length))
        closing = ''.join({ '(': ')', '[': ']', '{': '}', '<': '>' }[char] for char in reversed(half))
        return half + closing
    else:
        brackets = ['(', ')', '[', ']', '{', '}', '<', '>']
        length = random.randint(5, 15)
        return ''.join(random.choice(brackets) for _ in range(length))

def check_random_expressions(language):
    """Генерує та перевіряє 5 випадкових виразів, з яких один гарантовано симетричний."""
    clear_screen()
    print_banner(translate("task3", language))
    print(translate("checking_random_expressions", language))
    print()

    expressions = [generate_random_expression() for _ in range(4)]
    expressions.append(generate_random_expression(symmetrical=True))
    random.shuffle(expressions)

    for i, expression in enumerate(expressions, 1):
        result = is_balanced(expression, language)
        print(f"{i}. {expression} -> {result}\n")
        log_action(f"Random expression '{expression}' -> {result}")

    input(translate("press_enter", language))

def main(language):
    """Головний цикл програми для перевірки симетрії дужок."""
    while True:
        clear_screen()
        print_banner(translate("task3", language))
        print(f"🔹 [1] {translate('input_expression', language)}")
        print(f"🔹 [2] {translate('generate_random_expressions', language)}")
        print(f"🔹 [l] {translate('change_language', language)}")
        print(f"🔹 [q] {translate('exit', language)}")
        print()

        choice = input(f"{translate('enter_command', language)}: ").strip().lower()

        if choice == '1':
            expression = input(f"{translate('input_expression', language)}: ").strip()
            if not expression:
                print(Fore.RED + translate("empty_input", language))
                input(translate("press_enter", language))
                continue

            result = is_balanced(expression, language)
            print(f"\n{result}\n")
            log_action(f"Checked expression '{expression}' -> {result}")
            input(translate("press_enter", language))

        elif choice == '2':
            check_random_expressions(language)

        elif choice == 'l':
            language = set_language()
            input(translate("press_enter", language))

        elif choice == 'q':
            print(Fore.GREEN + translate("goodbye", language))
            log_action(translate("goodbye", language))
            break

        else:
            print(Fore.RED + translate("unknown_command", language))
            input(translate("press_enter", language))

if __name__ == "__main__":
    language = set_language()
    main(language)

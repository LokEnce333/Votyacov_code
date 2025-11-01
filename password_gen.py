import random
import string
import re

def generate_password(length, use_lowercase, use_uppercase, use_digits, use_special):
    """Generate a random password based on user preferences."""
    chars = ''
    if use_lowercase:
        chars += string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += '!@#$%^&*()-+'

    if not chars:
        return "Error: No character sets selected."

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def check_password_strength(password):
    """Check password strength and return rating and suggestions."""
    length_ok = len(password) >= 8
    has_lower = bool(re.search(r'[a-z]', password))
    has_upper = bool(re.search(r'[A-Z]', password))
    has_digit = bool(re.search(r'[0-9]', password))
    has_special = bool(re.search(r'[!@#$%^&*()\-+]', password))

    criteria = [length_ok, has_lower, has_upper, has_digit, has_special]
    met_criteria = sum(criteria)

    if met_criteria == 5:
        strength = "Надёжный"
        suggestions = []
    elif met_criteria >= 3:
        strength = "Средний"
        suggestions = []
        if not length_ok:
            suggestions.append("Увеличьте длину до 8 символов или больше.")
        if not has_lower:
            suggestions.append("Добавьте строчные буквы (a-z).")
        if not has_upper:
            suggestions.append("Добавьте заглавные буквы (A-Z).")
        if not has_digit:
            suggestions.append("Добавьте цифры (0-9).")
        if not has_special:
            suggestions.append("Добавьте специальные символы (!@#$%^&*()-+).")
    else:
        strength = "Слабый"
        suggestions = []
        if not length_ok:
            suggestions.append("Увеличьте длину до 8 символов или больше.")
        if not has_lower:
            suggestions.append("Добавьте строчные буквы (a-z).")
        if not has_upper:
            suggestions.append("Добавьте заглавные буквы (A-Z).")
        if not has_digit:
            suggestions.append("Добавьте цифры (0-9).")
        if not has_special:
            suggestions.append("Добавьте специальные символы (!@#$%^&*()-+).")

    return strength, suggestions

def main():
    print("Добро пожаловать в генератор паролей!")
    while True:
        try:
            length = int(input("Введите желаемую длину пароля (минимум 8): "))
            if length < 8:
                print("Длина должна быть не менее 8 символов.")
                continue
        except ValueError:
            print("Пожалуйста, введите число.")
            continue

        print("Выберите символы для использования (y/n):")
        use_lowercase = input("Строчные буквы (a-z)? ").lower() == 'y'
        use_uppercase = input("Заглавные буквы (A-Z)? ").lower() == 'y'
        use_digits = input("Цифры (0-9)? ").lower() == 'y'
        use_special = input("Специальные символы (!@#$%^&*()-+)? ").lower() == 'y'

        password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special)
        if password.startswith("Error"):
            print(password)
            continue

        print(f"Сгенерированный пароль: {password}")

        strength, suggestions = check_password_strength(password)
        print(f"Надёжность: {strength}")

        if suggestions:
            print("Предложения для улучшения:")
            for sug in suggestions:
                print(f"- {sug}")
            regenerate = input("Хотите сгенерировать новый пароль? (y/n): ").lower()
            if regenerate != 'y':
                break
        else:
            print("Пароль соответствует всем критериям безопасности!")
            another = input("Хотите сгенерировать ещё один пароль? (y/n): ").lower()
            if another != 'y':
                break

if __name__ == "__main__":
    main()

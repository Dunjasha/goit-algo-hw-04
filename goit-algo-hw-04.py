# ПЕРШЕ ЗАВДАННЯ
# Створюємо файл із зарплатами
file_path = "salary_file.txt"

data = """Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000"""

with open(file_path, "w", encoding="utf-8") as file:
    file.write(data)

# Функція для підрахунку зарплат
def total_salary(path):
    try:
        with open(path, encoding='utf-8') as file:
            salaries = []
            for line in file:
                try:
                    _, salary = line.strip().split(',')
                    salaries.append(int(salary))
                except ValueError:
                    print(f"Помилка у рядку: {line.strip()}")

            if not salaries:
                return 0, 0
            
            total = sum(salaries)
            average = total / len(salaries)
            return total, average
    
    except FileNotFoundError:
        print("Файл не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Помилка: {e}")
        return 0, 0

# Використовуємо правильний шлях до файлу
path = "salary_file.txt"
total, average = total_salary(path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

# ДРУГЕ ЗАВДАННЯ

# Функція для зчитування інформації про котів
file_path = "cats_file.txt"

data = """60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5"""

with open(file_path, "w", encoding="utf-8") as file:
    file.write(data)

# Функція для зчитування інформації про котів
def get_cats_info(path):
    try:
        with open(path, encoding="utf-8") as file:
            cats = []
            for line in file:
                try:
                    cat_id, name, age = line.strip().split(',')
                    cat_info = {"id": cat_id, "name": name, "age": age}
                    cats.append(cat_info)
                except ValueError:
                    print(f"Помилка у рядку: {line.strip()}")
            
            return cats

    except FileNotFoundError:
        print("Файл не знайдено.")
        return []
    except Exception as e:
        print(f"Помилка: {e}")
        return []


# Використання функції
cats_info = get_cats_info(file_path)
print(cats_info)

# Четверте завдання

def parse_input(user_input): # Ця функція розбирає введену команду.
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def add_contact(args, contacts): # Ця функція додає контакт у словник contacts.
    if len(args) != 2:
        return "Invalid input. Use: add [name] [phone]"
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts): # Ця функція змінює номер телефону у словнику.
    if len(args) != 2:
        return "Invalid input. Use: change [name] [new_phone]"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    return "Contact not found."


def show_phone(args, contacts): # Ця функція виводить номер телефону.
    if len(args) != 1:
        return "Invalid input. Use: phone [name]"
    name = args[0]
    return contacts.get(name, "Contact not found.")


def show_all(contacts): # Ця функція виводить всі контакти
    if not contacts:
        return "No contacts saved."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main(): # Головна функція.
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()

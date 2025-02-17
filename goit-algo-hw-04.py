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

        
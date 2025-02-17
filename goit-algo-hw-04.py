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

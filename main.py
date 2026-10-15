import random
import string

def generate_password(length=12):
    # Визначаємо набір символів: літери (верхній і нижній регістр), цифри та спецсимволи
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Генеруємо пароль за допомогою генератора списків
    password = "".join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("--- Генератор безпечних паролів ---")
    
    try:
        user_input = input("Введіть довжину пароля (натисніть Enter для 12 за замовчуванням): ")
        length = int(user_input) if user_input.strip() else 12
        
        if length < 4:
            print("Попередження: занадто короткий пароль не є безпечним.")
            
        secure_password = generate_password(length)
        print(f"\nВаш новий пароль: {secure_password}")
        
    except ValueError:
        print("Будь ласка, введіть коректне ціле число.")

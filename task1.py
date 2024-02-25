import queue
import time
import random
import threading

# Створення черги заявок
request_queue = queue.Queue()

# Функція для генерації нової заявки (буде діяти 15 секунд)
def generate_request():
    start_time = time.time()
    while time.time() - start_time < 15:
        # Генеруємо унікальний номер заявки
        request_id = random.randint(1, 1000)
        # Додаємо заявку до черги
        request_queue.put(request_id)
        print(f"Заявка {request_id} додана до черги")
        # Затримка перед наступною генерацією заявки
        time.sleep(random.uniform(1, 3))

# Функція для обробки заявки
def process_requests():
    start_time = time.time()
    while time.time() - start_time < 45:  # Обмеження часу виконання до 45 секунд
        if not request_queue.empty():
            # Видаляємо заявку з черги
            request_id = request_queue.get()
            print(f"Заявка {request_id} обробляється")
            # Симуляція обробки заявки
            time.sleep(random.uniform(2, 5))
            print(f"Заявка {request_id} видалена з черги")
        else:
            print("Черга порожня")
            # Затримка перед наступною спробою взяти заявку з черги
            time.sleep(1)

# Запускаємо функцію для генерації заявок у окремому потоці
generate_thread = threading.Thread(target=generate_request)
generate_thread.start()

# Запускаємо функцію для обробки заявок у окремому потоці
process_thread = threading.Thread(target=process_requests)
process_thread.start()

# Очікуємо завершення генерації заявок
generate_thread.join()

# Очікуємо завершення обробки заявок
process_thread.join()

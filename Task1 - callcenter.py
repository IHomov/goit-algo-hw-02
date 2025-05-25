from queue import Queue
import random
import time

def generate_request(queue_user, n):
    queue_user.put(f"Заявка №{n}")
    print(f"Створено заявку: Заявка №{n}")

def process_request(queue_user):
    if not queue_user.empty():
        current_request = queue_user.get()
        print(f"Обробляється: {current_request}")
    else:
        print("Черга порожня")

def main():
    queue_user = Queue()
    n = 0
    
    try:
        while True:
            if random.choice([True, False]):
                n +=1
                generate_request(queue_user, n)
            
            if random.choice([True, False]):
                process_request(queue_user)
                time.sleep(1)
    except KeyboardInterrupt:
        print("Програма завершена користувачем")
            
        
if __name__ == "__main__":
    main()

# Натисни Ctrl + C у терміналі щоб зупинити виконання програми    

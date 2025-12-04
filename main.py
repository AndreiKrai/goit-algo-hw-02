from queue import Queue
import time 

# Створити чергу заявок

def generate_request(queue):
    application = str(int(time.time()*1000))  # Унікальний ідентифікатор заявки на основі часу
    queue.put(application)

def process_request(queue):
    if not queue.empty():
        request = queue.get()
        print(f"Processing request: {request}")
    else:
        print("Queue is empty")

def main():
    queue = Queue()
    try:
        while True:
            generate_request(queue)
            process_request(queue)
            time.sleep(1)  # Затримка 1 секунда для читаємості
    except KeyboardInterrupt:
        print("\nProgram closed.")


if __name__ == "__main__":
    main()

import queue
import random

request_queue = queue.Queue()

def generate_request():
    user_input = input("\nPlease select a subject of your request or press exit: ").lower()
    if user_input == "exit":
        return user_input
    new_request = {"id": random.randint(1, 10), "subject": user_input}
    request_queue.put(new_request)
    print(f"\n The request {new_request} is registered")
    print("\n Queue: ", list(request_queue.queue))
   
def process_request():
    if not request_queue.empty():
        del_request = request_queue.get()
        print(f"\n The request {del_request} is proceeded")
        print("\n Queue: ", list(request_queue.queue))
    else:
        print("The queue is empty")

def main():

    # adding a few requests to the queue before running our main loop to demostrate the queue logic
    request_queue.put({'id': 0, 'subject': 'My first request'})
    request_queue.put({'id': 1, 'subject': 'My second request'})

    while True:
        user_input = generate_request()
        if user_input == "exit":
            break
        process_request()

if __name__ == "__main__":
    main()
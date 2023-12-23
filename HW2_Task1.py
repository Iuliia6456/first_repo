import queue
import uuid
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

request_queue = queue.Queue()

def generate_request():
    user_input = input("Please select a subject of your request or press 'exit' to end: ").lower()
    if user_input == "exit":
        return user_input

    new_request = {"id": str(uuid.uuid4()), "subject": user_input}
    request_queue.put(new_request)
    logging.info(f"\nThe request {new_request} is registered\n")
    logging.info("Queue: %s\n", list(request_queue.queue))

def process_request():
    if not request_queue.empty():
        del_request = request_queue.get()
        logging.info(f"The request {del_request} is executed\n")
        logging.info("Updated queue after executed request: %s\n", list(request_queue.queue))
    else:
        logging.info("The queue is empty")

def main():
    # adding a few requests to the queue before running our main loop to demonstrate the queue logic
    request_queue.put({'id': str(uuid.uuid4()), 'subject': 'My first request'})
    request_queue.put({'id': str(uuid.uuid4()), 'subject': 'My second request'})

    try:
        while True:
            generate_request()
            process_request()
    except KeyboardInterrupt:
        logging.info("\nProgram finished\n")

if __name__ == "__main__":
    main()

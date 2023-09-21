import threading

def task():
    pass
    # Code for the task to be executed concurrently

# Create multiple threads
thread1 = threading.Thread(target=task)
thread2 = threading.Thread(target=task)

# Start the threads
thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()

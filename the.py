import threading  # Import threading module to create threads

# Define a function that performs addition
def add():
    print("Thread 1: Starting addition")
    result = 5 + 3  # Simple addition
    print(f"Thread 1: Result of addition = {result}")

# Define a function that performs subtraction
def subtract():
    print("Thread 2: Starting subtraction")
    result = 10 - 4  # Simple subtraction
    print(f"Thread 2: Result of subtraction = {result}")

# Main part of the program
def main():
    # Create two threads and assign the functions
    t1 = threading.Thread(target=add)       # Thread for addition
    t2 = threading.Thread(target=subtract)  # Thread for subtraction

    # Start the threads
    t1.start()
    t2.start()

    # Wait for both threads to complete
    t1.join()
    t2.join()

    print("Both threads have finished.")

# Run the program
if __name__ == "__main__":
    main()

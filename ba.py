# Importing input method
# This lets us take input from the user
import sys

# Ask for number of processes
n = int(input("Enter number of processes: "))

# Create process list [0, 1, 2, ..., n-1]
processes = list(range(n))

# All processes are initially alive (1 = alive, 0 = crashed)
status = [1] * n

# Initial coordinator is the last (highest) process
coordinator = n - 1

# Function to simulate Bully Election
def elect(initiator):
    global coordinator
    print(f"\nProcess {initiator+1} initiates election.")
    coordinator = initiator

    for i in range(initiator+1, n):  # send to higher processes only
        print(f"Election message sent from {initiator+1} to {i+1}")
        if status[i] == 1:  # If the higher process is alive
            print(f"OK message received from {i+1} to {initiator+1}")
            elect(i)  # That process takes over the election
            return

    # If no higher alive process found, initiator becomes coordinator
    print(f"Process {initiator+1} becomes coordinator.")
    coordinator = initiator

# Menu Loop
while True:
    print("\nMENU")
    print("1. Crash a process")
    print("2. Recover a process")
    print("3. Start election")
    print("4. Exit")
    choice = int(input("> "))

    if choice == 1:
        p = int(input("Enter process to crash: ")) - 1
        status[p] = 0
        print(f"Process {p+1} crashed.")
    elif choice == 2:
        p = int(input("Enter process to recover: ")) - 1
        status[p] = 1
        print(f"Process {p+1} recovered.")
    elif choice == 3:
        ele = int(input("Which process initiates election? ")) - 1
        if status[ele] == 1:
            elect(ele)
        else:
            print("This process is crashed. Cannot start election.")
        print(f"Current Coordinator is: Process {coordinator+1}")
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice.")

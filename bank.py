# Function to check if system is in safe state
def is_safe(processes, available, max_demand, allocation):
    # Number of processes
    n = len(processes)
    # Number of resources
    m = len(available)

    # Calculate the need matrix = max - allocation
    need = [[max_demand[i][j] - allocation[i][j] for j in range(m)] for i in range(n)]

    # Finish list to track which processes are completed
    finish = [False] * n
    # Work represents current available resources
    work = available.copy()
    # To store the safe sequence
    safe_sequence = []

    # Repeat until all processes are finished
    while len(safe_sequence) < n:
        found = False
        # Try to find a process that can complete
        for i in range(n):
            if not finish[i]:
                # Check if current process's need can be satisfied
                if all(need[i][j] <= work[j] for j in range(m)):
                    # If yes, simulate finishing the process
                    for j in range(m):
                        work[j] += allocation[i][j]  # Release resources
                    finish[i] = True
                    safe_sequence.append(processes[i])
                    print(f"Process {processes[i]} has completed.")
                    found = True
        if not found:
            # If no process can complete, system is unsafe
            print("System is in an unsafe state. Deadlock may occur.")
            return False

    # If all processes finished
    print("System is in a safe state. No deadlock detected.")
    print("Safe sequence:", safe_sequence)
    return True

# Main code
def main():
    # Take number of processes and resources as input
    n = int(input("Enter number of processes: "))
    m = int(input("Enter number of resources: "))

    # Process identifiers (P0, P1, ...)
    processes = [f'P{i}' for i in range(n)]

    # Input max matrix
    print("Enter the Max matrix:")
    max_demand = [list(map(int, input(f"Max for P{i}: ").split())) for i in range(n)]

    # Input allocation matrix
    print("Enter the Allocation matrix:")
    allocation = [list(map(int, input(f"Allocation for P{i}: ").split())) for i in range(n)]

    # Input available resources
    available = list(map(int, input("Enter available resources: ").split()))

    # Run the safety check
    is_safe(processes, available, max_demand, allocation)

# Run the program
if __name__ == "__main__":
    main()

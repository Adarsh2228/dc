def print_load(servers, processes):
    each = processes // servers
    extra = processes % servers
    
    for i in range(extra):
        print(f"Server {i + 1} has {each + 1} Processes")
    
    for i in range(extra, servers):
        print(f"Server {i + 1} has {each} Processes")

def main():
    servers = int(input("Enter the number of Servers: "))
    processes = int(input("Enter the number of Processes: "))
    
    while True:
        print_load(servers, processes)
        print("\n1. Add Servers  2. Remove Server  3. Add Processes  4. Remove Processes  5. Exit ")
        choice = int(input("> "))
        
        if choice == 1:
            add_servers = int(input("How many more servers to add? "))
            servers += add_servers
        elif choice == 2:
            remove_servers = int(input("How many servers to remove? "))
            servers -= remove_servers
        elif choice == 3:
            add_processes = int(input("How many more processes to add? "))
            processes += add_processes
        elif choice == 4:
            remove_processes = int(input("How many processes to remove? "))
            processes -= remove_processes
        elif choice == 5:
            break

if __name__ == "__main__":
    main()


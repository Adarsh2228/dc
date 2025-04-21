# Define a class for each node in the system
class Node:
    # Each node is initialized with an ID and a local clock time
    def __init__(self, node_id, clock_time):
        self.id = node_id
        self.clock = clock_time

    # Function to adjust the clock
    def adjust_clock(self, offset):
        self.clock += offset

    # Function to return the clock time
    def get_time(self):
        return self.clock


# Main function to simulate Berkeley Algorithm
def main():
    # Ask the user for number of nodes
    n = int(input("Enter number of nodes (including master): "))

    nodes = []

    # Take input for each node's clock time
    for i in range(n):
        time = int(input(f"Enter clock time for Node {i} (in seconds): "))
        node = Node(i, time)
        nodes.append(node)

    # Assume the first node is the master (Node 0)
    master = nodes[0]

    print("\nMaster collecting times from all nodes...")
    total_time = 0

    # Collect times from all nodes
    for node in nodes:
        total_time += node.get_time()
        print(f"Node {node.id} time: {node.get_time()}")

    # Calculate average time
    average_time = total_time // n
    print(f"\nCalculated average time: {average_time}")

    # Master sends offset to all nodes
    print("\nSending time adjustments to all nodes...")
    for node in nodes:
        offset = average_time - node.get_time()
        node.adjust_clock(offset)
        print(f"Node {node.id} adjusted by {offset} seconds → New time: {node.get_time()}")


# Run the program
if __name__ == "__main__":
    main()

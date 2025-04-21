# Define a class to represent a node in the distributed system
class Node:
    # Each node is initialized with an ID and a local value
    def __init__(self, node_id, local_value):
        self.node_id = node_id
        self.local_value = local_value

    # This function lets the node share its value
    def share_value(self):
        return self.local_value


# Main function that simulates global averaging
def main():
    # Ask how many nodes are in the system
    num_nodes = int(input("Enter number of nodes: "))

    # Create a list to hold all node objects
    nodes = []

    # Ask for each node's local value (e.g., temperature, average loss, etc.)
    for i in range(num_nodes):
        value = float(input(f"Enter value for Node {i + 1}: "))
        node = Node(i, value)  # Create a node with the given value
        nodes.append(node)     # Add the node to the list

    # Collect all values from nodes by asking them to share
    total = 0
    for node in nodes:
        total += node.share_value()  # Add each node's value to the total

    # Compute the global average
    global_average = total / num_nodes

    # Print the result
    print(f"\nGlobal average from all {num_nodes} nodes is: {global_average:.2f}")


# Run the program
if __name__ == "__main__":
    main()

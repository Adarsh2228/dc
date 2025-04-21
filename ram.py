# Define a class for each node
class Node:
    def __init__(self, node_id):
        # Unique ID for the node
        self.id = node_id
        # Clock value for timestamp
        self.clock = 0
        # Whether this node is in critical section
        self.requesting = False
        # Timestamp of its own request
        self.request_time = None
        # Number of replies received
        self.replies = 0
        # Reference to all other nodes
        self.network = []

    # Set the network (list of all nodes)
    def set_network(self, nodes):
        self.network = nodes

    # Function to request critical section
    def request_cs(self):
        self.clock += 1  # Increment logical clock
        self.requesting = True
        self.request_time = self.clock
        self.replies = 0

        print(f"\nNode {self.id} is requesting CS at time {self.request_time}")
        
        # Send request to all other nodes
        for node in self.network:
            if node.id != self.id:
                node.receive_request(self.id, self.request_time)

    # Function to receive a request from another node
    def receive_request(self, sender_id, timestamp):
        self.clock = max(self.clock, timestamp) + 1  # Update clock

        # Decide whether to send reply immediately
        if not self.requesting or (self.request_time, self.id) > (timestamp, sender_id):
            print(f"Node {self.id} sends REPLY to Node {sender_id}")
            self.network[sender_id].receive_reply()
        else:
            print(f"Node {self.id} delays REPLY to Node {sender_id} (waiting for its own CS)")

    # Function to receive a reply
    def receive_reply(self):
        self.replies += 1
        # If replies from all others are received, enter CS
        if self.replies == len(self.network) - 1:
            self.enter_cs()

    # Enter critical section
    def enter_cs(self):
        print(f"Node {self.id} ENTERS Critical Section")

        # Simulate doing work
        print(f"Node {self.id} is working in CS...")

        # Exit CS after work
        self.exit_cs()

    # Exit critical section
    def exit_cs(self):
        print(f"Node {self.id} EXITS Critical Section")
        self.requesting = False
        self.request_time = None


# Main function to simulate Ricart-Agrawala
def main():
    # Create nodes
    n = int(input("Enter number of nodes: "))
    nodes = [Node(i) for i in range(n)]

    # Set the network for each node
    for node in nodes:
        node.set_network(nodes)

    # Ask which node wants to request CS
    requester = int(input("Enter the ID of the node requesting CS: "))
    if 0 <= requester < n:
        nodes[requester].request_cs()
    else:
        print("Invalid node ID")


# Run the program
if __name__ == "__main__":
    main()

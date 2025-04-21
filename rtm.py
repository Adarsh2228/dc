# Import required modules
from collections import deque

# Define a class for each Node in the network
class Node:
    # Constructor for the Node class
    def __init__(self, node_id, has_token, holder):
        # Node's unique ID
        self.id = node_id
        # Whether this node currently has the token
        self.has_token = has_token
        # ID of the node currently holding the token
        self.holder = holder
        # Queue to store token requests
        self.request_queue = deque()
        # Dictionary to reference all nodes in the network
        self.network = {}

    # Set the reference to the full network
    def set_network(self, network):
        self.network = network

    # Method to request the token
    def request_token(self):
        print(f"Node {self.id} requests the token.")

        # If node already has token, it can enter critical section
        if self.has_token:
            self.enter_critical_section()
            return

        # Add self to the request queue
        self.request_queue.append(self.id)

        # If it's the first request and not the holder, send a request to holder
        if len(self.request_queue) == 1 and self.holder != self.id:
            self.send_request_to_holder()

    # Send a request to the node that currently holds the token
    def send_request_to_holder(self):
        print(f"Node {self.id} forwards request to Node {self.holder}")
        holder_node = self.network[self.holder]
        holder_node.receive_token_from(self.id)

    # Receive token from another node
    def receive_token_from(self, requester_id):
        self.has_token = True
        self.holder = self.id
        print(f"Node {self.id} received the token!")

        # If the node is the requester
        if self.request_queue:
            next_id = self.request_queue.popleft()
            if next_id == self.id:
                self.enter_critical_section()
            else:
                self.send_token(next_id)
        else:
            # If requester is someone else, pass it
            if requester_id != self.id:
                self.send_token(requester_id)

    # Pass the token to another node
    def send_token(self, next_holder):
        self.has_token = False
        self.holder = next_holder
        print(f"Node {self.id} sends token to Node {next_holder}")
        next_node = self.network[next_holder]
        next_node.receive_token_from(self.id)

    # Enter critical section
    def enter_critical_section(self):
        print(f"Node {self.id} enters the Critical Section!")
        self.has_token = False
        if self.request_queue:
            next_id = self.request_queue.popleft()
            self.send_token(next_id)


# Main function to simulate the system
def main():
    network = {}

    # Take input for number of nodes
    n = int(input("Enter number of nodes: "))

    # Create each node and set up the token holder
    for i in range(n):
        parent = int(input(f"Enter parent (holder) for node {i} (-1 if root): "))
        has_token = (parent == -1)
        holder = i if has_token else parent
        node = Node(i, has_token, holder)
        network[i] = node

    # Provide each node access to the full network
    for node in network.values():
        node.set_network(network)

    # Simulate token requests
    r = int(input("Enter number of token requests: "))
    for i in range(r):
        requester_id = int(input(f"Enter node ID making request {i+1}: "))
        if requester_id in network:
            network[requester_id].request_token()
        else:
            print("Invalid node ID.")

# Run the main function
if __name__ == "__main__":
    main()

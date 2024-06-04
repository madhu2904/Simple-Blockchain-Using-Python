import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

    def __repr__(self):
        return f"Block(index={self.index}, previous_hash={self.previous_hash}, timestamp={self.timestamp}, data={self.data}, hash={self.hash})"

def create_genesis_block():
    timestamp = time.time()
    return Block(0, "0", timestamp, "Genesis Block", calculate_hash("0", timestamp, "Genesis Block"))

def calculate_hash(previous_hash, timestamp, data):
    value = str(previous_hash) + str(timestamp) + str(data)
    return hashlib.sha256(value.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [create_genesis_block()]

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        previous_block = self.get_latest_block()
        new_index = previous_block.index + 1
        new_timestamp = time.time()
        new_hash = calculate_hash(previous_block.hash, new_timestamp, data)
        new_block = Block(new_index, previous_block.hash, new_timestamp, data, new_hash)
        self.chain.append(new_block)

    def __repr__(self):
        return "Blockchain:\n" + "\n".join([str(block) for block in self.chain])

# Create blockchain and add blocks
blockchain = Blockchain()
blockchain.add_block("First Block")
#blockchain.add_block("Second Block")
blockchain.add_block("Third Block")

print(blockchain)

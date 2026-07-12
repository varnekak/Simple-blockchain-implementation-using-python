#what is blockchain?
#Remember that a blockchain is an immutable, sequential chain of records called Blocks. They can contain transactions, files or any data you like, really. But the important thing is that they’re chained together using hashes. 
import hashlib
import json
from time import time    


class Blockchain(object): #class is responsible for managing the chain. It will store transactions and have some helper methods for adding new blocks to the chain
    def __init__(self):
       self.chain =[]
       self.current_transactions =[]

       # Create the genesis block 
       self.new_block(previous_hash=1, proof=100)
     
    def new_block(self, proof, previous_hash=None):
        #creates a new block and adds it to the chain
         """
        Create a new Block in the Blockchain
        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash: (Optional) <str> Hash of previous Block
        :return: <dict> New Block
        """
        block = {
             'index': len(self.chain)+1,
             'timestamp': time(),
             'transactions': self.current_transactions,
             'proof': proof,
             'previous_hash': previous_ha
         }
        # reset the current lists of transactions
        self.current_transaction = []
        self.chain.append(block)
        return block 
    
    def new_transaction(self,sender, recipient, amount):
        #adds a new transaction to the list of transactions 
        """Creates a new transaction to go into the next mined block
        :param sender: <str> Address of the Sender
       :param recipient: <str> Address of the Recipient
       :param amount: <int> Amount
       :return: <int> The index of the Block that will hold this transaction"""
        self.current_transactions.append({
            'sender':sender,    
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1 
    
    def proof_of_work(self, last_proof):
        
    @staticmethod
    def hash(block):
        #Hashes a block 
         """
        Creates a SHA-256 hash of a Block
        :param block: <dict> Block
        :return: <str>
        """
    
    @property 
    def last_block(self):
        #returns the last block in the chain 
       return self.chain[-1]
  """At this point, the idea of a chain should be apparent—each new block contains within itself,
    the hash of the previous Block.
 This is crucial because it’s what gives blockchains immutability: If an attacker corrupted an earlier Block in the chain 
 then all subsequent blocks will contain incorrect hashes."""
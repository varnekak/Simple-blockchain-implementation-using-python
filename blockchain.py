#what is blockchain?
#Remember that a blockchain is an immutable, sequential chain of records called Blocks. They can contain transactions, files or any data you like, really. But the important thing is that they’re chained together using hashes. 
import hashlib
import json
from time import time 
from textwrap import dedent 
from uuid import uuid4
from flask import Flask,jsonify, request   #Flask is just a Python library that makes creating servers easy.


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
                then all subsequent blocks will contain incorrect hashes.
            """

            """ 
                       proof of work A Proof of Work algorithm (PoW) is how new Blocks are created or mined on the blockchain.
                        The goal of PoW is to discover a number which solves a problem. 
                        The number must be difficult to find but easy to verify—computationally speaking—by anyone on the network. 
                         This is the core idea behind Proof of Work.
            """
    def proof_of_work(self, last_proof):
    """
     Simple Proof of Work Algorithm:
         - Find a number p' such that hash(pp') contains leading 4 zeroes, where p is the previous p'
         - p is the previous proof, and p' is the new proof
        :param last_proof: <int>
        :return: <int>
    """
       proof = 0 
       while self.valid_proof(last_proof, proof) is False:#keep looking while the proof is NOTVALID
           proof += 1 
        return proof 
    
    @staticmethod
    def valid_proof(last_proof, proof):
        """
          Validates the Proof: Does hash(last_proof, proof) contain 4 leading zeroes?
        :param last_proof: <int> Previous Proof
        :param proof: <int> Current Proof
        :return: <bool> True if correct, False if not.
        
        """
        guess = f'{last_proof}{proof}'.encode()
        # we combine not sum the lastproof and current proof as a string and
        # and convert them to bytes because SHA-256 cannot hash a normal string hence we use encode 
        guess_hash = hashlib.sha256(guess).hexadigest()
        # hexadigest returns the result as a readable hexadecimal 
        return guess_hash[:4] == "0000"
        # checks if the first 4 digits start with 0000
# Instantiate our node 
app = Flask(__name__) # creates a flask application 

# Generate a globbaly unique address for this node 
node_identifier = str(uuid4()).replace('-','')

# intantiate the blockchain 
blockchain =  Blockchain()

@app.route('/mine', methods = ['GET '])
def mine():
    # we run the proof of work algorithms to get the next proof
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    # we  must recive a reward for finding the proof
    # the sender is "0" to signify that this node has mined a new coin

    blockchain.new_transaction(
        sender = "0",
        recipient = node_identifier,
        amount = 1,
    )
    # forge the new block by adding it to the chain
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'message': "New Block Forged "
    }

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()
    # check the required field 
    required = ['sender','recipient','amount']
    if not all (k in values for k in required):
        return 'Missing values',400
    #create a new transaction 
    index = Blockchain.new_transaction(values['sender'], values['recepient'], values['amount'])
    response = {'mesage': f'Transaction will be added to block {index}'}
    return jsonify(response),201

@app.route('/chain', methods =['GET'])
def full_chain():
    response = {
        'chain': Blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response),200
if __name__ == 'main':
    app.run(host = '0.0.0.0',port=5000)
import hashlib
import json
from time import time 
from uuid import uuid4
from flask import Flask,jsonify, request
from textwrap import dedent





class Blockchain(object):
    def __init__(self):
        self.chain = [] 
        #stores ur blockchain
        self.current_transactions = [] 
        # temporary storage for transactions before they are added to a block
        #Transactions are NOT immediately added to the blockchain.They first wait in memory.Mining collects them into a new block.
        self.new_block(previous_hash = 1, proof = 100 ) 
        # create the genesis block
        # genesis block has no previous block, it is the first block
        # because no previous vlaues exist for genesis block we use a dummy value which is 1

    def new_block(self, proof, previous_hash = None):
          """
        Create a new Block in the Blockchain
        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash: (Optional) <str> Hash of previous Block
        :return: <dict> New Block
        """
          
        block = {
             'index': len(self.chain)+1, # block number 
             'timestamp': time(), # creation time
             'transactions': self.current_transactions, #stored transactions
             'proof': proof, # mining solution
             'previous_hash': previous_hash or self.hash(self.chain[-1]),#connects chain
        }
        #creates a new block and adds it to the chain pass 
        
        self.current_transactions = []
        # reset the current list of transactions otherwise old transactions repeat forever
        self.chain.append(block)
        return block


    def new_transactions(self, sender, recipient, amount):
        # adds a new transaction to the list of transactions pass 
           """
        Creates a new transaction to go into the next mined Block
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
        """
        self.current_transactios.append({
              'sender':sender,
              'recipient': recipient,
              'amount': amount,
         })
        return self.last_block['index']+1 # we return the last block because transactions are not mined 
    
    @staticmethod 
    def hash(block):
        # Hashing converts data into a fixed-size string.
        # hashes a block 
        """
        Creates a SHA-256 hash of a Block
        :param block: <dict> Block
        :return: <str>
        """
        
        # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        # returns the last block in the chain
        return self.chain[-1]
    
    def proof_of_work(self, last_proof):
           """
        Simple Proof of Work Algorithm:
         - Find a number p' such that hash(pp') contains leading 4 zeroes, where p is the previous p'
         - p is the previous proof, and p' is the new proof
        :param last_proof: <int>
        :return: <int>
        """
         proof =0
         while self.valid_proof(last_proof, proof) is False:
              proof +=1
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
         guess_hash =  hashlib.sha256(guess).hexdigest()
         return guess_hash[:4] == "0000"
    
    # instatiate our Node
app = Flask(__name__)

# generate a globallay unique adress for this node 
node_identifier= str(uuid4()).replace('-','')

# instantiate a Blockchain
blockchain =  Blockchain()

@app.route('/mine',methods=['GET'])
def mine():
     return "We ll mine a new block"


@app.route('/chain', methods=['GET'])
def full_chain():
     response = {
          'chain': blockchain.chain,
          'length': len(blockchain.chain)
     }#dictionary
     return jsonify(response), 200

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000)

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
     values = request.get_json()

     required=['sender','recipient','amount']
     if not all(k in values for k in required):
          return 'Missing values', 400
     
     index = blockchain.new_transaction(
          values['sender'],
          values['recipient'],
          values['amount']
     )
     response = {
          'message': f'Transactions added to Block {index}'
     }

     return jsonify(response),201

@app.route('/mine', methods=['GET'])
def mine():
      # We run the proof of work algorithm to get the next proof...
     last_block = blockchain.last_block
     last_proof = last_block['proof']

     proof = blockchain.proof_of_work(last_proof)

      # We must receive a reward for finding the proof.
    # The sender is "0" to signify that this node has mined a new coin.

    blockchain.new_transaction(
         sender="0",
         recipient=node_identifier,
         amount=1,
    )
   # Forge the new Block by adding it to the chain

   response = {
        'message':"New Block Forged",
        'index':block['index'],
        'transactions': block['transactions'],
        'proof':block['proof'],
        'previous_hash': block['previous_hash'],
   }
    return jsonify(response), 200
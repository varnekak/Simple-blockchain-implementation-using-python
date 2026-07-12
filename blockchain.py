#what is blockchain?
#Remember that a blockchain is an immutable, sequential chain of records called Blocks. They can contain transactions, files or any data you like, really. But the important thing is that they’re chained together using hashes. 
class Blockchain(object): #class is responsible for managing the chain. It will store transactions and have some helper methods for adding new blocks to the chain
    def __init__(self):
       self.chain =[]
       self.current_transactions =[]
     
    def new_block(self):
        #creates a new block and adds it to the chain
        pass
    
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
    
    @staticmethod
    def hash(block):
        #Hashes a block 
        pass
    
    @property 
    def last_block(self):
        #returns the last block in the chain 
        pass 
  """At this point, the idea of a chain should be apparent—each new block contains within itself,
    the hash of the previous Block.
 This is crucial because it’s what gives blockchains immutability: If an attacker corrupted an earlier Block in the chain 
 then all subsequent blocks will contain incorrect hashes."""
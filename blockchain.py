#what is blockchain?
#Remember that a blockchain is an immutable, sequential chain of records called Blocks. They can contain transactions, files or any data you like, really. But the important thing is that they’re chained together using hashes. 
class Blockchain(object): #class is responsible for managing the chain. It will store transactions and have some helper methods for adding new blocks to the chain
    def __init__(self):
       self.chain =[]
       self.current_transactions =[]
     
     def new_block(self):
        #creates a new block and adds it to the chain
        pass
    
    def new_transaction(self):
        #adds a new transaction to the list of transactions 
        pass
    
    @staticmethod
    def hash(block):
        #Hashes a block 
        pass
class Blockchain(object):
    def __init__(self):
        self.chain = [] #stores ur blockchain
        self.current_transactions = [] #to store transactions

    def new_block(self):
        #creates a new block and adds it to the chain pass 


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
        return self.last_block['index']+1
    
    @staticmethod 
    def hash(block):
        # hashes a block 
        pass 

    @property
    def last_block(self):
        # returns the last blocj in the chain
        pass 

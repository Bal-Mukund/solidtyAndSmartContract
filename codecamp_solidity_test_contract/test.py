from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/b2d226b0e24449919afca162bb86dc2d'))

print(w3.isConnected())
print(w3.eth.chain_id)
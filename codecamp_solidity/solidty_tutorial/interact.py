from deploy import compiled_sol
import os
from web3 import Web3

abi = compiled_sol["contracts"]["sharedWallet.sol"]["SharedWallet"]["abi"]
private_key = os.environ.get('PRIVATE_KEY')
contract_address = "0xBB013603D65DAE0aB870fD5b547129407ba884db"

w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))

contract_obj = w3.eth.contract(address=contract_address,abi= abi)

balance = contract_obj.functions.getBalance().call()
print(balance)
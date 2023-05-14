from solcx import compile_standard
import json
from web3 import Web3
import os

#opening the file and storing it in a variable
with open("./sharedWallet.sol", "r") as file:
    shareWallet = file.read()

#compiling the opened file using solcx library
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"sharedWallet.sol": {"content": shareWallet}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                }
            }
        },
    },
    solc_version="0.8.0",
)

# storing the json output in a file
with open("compiled_Code.json", "w") as file:
    json.dump(compiled_sol, file)

# to get evm bytecode object
bytecode = compiled_sol["contracts"]["sharedWallet.sol"]["SharedWallet"]["evm"]["bytecode"]["object"]

#to get abi array
abi = compiled_sol["contracts"]["sharedWallet.sol"]["SharedWallet"]["abi"]

# connecting to ganache blockchain provider
connection_url = "HTTP://127.0.0.1:7545"
network_id = "5777"
account_address = "0x8ebAfd70A543755407E5E9d48496C123f21b8AB5"
private_key = os.environ.get('PRIVATE_KEY')

w3 = Web3(Web3.HTTPProvider(connection_url))

#getting the nonce value
nonce = w3.eth.get_transaction_count(account_address)

# creating contract object
contract_obj = w3.eth.contract(abi= abi, bytecode= bytecode)

# 1. Build a Transaction 
# 2. sign a Transaction
# 3. send a Transaction

#buildig a Transaction
transaction_obj = contract_obj.constructor().build_transaction({
    "gasPrice": w3.eth.gas_price,"chainId": w3.eth.chain_id,"from":account_address,"nonce":nonce})

# signing a raw Transaction
signed_transaction = w3.eth.account.sign_transaction(transaction_obj,private_key= private_key)

# sending a transaction
tran_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
# print("deploying contract...")

# wait for transaction to be mined
mined_hash = w3.eth.wait_for_transaction_receipt(tran_hash)
# print("contract Deployed !")

# interacting with a contractS
# 1. address of the contract 
# 2. the abi of the contract

shareWallet = w3.eth.contract(address=mined_hash.contractAddress,abi= abi)


























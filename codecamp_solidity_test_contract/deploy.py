from solcx import compile_standard
import json
from web3 import Web3
import os
from dotenv import load_dotenv


load_dotenv()
with open("./test.sol", "r") as file:
    content = file.read()


compiled_content = compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"test.sol": {"content": content}},
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

with open("./interact.json", "w") as file:
    json.dump(compiled_content,file)

abi = compiled_content["contracts"]["test.sol"]["Test"]["abi"]
bytecode = compiled_content["contracts"]["test.sol"]["Test"]["evm"]["bytecode"]["object"]


#********************************************************************************************************
#connecting to the blockchain
w3 = Web3(Web3.HTTPProvider("https://goerli.infura.io/v3/b2d226b0e24449919afca162bb86dc2d"))


# all 4 items for building a transaction object and 1. signign the transaction
account_address = os.environ.get('account-address')
chain_id = w3.eth.chain_id
nonce = w3.eth.get_transaction_count(account_address)
gas_price = w3.eth.gas_price
private_key = os.environ.get('private-key')

# 1. building contract object
contract_object = w3.eth.contract(abi= abi, bytecode= bytecode)

# gasPrice not gas_price 
# chainId not chain_id
# 2. converting to contract object just like transactin object
transaction_object = contract_object.constructor().build_transaction({
    "gasPrice": gas_price, "chainId": chain_id, "from": account_address, "nonce": nonce
})

# signing the transaction
transaction_signature = w3.eth.account.sign_transaction(transaction_object,private_key= private_key)

print("contract deploying ...")
# delploying the contract or sending the transaction
hash = w3.eth.send_raw_transaction(transaction_signature.rawTransaction)

# getting a receipt after delpoying 
receipt = w3.eth.wait_for_transaction_receipt(hash)
print("contract deployed!")

# ****************************************************************************************************
# interacting with the deployed contract as contract object
deployed_contract = w3.eth.contract(address=receipt.contractAddress, abi= abi)

print("previous value")
number = deployed_contract.functions.get_number().call()
print(number)

# transacting for state change
# setter function set_number()
transaction_object = deployed_contract.functions.set_number(555).buildTransaction({
    "gasPrice": gas_price, "chainId": chain_id, "from": account_address, "nonce": nonce + 1
    })

signature = w3.eth.account.sign_transaction(transaction_object, private_key= private_key)

hash = w3.eth.send_raw_transaction(signature.rawTransaction)
receipt = w3.eth.wait_for_transaction_receipt(hash)

# getter function get_number()
number = deployed_contract.functions.get_number().call()
print(number)
print("updated value")
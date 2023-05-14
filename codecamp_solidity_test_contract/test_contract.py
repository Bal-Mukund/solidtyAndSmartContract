from web3 import Web3
import json
import os

with open("./interact.json", "r") as file:
    data = json.load(file)
    abi = data["contracts"]["test.sol"]["Test"]["abi"]


contract_address = "0xa99bd6147b87cc56c7ab2a7461ed0ff941d714c4"

w3 = Web3(Web3.HTTPProvider("https://goerli.infura.io/v3/b2d226b0e24449919afca162bb86dc2d"))
check_sum_contract_address = w3.toChecksumAddress(contract_address)
# account_address = os.environ.get('account-address')
chain_id = w3.eth.chain_id
nonce = w3.eth.get_transaction_count(check_sum_contract_address)
gas_price = w3.eth.gas_price
private_key = os.environ.get('private-key')

deployed_contract = w3.eth.contract(address= check_sum_contract_address, abi= abi)

number = deployed_contract.functions.get_number().call()
print(number)

transaction_object = deployed_contract.functions.set_number(67).buildTransaction({
    "gasPrice": gas_price, "chainId": chain_id, 
    "from": check_sum_contract_address, "nonce": nonce
}) 

signed_signature = w3.eth.account.sign_transaction(transaction_object, private_key= private_key)

hash = w3.eth.send_raw_transaction(signed_signature.rawTransaction)
receipt = w3.eth.wait_for_transaction_receipt(hash)

# transaction_object = deployed_contract.functions.set_number(5).buildTransaction({
#     "gasPrice": gas_price, "chainId": chain_id, "from": check_sum_contract_address, "nonce": nonce
#     })

# signature = w3.eth.account.sign_transaction(transaction_object, private_key= private_key)

# hash = w3.eth.send_raw_transaction(signature.rawTransaction)
# receipt = w3.eth.wait_for_transaction_receipt(hash)

number = deployed_contract.functions.get_number().call()
print(number)

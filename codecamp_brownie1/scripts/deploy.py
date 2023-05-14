from brownie import accounts, simpleStorage, config

def acc() :
    account = accounts.add(config["wallets"]["from_key"])
    print(f"contract deploying ...  from {account}")
    
    contract_object = simpleStorage.deploy({"from": account})
    print("contract deployed !")
    
    number = contract_object.get_number()
    print(f"previous number is {number}")

    hash = contract_object.set_number(555, {"from": account})
    hash.wait(1)

    number = contract_object.get_number()
    print(f"updated number is {number}")
    
def main():
    acc()

if __name__ == '__main__':
    main()
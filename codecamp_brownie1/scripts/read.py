from brownie import accounts, simpleStorage, config

def main():
    read_contract()

def read_contract():
    simple_contract = simpleStorage[-1]
    print(simple_contract.get_number())
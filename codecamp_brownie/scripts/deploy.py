from brownie import accounts, simple_storage
import os

def acc() :
    account = accounts.add(os.getenv('private_key'))
    print(simple_storage)
    
    
    # hash = simple_storage.deploy({"from": account})
    # hash.wait(1)
    # print(hash)

def main():
    acc()
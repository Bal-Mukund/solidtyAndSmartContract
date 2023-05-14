from brownie import accounts, FundMe, config

def main():
    deploo()

def deploo():
    account = accounts.add(config['wallets']['from_key'])
    print(f"your account address is {account}")
    print("contract deploying ...")
    tx = FundMe.deploy({"from":account}, publish_source= True)
    print("contract deployed!")
    print(tx)




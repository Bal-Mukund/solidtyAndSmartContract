from brownie import accounts, simpleStorage

def main():
    test_acc()
    test_find()
    test_update()


def test_acc():
    # Arrange 
    
    global account
    account = accounts[0]

    # Act & Assert
    global contract_object
    contract_object = simpleStorage.deploy({"from": account})
    assert contract_object != None

def test_find():
    assert contract_object.get_number() == 0

def test_update():
    hash = contract_object.set_number(55, {"from": account})
    hash.wait(1)

    assert contract_object.get_number() == 55


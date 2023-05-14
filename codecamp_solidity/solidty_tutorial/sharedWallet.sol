// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;


contract SharedWallet {
    address public owner;
    uint internal  totalBalance = address(this).balance;
    mapping(address => uint) public children;

    constructor () public {
        owner = msg.sender; 
    }

    modifier onlyOwner () {
        require(msg.sender == owner, "you are not the owner");
        _;
    }

    function receiveBalance() external payable {}
    receive () external payable  {}

    function setAllownce(address _addr,uint _amount) public onlyOwner {
        require(_amount <= getBalance(), "allowance amount should be less than total Balnce of the contract");
        assert(children[msg.sender] + _amount >= children[msg.sender]);
        children[_addr] += _amount;
    }

    function getBalance() public view returns(uint) {
        return address(this).balance;
    }

    function withdraw(address payable  _addr,uint _amount) public payable  {
        if (msg.sender == owner) {
            assert(getBalance() - _amount <= getBalance());
            _addr.transfer(_amount);
        }
        else {
        require(children[_addr] >= _amount, "you can't withdraw more");
        assert(children[_addr] - _amount <= _amount);
        children[_addr] -= _amount;
        _addr.transfer(_amount);
    }}
}
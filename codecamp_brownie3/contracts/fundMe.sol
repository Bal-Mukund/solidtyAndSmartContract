pragma solidity >=0.6.6 <0.9.0;

contract FundMe{
    uint256 public balance;
    address public owner;

    mapping(address => uint256) public accounts;

    function pay() public payable{

    }
}
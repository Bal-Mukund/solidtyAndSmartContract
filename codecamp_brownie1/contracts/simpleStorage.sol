// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;


contract simpleStorage{
    uint public number;

    function get_number() public view returns(uint){
        return number;
    }

    function set_number(uint _set) public {
        number = _set;
    }

}
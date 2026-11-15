// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract BankAccount {
    uint public balance;
    address public owner;

    constructor() {
        owner = msg.sender;
    }

    function deposit() public payable {
        require(msg.value > 0, "Enter an amount");
        balance += msg.value;
    }

    function withdraw(uint amount) public {
        require(msg.sender == owner, "Only owner can withdraw");
        require(amount > 0 && amount <= balance, "Invalid amount");
        balance -= amount;
        payable(owner).transfer(amount);
    }

    function showBalance() public view returns (uint) {
        return balance;
    }
}
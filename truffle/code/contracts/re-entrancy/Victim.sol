pragma solidity ^0.4.18;

contract Victim {
  
    mapping (address => uint) public balances;

    event WithdrawEvent(address _sender, uint amount);

    function Victim() public  { }

    function deposit() payable public {
        balances[msg.sender] = msg.value;
    }

    function getBalance() constant public returns (uint) {
        return balances[msg.sender];
    }

    function() payable public {
      // this.deposit();
        balances[msg.sender] = msg.value;
    }

    function withdraw() public {
        WithdrawEvent(msg.sender, balances[msg.sender]);

        require(balances[msg.sender] > 0);

        if (!msg.sender.call.value(balances[msg.sender])()) {
            revert();
        } 

        balances[msg.sender] = 0;
    }

}
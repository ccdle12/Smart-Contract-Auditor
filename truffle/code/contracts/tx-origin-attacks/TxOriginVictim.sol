pragma solidity ^0.4.18;

contract TxOriginVictim {
  address owner;

  function TxOriginVictim() {
    owner = msg.sender;
  }

  function transferTo(address to, uint amount) public {
    require(tx.origin == owner);
    to.call.value(amount)();
  }

  function getOwner() public constant returns (address) {
    return owner;
  }

  function() payable public {}
}

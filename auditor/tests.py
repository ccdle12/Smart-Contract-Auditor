import unittest
import parse_contract as auditor

class MainTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("[Starting Parse Contract Tests]\n")
        cls.ContractParser = auditor.ContractParser()
        cls.contract_as_string = "pragma solidity ^0.4.18; contract Victim { mapping (address => uint) public balances; event WithdrawEvent(address _sender, uint amount); function Victim() {} function deposit() payable { balances[msg.sender] = msg.value; } \
                              function getBalance() constant returns (uint) { return balances[msg.sender]; } \
                              function() payable { // this.deposit(); balances[msg.sender] = msg.value; } \
                              function withdraw() { WithdrawEvent(msg.sender, balances[msg.sender]); require(balances[msg.sender] > 0); \
                              if (!msg.sender.call.value(balances[msg.sender])()) { revert(); }   balances[msg.sender] = 0; } }"
        
        cls.contract_as_string_fail = "pragma solidity ^0.4.18; contract Victim { mapping (address => uint) public balances; event WithdrawEvent(address _sender, uint amount); function Victim() {} function deposit() payable { balances[] = msg.value; } \
                              function getBalance() constant returns (uint) { return balances[]; } \
                              function() payable { // this.deposit(); balances[] = msg.value; } \
                              function withdraw() { WithdrawEvent(, balances[]); require(balances[] > 0); \
                              if (!call.value(balances[])()) { revert(); }   balances[] = 0; } }"


    def test_should_parse_string(self):                   
        print("[test_should_parse_string]")
        print("Should return True that contract string has msg.sender in the contract\n")
        has_msg_sender = self.ContractParser.has_msg_sender(self.contract_as_string)
        expected = True
        self.assertEqual(expected, has_msg_sender)

    def test_should_parse_string_2(self):                       
        print("[test_should_parse_string]")
        print("Should return False that contract string does not have msg.sender\n")
        has_msg_sender = self.ContractParser.has_msg_sender(self.contract_as_string_fail)
        expected = False
        self.assertEqual(expected, has_msg_sender)

if __name__ == '__main__':
    unittest.main()
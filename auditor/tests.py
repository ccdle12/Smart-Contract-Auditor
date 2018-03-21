import unittest
import parse_contract as auditor

class TestContractParser(unittest.TestCase):

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

        cls.withdraw_function_as_string = "".join("function withdraw() { WithdrawEvent(msg.sender, balances[msg.sender]); require(balances[msg.sender] > 0); \
                                           if (!msg.sender.call.value(balances[msg.sender])()) { revert(); }   balances[msg.sender] = 0; }".split())


    def test_should_parse_string(self):                   
        print("[test_should_parse_string]")
        print("Should return True that contract string has msg.sender in the contract\n")
        has_msg_sender = self.ContractParser.has_msg_sender(self.contract_as_string)
        expected = True
        self.assertEqual(expected, has_msg_sender)

    def test_should_parse_string_2(self):                       
        print("[test_should_parse_string_2]")
        print("Should return False that contract string does not have msg.sender\n")
        has_msg_sender = self.ContractParser.has_msg_sender(self.contract_as_string_fail)
        expected = False
        self.assertEqual(expected, has_msg_sender)

    def test_should_get_position_of_msg_sender(self):
        print('[test_should_get_position_of_msg_sender]')
        print("Should return the position of msg.sender.call\n")

        msg_sender_position = self.ContractParser.get_msg_sender_position(self.contract_as_string)
        self.assertTrue(msg_sender_position is not None)
    
    def test_should_get_position_of_msg_sender_2(self):
        print('[test_should_get_position_of_msg_sender_2]')
        print("Should return None when searching for position of msg.sender.call\n")

        msg_sender_position = self.ContractParser.get_msg_sender_position(self.contract_as_string_fail)
        self.assertEqual(None, msg_sender_position)

    def test_should_retrieve_withdraw_function(self):
        print('[test_should_retrieve_withdraw_function]')
        print("Should return the withdraw function given the position of the msg.sender.call\n")

        extracted_withdraw_function = self.ContractParser.extract_withdraw_function(self.contract_as_string)
        expected = self.withdraw_function_as_string

        self.assertEqual(expected, extracted_withdraw_function)

    def test_should_retrieve_withdraw_function_2(self):
        print('[test_should_retrieve_withdraw_function_2]')
        print("Should return None when extracting withdraw function is called given a contract without msg.sender.call\n")

        extracted_withdraw_function = self.ContractParser.extract_withdraw_function(self.contract_as_string_fail)
        expected = self.withdraw_function_as_string

        self.assertEqual(None, extracted_withdraw_function)

if __name__ == '__main__':
    unittest.main()
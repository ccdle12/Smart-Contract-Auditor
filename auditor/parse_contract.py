import re

class ContractParser: 
    def has_msg_sender(self, contract_as_string):
        match_msg_sender = re.search(r'msg.sender.call', contract_as_string)

        if match_msg_sender != None:
            return True

        return False
    
    def get_msg_sender_position(self, contract_as_string):
        if not self.has_msg_sender(contract_as_string):
            return None
        
        position = contract_as_string.find('msg.sender.call')

        return position

    def extract_withdraw_function(self, contract_as_string):
        if not self.has_msg_sender(contract_as_string):
            return None

        # Get the position of the msg.sender.call        
        msg_sender_position = self.get_msg_sender_position(contract_as_string)

        # Get the last function call between the start of the contract to the msg.sender.call position
        withdraw_function_position = contract_as_string.rfind('function', 0, msg_sender_position)

        # Need to split a string according to function and if statements, need to take into account '}'
        function_call_to_end_of_contract = "".join(contract_as_string[withdraw_function_position:].split())

        # Temporary - Naive solution to find the end of the function
        opening_brace = 0
        closing_brace = None
        last_position = None
        i = withdraw_function_position

        while opening_brace != closing_brace:
            character = contract_as_string[i]

            if character == '{':
                opening_brace += 1
            
            if character == '}':
                if closing_brace is None:
                    closing_brace = 0

                closing_brace += 1

            last_position = i
            i += 1

        withdraw_function = contract_as_string[withdraw_function_position:last_position + 1]

        return "".join(withdraw_function.split())
        

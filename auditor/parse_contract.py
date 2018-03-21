import re

class ContractParser: 
    def has_msg_sender(self, contract_as_string):
        match_msg_sender = re.search(r'msg.sender', contract_as_string)

        if match_msg_sender != None:
            print("Match Msg Sender: {}".format(match_msg_sender.group(0)))
            return True

        return False
    
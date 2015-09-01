__module_name__ = "helloworld"
__module_version__ = "1.0"
__module_description__ = "Python module example"
import hexchat
import re

def matchmask(msg, nick):

	nick = re.sub(r'!.*', r'', nick)
	return nick in msg.lower()



def print_list(a, b, c):
	list = hexchat.get_list("ignore")
	if list:
		for i in list:
			if matchmask(b[1], i.mask):		
				return hexchat.EAT_ALL



hexchat.hook_server("RAW LINE", print_list)


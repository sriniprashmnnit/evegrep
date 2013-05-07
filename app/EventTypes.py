
from _winreg import *
import sys

def getEventTypes(server):
	try:
		aReg = ConnectRegistry(server, HKEY_LOCAL_MACHINE)
		targ = r'System\CurrentControlSet\Services\Eventlog'
		key = OpenKey(aReg, targ, 0, KEY_ALL_ACCESS)
	except WindowsError:
		return []

	eventtypes = []

	try:
	    i = 0
	    while True:
	        subkey = EnumKey(key, i)
	        #print subkey
	        eventtypes.append(subkey)
	        i += 1
	except WindowsError:
	    # WindowsError: [Errno 259] No more data is available    
	    pass

	return eventtypes

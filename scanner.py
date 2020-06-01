import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])
else:
	print('Invalid Argument!')
	print('Syntax: python3 scanner.py <ip>')

print('-' * 50)
print('Scanning target ' + target)
print('Time Started: ' + str(datetime.now()))

try: 
	for port in range(1, 65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target, port))
		if result == 0: 
			print('Port {} is open'.format(port))
		s.close()
except KeyboardInterrupt: 
	print('Exiting')
	sys.exit()

except socket.gaierror:
	print('Hostname cannot be resolved')
	sys.exit()

except socket.error:
	print('Could not connect to the server')
	sys.exit()

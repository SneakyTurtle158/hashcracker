from pwn import *
import sys

if len(sys.argv) != 4:
	print("Invalid Arguements!")
	print(">> python3 {} <hash> <passwordfilepath> <algorithm>".format(sys.argv[0]))
	exit()

wanted_hash = sys.argv[1]
password_file = sys.argv[2]
algo_type = eval(sys.argv[3])
attempts = 0


with log.progress("Attempting to crack: {}!\n".format(wanted_hash)) as p:
	with open(password_file, "r", encoding='latin-1') as password_list:
		for password in password_list:
			password = password.strip("\n").encode('latin-1')
			password_hash = algo_type(password)
			p.status("[{}] {} == {}".format(attempts, password.decode('latin-1'), password_hash))
			if password_hash == wanted_hash:
				p.success("Password hash found after {} attempts! {} hashes to {}!".format(attempts, password.decode('latin-1'), password_hash))
				exit()
			attempts += 1
		p.failure("Password hash not found")

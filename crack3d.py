#!/bin/python2

# My MD5 hash cracker
# Example hash below for testing
# 42f749ade7f9e195bf475f37a44cafcb
# Website to test your passwords
# http://www.miraclesalad.com/webtools/md5.php
# Use any dictionary file you want

import md5

counter = 1

hash = raw_input("[+] Please enter the MD5 hash: ")
default = raw_input("[+] Would you like to use the default wordlist? [y/n]: ")
if default in ['y', 'yes']:
	passList = 'rockyou.txt'
else:
	passList = raw_input("[+] Please enter the name of wordlist to use: ")

try:
	passList = open(passList, "r")
except:
	print "\nFile Not Found."
	quit()

print "Trying password number "
for password in passList:
	filemd5 = md5.new(password.strip()).hexdigest()
	print "[%d]--> %s" % (counter, password.strip())
	counter += 1
	
	if hash == filemd5:
		print "\n[+] Match Found! \nPassword is: %s" % password
		break
	else: print "\nPassword Not Found."

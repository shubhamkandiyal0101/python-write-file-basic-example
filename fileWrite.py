from termcolor import colored # import for  color
file_object = open('pythonwritefile.txt', 'w+') # write file with overwrite permission
print colored('NOTE: ', 'red'), colored('Type', 'green'), colored(' exit ', 'red'), colored('when You are Done with Writing', 'green') 
strinput = raw_input('Enter Something from Your Mind: ')
completeString = ''
take_input = 1
while(take_input == 1):
	completeString = completeString + '\n' + strinput
	strinput = raw_input('Enter Something from Your Mind: ')
	if(strinput == 'exit'):
		take_input = 0
file_object.write(completeString)
file_object.close()

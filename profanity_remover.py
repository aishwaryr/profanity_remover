"""This script censors any profanities in a file by vanishing the 2nd and 3rd letters
of the profanity. Number of letters to be vanished can be adjusted. Any combination possible
with the capital and small letters of a profanity is blocked. eg- If Puck is a profanity 
then PUCK, pUCK, etc all are blocked.
Profanity words can be added in the profanity_list."""
import itertools

profanity_list = ['fuck']                #new profanity words can be added to this list
profanity_combo_list = []

for l in profanity_list:
	profanity_combo_list += map(''.join, itertools.product(*((c.upper(), c.lower()) for c in l)))

file_path = '/home/ash/code/python/'     #here goes the path of the file excluding the file name.
file_name = 'profanity.txt'              #here goes the file name + .txt
clean_file_name = 'profanity_clean.txt'  #here goes the file name of new clean file to be created
def read_text():
	text = open(file_path+file_name)     #put path to your text file here
	string = text.read()
	
	text.close()
	profanity_remover(string)


def profanity_remover(string):
	for word in profanity_combo_list:
		word_len = len(word)
		for i in range (len(string)):
			if string[i:i+(word_len)] == word:
				string = string[:i+1] + '**' + string[i+3:]
				"""numbers of letters to be vanished can be adjusted by adding stars in the middle 
				   string and ading the same number to i+3. e.g. - You want F*** instead of F**k, 
				   then edit the above statement like this >>>string = string[:i+1] + '***' + string[i+4:]"""    
	print string
	text_new = open(file_path+clean_file_name, "wb")
	text_new.write(string)
	text_new.close()

read_text()





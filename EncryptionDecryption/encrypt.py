import cipher
from cipher import alpha


#converts a string into a list of integers according to the alpha director
#alphabet.py
# def encrypt(str1, alpha):
	# str1 = str1.lower()
	# for i in str1:
		# ciphertext.append(alpha[i])


def encrypt(str1, alpah):
	str1 = str1.lower()
	for i in str1:
		try:
			ciphertext.append(alpha[i])
		except:
			print('-' * 30, "\nEncountered Unknown symbol")
			ciphertext.append('30')
		
	
	
#prints a whole string
def printStr(str1):
	for i in str1:
		print(i)
	print()
	
#converts a list to a string
def listToString(L):
	s = ' '
	return s.join(map(str, L))


print("Enter the file to read from: ")
infile = input()
print("Enter the file to write to: ")
outfile = input()

f = open(infile)
str1 = f.read()
f.close()
	
ciphertext = []
encrypt(str1, alpha)
lts = listToString(ciphertext)

f = open(outfile, 'w')
f.write(lts)
f.close()


	
#WORK ON
#instead of declaring str1 outright, input a file
#remember to include a method for any other symbol other than what is in alpha

#After all of that works, change it so that it can use different ciphers
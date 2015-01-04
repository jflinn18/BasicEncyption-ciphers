import cipher
from cipher import realpha


def format():
    L = []
    str = ''

    i = 0

    while i < len(ciphertext):
        if ciphertext[i].isspace():
            L.append(str)
            str = ''
            i = i + 1

        str = str + ciphertext[i]
        i = i + 1
   
    L.append(str)
    return L

def decrypt(list):
	for i in list:
		plaintext.append(realpha[i])
		
#converts a list to a string
def listToString(L):
	s = ''
	return s.join(map(str, L))



print("Enter the file to read from: ")
infile = input()
print("Enter the file to write to: ")
outfile = input()

f = open(infile)
ciphertext = f.read()
f.close()

plaintext = []
L = format()
decrypt(L)

lts = listToString(plaintext)

f = open(outfile, 'w')
f.write(lts)
f.close()


#ifndef _Cipher_H
#define _Cipher_H

#include <string>
#include "Alphabet.h"

using std::string;

class Cipher
{
private:
	Alphabet a;
	string inputText;
	string outputText;

public:
	Cipher();
	void fileOut();
	string getText();
	void setText();
	virtual string decrypt() = 0;
	virtual string encrypt() = 0;
};

#endif
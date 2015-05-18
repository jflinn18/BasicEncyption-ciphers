#ifndef _UserInterface_H
#define _UserInterface_H

#include <string>
#include <vector>
#include <iostream>
#include "Cipher.h"

using std::string;

class UserInterface
{
private:
	string resp;
	string operation;
	string cipher;
	string text;
	std::vector<string> ciphers;

public:
	UserInterface();
	
	void getInput();
	string getText();
	void whichCipher();
	void printMenu();
	void clear_cmd();
};

#endif
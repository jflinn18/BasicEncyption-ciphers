#include "UserInterface.h"
#include <algorithm>

using std::cout;
using std::cin;
using std::endl;
using std::string;

UserInterface::UserInterface()
{
	ciphers.push_back("caesarshift");
	printMenu();
}

void UserInterface::printMenu()
{
	cout << "Pick an operation.\n";
	cout << "1. Encrypt\n2. Decrypt\n";
	getInput();
	operation = resp;

	std::transform(operation.begin(), operation.end(), operation.begin(), ::tolower);


	cout << "Which cipher would you like to use?\n";
	getInput();

}

void UserInterface::getInput()
{
	cout << ">>: ";
	cin >> resp;
}

void UserInterface::clear_cmd()
{
	system("cls");
}

void UserInterface::whichCipher()
{
	if 
}
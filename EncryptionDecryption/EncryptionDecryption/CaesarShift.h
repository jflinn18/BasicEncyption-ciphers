#ifndef _CaesarShift_H
#define _CeasarShift_H

#include "Cipher.h"
#include <string>

using std::string;


class CaesarShift : public Cipher
{
private:
	int numShifts;

public:
	string encrypt;
	string decrypt;
};

#endif
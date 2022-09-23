#include<Arduino.h>
int X,Y,Z,F;

void setup()
{
		pinMode(2,OUTPUT);
		pinMode(3,OUTPUT);
		pinMode(4,OUTPUT);
		pinMode(13,OUTPUT);
}
void loop()
{
		X=digitalRead(2);
		Y=digitalRead(3);
		Z=digitalRead(4);
		F=(!X&&Y&&!Z)||(X&&Y)||(!Y&&Z);
		digitalWrite(13,F);
}

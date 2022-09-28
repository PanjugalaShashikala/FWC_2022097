#include<avr/io.h>
#include<stdbool.h>
int main(void){

bool x,y,z,f;
DDRB = 0b00001111; //8&9&10&11 as inputs
PORTB= 0b11110000;
DDRD = 0b00000100; //2as output


while(1)
   {
	   x = (PINB & (1<<PINB0)) == (1<<PINB0);	
	   y = (PINB & (1<<PINB1)) == (1<<PINB1);
	   z = (PINB & (1<<PINB2)) == (1<<PINB2);
	   f=(!x&&y&&!z)||(x&&y)||(!y&&z);
	   PORTD |= (f<<2);

   }

	return 0;
}

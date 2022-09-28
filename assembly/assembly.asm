.include "/home/shashi/m328Pdef.inc"

ldi r16, 0b00111100 ;identifying output pins 2,3,4,5
out DDRD,r16		;declaring pins as output
ldi r16, 0b00100000
out DDRB,r16


ldi r16,0b00000000	;initializing X
ldi r17,0b00000000	;initializing Y
ldi r18,0b00000001	;initializing Z



ldi r23,0b00000001
eor r23,r16        ;X'

ldi r24,0b00000001 
eor r24,r18        ;Z'

ldi r25,0b00000001
eor r25,r17        ;Y'

AND r16,r17        ;X&&Y
AND r25,r18        ;Y'&&Z
AND r23,r17,r24    ;X'&&Y&&Z'

OR r16,r25,r23     ;(X'&&Y&&Z')||(X&&Y)||(Y'&&Z)



;following code is for displaying output
;shifting LSB in r16 to 2nd position
ldi r20, 0b00000010	;counter = 2

rcall loopw		;calling the loopw routine

out PORTD,r16		;writing output to pins 2,3,4,5


Start:
rjmp Start

;loop for bit shifting
loopw:	lsl r16 	      ;left shift
	dec r20			          ;counter --
	brne loopw	          ;if counter != 0
	ret

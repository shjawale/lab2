/*	Author: sjawa006
 *  Partner(s) Name: 
 *	Lab Section:
 *	Assignment: Lab #  Exercise #
 *	Exercise Description: [optional - include for your own benefit]
 *
 *	I acknowledge all content contained herein, excluding template or example
 *	code, is my own original work.
 */
#include <avr/io.h>
#ifdef _SIMULATE_
#include "simAVRHeader.h"
#endif

int main(void) {
    /* Insert DDR and PORT initializations */
    DDRA = 0x00; PORTA = 0xFF; // Configure port A's 8 pins as inputs
    DDRC = 0xFF; PORTC = 0x00; // Configure port B's 8 pins as outputs, initialize to 0s
    unsigned char tmpC = 0x00; // Temporary variable to hold the value of B
    unsigned char tmpA = 0x00; // Temporary variable to hold the value of A
    unsigned char cntavail = 0x00;
    unsigned char i;

    /* Insert your solution below */
    while(1) {
        // 1) Read input
        tmpA = PINA & 0x0F; // store A3A2A1A0
	cntavail = 0x00;
        for(i = 0; i <= 3; i++){
            if(!(tmpA & (0x01 << i))){
		cntavail += 1;
	    }
	}

/*
        tmpA = PINA & 0x01;
        tmpA = PINA & 0x02;
        tmpA = PINA & 0x04;
        tmpA = PINA & 0x08;

        // 2) Perform computation
        // count number of open parking spaces in cntavail
        if (tmpA == 0x01) { // True if PA0 is 1
            tmpC = (tmpB & 0xFC) | 0x00; 
        }
	if (tmpA == 0x01) {
	    tmpC = (tmpB & 0xFC) | 0x01; 
	}
	if(tmpA == 0x01) {
	    tmpC = (tmpB & 0xFC) | 0x02;
	}
	if(tmpA == 0x01) {
            tmpC = (tmpB & 0xFC) | 0x02;
        }
*/
	// 3) Output   
        PORTC = cntavail;    
    }    
    return 0;
}

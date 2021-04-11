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
//#include <iostream>
#ifdef _SIMULATE_
#include "simAVRHeader.h"
#endif

int main(void) {
    /* Insert DDR and PORT initializations */
    DDRA = 0x00; PORTA = 0xFF; // Configure port A's 8 pins as inputs
    DDRB = 0xFF; PORTB = 0x00; // Configure port B's 8 pins as inputs
    DDRC = 0xFF; PORTC = 0x00; // Configure port B's 8 pins as inputs
    DDRD = 0xFF; PORTD = 0x00; // Configure port B's 8 pins as outputs, initialize to 0s

    unsigned char tmpA = 0x00; // Temporary variable to hold the value of A
    unsigned char tmpB = 0x00; // Temporary variable to hold the value of B
    unsigned char tmpC = 0x00; // Temporary variable to hold the value of C
//    unsigned char tmpD = 0x00; // Temporary variable to hold the value of D
    short tmpsA = 0x00; // Temporary variable to hold the value of C
    short tmpsC = 0x00; // Temporary variable to hold the value of C
    unsigned short totweight = 0x00;
    unsigned char i;

    /* Insert your solution below */
    while(1) {
        // 1) Read input
        tmpA = (PINA >> 2); //shift right 2 to made addition easier
        tmpB = (PINB >> 2);
        tmpC = (PINC >> 2); 
	tmpsA = tmpA;
	tmpsC = tmpC;

	// 2) Perform computation
	// total weight ignoring bits 1 and 0
        totweight = tmpA + tmpB + tmpC;

	// 3) Output   
	PORTD = totweight & 0xF6; //clears bits 1 and 0
        //PORTD = (PORTD & 0x03) | tmpD; //retains PORTC's bit 1 and 0
/*	
	if(totweight > 0x86){ //check if total weight is above 140 kg
	    PORTD = PORTD | 0x01; //set bit 0 to 1
	}
	if( ( ( tmpsA - tmpsC ) > 0x50 ) || ( (tmpsC - tmpsA) > 0x50 ) ) { //check if weight |A-C| is above 80 kg
            PORTD = PORTD | 0x02; //set bit 1 to 1
        }
*/
    }    
    return 0;
}

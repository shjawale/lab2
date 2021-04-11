# Array of tests to run (in order)
# Each test contains
#   description - 
#   steps - A list of steps to perform, each step can have
#       inputs - A list of tuples for the inputs to apply at that step
#       *time - The time (in ms) to wait before continuing to the next step 
#           and before checking expected values for this step. The time should be a multiple of
#           the period of the system
#       *iterations - The number of clock ticks to wait (periods)
#       expected - The expected value at the end of this step (after the "time" has elapsed.) 
#           If this value is incorrect the test will fail early before completing.
#       * only one of these should be used
#   expected - The expected output (as a list of tuples) at the end of this test
# An example set of tests is shown below. It is important to note that these tests are not "unit tests" in 
# that they are not ran in isolation but in the order shown and the state of the device is not reset or 
# altered in between executions (unless preconditions are used).
tests = [ {'description': 'PINA: 0x00 & PINB: 0x00 & PINC: 0x00 => PORTD: 0x00',
    'steps': [ {'inputs': [('PINA', 0x00), ('PINB', 0x00), ('PINC', 0x00)], 'iterations': 5 } ],
    'expected': [('PORTD', 0x00)],
    },
	{'description': 'PINA: 0x01 & PINB: 0x02 & PINC: 0x04 => PORTD: 0x00',
    'steps': [ {'inputs': [('PINA', 0x01), ('PINB', 0x02), ('PINC', 0x04)], 'iterations': 5 } ],
    'expected': [('PORTD', 0x00)],
    },
        {'description': 'PINA: 0x02 & PINB: 0x04 & PINC: 0x08 => PORTD: 0x00',
    'steps': [ {'inputs': [('PINA', 0x02), ('PINB', 0x04), ('PINC', 0x08)], 'iterations': 5 } ],
    'expected': [('PORTD', 0x00)],
    },
        {'description': 'PINA: 0x08 & PINB: 0x10 & PINC: 0x20 => PORTD: 0x0C',
    'steps': [ {'inputs': [('PINA', 0x08), ('PINB', 0x10), ('PINC', 0x20)], 'iterations': 5 } ],
    'expected': [('PORTD', 0x0C)],
    },
        {'description': 'PINA: 0x59 & PINB: 0x04 & PINC: 0x08 => PORTD: 0x1A',
    'steps': [ {'inputs': [('PINA', 0x59), ('PINB', 0x04), ('PINC', 0x08)], 'iterations': 5 } ],
    'expected': [('PORTD', 0x1A)],
    },
        {'description': 'PINA: 0x80 & PINB: 0x30 & PINC: 0x2F => PORTD: 0x37',
    'steps': [ {'inputs': [('PINA', 0x80), ('PINB', 0x30), ('PINC', 0x2F)], 'iterations': 5 } ],
    'expected': [('PORTD', 0x37)],
    },
        {'description': 'PINA: 0x80 & PINB: 0x30 & PINC: 0x30 => PORTD: 0x39',
    'steps': [ {'inputs': [('PINA', 0x80), ('PINB', 0x30), ('PINC', 0x30)], 'iterations': 5 } ],
    'expected': [('PORTD', 0x39)],
    },
        {'description': 'PINA: 0x80 & PINB: 0x10 & PINC: 0x10 => PORTD: 0x2B',
    'steps': [ {'inputs': [('PINA', 0x80), ('PINB', 0x10), ('PINC', 0x10)], 'iterations': 5 } ],
    'expected': [('PORTD', 0x2B)],
    },
        {'description': 'PINA: 0x80 & PINB: 0x80 & PINC: 0x80 => PORTD: 0x61',
    'steps': [ {'inputs': [('PINA', 0x80), ('PINB', 0x80), ('PINC', 0x80)], 'iterations': 5 } ],
    'expected': [('PORTD', 0x61)],
    },


        {'description': 'PINA: 0x40 & PINB: 0x40 & PINC: 0x40 => PORTD: 0x31',
    'steps': [ {'inputs': [('PINA', 0x40), ('PINB', 0x40), ('PINC', 0x40)], 'iterations': 5 } ],
    'expected': [('PORTD', 0x31)],
    },
        {'description': 'PINA: 0x00 & PINB: 0x23 & PINC: 0x55 => PORTD: 0x1e',
    'steps': [ {'inputs': [('PINA', 0x00), ('PINB', 0x23), ('PINC', 0x55)], 'iterations': 5 } ],
    'expected': [('PORTD', 0x1e)],
    },
        {'description': 'PINA: 0x00 & PINB: 0x38 & PINC: 0x55 => PORTD: 0x1e',
    'steps': [ {'inputs': [('PINA', 0x00), ('PINB', 0x38), ('PINC', 0x55)], 'iterations': 5 } ],
    'expected': [('PORTD', 0x23)],
    },
    ]

# Optionally you can add a set of "watch" variables these need to be global or static and may need
# to be scoped at the function level (for static variables) if there are naming conflicts. The 
# variables listed here will display everytime you hit (and stop at) a breakpoint
#watch = ['<function>::<static-var>','PORTB']


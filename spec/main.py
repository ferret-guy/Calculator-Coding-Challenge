#!/usr/bin/env python

import sys

class Calculator(object):
    def calc(self, input_str):
        # Put your code here...
        pass

    def calc_with_vars(self, input_list):
        # Put your code here...
        pass

def main(argv):
    calculator = Calculator()

    print "First Step"
    print calculator.calc("3 + 4 * 5 / 7")

    print "\nSecond Step"
    print calculator.calc("( 3 + 4 ) * 5 / 7")

    print "\nThird Step"
    print calculator.calc_with_vars(
        ["pi = 3",
         "pizza = 9 * 9 * pi"])

main("")


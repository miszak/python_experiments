#!/usr/bin/python

from traceback import format_stack
from sys import exc_info

def assert_eq(expected, actual):
	if expected != actual:
		print "assert_eq failure!"
		print "     expected: " + str(expected)
		print "          got: " + str(actual)
		print "    traceback:"
		for line in format_stack():
			print "               " + line.strip().replace('\n','\n               ')
		exit("")


def assert_true(expr):
	if not expr:
		print "assert_true failure!"
		print "         traceback:"
		for line in format_stack():
			print "                    " + line.strip().replace('\n','\n                    ')
		exit("")

assert_eq("x", "x")
assert_eq([0,1], [1,0])
assert_true(1 == 1)
assert_true(1 != 1)

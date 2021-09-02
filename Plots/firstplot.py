import time
import sys
import os
import cursor

def fasttype(a):
	for b in a:
		time.sleep(0.003)
		sys.stdout.write(b)
		sys.stdout.flush()

def midtype(a):
	for b in a:
		time.sleep(0.03)
		sys.stdout.write(b)
		sys.stdout.flush()

def slowtype(a):
	for b in a:
		time.sleep(0.08)
		sys.stdout.write(b)
		sys.stdout.flush()
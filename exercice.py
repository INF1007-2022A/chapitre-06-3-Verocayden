#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools


def get_maximums(numbers):
	maximums = []
	for list in numbers:
		maximums.append(max(list))
	return maximums

def join_integers(numbers):
	return int(''.join(str(nb) for nb in numbers))

def generate_prime_numbers(limit):
	prime = []
	nbs = []
	for i in range(2, limit+1):
		nbs.append(i)
	while len(nbs) > 0:
		prime.append(nbs[0])
		for number in nbs:
			if number % nbs[0] == 0:
				nbs.remove(number)
	return prime

def combine_strings_and_numbers(strings, num_combinations, excluded_multiples):
	combine = []
	nbs = []
	for number in range(1, num_combinations+1):
		if excluded_multiples == None:
			nbs.append(number)
		elif number % excluded_multiples != 0:
			nbs.append(number)
	for number in nbs:
		for letter in strings:
			combine.append(letter + str(number))

	return combine

if __name__ == "__main__":
	print(get_maximums([[1,2,3], [6,5,4], [10,11,12], [8,9,7]]))
	print("")
	print(join_integers([111, 222, 333]))
	print(join_integers([69, 420]))
	print("")
	print(generate_prime_numbers(17))
	print("")
	print(combine_strings_and_numbers(["A", "B"], 2, None))
	print(combine_strings_and_numbers(["A", "B"], 5, 2))

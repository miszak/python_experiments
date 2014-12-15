#!/usr/bin/python

def is_anagram(word, anagram):
	if len(word) != len(anagram):
		return False
	dict_word = {}
	dict_anagram = {}
	for i in range(len(word)):
		if word[i] in dict_word:
			dict_word[word[i]] += 1
		else:
			dict_word[word[i]] = 1
	for i in range(len(anagram)):
		if anagram[i] in dict_anagram:
			dict_anagram[anagram[i]] += 1
		else:
			dict_anagram[anagram[i]] = 1
	return dict_word == dict_anagram


assert(is_anagram("bla", "alb"))
assert(is_anagram("hook", "koho"))
assert(not is_anagram("book", "kob"))
assert(not is_anagram("twigli", "elgiwt"))
assert(not is_anagram("twiglj", "elgiwt"))

def is_palindrome(word):
	for i in range(len(word) / 2):
		if word[i] != word[len(word) - i - 1]:
			return False
	return True

assert(is_palindrome("rotor"))
assert(is_palindrome("tennet"))
assert(not is_palindrome("tenket"))
assert(not is_palindrome("tennit"))
assert(not is_palindrome("kinga"))
assert(not is_palindrome("michal"))

import sys
import time
import random
import re
import sqlite3
import os
from string import punctuation
from collections import Counter
from math import sqrt

def pre_regular():
	print(" " * 63, end="")
	
	print("\/" * 18)
	print("\n" * 3)
	print(" " * 60, end="")
	
	print("    -========", " " * 14, "========-")
	print(" " * 60, end="")
	
	print("      ___", " " * 19, "  ___")
	print(" " * 60, end="")
	
	print("     |   |", " " * 9, "|", " " * 7, "|   |")
	print(" " * 60, end="")
	
	print("     |0  |", " " * 9, "|", " " * 7, "|0  |")
	print(" " * 60, end="")
	
	print("      ---", " " * 10, "|", " " * 6, "  ---")
	print(" " * 60, end="")
	
	print("\n" * 5)
	print(" " * 67, end="")
	print("      ", "_" * 12, "/")
	print("\n" * 2)
	time.sleep(2)
def regular():
	print(" " * 63, end="")
	
	print("\/" * 18)
	print("\n" * 3)
	print(" " * 60, end="")
	
	print("    -========", " " * 14, "========-")
	print(" " * 60, end="")
	
	print("      ___", " " * 19, "  ___")
	print(" " * 60, end="")
	
	print("     |   |", " " * 9, "|", " " * 7, "|   |")
	print(" " * 60, end="")
	
	print("     | 0 |", " " * 9, "|", " " * 7, "| 0 |")
	print(" " * 60, end="")
	
	print("      ---", " " * 10, "|", " " * 6, "  ---")
	print(" " * 60, end="")
	
	print("\n" * 4)
	print(" " * 65, end="")
	
	print("       \\", " " * 16, "/")
	print(" " * 67, end="")
	
	print("      \\", "_" * 14, "/")
	print("\n" * 2)
	time.sleep(2)
def pre_question():
	print(" " * 63, end="")
	
	print("\/" * 18)
	print("\n" * 3)
	print(" " * 60, end="")
	
	print("    -========", " " * 14, "========-")
	print(" " * 60, end="")
	
	print("      ___", " " * 19, "  ___")
	print(" " * 60, end="")
	
	print("     |  0|", " " * 9, "|", " " * 7, "|  0|")
	print(" " * 60, end="")
	
	print("     |   |", " " * 9, "|", " " * 7, "|   |"
	"")
	print(" " * 60, end="")
	
	print("      ---", " " * 10, "|", " " * 6, "  ---")
	print(" " * 60, end="")
	
	print("         ", " " * 10, " \\", )
	print(" " * 60, end="")
	
	print("         ", " " * 10, "__\\", )
	print("\n" * 5)
	print(" " * 66, end="")
	
	print("     (", "_" * 13)
	print("\n" * 16)
	time.sleep(2)
def question():
	print(" " * 17, end ="")
	print("\/\/\/\/")
	print(" " * 17, end ="")
	print(" ^    _")
	print(" " * 17, end ="")
	print(" o  | o\n")
	print(" " * 17, end ="")
	print("  ___\n\n")
	print("\n"* 3)
def pre_amazing():
	print(" " * 17, end ="")
	print("\/\/\/\/")
	print(" " * 17, end ="")
	print(" -    -")
	print(" " * 17, end ="")
	print(" O  | O\n")
	print(" " * 17, end ="")
	print("  (___)\n\n")
	print("\n"* 3)
	time.sleep(.5)
def amazing():
	print(" " * 17, end ="")
	print("\/\/\/\/")
	print(" " * 17, end ="")
	print(" -    -")
	print(" " * 17, end ="")
	print(" ^  | ^\n")
	print(" " * 17, end ="")
	print("  (___)\n\n")
	print("\n"* 5)
def pre_happiness():
	print(" " * 17, end ="")
	print("\/\/\/\/")
	print(" " * 17, end ="")
	print(" -    -")
	print(" " * 17, end ="")
	print(" ^  | ^\n")
	print(" " * 17, end ="")
	print("  \__/\n\n")
	print("\n"* 5)
	time.sleep(2)
def happiness():
	print(" " * 17, end ="")
	print("\/\/\/\/")
	print(" " * 17, end ="")
	print(" v    v")
	print(" " * 17, end ="")
	print(" ^  | ^\n")
	print(" " * 17, end ="")
	print("  \__/\n\n")
	print("\n"* 3)
def sad():
	print(" " * 17, end ="")
	print("\/\/\/\/")
	print(" " * 17, end ="")
	print(" _    _")
	print(" " * 17, end ="")
	print(" v  | v\n")
	print(" " * 17, end ="")
	print("  __\n\n")
	print("\n"* 3)
def pre_hmm():
	print(" " * 17, end ="")
	print("\/\/\/\/")
	print(" " * 17, end ="")
	print(" _    _")
	print(" " * 17, end ="")
	print(" o  | o\n")
	print(" " * 17, end ="")
	print("   __\n\n")
	print("\n"* 3)
def hmm():
	print(" " * 17, end ="")
	print("\/\/\/\/")
	print(" " * 17, end ="")
	print(" /    _")
	print(" " * 17, end ="")
	print(" o  | o\n")
	print(" " * 17, end ="")
	print("  __\n\n")
	print("\n"* 3)
def pre_bye():
	print(" " * 17, end ="")
	print("\/\/\/\/")
	print(" " * 17, end ="")
	print(" \    /")
	print(" " * 17, end ="")
	print(" 0  | 0\n")
	print(" " * 17, end ="")
	print("  ____\n\n")
	print("\n"* 5)
	time.sleep(2)
def bye():
	print(" " * 17, end ="")
	print("\/\/\/\/")
	print(" " * 17, end ="")
	print(" v    v")
	print(" " * 17, end ="")
	print(" o, | o\n")
	print(" " * 17, end ="")
	print("  ____\n\n")
	print("\n"* 3)
	
	
face_preview = "off"

if "on" in face_preview:
	pre_regular()
	regular()
	pre_question()
	question()
	pre_amazing()
	amazing()
	pre_happiness()
	happiness()
	sad()
	pre_hmm()
	hmm()
	pre_bye()
	bye()
	
connection = sqlite3.connect('chatbot.sqlite')
cursor = connection.cursor()

try:

	cursor.execute('''
	CREATE TABLE words (
	word TEXT UNIQUE
	)''')
	
	cursor.execute('''
	CREATE TABLE sentences (
	sentence TEXT UNIQUE,
	used INT NOT NULL DEFAULT 0
	)''')
	
	cursor.execute('''
	CREATE TABLE associations (
	word_id INT NOT NULL,
	sentence_id INT NOT NULL,
	weight REAL NOT NULL
	)''')
	
except:
	pass
	
	
def get_id(entityName, text):
	tableName = entityName + 's'
	columnName = entityName
	cursor.execute('SELECT rowid FROM ' + tableName + ' WHERE ' + columnName + ' = ?', (text,))
	row = cursor.fetchone()
	if row:
		return row[0]
	else:
		cursor.execute('INSERT INTO ' + tableName + ' (' + columnName + ') VALUES (?)', (text,))
		return cursor.lastrowid
		
def get_words(text):
	wordsRegexpString = '(?:\w+|[' + re.escape(punctuation) + ']+)'
	wordsRegexp = re.compile(wordsRegexpString)
	wordsList = wordsRegexp.findall(text.lower())
	return Counter(wordsList).items()
	
def next():
	print("\n" * 18)
	
def slow_type(x):
	typing_speed = 50
	for l in x:
		sys.stdout.write(l)
		sys.stdout.flush()
		n = random.random()
		time.sleep(n * 10.0/typing_speed)
		
next()

regular()
L = input("Whats your name? \n\nYou: ")
if "!=" in L:
	cursor.execute('DELETE FROM sentences')
	cursor.execute('DELETE FROM words')
	cursor.execute('DELETE FROM associations')
	L = L.replace("!=", "")
next()

pre_regular()
regular()
print("Hi " + L, end = "")

A = ' how are you '
need_be = 5
count = 1
ae = 0
users_time = 0
emotion_lvl = 0
total_time = 0
response_length = 0
total_rlen = 0
warning_rlen = 0
warning_low = .2
warning_hi = 1.275
l_wl = .2
while True:

	name_random = random.randint(1, 5)
	response_wait = random.randint(0, 2)
	
	total_time += users_time
	avg_time = total_time/count
	
	total_rlen += response_length
	avg_rlen = int(total_rlen/count)
	
	if ae <= 1:
		Z = ("")
		id_number = 2
		ae += 1
		
	if ae >= 2:
		ae += 1
		count += 1
		if avg_time * warning_low >= users_time >= avg_time * warning_hi:
			if count - 1 > need_be:
				emotion_lvl = 5
				# 4s
				# 1.35 = 5s
				# * .075 = 1s
		if response_length < avg_rlen * l_wl:
			if count - 1 > need_be:
				emotion_lvl = 5
				
		inB = B.title()
		if "?" in inB:
			emotion_lvl = 1
			id_number = 1
		if "!" in inB:
			emotion_lvl = 2
			id_number = 1
		if "Happy" in inB:
			emotion_lvl = 3
			id_number = 1
		if "Sad" in inB:
			emotion_lvl = 4
			id_number = 1
			
			
		inA = A.title()
		if "Happy" in inA:
			emotion_lvl = 3
			id_number = 2
		if "Sad" in inA:
			emotion_lvl = 4
			id_number = 2
		if "Idk" in inA:
			emotion_lvl = 5
			id_number = 2
		if "!" in inA:
			emotion_lvl = 0
			id_number = 2
			
			
		if "Bye" in inB:
			emotion_lvl = 6
			id_number = 1
			
			
		if emotion_lvl == 0:
			pre_regular()
			regular()
		if emotion_lvl == 1:
			pre_question()
			question()
			response_wait += 1
		if emotion_lvl == 2:
			pre_amazing()
			amazing()
			response_wait = 0
		if emotion_lvl == 3:
			pre_happiness()
			happiness()
		if emotion_lvl == 4:
			sad()
			name_random = random.randint(1,3)
			response_wait += 3
		if emotion_lvl == 5:
			pre_hmm()
			hmm()
		if emotion_lvl == 6:
			pre_bye()
			bye()
			slow_type("Aw, ok bye...")
			break
			
	reading_time = response_length * .3
	response_final = response_wait + reading_time
	
	if ae > 1:
	
		analysis = "off"
		
		if "on" in analysis:
			l = L.title()
			if id_number == 1:
				user = L
			if id_number == 2:
				user = "Computer"
			if name_random == 1:
				yes_no = "yes"
			if name_random > 1:
				yes_no = "no"
			prop_check = users_time / avg_time
			lw_wl = int(avg_rlen * l_wl)
			print("(Anaylsis:\n")
			print("Count: ", count - 1, "\n")
			
			print("Subject: ", l)
			print("Avg response time: ", avg_time)
			print("Last response time: ", users_time)
			print("Avg word length: ", avg_rlen)
			print("Last word length: ", response_length, "\n")
			
			print("Subject: Computer")
			print("Reading time:", reading_time)
			print("Response time selected:", response_wait)
			print("Final response time: ", response_final)
			print("Used Subjects Name?: ", yes_no, "(", name_random, ")", "\n")
			if count - 1 >= need_be:
				print("(AI)")
				print("Time proportion check: ", prop_check)
				print("Count ", count - 1, " warning response word length(L): ", lw_wl, "\n")
			print("Emotion lvl: ", emotion_lvl, "(", user, ")", ")\n")
			# Anaylsis ends
			
	print(Z, end = "")
	time.sleep(response_final)
	if name_random == 1:
		slow_type(A + " " + L + "\n")
	else:
		slow_type(A + "\n")
	start = time.time()
	print("")
	
	B = input(L + ": ").strip()
	next()
	stop = time.time()
	users_time = stop - start
	response_length = len(B.split())
	
	
	words = get_words(A)
	words_length = sum([n * len(word) for word, n in words])
	sentence_id = get_id('sentence', B)
	for word, n in words:
		word_id = get_id('word', word)
		weight = sqrt(n / float(words_length))
		cursor.execute('INSERT INTO associations VALUES (?, ?, ?)', (word_id, sentence_id, weight,))
		connection.commit()
		
	cursor.execute('CREATE TEMPORARY TABLE results(sentence_id INT, sentence TEXT, weight REAL)')
	
	words = get_words(B)
	words_length = sum([n * len(word) for word, n in words])
	for word, n in words:
		weight = sqrt(n / float(words_length))
		cursor.execute(
		'INSERT INTO results SELECT associations.sentence_id, sentences.sentence, ?*associations.weight/(4+sentences.used) FROM words INNER JOIN associations ON associations.word_id=words.rowid INNER JOIN sentences ON sentences.rowid=associations.sentence_id WHERE words.word=?',
		(weight, word,))
		
	cursor.execute(
	'SELECT sentence_id, sentence, SUM(weight) AS sum_weight FROM results GROUP BY sentence_id ORDER BY sum_weight DESC LIMIT  1')
	row = cursor.fetchone()
	cursor.execute('DROP TABLE results')
	
	if row is None:
		cursor.execute(
		'SELECT rowid, sentence FROM sentences WHERE used = (SELECT MIN(used) FROM sentences) ORDER BY RANDOM() LIMIT 1')
		row = cursor.fetchone()
		
	A = row[1]
	cursor.execute('UPDATE sentences SET used = used + 1 WHERE rowid = ?', (row[0],))


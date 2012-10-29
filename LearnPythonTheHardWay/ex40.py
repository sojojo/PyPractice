#Exercise 40 - Modules, Classes, And Objects
#Modules, classes, and objects -> 3 types of key value type storage
#Using classes and object oriented practice
class Song(object):
	
	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

#split up and concatenate a string by putting into an array 			
happy_bday = Song(["Happy birthday to you",
				"I don't want to get sued",
				"So I'll stop right there"])
				
bulls_on_parade = Song(["They rally around the family",
						"With pockets full of shells"])
						
#EC - make a string to pass to song instead with a new song
coconut_song = ["""
I've got a lovely bunch of coconuts.
Doodelee doo.
here they are a standing in a row.
Two, Three, Four.
Big ones small ones, some as big as your head.
"""]

Song(coconut_song).sing_me_a_song()
						
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
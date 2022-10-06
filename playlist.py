"""
This class implements the playlist class using a deque.

Author: Matthew Festa
festam@merrimack.edu
CSC 6003 - Foundations of Programming
Programming Project 6 (Module 6 Assignment 1)
"""

from collections import deque
from random import random
from song import Song


class Playlist:

	def __init__(self, name, length):
		self.__name = name
		self.__songs = deque(maxlen=length)
		self.__current_song = None  # The current song is None at first

	def add_first_song(self, song):
		"""
		Adds a song to the beginning of the playlist.
		:param song:
		"""
		if song not in self.__songs:
			self.__songs.appendleft(song)
			self.__current_song = song
			# Current song will always be the first song in the deque
			print(f'Now playing: {self.__current_song}')
			print('You have {} song(s) in your playlist.'.format(
				len(self.__songs)))
			return True
		return False

	def add_last_song(self, song):
		"""
		Adds a song to the end of the playlist.
		:param song:
		"""
		if song not in self.__songs:
			self.__songs.append(song)
			if self.__current_song is None:
				self.__current_song = song
				print(f'Now playing: {self.__current_song}')
			else:
				# Only the 0 index is the current song
				print(f'{song} added to the end of the playlist.')
			print('You have {} song(s) in your playlist.'.format(
				len(self.__songs)))
			return True
		return False

	def shuffle(self):
		"""
		Shuffles the playlist.
		"""
		if len(self.__songs) > 1:
			# Randomize order using lamda function on the deque:
			self.__songs = deque(sorted(self.__songs, key=lambda k: random()))
			print('Playlist shuffled.')
		else:
			print("The playlist is too short to shuffle.")

	def play_next(self):
		"""
		Plays the next song in the playlist.
		:return:
		"""
		if len(self.__songs) > 1:
			# Rotate the deque to the right
			self.__songs.rotate(1)
			# Set the current song to the first song in the deque
			self.__current_song = self.__songs[0]
			# Print the current song
			print(f'Now playing: {self.__current_song}')
			return self.__current_song
		else:
			print("Cannot play next song.")

	def play_previous(self):
		"""
		Plays the previous song in the playlist.
		:return:
		"""
		if len(self.__songs) > 1:
			# Rotate the deque to the left
			self.__songs.rotate(-1)
			# Set the current song to the first song in the deque
			self.__current_song = self.__songs[0]
			# Print the current song
			print(f'Now playing: {self.__current_song}')
			return self.__current_song
		else:
			print("Cannot play previous song.")

	def repeat(self):
		"""
		Repeats the song.
		:param song:
		"""
		if len(self.__songs) > 0:
			print(f'Now playing: {self.__current_song}')
			return self.__current_song
		else:
			print("Cannot repeat song.")

	def remove_song(self, song):
		"""
		Removes the song from the playlist.
		:param song:
		:return:
		"""
		if song in self.__songs:
			print(f'Removing {song} from the playlist.')
			self.__songs.remove(song)
			print('You have {} song(s) in your playlist.'.format(
				len(self.__songs)))
			return True
		else:
			print('Song not found.')
			return False

	def __str__(self):
		"""
		Returns the string representation of the playlist.
		:return:
		"""
		if len(self.__songs) == 0:
			return f'{self.__name}\'s playlist is empty. Please add a song. \n'
		# Convert songs to an iterable string on each line and enumerate:
		songs = ''.join(
			f'{i + 1}. {song}' for i, song in enumerate(self.__songs))
		return f'{self.__name}\'s Playlist: \n' \
		       f'{songs} \n'

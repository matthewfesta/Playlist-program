"""
This module creates a blueprint for the song class and methods.

Author: Matthew Festa
festam@merrimack.edu
CSC 6003 - Foundations of Programming
Programming Project 6 (Module 6 Assignment 1)
"""


class Song:

	def __init__(self, title, artist):
		"""
		Initializes the song.
		:param title:
		:param artist:
		"""
		self.__title = title
		self.__artist = artist

	def get_title(self):
		"""
		Returns the title of the song.
		:return:
		"""
		return self.__title

	def get_artist(self):
		"""
		Returns the artist of the song.
		:return:
		"""
		return self.__artist

	def __str__(self):
		"""
		Returns the string representation of the song.
		:return:
		"""
		return f'\"{self.__title}\" by {self.__artist}\n'

	def __eq__(self, other):
		"""
		Returns True if the song is equal to the other song.
		:param other:
		:return:
		"""
		return self.__title == other.get_title() \
		       and self.__artist == other.get_artist()

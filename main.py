"""
This is the main module for the program. It contains the main function and
runs the program.

Author: Matthew Festa
festam@merrimack.edu
CSC 6003 - Foundations of Programming
Programming Project 6 (Module 6 Assignment 1)
"""
from playlist import Playlist
from song import Song

def main():
	while True:
		print("Welcome to the next hit playlist program.")
		main_menu = input('*** Press: ***\n'
		                  '1 - Create a new playlist\n'
		                  '2 - Add a song at the beginning of the playlist\n'
		                  '3 - Add a song at the end of the playlist\n'
		                  '4 - Play the next song\n'
		                  '5 - Play the previous song\n'
		                  '6 - Repeat the current song\n'
		                  '7 - Remove a song from the playlist\n'
		                  '8 - Display the playlist\n'
		                  '9 - Shuffle the playlist\n'
		                  '10 - Quit\n')
		if main_menu == '1':
			user_name = input('Enter your name: ')
			# 5 is the amount of songs one can put on the playlist to
			# to demonstrate the functionality of the program using a deque.
			playlist = Playlist(user_name, 5)
			print(f"Playlist created for {user_name}.")
			print(playlist)
		elif main_menu == '2':
			song_title = input('Enter the song title: ')
			song_artist = input('Enter the song artist: ')
			song = Song(song_title, song_artist)
			try:
				playlist.add_first_song(song)
			except NameError:
				print('Please create a playlist first.')
		elif main_menu == '3':
			song_title = input('Enter the song title: ')
			song_artist = input('Enter the song artist: ')
			song = Song(song_title, song_artist)
			try:
				playlist.add_last_song(song)
			except NameError:
				print('Please create a playlist first.')
		elif main_menu == '4':
			try:
				playlist.play_next()
			except NameError:
				print('Please create a playlist first.')
		elif main_menu == '5':
			try:
				playlist.play_previous()
			except NameError:
				print('Please create a playlist first.')
		elif main_menu == '6':
			try:
				playlist.repeat()
			except NameError:
				print('Please create a playlist first.')
		elif main_menu == '7':
			song_to_remove = input('Enter the song to remove: ')
			try:
				playlist.remove_song(song_to_remove)
			except NameError:
				print('Please create a playlist first.')
		elif main_menu == '8':
			print(playlist)
		elif main_menu == '9':
			try:
				playlist.shuffle()
			except NameError:
				print('Please create a playlist first.')
		elif main_menu == '10':
			break
		else:
			print('Invalid input.')


if __name__ == '__main__':
	main()
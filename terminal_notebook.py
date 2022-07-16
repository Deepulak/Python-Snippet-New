import os
from notebook import Notebook, Note

class Menu(object):
	""" Display a command line interface (CLI) """
	def __init__(self):
		self.notebook = Notebook()
		self.choices = {
			"1": self.show_notes,
			"2": self.search_notes,
			"3": self.add_notes,
			"4": self.modify_notes,
			"5": self.quit
		}

	def display_menu(self):
		print(""" [ Notebook Menu ]
				1. Show All Notes.
				2. Search Notes.
				3. Add Note.
				4. Modify Note.
				5. Quit
			""")

	def run(self):
		""" Display the menu and respond to choices. """
		while True:
			self.display_menu()
			choice = input("Enter Option >> ")
			action = self.choices.get(choice)
			if action:
				action()
			else:
				print(f"{choice} is not a valid choice")

	def show_notes(self, notes=None):
		if not notes:
			notes = self.notebook.notes
		for note in notes:
			print(f"{note.id}: {note.id}\n{note.memo}")

	def search_notes(self):
		filter = input("Search for >> ")
		notes = self.notebook.search(filter)
		self.show_notes(notes)

	def add_notes(self):
		memo = input("Enter memo >> ")
		self.notebook.new_note(memo)
		print("Your note has been added.")

	def modify_note(self):
		id = input("Enter a note id >> ")
		memo = input("Enter a memo >> ")
		tags = input("Enter tags >> ")
		if memo:
			self.notebook.modify_memo(id, memo)
		if tags:
			self.notebook.modify_tags(id, tags)

	def quit(self):
		print("Thanks for using our notebook.")

if __name__ == "__main__":
	Menu().run()


import datetime

# Store the next available id for all new notes
last_id = 0

class Note(object):
	""" Represent a note in the notebook. Match against a
	string in searches and store tags for each note. """ 
	def __init__(self, memo, tags=""):
		""" Initialize a note with memo and optional
		space-separated tags. Automatically set the note's
		creation date and a unique id. """
		self.memo = memo
		self.tags = tags
		self.creation_date = datetime.date.today()
		global last_id
		last_id += 1
		self.id = last_id

	def match(self, filter):
		""" Determine if this note matches the filter
		text. Returns True if it matches, False otherwise.
		Search is case sensitive and matches both text and tags. """
		return filter in self.memo or filter in self.tags

class Notebook(objec):
	""" Represents a colection of notes that can be tagged,
	modified, and searched."""
	def __init__(self):
		""" Initialize a notebook with an empty list. """ 
		self.notes = []

	def new_note(self, memo, tags=""):
		""" Create a new note and add it to the list. """
		self.notes.append(Note(memo, tags))

	def modify_memo(self, note_id, memo):
		""" Find the note with the given id and change its
		memo to the given values. """
		note = self._find_note(note_id)
		if note:
			note.memo = memo
			return True
		return False

	def modify_tags(self, note_id, tags):
		""" Find the note with the given id and change its
		tags to the given value. """
		for note in self.notes:
			if note.id == note_id:
				note.tags = tags
			break

	def search(self, filter):
		""" Find all notes that match the given filter string. """
		return [note for note in self.notes if note.match(filter)]
				
	def _find_note(self, note_id):
		""" Locate the note with the given id. """
		for note in self.notes:
			if str(note.id) == str(note_id):
				return note
		return None
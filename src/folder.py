import os
from .file import File


class Folder:
	def __init__(self, name: str, content: list[File]) -> None:
		self.name = name
		self.content = content

	def place_at(self, path: str) -> str:
		if os.path.exists(path):
			return

		os.mkdir(path)

		for f in self.content:
			f.place_at(os.path.join(path, f.name))

		return path

	def __repr__(self) -> str:
		return f'{self.name}/'

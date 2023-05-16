import os


class File:
	def __init__(self, name: str, content: bytes) -> None:
		self.name = name
		self.content = content


	def place_at(self, path: str) -> str:
		with open(path, 'wb') as f:
			f.write(self.content)

	def __repr__(self) -> str:
		return self.name

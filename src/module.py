import os
from .file import File
from .errors import VersionError


class Module:
	def __init__(self, name: str, config: dict, files: list[File]) -> None:
		print(f'Loading module: {name}')
		self.name = name
		self.files = files

		self.type = config.get('type', None)
		self.version = config.get('version', None)
		self.global_path = config.get('path', None)

		if self.version is None:
			self.version = 1
			print(f'{self} missing version, defaulting to {self.version}')

		print('Done Loading')

	def initiate(self, extra_path: str=None) -> None:
		print('Initiating')
		if self.type == 'local':
			full_path = os.path.join(os.getcwd(), extra_path)
		elif self.type == 'global':
			full_path = self.global_path
		else:
			raise ValueError(f'"{self.type}" is not a valid type... can be ["local", "global"]')

		if self.version == 1:
			return self.__initiate_ver_1(full_path)
		else:
			raise VersionError(f'"{self.version}" does not exist')

	def __initiate_ver_1(self, full_path: str) -> None:
		print(f'Using path: {full_path}')
		for file in self.files:
			file.place_at(os.path.join(full_path, file.name))
		print('Finished')

	def __repr__(self) -> str:
		s = 's' if len(self.files) > 1 else ''
		return f'Module({self.name}, {len(self.files)} file{s})'



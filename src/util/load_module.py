import json
import os
from github import Github, Repository
import settings
from .. import Folder, File, Module


def crawl_files(repo: Repository, path: str, active_dir: list|Folder) -> Folder:
	for file in repo.get_contents(path):
		if file.name == 'configurator-options.json':
			continue

		if file.type == 'dir':
			active_dir.content.append(Folder(file.name, []))
			crawl_files(repo, os.path.join(path, file.name), active_dir.content[-1])
		else:
			active_dir.content.append(File(file.name, file.decoded_content))

	return active_dir


def load_module(gh: Github, name: str) -> Module:
	repo = gh.get_repo(settings.target_repo)
	root_folder = Folder(f'/{name}', [])
	files = crawl_files(repo, f'/{name}', root_folder)

	config = None
	for file in repo.get_contents(f'/{name}'):
		if file.name == 'configurator-options.json':
			config = json.loads(file.decoded_content)
			break

	if config is None:
		print('Missing configurator-options.json')
		config = {}

	return Module(name, config, files.content)

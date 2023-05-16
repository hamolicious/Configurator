import os
from sys import argv
import json
import github
import settings
from src import File
from src.util import get_all_available_configs, load_module, get_num_user_input


def help():
	string = [
		f'Usage: {os.path.basename(__file__)} <module> <directory>',
		'Examples:',
		f'\t {os.path.basename(__file__)} <module> <directory>',
		f'\t {os.path.basename(__file__)} <directory>',
		f'\t {os.path.basename(__file__)} <module>',
		f'\t {os.path.basename(__file__)}',
	]
	return '\n'.join(string)

directory = './'
if len(argv[1::]) == 0:
	module_name = None
elif len(argv[1::]) == 1:
	if '/' in argv[-1]:
		directory = argv[-1]
		module_name = None
	else:
		module_name = argv[-1]
elif len(argv[1::]) == 2:
	directory = argv[2]
	module_name = argv[1]

github_token = os.environ.get('GITHUB_TOKEN')
gh = github.Github(github_token)

modules = get_all_available_configs(gh)

if module_name not in modules:
	print('Invalid module name')
	module_name = None

if module_name is None:
	print('Configs:')
	print('\n'.join(map(lambda m : f'\t - [{m[0]:03}] {m[1]}', enumerate(modules))))
	selection = get_num_user_input(0, len(modules))
else:
	selection = modules.index(module_name)

module = load_module(gh, modules[selection])
module.initiate(directory)

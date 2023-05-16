import os
from sys import argv
import json
import github
import settings
from src import File
from src.util import get_all_available_configs, load_module, get_num_user_input


def help():
	string = [
		f'Usage: {os.path.basename(__file__)} <directory> <*module>',
		'Examples:',
		f'\t {os.path.basename(__file__)} <directory> <module>',
		f'\t {os.path.basename(__file__)} <directory> <module> <module> <module> <module>',
		f'\t {os.path.basename(__file__)} <directory>',
		f'\t {os.path.basename(__file__)} <module>',
		f'\t {os.path.basename(__file__)} <module> <module> <module>',
		f'\t {os.path.basename(__file__)}',
	]
	return '\n'.join(string)

directory = './'
if argv[1] in ['-h', '--help', '/?', '-?']:
	print(help())
	quit()

arguments = argv[1::]
if len(arguments) == 0:
	module_names = None

if '/' in arguments[0] or '\\' in arguments[0]:
	directory = arguments[0]
	arguments = arguments[1::]
module_names = arguments


github_token = os.environ.get('GITHUB_TOKEN')
gh = github.Github(github_token)

modules = get_all_available_configs(gh)

for module_name in module_names:
	if module_name not in modules:
		print(f'Invalid module name "{module_name}"')
		module_name = None

	if module_name is None:
		print('Configs:')
		print('\n'.join(map(lambda m : f'\t - [{m[0]:03}] {m[1]}', enumerate(modules))))
		selection = get_num_user_input(0, len(modules))
	else:
		selection = modules.index(module_name)

	module = load_module(gh, modules[selection])
	module.initiate(directory)

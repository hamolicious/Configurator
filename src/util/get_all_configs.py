import json
from github import Github
import settings


def get_all_available_configs(gh:Github) -> list[str]:
	repo = gh.get_repo(settings.target_repo)
	modules = []
	for file in repo.get_contents('/'):
		modules.append(file.name)
	return modules






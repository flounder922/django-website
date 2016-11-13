from fabric.api import local

def prepare_deployment(branch_name):
	local('python manage.py test main')
	local('git add -p && git commit')
	local('git checkout master && git merge' + branch_name)

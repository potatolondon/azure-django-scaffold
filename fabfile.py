from fabric.api import task, local, warn_only


@task
def prepare(skip_static=False):
    """
    Will prepare the files for deployment
    """

    local('npm install')
    local('grunt build')

    with warn_only():
        local('git add staticfiles')
        local('git add {{ project_name }}/templates')
        local('git commit -m "PRODUCTION ONLY: Build static files."')

    files_to_remove = (
        '.bowerrc',
        '.editorcinfig',
        '.gitignore',
        '.jshintrc',
        'bower.json',
        'dev-only-package.json',
        'error.log',
        'fabfile.py',
        'Gruntfile.js',
        'migrate.sh',
        'README.md',
        'serve.sh',
        'flush_cache.py',
    )

    with warn_only():
        for file_ in files_to_remove:
            local('git rm {}'.format(file_))

    # store it
    local('git commit -m "PRODUCTION ONLY: Removing files."')

    if skip_static:
        local('touch .skipDjango')
        local('git add .skipDjango')
        local('git commit -m "PRODUCTION ONLY: Skip static files"')

from fabric.api import *

env.use_ssh_config = True

def deploy():
    with cd('apps/vahti/'):
        run('git pull')
        with prefix('workon django'):
            run('umask 0022 && ./manage.py collectstatic --noinput')
    run('supervisorctl restart vahti:*')

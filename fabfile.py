'''
Fabric examples for Dynamic Languages Community
'''

from pwd import getpwuid
from os import getuid, listdir
from fabric.api import run, local, env, prompt, execute, cd, settings
from fabric.api import parallel, task, serial, hosts
from sys import argv


#===============================================================================
# env.roledefs = {'myservers': ['HOST1_HERE', 'HOST2_HERE'],
#                'myhost': ['HOST3_HERE']
#                }
#===============================================================================

#===============================================================================
# if env.hosts == []:
#    env.hosts = ['HOST1_HERE', 'HOST2_HERE']
# 
# 
# if env.user == getpwuid(getuid())[0] and not ('-u' in argv or '--user' in argv):
#    env.user = 'USERNAME_HERE'
#    env.password = 'PASSWORD_HERE'
#===============================================================================


@task
def host_type():
    '''Get host type'''
    run('uname -s')


@task
#@hosts('localhost')
def host_and_date():
    with cd('/tmp'):
        run('pwd')
        if prompt('Get date and host type? (y/n)').lower() == 'y':
            execute(host_type)
            execute(serial_date)


def not_a_task():
    '''This is not a task'''
    run('uname -a')


@task
def listdir_py():
    '''List current folder content'''
    print 'Listing folder...'
    listdir('.')


@task
def listdir_sh():
    '''List current folder content'''
    print 'Listing folder...'
    run('ls .')


@task
def date():
    '''Get current local date'''
    local('date')


@task
@hosts('localhost')
def local_date():
    '''Get current local date with decorator'''
    local('date')


@task
@serial
def serial_date():
    '''Get current date (serial)'''
    run('date')


@task
@parallel(pool_size=5)
def parallel_date():
    '''Get current date in parallel'''
    run('date')


@task
def fail():
    '''Task intended to fail'''
    run('cat fileWhichShouldNeverEverExist12345.txt')


@task
def warn_fail():
    '''Task intended to fail but just warn'''
    with(settings(warn_only=True)):
        run('cat fileWhichShouldNeverEverExist12345.txt')


@task
def listdir(folder='.'):
    '''List given folder content'''
    print 'Listing folder...'
    run('ls {0}'.format(folder))



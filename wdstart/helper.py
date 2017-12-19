import os
import subprocess
import sys


def find_file(name, path=os.environ['PATH'], deep=False, partial=False):
    """Returns the path of a file in a directory"""

    paths = path.split(os.pathsep) if type(path) is str else path
    for p in paths:
        ret = __find_file(name, p, deep, partial)
        if ret:
            return ret


def __find_file(name, path, deep=False, partial=False):
    if deep:
        for root, dirs, files in os.walk(path):
            if partial:
                for file in files:
                    if name in file:
                        return os.path.join(root, file)
            else:
                if name in files:
                    return os.path.join(root, name)
    else:
        f = os.path.join(path, name)
        if os.path.isfile(f):
            return f


def find_selenium_server():
    """Returns the path of the 'standalone-server-standalone-x.x.x.jar' file."""

    for root, dirs, files in os.walk(os.getcwd()):
        for name in files:
            try:
                if '-'.join(name.split('-')[:3]) == 'selenium-server-standalone':
                    return os.path.join(root, name)
            except IndexError:
                pass


def find_executable(name):
    """Returns the path of binary file in a given directory"""

    if sys.platform.startswith('win') or os.name.startswith('os2'):
        name = name + '.exe'
    executable_path = find_file(name=name, path=os.getcwd())

    if executable_path:
        return executable_path
    else:
        print('[!] {name} not found in the working directory.'.format(name=name))


def start_selenium_server():
    """Starts the Java Standalone Selenium Server."""

    seleniumserver_path = find_selenium_server()
    if not seleniumserver_path:
        print('[!] The file "standalone-server-standalone-x.x.x.jar" not found.')
        return

    cmd = ['java', '-jar', seleniumserver_path]
    subprocess.Popen(cmd)

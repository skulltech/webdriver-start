import os
import subprocess
import sys



def find_file(name, path):
    """Returns the path of a file in a directory"""

    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


def find_selenium_server():
    """Returns the path of the 'standalone-server-standalone-x.x.x.jar' file."""

    for root, dirs, files in os.walk(os.getcwd()):
        for name in files:
            try:
                if '-'.join(name.split('-')[:3]) == 'selenium-server-standalone':
                    return os.path.join(root, name)
            except IndexError:
                pass


def find_binary_file(name):
    """Returns the path of binary file in a given directory"""

    binary_path = None

    if sys.platform.startswith('win'):
        binary_path = find_file(name=name + '.exe', path=os.getcwd())
    elif sys.platform.startswith('darwin') or sys.platform.startswith('linux'):
        binary_path = find_file(name=name, path=os.getcwd())

    if binary_path:
        return binary_path
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

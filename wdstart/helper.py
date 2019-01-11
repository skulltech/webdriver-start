import os
import sys


def find_file(name, path=os.getcwd(), deep=False, partial=False):
    """
    Searches for a file and returns its path upon finding it.

    Searches for a file with the given `name` in the list of directories
    mentioned in `path`. It also supports `deep` search (recursive) and
    `partial` search (searching for files having filename matching
    partially with the query) through the respective boolean arguments.

    Parameters
    ----------
    name : str
        The name of the file to search for.
    path : str or list of str, optional
        The list of directories to be searched. It can be either a 
        single str with the directory paths being seperated by
        `os.pathsep`, or a list of the directory path strings. The 
        default is the system `PATH`.
    deep : bool, optional
        Enables deep-searching, i.e. recursively looking for the file 
        in the sub-directories of the mentioned directories.
    partial : bool, optional
        Whether look for files having filename partially matching with 
        the query `name`.

    Returns
    -------
    str
        The path of the file. In case of multiple hits, it only return 
        the first one.
    """

    paths = path.split(os.pathsep) if type(path) is str else path
    for p in paths:
        ret = __find_file(name, p, deep, partial)
        if ret:
            return ret


def __find_file(name, path, deep=False, partial=False):
    """
    Searches for a file and returns its path upon finding it.

    Searches for a file with the given `name` in the list of directory
    mentioned in `path`. It also supports `deep` search (recursive) and
    `partial` search (searching for files having filename matching
    partially with the query) through the respective boolean arguments.
    This function is internally called by `find_file` for each of the
    input directory of that.


    Parameters
    ----------
    name : str
        The name of the file to search for.
    path : str
        The path of the directory to be searched.
    deep : bool, optional
        Enables deep-searching, i.e. recursively looking for the file 
        in the sub-directories of the mentioned directory.
    partial : bool, optional
        Whether look for files having filename partially matching with 
        the query `name`.

    Returns
    -------
    str
        The path of the file. In case of multiple hits, it only returns 
        the first one.
    """

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


def find_executable(name):
    """
    Returns the path of an executable file.

    Searches for an executable with the given name, first in the `PATH`, 
    then in the current directory (recursively). Upon finding the file,
    returns the full filepath of it.

    Parameters
    ----------
    name : str
        The name of the executable. This is platform-independent so 
        you don't have to include any platform-specific file extension 
        (such as `.exe`).

    Returns
    -------
    str
        The path of the executable file. In case of multiple hits, it 
        only returns the first one.
    """

    if sys.platform.startswith('win') or os.name.startswith('os2'):
        name = name + '.exe'

    executable_path = find_file(name, deep=True)
    return executable_path

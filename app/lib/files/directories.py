import os


def getFilesnamesAndFilepathsInDirectory(directory) -> list[dict[str, str]]:
    """
    Returns a list of filesnames in a directory.
    """
    filepaths = []

    for f in getFilesInDirectory(directory):
        filepaths.append({
            'filename': f,
            'filepath': os.path.join(directory, f)
        })

    return filepaths


def getFilesInDirectory(directory):
    """
    Returns a list of files in a directory.
    """
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]


def removeFilesInDirectory(directory):
    """
    Removes all files in a directory.
    """
    for f in getFilesInDirectory(directory):
        os.remove(os.path.join(directory, f))


def createDirectory(directory, deleteContent=False):
    """
    Creates a directory.
    """
    os.makedirs(directory, exist_ok=True)

    if deleteContent:
        removeFilesInDirectory(directory)

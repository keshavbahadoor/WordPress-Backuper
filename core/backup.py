import abc


class Backup(metaclass=abc.ABCMeta):

    def __init__(self):
        pass

    @abc.abstractmethod
    def backup_directory(self, source_directory, destination_directory):
        """
        Defines the method of backing up a given source directory to a given
        destination directory. This can be cloud storage, or local storage.
        Extend as needed.
        :param source_directory:
        :param destination_directory:
        :return:
        """
        pass

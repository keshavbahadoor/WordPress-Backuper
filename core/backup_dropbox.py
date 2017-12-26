from backup import Backup
import dropbox, os


class BackupDropbox(Backup):

    def __init__(self):
        self.dbx = dropbox.Dropbox('DROPBOX SECURITY STRING HERE')

    def backup_directory(self, source_directory, destination_directory):
        """
        Uploads all files of a specified source directory to a specified destination
        directory configured on DropBox
        :param source_directory:
        :param destination_directory:
        :return:
        """
        for root, dirs, files in os.walk(source_directory):
            for curr_file in files:
                try:
                    file_path = os.path.join(root, curr_file)
                    dest_path = os.path.join(destination_directory, os.path.relpath(file_path, source_directory))
                    print 'Uploading {} to {}'.format(file_path, dest_path)
                    with open(file_path) as f:
                        self.dbx.files_upload(f.read(), self.get_appropriate_dropbox_path(dest_path), mute=True)

                except Exception, e:
                    print 'Failed to upload {}'.format(e.message)

    def get_appropriate_dropbox_path(self, path):
        """
        Dropbox can only have '/' slashes in path.
        :param path:
        :return:
        """
        return path.replace('\\', '/')
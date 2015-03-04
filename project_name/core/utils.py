from logging import FileHandler


class NonLockingFileHandler(FileHandler):

    def emit(self, record):
        super(NonLockingFileHandler, self).emit(record)
        self.close()

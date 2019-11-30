"""Example business services module."""


class BaseService(object):
    """Service base class."""


class PhotosService(BaseService):
    """Photos service."""

    def __init__(self, logger, db):
        """Initializer."""
        self.logger = logger
        self.db = db

    def upload_photo(self, uid, photo_path):
        """Upload user photo."""
        self.logger.debug('Photo %s has been successfully uploaded by user %s',
                          photo_path, uid)

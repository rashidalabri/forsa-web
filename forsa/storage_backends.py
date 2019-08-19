from storages.backends.s3boto3 import S3Boto3Storage
from django_hashedfilenamestorage.storage import HashedFilenameMetaStorage


class MediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False


S3HashedFilenameStorage = HashedFilenameMetaStorage(
    storage_class=MediaStorage,
)

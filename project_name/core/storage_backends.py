from storages.backends.azure_storage import AzureStorage
from storages.utils import setting


class AzureStaticStorage(AzureStorage):
    azure_container = setting("AZURE_CONTAINER_STATIC")


class AzureMediaStorage(AzureStorage):
    azure_container = setting("AZURE_CONTAINER_MEDIA")

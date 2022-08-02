from webdav4.client import Client

from settings import NEXTCLOUD_PASSWORD, NEXTCLOUD_URL, NEXTCLOUD_USERNAME


class NextCloudConnection:
    def __init__(self):
        self.client = Client(NEXTCLOUD_URL, auth=(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD))

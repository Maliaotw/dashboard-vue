from imgurpython import ImgurClient
from django.conf import settings

def push_imgur(filename):
    # 連接
    client_id = settings.IMGUR_ID
    client_secret = settings.IMGUR_SECRET
    client = ImgurClient(client_id, client_secret)

    text = client.upload_from_path(filename)
    returnlink = str(text['link'])
    return returnlink

import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7341561892:AAHDXnPLYUxW0Qh5XG8ynGGY1lKW8PumNqk")
    API_ID = int(os.environ.get("API_ID", "14631157"))
    API_HASH = os.environ.get("API_HASH", "aa7c2b3be68a7488abdb9de6ce78d311")
    #Add your channel id. For force Subscribe.
    CHANNEL = os.environ.get("CHANNEL", "-1002106332206")
    #Skip or add your proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ''

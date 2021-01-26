import os

os.chdir(os.path.dirname(__file__))

PORT = 4443
USERS = {
    "tg": open("secret", "r").read() if os.path.exists("secret") else "",
}

MODES = {
    "classic": False,
    "secure": False,
    "tls": True,
}

TLS_DOMAIN = "www.ngrok.com"
AUTHTOKEN = "1nYi7egMPEFg5aIBMe8eEBNgG2C_3GkMnDGbAhUBmFGScUJm6"  # set to your ngrok's token
# AD_TAG = ""

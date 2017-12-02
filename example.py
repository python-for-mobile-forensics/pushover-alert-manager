from pushover_alerts import *
import os
from os.path import join, dirname
from dotenv import load_dotenv

# Load the ENV file
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

APIURL = os.environ.get("APIURL")
TOKEN = os.environ.get("PUSHTOKEN")
USER = os.environ.get("PUSHUSER")

msg = 'This is a test of the pushover system.'
pushover(APIURL,TOKEN,USER,msg)

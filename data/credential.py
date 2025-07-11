import os

from dotenv import load_dotenv

load_dotenv()


class Credential:
	STAGE = os.getenv("STAGE")
	
	USERNAME = os.getenv("USERNAME")
	PASSWORD = os.getenv("PASSWORD")

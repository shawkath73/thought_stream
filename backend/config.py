import os
from dotenv import load_dotenv

# This physically opens your .env file and loads the passwords into memory
load_dotenv()

class Config:
    # This grabs the specific URI string you saved earlier
    MONGO_URI = os.getenv("MONGO_URI")
    
    # This is the name of the specific database inside your MongoDB cluster
    DB_NAME = "thought_stream_db"
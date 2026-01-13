from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

import os
from dotenv import load_dotenv
load_dotenv()

print('DATABASE_URL =', os.getenv('DATABASE_URL'))

engine = ''
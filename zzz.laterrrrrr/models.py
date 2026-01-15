from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
import asyncio

import os
from dotenv import load_dotenv
load_dotenv()

database_url=os.getenv('DATABASE_URL')

engine = create_async_engine(database_url)
Base = declarative_base()




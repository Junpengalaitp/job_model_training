from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine('mysql://root:rootroot@localhost:3306/alaitp')

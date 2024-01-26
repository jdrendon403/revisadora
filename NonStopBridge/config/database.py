import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import dotenv_values

env = dotenv_values(".env")

host = env.get("MYSQL_HOST")
user = env.get("MYSQL_USER")
password = env.get("MYSQL_PASSWORD")
database = env.get("MYSQL_DB")
port = env.get("MYSQL_PORT")

url = "mysql+pymysql://"+user+":"+password+"@"+host+":"+port+"/"+database

engine = create_engine(url, echo=True)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# sqlite_file_name = "../database.sqlite"
# base_dir = os.path.dirname(os.path.realpath(__file__))

# database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"

# engine = create_engine(database_url, echo=True)

# Session = sessionmaker(bind=engine)

# Base = declarative_base()
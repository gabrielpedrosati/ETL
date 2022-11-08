
from sqlite3 import Timestamp
from pandas import DatetimeTZDtype
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import config


Base = declarative_base()

class Coins(Base):
    __tablename__ = 'Coins'  # if you use base it is obligatory
    id = Column(Integer, primary_key=True)  # obligatory
    name = Column(String)
    symbol = Column(String)
    data_added = Column(Text)
    last_updated = Column(Text)
    price = Column(Float)
    volume_24h = Column(Float)
   
    def start():
        string_connection = "postgresql://"+ config.db_user + ":" + config.db_password + "@" + config.db_hostname + ":" + config.db_port + "/"+ config.db_name
        print (string_connection)
        engine = create_engine(string_connection)
        Session = sessionmaker(bind=engine)
        session = Session()
        Base.metadata.create_all(engine)
        print ('\nTable created on database')
        return session, engine

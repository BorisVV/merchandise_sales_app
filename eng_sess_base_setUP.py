
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker



class E_S_B():
    ''' This class is for the Engine, Session and Base,
    created to be easier to call the connections
    '''
    Base = declarative_base()
    engine = create_engine('sqlite:///merchandise_sales.db', echo = False)
    Session = sessionmaker(bind=engine)

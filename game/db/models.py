from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine

engine = create_async_engine(os.getenv("DATABASE_URL"))
Base = declarative_base()

class PlayerModel(Base):
    __tablename__ = 'players'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    level = Column(Integer)
    stats = Column(JSON)
    inventory = Column(JSON)
    wallet_address = Column(String(100))
    encrypted_seed = Column(String(200))
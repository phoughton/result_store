from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Hand(Base):
    __tablename__ = 'hands'

    id = Column(Integer, primary_key=True)
    starter = Column(String)
    card1 = Column(String)
    card2 = Column(String)
    card3 = Column(String)
    card4 = Column(String)
    is_crib = Column(Boolean)
    timestamp = Column(DateTime, server_default=func.now())

    def to_dict(self):
        return {
            'id': self.id,
            'starter': self.starter,
            'hand': [
                self.card1,
                self.card2,
                self.card3,
                self.card4
            ],
            'is_crib': self.is_crib,
            'timestamp': self.timestamp.isoformat()
        }

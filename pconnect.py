from sqlalchemy import create_engine
from user_model import Base, Hand
from sqlalchemy.orm import sessionmaker
import json

engine = create_engine('postgresql://postgres:postgresql1215@172.17.0.4:5432/mydatabase')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new_hand = Hand(starter='JH', card1='AH', card2='2H',
                card3='3H', card4='4H', is_crib=False)
session.add(new_hand)
session.commit()

hands = session.query(Hand).all()
for hand in hands:
    print(json.dumps(hand.to_dict(), indent=4))

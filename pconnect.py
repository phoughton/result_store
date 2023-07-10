from sqlalchemy import create_engine
from user_model import Base, Hand
from sqlalchemy.orm import sessionmaker
import json
from decouple import config


password = config('DATABASE_PASSWORD')
ip = config('DATABASE_IP')
print(f'password: {password}')
print(f'ip: {ip}')

engine = create_engine(f"""postgresql://postgres:{password}@{ip}:5432/mydatabase""")

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

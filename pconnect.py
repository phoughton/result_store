from sqlalchemy import create_engine
from user_model import Base, Hand
from sqlalchemy.orm import sessionmaker
import json
from decouple import config


password = config('DATABASE_PASSWORD')
db_ip = config('DATABASE_IP')
db_name = config('DATABASE_NAME')
db_user = config('DATABASE_USER')
db_port = config('DATABASE_PORT')

engine = create_engine(
    f"""postgresql://{db_user}:{password}@{db_ip}:{db_port}/{db_name}""")

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

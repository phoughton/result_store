from sqlalchemy import create_engine
from user_model import Base, User
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgresql://postgres:postgresql1215@172.17.0.4:5432/mydatabase')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new_user = User(name='Pete H', email='Pete@example.com')
session.add(new_user)
session.commit()

users = session.query(User).all()
for user in users:
    print(user.name)

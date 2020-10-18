from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, joinedload
from sqlalchemy.schema import Column, ForeignKey, Table
from sqlalchemy.types import Integer, String
from sqlalchemy import create_engine
import logging

engine = create_engine("postgresql://sqlalchemy_test:password@localhost/sqlalchemy_test")

Base = declarative_base()

SessionFactory = sessionmaker(bind=engine)

session = SessionFactory()

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


# CREATE TABLE pony_handlers (
#   pony_id INTEGER NOT NULL,
#   handler_id INTEGER NOT NULL,
#   PRIMARY KEY (pony_id, handler_id),
#   FOREIGN KEY (pony_id) REFERENCES ponies(id),
#   FOREIGN KEY (handler_id) REFERENCES handlers(id)
# );
pony_handlers = Table(
    "pony_handlers",
    Base.metadata,
    Column("pony_id", ForeignKey("ponies.id"), primary_key=True),
    Column("handler_id", ForeignKey("handlers.id"), primary_key=True))



# CREATE TABLE owners (
#   id SERIAL PRIMARY KEY,
#   first_name VARCHAR(255) NOT NULL,
#   last_name VARCHAR(255) NOT NULL,
#   email VARCHAR(255) NOT NULL
# );
class Owner(Base):
    __tablename__ = 'owners'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    email = Column(String(255))

    ponies = relationship("Pony",
                          back_populates="owner",
                          cascade="all, delete-orphan")
# CREATE TABLE ponies (
#   id SERIAL PRIMARY KEY,
#   name VARCHAR(255) NOT NULL,
#   birth_year INTEGER NOT NULL,
#   breed VARCHAR(255),
#   owner_id INTEGER NOT NULL,
#   FOREIGN KEY (owner_id) REFERENCES owners(id)
# );
class Pony(Base):
    __tablename__ = 'ponies'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    birth_year = Column(Integer)
    breed = Column(String(255))
    owner_id = Column(Integer, ForeignKey("owners.id"))

    owner = relationship("Owner", back_populates="ponies")
    handlers = relationship("Handler",
                            secondary=pony_handlers,
                            back_populates="ponies")


class Handler(Base):
    __tablename__ = "handlers"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    employee_id = Column(String(12))

    ponies = relationship("Pony",
                          secondary=pony_handlers,
                          back_populates="handlers")


# Create an owner
owner = Owner(first_name="Lord",
              last_name="Dogknife",
              email="doggy@poodles.net")

# Create a pony
pony = Pony(name="Walking Walker",
            birth_year=3023,
            breed="Cyborg")

# Set the pony's owner
pony.owner = owner

# MAGIC: SQLAlchemy adds it to the ponies list!
print(owner.ponies)
# Prints [<Pony ...>]

you = Owner(first_name="Liz",
            last_name="Xu",
            email="Liz@example.com")

your_pony = Pony(name="Benny",
                 birth_year=2020,
                 breed="whatever you want",
                 owner=you)

print(you.id)         # > None
print(your_pony.id)   # > None

# The Session object has already been created and
# bound to the engine.
session.add(you)      # Connects you and your_pony objects
session.commit()      # Saves data to the database

print(you.id)         # > 4 (or whatever the new id is)
print(your_pony.id)   # > 4 (or whatever the new id is)


# All the code from above
print(your_pony.birth_year)    # > 2020

your_pony.birth_year = 2019
print(your_pony.birth_year)    # > 2019

session.commit()

print(your_pony.birth_year)    # > 2019

your_pony.name = "Mr. Fancy Pants"
your_pony.birth_year = 1896
print(your_pony.name)          # > Mr. Fancy Pants
print(your_pony.birth_year)    # > 1896

session.rollback()
print(your_pony.name)          # > your pony's original name
print(your_pony.birth_year)    # > 2019


session.delete(you)
session.commit()

pony_query = session.query(Pony)
print(pony_query, pony_query.count())

ponies = pony_query.all()
for pony in ponies:
  print(pony.name)

pony_id_4_query = session.query(Pony).get(4)
print(pony_id_4_query)

pony_query = session.query(Pony).filter(Pony.name.ilike("%u%")).filter(Pony.birth_year < 2015)
print(pony_query)

owner_query = session.query(Owner.first_name, Owner.last_name).order_by(Owner.last_name)

print(owner_query)

hirzai_owners = session.query(Owner) \
                       .join(Pony)  \
                       .filter(Pony.breed == "Hirzai")
for owner in hirzai_owners:
    print(owner.first_name, owner.last_name)


for owner in session.query(Owner):
    print(owner.first_name, owner.last_name)
    for pony in owner.ponies:
        print("\t", pony.name)

owners_and_ponies = session.query(Owner).options(joinedload(Owner.ponies))
for owner in owners_and_ponies:
    print(owner.first_name, owner.last_name)
    for pony in owner.ponies:
        print("\t", pony.name)


hirzai_owners_and_ponies = session.query(Owner) \
                                  .join(Pony)  \
                                  .filter(Pony.breed == "Hirzai") \
                                  .options(joinedload(Owner.ponies))
for owner in hirzai_owners_and_ponies:
    print(owner.first_name, owner.last_name)
    for pony in owner.ponies:
        print("\t", pony.name)


session.close()
engine.dispose()

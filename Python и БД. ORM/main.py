import json
from tables import create_tables, Publisher, Sale, Shop, Book, Stock
import sqlalchemy
from sqlalchemy.orm import sessionmaker

log = 'postgres'
pas = 'zapil43'
base = 'orm'

DSN = f'postgresql://{log}:{pas}@localhost:5432/{base}'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

with open('tests_data.json', 'r') as f:
    data = json.load(f)

for record in data:
    model = {
        'publisher': Publisher,
        'shop': Shop,
        'book': Book,
        'stock': Stock,
        'sale': Sale,
    }[record.get('model')]
    session.add(model(id=record.get('pk'), **record.get('fields')))
    session.commit()

for author in session.query(Publisher):
    print(author.id, author.name, end='\n')

num_author = int(input('Введите номер автора: '))

for el in session.query(Book.title, Shop.name, Sale.price, Sale.count, Sale.date_sale). \
        join(Publisher).join(Stock).join(Shop).join(Sale).filter(Publisher.id == num_author):

    print(f' {el.title} | {el.name} | {el.price} | {el.date_sale}')


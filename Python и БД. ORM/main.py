import json
from tables import create_tables, Publisher, Sale, Shop, Book, Stock
import sqlalchemy
from sqlalchemy.orm import sessionmaker

log = 'login'
pas = 'password'
base = 'base_name'

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
    print(author.id, author.name, end='\n\n')

num_author = int(input('Введите номер автора: '))

for p, b, s, s1, s2 in session.query(Publisher, Book, Stock, Shop, Sale).filter(Publisher.id == Book.id_publisher).filter(
    Stock.id_book == Book.id).filter(Shop.id == Stock.id_shop).filter(Sale.id_stock == Stock.id).filter(
    Publisher.id == num_author).distinct(Book.id).all():
    print(f' {b.title} | {s1.name} | {s2.price} | {s2.date_sale}')


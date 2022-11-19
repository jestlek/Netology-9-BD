import psycopg2


def create_tables(cur):
    """This function creates new DB"""

    cur.execute("""
        CREATE TABLE clients(
        client_id serial PRIMARY KEY,
        name varchar(60) NOT NULL,
        surname varchar(60)NOT NULL,
        email varchar(60)
        );""")

    cur.execute("""
        CREATE TABLE phones(
        phone_id serial PRIMARY KEY,
        phone varchar(60) UNIQUE,
        client_id integer REFERENCES clients(client_id)
        ); """)

    print('Таблицы успешно созданы')


def add_client(cur, name, surname, email):
    """This function adds new client in DB"""

    cur.execute("""
        INSERT INTO clients(name, surname, email)
        VALUES (%s, %s, %s);        
        """, (name, surname, email))

    print('Данные добавлены!')


def add_phone(cur, phone, id):
    """This function adds new phone in DB"""

    cur.execute("""
        INSERT INTO phones(phone, client_id)
        VALUES (%s, %s);        
        """, (phone, id))

    print('Данные добавлены!')


def update_client(cur, name=None, surname=None, email=None, id=None):
    """This function changes client info"""
    if name is not None and surname is not None and email is not None:
        cur.execute("""
            UPDATE clients
            SET name = %s, surname = %s, email = %s
            WHERE client_id = %s;
            """, (name, surname, email, id))

    elif name is not None and surname is not None and email is None:
        cur.execute("""
            UPDATE clients
            SET name = %s, surname = %s
            WHERE client_id = %s;
            """, (name, surname, id))

    elif name is not None and surname is None and email is not None:
        cur.execute("""
            UPDATE clients
            SET name = %s, email = %s
            WHERE client_id = %s;
            """, (name, email, id))

    elif name is None and surname is not None and email is not None:
        cur.execute("""
            UPDATE clients
            SET surname = %s, email = %s
            WHERE client_id = %s;
            """, (surname, email, id))

    elif name is None and surname is None and email is not None:
        cur.execute("""
            UPDATE clients
            SET email = %s
            WHERE client_id = %s;
            """, (email, id))

    elif name is None and surname is not None and email is None:
        cur.execute("""
                UPDATE clients
                SET surname = %s
                WHERE client_id = %s;
                """, (surname, id))

    elif name is not None and surname is None and email is None:
        cur.execute("""
                UPDATE clients
                SET name = %s
                WHERE client_id = %s;
                """, (name, id))

    print('Данные успешно обновлены!')


def delete_phone(cur, client_id):
    """This function deletes phone number by client_id"""

    cur.execute("""
        DELETE FROM phones
        WHERE client_id = %s;
        """, (client_id,))

    print('Телефон успешно удален!')


def delete_client(cur, client_id):
    """This function deletes clients info by client_id"""

    cur.execute("""
        DELETE FROM clients
        WHERE client_id = %s;
        """, (client_id,))

    print('Данные удалены!')


def find_client(cur, **values):
    """This function print client info"""
    for key, value in values.items():
        cur.execute(f"""SELECT * FROM clients as c 
                LEFT JOIN phones as p ON c.client_id = p.client_id 
                WHERE {key} = '{value}'
        """)
    print(cur.fetchone())


if __name__ == '__main__':
    conn = psycopg2.connect(database=input('Введите название базы: '), user=input('Введите имя пользователя: '),
                            password=input('Введите пароль: '))
    with conn.cursor() as cur:
        create_tables(cur)
        add_client(cur, 'Oleg', 'Petrov', 'petrov@mail.ru')
        add_client(cur, 'Vlad', 'Namchin', 'namchin@mail.ru')
        add_phone(cur, '+79153336569', '1')
        update_client(cur, 'Luka', id='2')
        delete_phone(cur, '1')
        delete_client(cur, '1')
        find_client(cur, name='Ivan')
        conn.commit()

    conn.close()

import psycopg2


def create_tables(conn):
    """This function creates new DB"""
    with conn.cursor() as cur:
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

        conn.commit()
        print('Таблицы успешно созданы')


def add_client(conn, name, surname, email):
    """This function adds new client in DB"""
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO clients(name, surname, email)
            VALUES (%s, %s, %s);        
            """, (name, surname, email))

        conn.commit()
        print('Данные добавлены!')


def add_phone(conn, phone, id):
    """This function adds new phone in DB"""
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO phones(phone, client_id)
            VALUES (%s, %s);        
            """, (phone, id))

        conn.commit()
        print('Данные добавлены!')


def update_client(conn, name, surname, email, id):
    """This function changes client info"""
    with conn.cursor() as cur:
        cur.execute("""
            UPDATE clients
            SET name = %s, surname = %s, email = %s
            WHERE client_id = %s;        
            """, (name, surname, email, id))

        conn.commit()
        print('Данные успешно обновлены!')


def delete_phone(conn, client_id):
    """This function deletes phone number by client_id"""
    with conn.cursor() as cur:
        cur.execute("""
            DELETE FROM phones
            WHERE client_id = %s;
            """, (client_id,))

        conn.commit()
        print('Телефон успешно удален!')


def delete_client(conn, client_id):
    """This function deletes clients info by client_id"""
    with conn.cursor() as cur:
        cur.execute("""
            DELETE FROM clients
            WHERE client_id = %s;
            """, (client_id,))

        conn.commit()
        print('Данные удалены!')


def find_client(conn, name=None, surname=None, email=None, phone=None):
    """This function print client info"""
    with conn.cursor() as cur:
        cur.execute("""
            SELECT * FROM clients as c
            LEFT JOIN phones as p ON c.client_id = p.client_id
            WHERE name LIKE %s OR surname LIKE %s OR email LIKE %s OR phone LIKE %s;            
            """, (name, surname, email, phone))

        conn.commit()
        print(cur.fetchone())


if __name__ == '__main__':
    conn = psycopg2.connect(database=input('Введите название базы: '), user=input('Введите имя пользователя: '),
                            password=input('Введите пароль: '))
    create_tables(conn)
    add_client(conn, 'Oleg', 'Petrov', 'petrov@mail.ru')
    add_client(conn, 'Vlad', 'Namchin', 'namchin@mail.ru')
    add_phone(conn,'+79153336569', '1')
    update_client(conn, 'Ivan', 'Losin', 'losin@mail.ru', '2')
    delete_phone(conn, '1')
    delete_client(conn, '1')
    find_client(conn, 'Ivan')

    conn.close()

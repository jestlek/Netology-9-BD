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


def update_client(cur, name, surname, email, id):
    """This function changes client info"""

    cur.execute("""
        UPDATE clients
        SET name = %s, surname = %s, email = %s
        WHERE client_id = %s;        
        """, (name, surname, email, id))

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


def find_client(cur, name=None, surname=None, email=None, phone=None):
    """This function print client info"""

    cur.execute("""SELECT * FROM clients as c 
                LEFT JOIN phones as p ON c.client_id = p.client_id 
                WHERE (name=%s OR name='None') 
                    AND (surname=%s OR surname='None') 
                    AND (email=%s OR email='None') 
                    AND (phone=%s OR phone='None');""", (name, surname, email, phone))

    print(cur.fetchone())


if __name__ == '__main__':
    conn = psycopg2.connect(database=input('Введите название базы: '), user=input('Введите имя пользователя: '),
                            password=input('Введите пароль: '))
    with conn.cursor() as cur:
        create_tables(cur)
        add_client(conn, 'Oleg', 'Petrov', 'petrov@mail.ru')
        add_client(conn, 'Vlad', 'Namchin', 'namchin@mail.ru')
        add_phone(conn,'+79153336569', '1')
        update_client(conn, 'Ivan', 'Losin', 'losin@mail.ru', '2')
        delete_phone(conn, '1')
        delete_client(conn, '1')
        find_client(cur, 'Ivan')

    conn.close()

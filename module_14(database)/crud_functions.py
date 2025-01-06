import sqlite3

def initiate_db():
    # Подключаемся к базе данных
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Проверяем, существует ли таблица Products
    c.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='Products'")
    if c.fetchone()[0] == 0:
        # Если таблицы нет, создаем ее
        c.execute("""CREATE TABLE Products (
                    id INTEGER PRIMARY KEY,
                    title TEXT NOT NULL,
                    description TEXT,
                    price INTEGER NOT NULL
                );
                """)
        print("Таблица Products создана.")
    # Проверяем, существует ли таблица Users
    c.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='Users'")
    if c.fetchone()[0] == 0:
        # Если таблицы нет, создаем ее
        c.execute("""CREATE TABLE Users (
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL,
                    email TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    balance INTEGER NOT NULL
                );
                """)
        print("Таблица Users создана.")


    # Добавляем несколько записей в таблицу
    products = [
        (1, 'Product1', "Первый товар", 100),
        (2, 'Product2', "Второй товар", 200),
        (3, 'Product3', "Третий товар", 300),
        (4, 'Product4', "Четвёртый товар", 400)
    ]

    def set_products(title, description, price):
        c.execute('INSERT INTO Products (title, description, price) VALUES (?,?,?)', (title, description, price))
    # for product in products:
    #     set_products(product[1],product[2],product[3])


    # Сохраняем изменения и закрываем соединение с базой данных
    conn.commit()
    conn.close()

def get_all_products():
    # Подключаемся к базе данных
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Выполняем запрос на получение всех записей из таблицы Products
    c.execute("SELECT * FROM Products")
    products = c.fetchall()

    # Закрываем соединение с базой данных
    conn.close()

    return products


def add_user(username, email, age):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    try:
        # Добавляем запись в таблицу Users
        cursor.execute('''
        INSERT INTO Users (username, email, age, balance)
        VALUES (?, ?, ?, ?)
        ''', (username, email, age, 1000))

        conn.commit()
        print(f"User {username} added successfully.")
    except sqlite3.IntegrityError:
        print(f"User {username} already exists.")
    finally:
        conn.close()


def is_included(username):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Проверяем, есть ли пользователь в таблице
    cursor.execute('''
    SELECT COUNT(*) FROM Users WHERE username = ?
    ''', (username,))

    count = cursor.fetchone()[0]
    conn.close()

    return count > 0





# Создаем таблицу Products, если она еще не существует, и добавляем несколько записей
initiate_db()


# Получаем все записи из таблицы Products
all_products = get_all_products()
print(all_products)


def close_base():
    return None
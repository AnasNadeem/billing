import psycopg2

DB_HOST = 'localhost'
DB_NAME = 'postgres'
DB_USER = 'postgres'
DB_PASS = 'Anas@123Great'

# DB_HOST = '206.189.140.222'
# DB_NAME = 'billingsoftwaredb'
# DB_USER = 'billinguser'
# DB_PASS = 'Mdbillingpassword@123'

def create_db():
    conn = psycopg2.connect(host=DB_HOST,database=DB_NAME, user=DB_USER, password=DB_PASS)
    cur = conn.cursor()
    
    # cur.execute('DROP TABLE bill')
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
        id SERIAL PRIMARY KEY,
        username varchar(100) NOT NULL UNIQUE,
        admin varchar(50) NOT NULL,
        email varchar(100),
        phone varchar(15),
        location varchar(100) NOT NULL,
        pass varchar NOT NULL
    );""")
    cur.execute("""CREATE TABLE IF NOT EXISTS inventory(
        pr_id SERIAL PRIMARY KEY,
        pr_name varchar(250) NOT NULL,
        stocks INTEGER NOT NULL,
        cost_price DECIMAL NOT NULL,
        sell_price DECIMAL NOT NULL,
        gst DECIMAL,
        ven_name varchar(100),
        ven_num varchar(100),
        location varchar(100) NOT NULL
    );""")

    cur.execute("""CREATE TABLE IF NOT EXISTS bill(
        bill_no SERIAL PRIMARY KEY,
        cus_name varchar(200) NOT NULL,
        cus_num varchar(200) NOT NULL,
        bill_file bytea NOT NULL,
        date varchar(200),
        location varchar(100) NOT NULL
    );""")
    conn.commit()
    cur.close()
    conn.close()

create_db()
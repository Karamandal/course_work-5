import psycopg2


def create_tables():
    """Создаёт таблицы"""
    conn = psycopg2.connect(
        dbname="123",
        user="postgres",
        password="Qwer951753",
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()
    """Удаление таблиц перед созданием"""
    cur.execute("DROP TABLE IF EXISTS employers CASCADE")
    cur.execute("DROP TABLE IF EXISTS vacancies CASCADE")

    """Создаёт таблицу с компаниями"""
    cur.execute('''
               CREATE TABLE employers(
               company_id SERIAL PRIMARY KEY ,
               company_name VARCHAR(150) UNIQUE NOT NULL,
               url_company TEXT
               )
               ''')

    """Создаёт таблицу с вакансиями"""
    cur.execute('''
           CREATE TABLE vacancies(
           vacancy_id SERIAL PRIMARY KEY,
           vacancy_name VARCHAR(150) NOT NULL,
           city_name VARCHAR(100),
           publish_date DATE,
           company_name VARCHAR(150) NOT NULL ,
           salary_from INTEGER,
           salary_to INTEGER,
           url_vacancy TEXT
           )
           ''')

    conn.commit()
    conn.close()

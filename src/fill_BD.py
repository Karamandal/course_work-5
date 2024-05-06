import psycopg2
from src.API import get_vacancies


def fill_tables(employer_ids, params):
    """Заполняет таблицы"""
    conn = psycopg2.connect(**params)
    conn.autocommit = True
    cur = conn.cursor()

    for employer_id in employer_ids:
        vacancies = get_vacancies(employer_id)

        for vacancy in vacancies['items']:
            company_name = vacancy['employer']['name']
            company_url = f"https://hh.ru/employers/{employer_id}"  # используем метод get

            """Выполняет запрос для вставки данных в таблицу employers"""
            cur.execute(""" 
                            INSERT INTO employers (company_name, url_company) 
                            SELECT %s, %s 
                            WHERE NOT EXISTS (SELECT 1 FROM employers WHERE company_name = %s)
                        """, (company_name, company_url, company_name))

            if vacancy['salary'] is not None and 'from' in vacancy['salary']:
                salary_from = vacancy['salary']['from']
            else:
                salary_from = None

            if vacancy['salary'] is not None and 'to' in vacancy['salary']:
                salary_to = vacancy['salary']['to']
            else:
                salary_to = None

            vacancy_name = vacancy['name']
            city_name = vacancy['area']['name']
            publish_date = vacancy['published_at']
            company_name = vacancy['employer']['name']
            url_vacancy = vacancy['alternate_url']

            """Выполняет запрос для вставки данных в таблицу vacancies"""
            cur.execute("""
                INSERT INTO vacancies (vacancy_name, city_name, publish_date, company_name, salary_from, salary_to, 
                url_vacancy)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
                        (vacancy_name, city_name, publish_date, company_name, salary_from, salary_to, url_vacancy))

        conn.commit()
    conn.close()

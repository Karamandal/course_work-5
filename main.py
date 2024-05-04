from src.API import get_vacancies, get_employers
from src.create_BD import create_tables
from src.fill_BD import fill_tables


def main():
    """Входные данные по компаниям"""
    employer_ids = [1479944, 64174, 3530, 8550, 13819, 48735, 50233, 51296, 55125, 56433]
    """Получает данные с HH"""
    get_employers(employer_ids)
    get_vacancies(employer_ids)
    """Создаёт таблицы"""
    create_tables()
    """Заполняет таблицы"""
    fill_tables(employer_ids)


if __name__ == '__main__':
    main()

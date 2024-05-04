import requests


def get_employers(employer_ids):
    """Получает данные с HH по компаниям"""
    url = f"https://api.hh.ru/employers/{employer_ids}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def get_vacancies(employer_ids):
    """Получает данные с HH по вакансиям"""
    url = f"https://api.hh.ru/vacancies?employer_id={employer_ids}&per_page=100"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

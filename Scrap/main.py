import json
import requests
import bs4
from bs4 import BeautifulSoup
import fake_headers
from unicodedata import normalize


class Web_scraping:

    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def _get_data(self):
        """Получение данных из сайта"""

        response_url = requests.get(url, headers=headers.generate())
        main_soup = bs4.BeautifulSoup(response_url.text, 'lxml')
        div_article_list_tag = main_soup.find('div', id='a11y-main-content')
        title_tag = div_article_list_tag.find_all('div', class_='serp-item')
        return title_tag

    def _parsed_data(self):
        """Обработка данных"""

        self.parsed_data = []
        for article_tag in self._get_data():
            link_tag = article_tag.find('a')
            salary_tag = article_tag.find('span', class_='bloko-header-section-2')
            name_company_tag = article_tag.find('div', class_='vacancy-serp-item__meta-info-company')
            city_tag = article_tag.find('div', attrs={'data-qa': 'vacancy-serp__vacancy-address'})
            city_hh = normalize('NFKC', city_tag.text)
            name_company_hh = normalize('NFKC', name_company_tag.text)
            if salary_tag == None:
                salary_hh = 'Зарплата не указана'
            else:
                salary_hh = normalize('NFKC', salary_tag.text)
            link_hh = link_tag['href']
            self.parsed_data.append({'link': link_hh,
                                     'salary': salary_hh,
                                     'company': name_company_hh,
                                     'city': city_hh})
        return self.parsed_data

    def download_parsed_data_json(self):
        """Скачивание данных в файл json"""

        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(self._parsed_data(), f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    headers = fake_headers.Headers(browser='chrome', os='win')
    url = 'https://spb.hh.ru/search/vacancy?text=python+django+flask&salary=&ored_clusters=true&area=2'
    scraping = Web_scraping(url, headers)
    scraping.download_parsed_data_json()








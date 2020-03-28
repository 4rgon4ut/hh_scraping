import scrapy


class HHspider(scrapy.Spider):
    name = 'hh_spider'
    start_urls = [
        'https://hh.ru/search/vacancy?clusters=true&area=1&enable_snippets=true&salary=&st=searchVacancy&text=Python'
        '+back-end&from=suggest_post']

    def parse(self, response):
        vacancy_selector = 'div.vacancy-serp-item__info a::attr(href)'
        for vacancy_url in response.css(vacancy_selector).getall():
            yield response.follow(vacancy_url, callback=self.extract_skills)

        next_page_selector = 'span.bloko-button-group ~ a::attr(href)'
        next_page = response.css(next_page_selector).get()
        yield response.follow(next_page, callback=self.parse)

    def extract_skills(self, response):
        skills_selector = 'div.bloko-tag-list span::text'
        skills = response.css(skills_selector).extract()

        salary_selector = 'div.vacancy-title span::text'
        salary = response.css(salary_selector).extract()

        yield {'skills': skills, 'salary': salary}

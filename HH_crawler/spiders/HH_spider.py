import scrapy


class HhSpider(scrapy.Spider):
    name = 'hh_spider'
    print('Now input start url for spider:')
    start_urls = [str(input())]

    def parse(self, response):

        # Iterates over list of vacancies urls
        # Pass every url to extract_skills()
        vacancy_selector = 'div.vacancy-serp-item__info a::attr(href)'
        for vacancy_url in response.css(vacancy_selector).getall():
            yield response.follow(vacancy_url, callback=self.extract_skills)

        # Find next page url and pass it to parse() for crawling
        next_page_selector = 'span.bloko-button-group ~ a::attr(href)'
        next_page = response.css(next_page_selector).get()
        yield response.follow(next_page, callback=self.parse)

    # Parse every vacancy page
    def extract_skills(self, response):
        skills_selector = 'div.bloko-tag-list span::text'
        skills = response.css(skills_selector).extract()

        salary_selector = 'div.vacancy-title span::text'
        salary = response.css(salary_selector).extract()

        yield {'skills': skills, 'salary': salary}

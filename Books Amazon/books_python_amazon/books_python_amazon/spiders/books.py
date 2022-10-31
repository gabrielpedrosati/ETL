import scrapy
from scrapy.http import Request
import mysql.connector
import json


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['amazon.com.br']
    start_urls = ['http://www.amazon.com.br/s?k=python']
        
    def parse(self,response):
        url = 'http://www.amazon.com.br'
        links = response.xpath('//*[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]/@href').extract()
        for link in links:
            absolute_url_path = url + link
            yield Request(absolute_url_path, callback=self.parse_page)

    def parse_page(self, response):
        title = response.xpath('//*[@id="productTitle"]/text()').extract_first()
        rating = response.xpath('//*[@class="a-icon-alt"]/text()').extract_first()
        author = response.xpath('//*[contains(@class, "author")]/a/text()').extract_first()
        description = response.xpath('//*[contains(@class, "a-expander-content")]/span/text()').extract_first()
        # price = (response.xpath('//*[@id="price"]/text()').extract_first()).replace("\xa0",' ')
        try:
            price = response.xpath('//*[@id="price"]/text()').extract_first()
        except:
            price = '999'
        try:
            availability = response.xpath('//*[@id="availability"]/span/text()').extract_first().strip()
        except:
            availability = 'None'
        try:
            editor_edicao = response.xpath('//*/span[starts-with(text(), "Editora") and contains(@class, "a-text-bold")]/following-sibling::span/text()').extract_first()
            editor = editor_edicao.split(';')[0]
        except:
            editor = 'None'
        try:
            edicao = editor_edicao.split(';')[1].strip()
        except:
            edicao = 'None'

        language = response.xpath('//*/span[starts-with(text(), "Idioma") and contains(@class, "a-text-bold")]/following-sibling::span/text()').extract_first()
        pages = response.xpath('//*/span[starts-with(text(), "Número de páginas") and contains(@class, "a-text-bold")]/following-sibling::span/text() | //*/span[starts-with(text(), "Capa comum") and contains(@class, "a-text-bold")]/following-sibling::span/text()').extract_first()

        yield {'Title':title,
                'Rating':rating,
                'Availability':availability,
                'Author':author,
                'Description':description,
                'Price':price,
                'Editor': editor,
                'Edicao':edicao,
                'Language':language,
                'Pages': pages}

    def close(self, reason):
        json_file_path = r'C:\Users\DELL\Documents\Dev\Python\Curso Web Scraping\class_01\books_python_amazon\books.json'
        conn = mysql.connector.connect(database='books_scrapy', user='root', password='', host='localhost')
        cursor = conn.cursor()
# with open(json_file_path, 'r') as j:
#      contents = json.load(j.read())

        with open(json_file_path, encoding='utf-8', errors='ignore') as json_data:
            data = json.load(json_data, strict=False)
            for v in data:
                try:
                    v['Description'] = v['Description'].replace('\'','')
                    v['Description'] = v['Description'].replace('\"','')
                except:
                    pass
                cursor.execute("INSERT INTO books (title, rating, author, description, price, availability, editor, language_book, pages) VALUES (\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\");".format(v['Title'],v['Rating'],v['Author'],v['Description'],v['Price'],v['Availability'],v['Editor'],v['Language'], v['Pages']))
                conn.commit()
                

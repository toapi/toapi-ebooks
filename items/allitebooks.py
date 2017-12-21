from toapi import Item, Css


class Page(Item):
    __base_url__ = "http://www.allitebooks.com"

    pages = Css('.pagination>.pages')
    current_page = Css('.pagination>.current')
    next_page = Css('.pagination>a', attr='href')

    def clean_next_page(self, value):
        if isinstance(value, list):
            return [i.get('href').replace('http://www.allitebooks.com/', 'http://127.0.0.1:5000/allitebooks/')
                    for i in value]
        else:
            return ['http://127.0.0.1:5000/' + value]

    class Meta:
        source = None
        route = {
            '/allitebooks/': '/',
            '/allitebooks/?s=:keyword': '/?s=:keyword',
            '/allitebooks/:keyword/': '/:keyword/',
            '/allitebooks/page/:path': '/page/:path'
        }


class Book(Item):
    __base_url__ = "http://www.allitebooks.com"

    book_list = Css('article>div.entry-body>header>.entry-title>a', attr='href')

    def clean_book_list(self, book_list):
        if isinstance(book_list, list):
            result = [
                {'id': str(index),
                 "name": value.text,
                 "url": value.get('href').replace('http://www.allitebooks.com/',
                                                  'http://127.0.0.1:5000/allitebooks-info/')
                 } for index, value in enumerate(book_list)
            ]
            return result
        else:
            return [{'id': '0', 'name': '', 'href': 'http://127.0.0.1:5000/' + book_list}]

    class Meta:
        source = None
        route = Page.Meta.route


class Detail(Item):
    __base_url__ = "http://www.allitebooks.com"

    title = Css('.single-title')
    abstract = Css('.entry-header>h4')
    cover = Css('.entry-body-thumbnail>a>img', attr='src')
    description = Css('.entry-content')
    pdf_url = Css('span.download-links>a', attr='href')

    def clean_pdf_url(self, pdf_url):
        if isinstance(pdf_url, list):
            return pdf_url[0].get('href')
        else:
            return pdf_url

    class Meta:
        source = None
        route = {'/allitebooks-info/:keyword': '/:keyword/'}

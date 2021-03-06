from toapi import Api
from items.allitebooks import Page, Book, Detail
from settings import MySettings

api = Api(settings=MySettings)

api.register(Page)
api.register(Book)
api.register(Detail)

if __name__ == '__main__':
    api.serve()

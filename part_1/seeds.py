import json

from mongoengine import NotUniqueError

from models import Author, Quote


def seed_authors():
    with open('authors.json', encoding='utf-8') as f:
        authors = json.load(f)

    for author in authors:
        try:
            Author(fullname=author['fullname'],
                   born_date=author['born_date'],
                   born_location=author['born_location'],
                   description=author['description']).save()
        except NotUniqueError:
            print(f'Author {author["fullname"]} already exists')


def seed_quotes():
    with open('quotes.json', encoding='utf-8') as f:
        quotes = json.load(f)

        for quote in quotes:
            Quote(tags=quote['tags'],
                  author=Author.objects(fullname=quote['author']).first(),
                  quote=quote['quote'].encode('utf-8')).save()


if __name__ == '__main__':
    seed_authors()
    seed_quotes()

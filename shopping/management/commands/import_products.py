import csv
from shopping.models import Products

from django.core.management import BaseCommand

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Input csv file')
    def handle(self, *args, **options):
        print('Import products')
        file_path = options['csv_file']
        #file_path = 'C:\\Users\\szaut\\OneDrive\\Asztali gép\\prooktatas\\django\\first_django_project\\shopping\\management\\commands\\products.csv'
        try:
            with open(file_path, encoding='utf-8') as f:
                #print(f.read())
                reader = csv.DictReader(f)
                for row in reader:
                    print(row)
                    #Products.objects.create(
                    #    name=row['name'],
                    #    price=row['price'],
                    #)
            print(Products.objects.all())
            print(self.style.SUCCESS(f'Products imported from {file_path}'))
        except FileNotFoundError:
            print(self.style.ERROR((f'File not found: {file_path}')))


                    
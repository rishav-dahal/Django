import os
import random
from faker import Faker

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learn.settings')

django.setup()
from template_example.models import AccessRecord, Topic, Webpage , Usercustom

fake = Faker()
topics = ['Python', 'Django', 'JavaScript', 'React', 'Machine Learning']

def add_topic():
    topic = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    topic.save()
    return topic

def populate(N=5):
    for entry in range(N):

        # Create a new topic
        top = add_topic()

        # Generate fake data for the webpage
        fake_url = fake.url()
        fake_name = fake.company()
        fake_date = fake.date()


        # Create a new webpage entry 
        webpage = Webpage.objects.get_or_create(topic=top, name=fake_name, url=fake_url)[0]

        # Create a new access record entry
        access_record = AccessRecord.objects.get_or_create(name=webpage, date=fake_date)[0]

        fake_first_name = fake.first_name()
        fake_last_name = fake.last_name()
        fake_email = fake.email()

        # Create a new user entry
        user = Usercustom.objects.get_or_create(
            first_name=fake_first_name,
            last_name=fake_last_name,
            email=fake_email
        )[0]

if __name__ == '__main__':
    print("Populating the database...")
    populate(20)  # Adjust the number of entries as needed
    print("Database populated successfully!")
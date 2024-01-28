import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djproject.settings')
import django
django.setup()

from testapp.models import HydJobs
from faker import Faker
from random import randint

fake = Faker()

def phonenumbergen():
    d1 = randint(7, 9)
    num = str(d1)
    for i in range(9):
        num += str(randint(0, 9))
    return int(num)

def populate(n):
    for _ in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements=('Project Manager', 'Team Leader', 'Software Engineer'))
        feligibility = fake.random_element(elements=('B.Tech', 'M.Tech', 'MCA', 'PhD'))
        faddress = fake.address()
        femail = fake.email()
        fphonenumber = phonenumbergen()

        hydjobs_instance, created = HydJobs.objects.get_or_create(
            date=fdate,
            company=fcompany,
            title=ftitle,
            eligibility=feligibility,
            address=faddress,
            email=femail,
            phonenumber=fphonenumber
        )
        # Optional: Print created instances for verification
        if created:
            print(f"Created job: {hydjobs_instance}")

# Call the populate function with the desired number of entries
populate(25)



import csv
import sys

from ims.ims import IMS
from ims.person import Person

data = IMS(sys.argv[1])
with open('persons.csv', 'w', newline='') as csv_file:
    file_writer = csv.writer(csv_file, delimiter=';')
    file_writer.writerow(['ID', 'GIVENNAME', 'SN'])
    for person in data.persons(role='Student'):
        person_obj = Person(person)
        identifier = person_obj.id()
        first = person_obj.first_name()
        last = person_obj.last_name()

        file_writer.writerow([identifier, first, last])

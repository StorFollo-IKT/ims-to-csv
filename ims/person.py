class Person:
    def __init__(self, person):
        self.person = person

    def last_name(self):
        return self.person.find('name/n/family').text

    def first_name(self):
        return self.person.find('name/n/given').text

    def id(self):
        return self.person.find('sourcedid/id').text

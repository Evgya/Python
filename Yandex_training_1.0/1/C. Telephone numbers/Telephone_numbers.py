class Contacts:
    def __init__(self):
        self.contacts = set()

    def is_in_contact(self, number):
        number = "".join(filter(lambda x: x.isdigit(), number))
        if len(number) == 7:
            return ("+7495" + number) in self.contacts
        else:
            return "+7" + number[1:] in self.contacts

    def add_number(self, number):
        number = "".join(filter(lambda x: x.isdigit(), number))
        if len(number) == 7:
            self.contacts.add("+7495" + number)
        else:
            self.contacts.add("+7" + number[1:])

contacts = Contacts()
contacts.add_number(input())
for _ in range(3):
    if contacts.is_in_contact(input()):
        print("YES")
    else:
        print("NO")

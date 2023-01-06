from faker import Faker
f = Faker()

# name = f.name();
# address = f.address();
# email = f.email();

#Création d'une liste de noms
def user_list(how_many):
    FirstName = []
    LastName = []
    Birthday = []
    Country = []
    Address = []
    Email = []
    PhoneNumber = []
    for i in range(0,how_many):
        FirstName.append(f.first_name())
        LastName.append(f.last_name)
        Address.append(f.address())
        Birthday.append(f.date())
        Country.append(f.country())
        Email.append(f.email())
        PhoneNumber.append(f.phone_number())
    return FirstName, LastName, Address, Birthday, Country, Email, PhoneNumber



print(user_list(2));
#print(f.name());
#print(f.address());
#print(f.email());
#print(f.date())




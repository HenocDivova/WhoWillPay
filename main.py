 # CODING CHALLENGE "WHO WILL PAY THE BILL"

names_string = input("Give me everybody's name separated with a comma \n")
names = names_string.split(", ")

import random
amount_of_people = (len(names))

random_choice = random.randint(0, amount_of_people -1)
person_paying = names[random_choice]
print(f"The person who has to pay the bill is {person_paying} ")
# OR
# person_paying = random.choice(names)
# print(f"{person_paying} has to pay the bill")
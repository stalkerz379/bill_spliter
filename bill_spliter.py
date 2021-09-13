import random


def people_to_join_the_dinner():
    number_of_people = int(input('Enter the number of friends joining (including you)\n'))
    people = {}
    if number_of_people <= 0:
        return people
    else:
        print('Enter the name of every friend (including you), each on a new line')
        for person in range(0, number_of_people):
            name = input()
            people.setdefault(name, 0)
    return people


def split_the_bill():
    people = people_to_join_the_dinner()
    if len(people) == 0:
        return people, 0
    total_bill = int(input('Enter the total bill value\n'))
    for name in people.keys():
        people[name] += round(total_bill / len(people), 2)
    return people, total_bill


def who_is_lucky():
    people, total_bill = split_the_bill()
    if len(people) == 0:
        return 'No one is joining for the party'
    option = input('Do you want to use the "Who is lucky?" feature? Write Yes/No\n').lower()
    if option == 'no':
        print('No one is going to be lucky')
        return people
    else:
        lucky_name = random.choice(list(people.keys()))
        print(f'{lucky_name} is the lucky one!')
        for name in people.keys():
            if name == lucky_name:
                people[lucky_name] = 0
            else:
                people[name] = total_bill / (len(people) - 1)
        return people


print(who_is_lucky())

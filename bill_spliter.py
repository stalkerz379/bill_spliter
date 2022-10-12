import random


def read_num(message_for_input=None, invalid_value_message=None) -> int:
    try:
        user_num = int(input(message_for_input))
        return user_num
    except ValueError:
        print(invalid_value_message if invalid_value_message else '')
        return read_num(message_for_input, invalid_value_message)


def validate_input(valid_options: tuple, invalid_input_message=None, input_message=None) -> str:
    user_input = input(input_message).lower()
    while user_input not in valid_options:
        print(invalid_input_message if invalid_input_message else '')
        user_input = input(input_message).lower()
    return user_input


def people_to_join_the_dinner() -> dict:
    number_of_people = read_num(message_for_input='Enter the number of friends joining (including you)\n',
                                invalid_value_message='Please, enter an integer')
    people = {}
    if number_of_people <= 0:
        print('No one is joining for the party')
        exit()
    print('Enter the name of every friend (including you), each on a new line')
    for person in range(0, number_of_people):
        name = input()
        people.setdefault(name, 0)
    return people


def split_the_bill() -> tuple[dict, int]:
    people = people_to_join_the_dinner()
    total_bill = read_num('Enter the total bill value\n', 'Please, enter a number')
    for name in people.keys():
        people[name] += round(total_bill / len(people), 2)
    return people, total_bill


def who_is_lucky(people: dict, total_bill: int) -> dict:
    option = validate_input(('yes', 'no'),
                            input_message='Do you want to use the "Who is lucky?" feature? Write Yes/No\n',
                            invalid_input_message='Please, select one of the possible options')
    if option == 'no':
        print('No one is going to be lucky')
        return people
    elif len(people) == 1:
        print('Cannot select lucky one since only 1 person joined the dinner')
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


if __name__ == '__main__':
    people, total_bill = split_the_bill()
    print(who_is_lucky(people, total_bill))

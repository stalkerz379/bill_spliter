# bill_spliter
## Stage 1: Invite your friends
### Description
You have planned a dinner with your friends today. It's the right time to add them to your program. You need to be sure how many friends are joining you for dinner including you.

The idea is to take names from user input. Store them in a dictionary.

For example, if five friends are joining including you, you need to add five people to the dictionary so that you can access/update the corresponding bill value later.

### Objectives
In this stage your program should perform the following steps:

- [x] Take user input — how many people want to join, including the user;
- [x] In case of an invalid number of people (zero or negative), "No one is joining for the party" is expected as an output;
- [x] Otherwise, take the friends' names as input, iteratively;
- [x] Store them in a dictionary initialized with zeros;
- [x] Print out the dictionary.

To communicate with the user, please use the prompts specified in the examples. Note that here and in the following stages we expect you to take every input in a new line.

## Stage 2: The bill has arrived
### Description
It's bill time! Let's split the bill among everyone and update the values in the dictionary you have created in the previous stage.

Since we don't want to deal with too many decimals (who carries that much change anyway?), round the split amount to two decimal places and then update the dictionary with the split values.

### Objectives

In this stage your program should perform the following steps together with the steps of the previous stage:

- [x] If there are no people to split the bill (the number of friends is 0 or an invalid input), output "No one is joining for the party";
- [x] Else, take user input: the final bill;
- [x] Split the total bill equally among everyone;
- [x] Round the split value to two decimal places;
- [x] Update the dictionary with the split values;
- [x] Print the updated dictionary.

## Stage 3: The Lucky One
### Description
In this stage, you need to add a new feature to the project — pick one name from the dictionary at random; this person's share will be paid by others. Make it a lucky day for somebody!

Make sure you give your users a choice whether they want to use this feature or not. Don't turn it on by default.

After picking a random name, print it so that everyone knows who is the lucky one.

### Objectives
In this stage your program should perform the following steps together with the steps from the previous stages:

- [x] In case of an invalid number of people, "No one is joining for the party" is expected as an output;
- [x] Otherwise, ask the user whether they want to use the "Who is lucky?" feature;
- [x] Take input from the user;
- [x] If a user wants to use the feature (Yes), choose a name from the dictionary keys at random and print the following: {Name} is the lucky one!;
- [x] If the user enters anything else, print No one is going to be lucky.

## Stage 4:
### Description
It's the right time to update your dictionary with new split values to make our "Who is lucky?" feature better. First, we need to recalculate the split value for everyone. Make sure that our lucky one pays 0.

Recalculate the split value for n-1 people where n is the total length of the dictionary and update the values in the dictionary with the new split value for everyone.

If a user decides not to use the "Who is lucky" feature, print the original dictionary.

### Objectives
In this stage your program should perform the following steps together with the steps from the previous stages:

- [x] In case of an invalid number of people, "No one is joining for the party" is expected as an output;
- [x] Otherwise, if the user choice is Yes, re-split the bill according to the feature;
- [x] Round the split value to two decimal places;
- [x] Update the dictionary with new split values and 0 for the lucky person;
- [x] Print the updated dictionary;
- [x] If the user entered anything else instead of Yes, print the original dictionary.

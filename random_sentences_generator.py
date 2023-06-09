import random

names = ['Kris', 'Toni', 'Mike', 'Peter', 'Dave']
places = ['Varna', 'Sofia', 'Plovdiv', 'Bourgas']
verbs = ['eats', 'holds', 'sees', 'play with', 'brings', 'ride']
nouns = ['stones', 'cake', 'apple', 'laptop', 'bikes']
adverbs = ['slowly', 'diligently', 'warmly', 'sadly', 'rapidly']
details = ['near the river', 'at home', 'in the park']


def get_random_word(words):
    return random.choice(words)


print('Welcome to the random generator.')
while True:
    random_name = get_random_word(names)
    random_place = get_random_word(places)
    random_verb = get_random_word(verbs)
    random_noun = get_random_word(nouns)
    random_adverb = get_random_word(adverbs)
    random_detail = get_random_word(details)

    print(f'{random_name} from {random_place} {random_adverb} {random_verb} {random_noun}.')
    input('Click [Enter] to generate a new one. ')

# Description #
# Program that generate random sentences based on preloaded words.
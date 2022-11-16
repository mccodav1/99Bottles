# 99 bottles of beer
def get_bottle_count():
    bottles = -1
    while bottles < 1:
        try:
            print('How many bottles are on the wall?')
            bottles = int(input())
            if bottles < 1:
                print('Enter at least one bottle bro!')
        except ValueError:
            print('Enter an integer, silly.')
    return bottles

    
bottles = get_bottle_count()
while bottles >0:
    next_bottles = bottles-1
    if bottles == 1:
        word = 'bottle'
    else:
        word = 'bottles'
    if next_bottles == 1:
        next_word = 'bottle'
    else:
        next_word = 'bottles'
    print(bottles, word, 'of beer on the wall,', bottles, word, 'of beer, take one down, pass it around,', next_bottles, next_word, 'of beer on the wall!\n')
    bottles -= 1

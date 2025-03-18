Words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
N = int(input('Enter a number: '))
if N < 20:
    print('Your written number is :',Words[N])
else:
    print('Number out of range')
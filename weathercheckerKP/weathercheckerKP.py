# WeathercheckerKP ver.0.00.0.3
# Changlog: 0.00.0.1 -> 0.00.0.2:
# => More branches in line 14
# => New variable "umb" define by new input
# Changlog: 0.00.0.2 -> 0.00.0.3:
# => Replace 3 lies of prit to while
# print, input, if, else, assigments, bool, comparisons, basic branches
# Any input = True // No input == False
# Code inspired by https://automatetheboringstuff.com/chapter2/
# Code under developed :)
# ToDo: 
# => Script to auto chagelog
# => Input from real source

print('It is raining?:')
x = input(bool)
rain = x
print ('It is windy:')
y = input(bool)
wind = y
if rain and wind:
    print('You need a jacket and umbrella')
    print('Do you have umbrella?')
    z = input(bool)
    umb = z
    if not umb:
        print('Stay home')
    else:
        print('Is raining man!!! Halleluya')
if rain != wind:
    print('Better to take a jacket')
if not rain and not wind:
    print('Anyway you go allways take a weather with you')
count = 0
while count < 5:
    print('.')
    count += 1
print('WeathercheckerKP ver.0.00.0.1 by @Hubadev')

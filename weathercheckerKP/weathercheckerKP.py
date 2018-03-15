# WeathercheckerKP ver.0.00.0.2
# Changes:
# => More branches in line 14
# => New variable "umb" define by new input
# print, input, if, else, assigments, bool, comparisons, basic branches
# Any input = True // No input == False
# Code inspired by https://automatetheboringstuff.com/chapter2/
# Code under developed :)

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
print(".")
print(".")
print(".")
print('WeathercheckerKP ver.0.00.0.1 by @Hubadev')

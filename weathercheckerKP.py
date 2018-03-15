# WeathercheckerKP ver.0.00.01
# print, input, if, assigments, bool, com, comparisons
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
if rain != wind:
    print('Better to take a jacket')
if not rain and not wind:
    print('Anyway you go allways take a weather with you')
print(".")
print(".")
print(".")
print('Whetherchecker ver.0.00.1 by @Hubadev')

# My own interpretation of code what i found on https://automatetheboringstuff.com/chapter1/.
# I change that code to pretending that he got a error(based on your input) and if you to old, saddly, you not allow to trip
# + some data type changes.


print('What is your name?')
name = input()
print('Error: &&&&##' +str(name[1:]) + '33##11' +str(name)[0:-3] + '!QQ@@#') #error simulation :D 
print('Status: error fixed') # autofixed simulation xD
print('...')
print('...')
print('It is good to meet you, ' + name)
print('Nice error mate? BTW length of your name is:')
print(len(name))
print('What is your age?')
myAge = input(int)
if int(myAge) >= 20:
    print('To old for school trip... anyway:')
if int(myAge) <= 20:
    print('Welcome abord young being! anyway:')
print('You will be ' + str(int(myAge) + 1) + ' in a year.')

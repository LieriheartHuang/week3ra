### 
### Author: wenjunhuang
### Course: CSc 110
### Description: Describe your program with one
###              or more sentences of text.
###

print('-----------------------------')
print('----- WHERE\'S THE MONEY -----')
print('-----------------------------')
a=int(input('What is your annual salary?\n'))
if type(a)!=int
    print('Must enter positive integer for saraly.')
elif a<=0
    print('Must enter positive integer for saraly.')

b=int(input('How much is your monthly mortgage or rent?\n'))
if type(b)!=int
    print('Must enter positive integer for rent.')
elif b<=0
    print('Must enter positive integer for rent.)
c=int(input('What do you spend on bills monthly?\n'))
if type(c)!=int
    print('Must enter positive integer for bills.')
elif c<=0
    print('Must enter positive integer for bills.')
d=int(input('What are your weekly grocery/food expenses?\n'))
if type(d)!=int
    print('Must enter positive integer for food.')
elif d<=0
    print('Must enter positive integer for food.')

e=int(input('How much do you spend on travel annually?\n'))
if type(e)!=int
    print('Must enter positive integer for travel annually.')
elif e<=0
    print('Must enter positive integer for travel annually.')
print(' ')
if a<=15000:
    f=0.1
elif a<=75000:
    f=0.2
elif a<=200000:
    f=0.25
else:
    f=0.3

g=a-12*b-12*c-52*d-e-f*a
h=12*b
      
      
      
      
print('------------------------------------------------------------------')
print('See the financial breakdown below, based on a salary of $'+str(a))
print('------------------------------------------------------------------')
print('| mortgage/rent | $  '+"{:>8d}".format(h),'|',"{:3.1%}".format(h/a),'|'+int(h/a)*'#')
print('|         bills | $  '+"{:>8d}".format(12*c),'|',"{:3.1%}".format(12*c/a)+' | '+int(12*c/a)*'#')
print('|          food | $  '+"{:>8d}".format(52*d),'|',"{:3.1%}".format(52*d/a)+' | '+int(52*d/a)*'#')
print('|        travel | $  '+"{:>8d}".format(e),'|',"{:3.1%}".format(e/a)+' | '+int(e/a)*'#')
print('|           tax | $  '+"{:>8d}".format(int(f*a)),'|',"{:3.1%}".format(f)+' | '+int(f)*'#')
print('|         extra | $  '+"{:>8d}".format(int(g)),'|',"{:3.1%}".format(g/a)+' | '+int(g/a)*'#')
print('------------------------------------------------------------------')
if g<=0:
    print('>>> WARNING: DEFICIT <<<')
if a>75000:
    print('>>> TAX LIMIT REACHED <<<')

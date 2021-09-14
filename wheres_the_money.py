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

b=int(input('How much is your monthly mortgage or rent?\n'))
c=int(input('What do you spend on bills monthly?\n'))

d=int(input('What are your weekly grocery/food expenses?\n'))

e=int(input('How much do you spend on travel annually?\n'))
      
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
print('See the financial breakdown below, based on a salary of $'+a)
print('------------------------------------------------------------------')
print('| mortgage/rent | $  '+"{:>10d}".format(h)+ '|'+"{:3.1%}"format(h/a)+' | '+int(h/a)*'#')
print('|         bills | $  '+"{:>10d}".format(12*c)+ '|'+"{:3.1%}"format(12*c/a)+' | '+int(12*c/a)*'#')
print('|          food | $  '+"{:>10d}".format(52*d)+ '|'+"{:3.1%}"format(52*d/a)+' | '+int(52*d/a)*'#')
print('|        travel | $  '+"{:>10d}".format(e)+ '|'+"{:3.1%}"format(e/a)+' | '+int(e/a)*'#')
print('|           tax | $  '+"{:>10d}".format(f*a)+ '|'+"{:3.1%}"format(f)+' | '+int(f)*'#')
print('|         extra | $  '+"{:>10d}".format(g)+ '|'+"{:3.1%}"format(g/a)+' | '+int(g/a)*'#')
print('------------------------------------------------------------------')
if g<=0
    print('>>> WARNING: DEFICIT <<<')
if a>75000
    print('>>> TAX LIMIT REACHED <<<')

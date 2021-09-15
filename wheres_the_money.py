### 
### Author: wenjunhuang
### Course: CSc 110
### Description: Describe your program with one
###              or more sentences of text.
###

print('-----------------------------')
print('----- WHERE\'S THE MONEY -----')
print('-----------------------------')
saraly=int(input('What is your annual salary?\n'))

rent=int(input('How much is your monthly mortgage or rent?\n'))
bill=int(input('What do you spend on bills monthly?\n'))

food=int(input('What are your weekly grocery/food expenses?\n'))

travel=int(input('How much do you spend on travel annually?\n'))
print(' ')
if saraly<=15000:
    f=0.1
elif saraly<=75000:
    f=0.2
elif saraly<=200000:
    f=0.25
else:
    f=0.3

g=saraly-12*rent-12*bill-52*food-travel-f*saraly
h=12*rent
      
      
      
      
print('------------------------------------------------------------------')
print('See the financial breakdown below, based on a salary of $'+str(saraly))
print('------------------------------------------------------------------')
print('| mortgage/rent | $  '+"{:>7d}".format(h),'|',"{:3.1%}".format(h/saraly),'|'+int(h/saraly)*'#')
print('|         bills | $  '+"{:>7d}".format(12*bill),'|',"{:3.1%}".format(12*bill/saraly)+' | '+int(12*bill/saraly)*'#')
print('|          food | $  '+"{:>7d}".format(52*food),'|',"{:3.1%}".format(52*food/a)+' | '+int(52*food/a)*'#')
print('|        travel | $  '+"{:>7d}".format(travel),'|',"{:3.1%}".format(travel/saraly)+' | '+int(travel/saraly)*'#')
print('|           tax | $  '+"{:>7d}".format(int(f*saraly)),'|',"{:3.1%}".format(f)+' | '+int(f)*'#')
print('|         extra | $  '+"{:>7d}".format(int(g)),'|',"{:3.1%}".format(g/saraly)+' | '+int(g/saraly)*'#')
print('------------------------------------------------------------------')
if g<=0:
    print('>>> WARNING: DEFICIT <<<')
if saraly>75000:
    print('>>> TAX LIMIT REACHED <<<')


### 
### Author: wenjunhuang
### Course: CSc 110
### Description: Describe your program with one
###              or more sentences of text.
###

print('-----------------------------')
print('----- WHERE\'S THE MONEY -----')
print('-----------------------------')
a=int(input('What is your annual salary?'))

b=int(input('How much is your monthly mortgage or rent?'))
c=int(input('What do you spend on bills monthly?'))

d=int(input('What are your weekly grocery/food expenses?'))

e=int(input('How much do you spend on travel annually?'))
      
      if a<=15000:
            f=0.1
      elif a<=75000:
            f=0.2
      elif a<=200000:
            f=0.25
      else:
            f=0.3
      
      g=a-12*b-12*c-52*d-e-f*a
      
      
      
      
      
      
      
print('------------------------------------------------------------------')
print('See the financial breakdown below, based on a salary of $'+a)
print('------------------------------------------------------------------')
print('| mortgage/rent | $  '+12*b+' |  24.0% | '+'#')
print('|         bills | $  '+12*c+' |   9.6% | '+'#')
print('|          food | $  '+52*d+' |  20.8% | '+'#')
print('|        travel | $  '+e+' |   5.0% | '+'#')
print('|           tax | $  '+f*a+' |  20.0% | '+'#')
print('|         extra | $  '+g+' |  20.6% | '+'#')
print('------------------------------------------------------------------')
      if g<=0
            print('>>> WARNING: DEFICIT <<<')
      if a>75000
            print('>>> TAX LIMIT REACHED <<<')

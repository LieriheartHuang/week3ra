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
if (not isinstance(a,int)):
    print('Must enter positive integer for saraly.')
if a<=0:
    print('Must enter positive integer for saraly.')

b=int(input('How much is your monthly mortgage or rent?\n'))
if (not isinstance(b,int)):
    print('Must enter positive integer for rent.')
if b<=0:
    print('Must enter positive integer for rent.')
c=int(input('What do you spend on bills monthly?\n'))
if (not isinstance(c,int)):
    print('Must enter positive integer for bills.')
if c<=0:
    print('Must enter positive integer for bills.')
d=int(input('What are your weekly grocery/food expenses?\n'))
if (not isinstance(d,int)):
    print('Must enter positive integer for food.')
if d<=0:
    print('Must enter positive integer for food.')

e=int(input('How much do you spend on travel annually?\n'))
if (not isinstance(e,int)):
    print('Must enter positive integer for travel annually.')
if e<=0:
    print('Must enter positive integer for travel annually.')
print(' ')
if a<15000:
    f=0.1
elif a<75000:
    f=0.2
elif a<2000000:
    f=0.25
else:
    f=0.3

g=a-12*b-12*c-52*d-e-f*a
h=12*b
      
      
      
      
print('------------------------------------------'+int(max(100*h/a,12*100*c/a,52*100*d/a,100*e/a,100*f,100*g/a))*'-')
print('See the financial breakdown below, based on a salary of $'+str(a))
print('------------------------------------------'+int(max(100*h/a,12*100*c/a,52*100*d/a,100*e/a,100*f,100*g/a))*'-')
print('| mortgage/rent | $ '"{:10,.2f}".format(h),'|',"{:6.1%}".format(h/a),'|',int(100*h/a)*'#')
print('|         bills | $ '"{:10,.2f}".format(12*c),'|',"{:6.1%}".format(12*c/a),'|',int(12*100*c/a)*'#')
print('|          food | $ '"{:10,.2f}".format(52*d),'|',"{:6.1%}".format(52*d/a),'|',int(52*100*d/a)*'#')
print('|        travel | $ '"{:10,.2f}".format(e),'|',"{:6.1%}".format(e/a),'|',int(100*e/a)*'#')
print('|           tax | $ '"{:10,.2f}".format(f*a),'|',"{:6.1%}".format(f),'|',int(100*f)*'#')
print('|         extra | $ '"{:10,.2f}".format(g),'|',"{:6.1%}".format(g/a),'|',int(100*g/a)*'#')
print('------------------------------------------'+int(max(100*h/a,12*100*c/a,52*100*d/a,100*e/a,100*f,100*g/a))*'-')
if g<=0:
    print('>>> WARNING: DEFICIT <<<')
if a*f>75000:
    print('>>> TAX LIMIT REACHED <<<')

import turtle
s=turtle.Screen()
s.setup(1.0,1.0)
t1=turtle.Turtle()
t2=turtle.Turtle()
t4=turtle.Turtle()
t8=turtle.Turtle()
t16=turtle.Turtle()
tw=turtle.Turtle()
tw.ht()
s.register_shape('1.gif')
s.register_shape('2.gif')
s.register_shape('4.gif')
s.register_shape('8.gif')
s.register_shape('16.gif')
t16.shape('16.gif')
t16.up()
t16.goto(-350,200)

t8.shape('8.gif')
t8.up()
t8.goto(-250,200)

t4.shape('4.gif')
t4.up()
t4.goto(-150,200)

t2.shape('2.gif')
t2.up()
t2.goto(-50,200)

t1.shape('1.gif')
t1.up()
t1.goto(50,200)

turtles=[t16,t8,t4,t2,t1]

i=s.numinput('Decimal to Binary', 'Enter a decimal number[0-31]:', minval=0, maxval=31)
i=int(i)
b = bin(i)[2:]

if len(b)<5:
     l= len(b)
     b = str(0) * (5 - l) + b 
print(b)

x=list(b)
for j in range(len(b)):
     if x[j]=='0':
          turtles[j].ht()

tw.up()
tw.goto(-150,50)
tw.write('Decimal= ',font=('Times New Roman',22,'bold'))
tw.goto(-30,50)
tw.write(i,font=('Times New Roman',22,'bold'))
tw.goto(-150,10)
tw.write('Binary= ',font=('Times New Roman',22,'bold'))
tw.goto(-40,10)
tw.write(b,font=('Times New Roman',22,'bold'))
tw.ht()
s.mainloop()
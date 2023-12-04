



#create a exception 'valueerror' if user enter invalid age

class fivedivisionerror(Exception):
    def __init__(self,message):
        self.message=message


try:
    a1=int(input('enter first number'))
    a2=int(input('enter second number'))
    if a2==5:
        raise fivedivisionerror("cannot divide by 5")
    div=a1/a2
    print(div)
except(fivedivisionerror) as a:
    print(a.message)


    

                 

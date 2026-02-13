def validateAge(age):
    if(age<18):
        raise LessAgeException("invalid age, less than 18")
    elif(age>50):
        raise MoreAgeException("age is more than 50")
    print(f"You are Eligible {age} ")


class LessAgeException(Exception):
    pass 

class MoreAgeException(Exception):
    pass 

try:
  validateAge(3)
except LessAgeException as l:
   print(l) 
except MoreAgeException as m:
    print(m)

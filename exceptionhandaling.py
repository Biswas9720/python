a=5
b=0

try:
   print(a/b)
except Exception:
   print("you can't divide by zero ")
else:
   print("I said I can't")
finally:
   print("I'm busy")

from lesson7ui import a, b, op  #если написать просто импорт то не подтягивает а,б и оп
from lesson7logger import save_log

if 'j' in a or 'j' in b:
   def operations(a,op,b):
    operation = {'+': lambda a,b: complex(a)+complex(b),
                 '-': lambda a,b: complex(a)-complex(b),
                 '*': lambda a,b: complex(a)*complex(b),
                 '/': lambda a,b: complex(a)/complex(b)}
    return operation[op](a,b) 
else:
    a = int(a)
    b = int(b)
    def operations(a,op,b):
        operation = {'+': lambda a, b: a + b,
                     '-': lambda a, b: a - b,
                     '*': lambda a, b: a * b,
                     '/': lambda a, b: a / b}
        return operation[op](a, b)
    
result = operations(a,op,b)
save_log(f"result = {result}")
import logging
logger = logging.getLogger(__name__)

op = input("Podaj operacje: 1: +, 2: -,3: *,4: /")
a = int(input("a: "))
b = int(input("b: "))
def kalkulator_v1():
    op = input("Podaj operacje: 1: +, 2: -,3: *,4: /")
    a = int(input("a: "))
    b = int(input("b: "))



def add(a, b): 
    logger.info(f"Wywołano sumę: a:{a} b:{b}")
    return a + b


def sub(a, b): 
    logger.info(f"Wywołano różnicę: a:{a} b:{b}")
    return a - b

def mul(a, b):
    logger.info(f"Wywołano iloczyn: a:{a} b:{b}")
    return a * b

def div(a, b): 
    logger.info(f"Wywołano iloraz: a:{a} b:{b}")
    return a / b     

def get_data():
    op = input(f"Podaj operacje: 1: +, 2: -,3: *, 4: :")
    a = int(input("a: "))
    b = int(input("b: "))
    return op, a, b

operations = {
    "1": add,
    "2": sub,
    "3": mul,
    "4": div
}
print(operations["1"](1,2))



def main():
    op, a, b = get_data()
    result = operations[op](a, b)

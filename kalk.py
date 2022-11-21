import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')
print('Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:')


   
def calc():
    x = float(input('pierwsza liczba:'))
    y = float(input('druga liczba:'))
    do = float(input('rodzaj działania:')) 
    if do == 1 :
        logging.debug(f"Dodajemy {x} i {y}")
        print('Wynik:')
        print(x + y)
    
    elif do == 2 :
        logging.debug(f"Odejmujemy {x} i {y}")
        print('Wynik:')
        print(x - y)
    elif do == 3 :
        logging.debug(f"Mnożymy {x} i {y}")
        print('Wynik:')
        print(x * y)     
    elif do == 4 :
        logging.debug(f"Dzielimy {x} i {y}")
        print('Wynik:')
        print(x / y)
calc()        
           
    
   


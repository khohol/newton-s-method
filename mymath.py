from sympy import *

x = symbols('x')
#init_printing(use_unicode=True)
#epsilon = 4                                 #знаків після коми
#iterations = 1000                           #кількість ітерацій
#x1 = -100                                   #початкове значення Xn
#fun = x**2 - 5 + 0.4**(2*x)

def function(fun, value):                   #функція функції
    res_fun = fun.subs(x, value)            #підставляємо в функцію аргумент з переданим значенням value
    return res_fun                          #повертаємо результат


def derivation(fun, value):                 #функція похідної
    der = diff(fun, x)                      #отримуємо похідну
    res_der = der.subs(x, value)            #підставляємо в похідну аргумент з переданим значенням value
    return res_der                          #повертаємо результат


def calculation(fun, x1, epsilon, iterations):
    fun = parse_expr(fun)
    result = ''
    currentInteration = 0                       #резервуємо змінну, яка буде зберігати теперішню ітерацію
    while currentInteration < iterations:
        currentInteration = currentInteration + 1       #ітеруємо
        x2 = x1 - (function(fun=fun, value=x1)/derivation(fun=fun, value=x1))        #Xn+1
        x2 = round(x2, epsilon)
        result = result + "Ітерація " + str(currentInteration) + ": " + str(x2) + '\n'
        if abs(x2 - x1) < (0.1**epsilon):
            result = result + "Фінальний результат: " + str(x2) + '\n'
            return(result)
        x1 = x2


#calculation(fun, x1, epsilon, iterations)
#print(calculation(fun='x**2 - 5 + 0.4**(2*x)', x1=-100, epsilon=4, iterations=1000))
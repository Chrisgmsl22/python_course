class ConvertidorTemperatura:
    #Atributo de clase constante
    MAX_CELCIUS = 100
    MAX_FAHRENHEIT = 213

    @classmethod
    def c_to_f(cls, celcius):
        if celcius > cls.MAX_CELCIUS:
            raise ValueError(f'Temperatura Celcius demasiado alta: {celcius}')
        return celcius * 9/5 + 32
    @classmethod
    def f_to_c(cls, fahrenheit):
        if fahrenheit > cls.MAX_FAHRENHEIT:
            raise ValueError(f'Temperatura Fahrenheit demasiado alta: {fahrenheit}')
        return (fahrenheit-32) * 5/9

if __name__ == '__main__':
    resultado = ConvertidorTemperatura.c_to_f(15)
    print(f'15 Celsius es: {resultado:.2f} Fahrenheit')

    resultado = ConvertidorTemperatura.f_to_c(10)
    print(f'10 F es : {resultado:.2f} Celsius')
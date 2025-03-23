#Creamos una función
def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento/100)
    return descuento

if __name__=="__main__":
    monto1 = 535
    monto2 = 600
    ##Primera llamada de la función.
    descuento1 = calcular_descuento(monto1)
    print(f"El monto de su primera compra es {monto1}, y su descuento es de {descuento1}")
    ##Segunda llamada de la función.
    descuento2 = calcular_descuento(monto2, 15)
    print(f"El monto de su segunda compra es {monto2}, y su descuento es de {descuento2}")
    print(f"Gracias por su compra")
print ('Calcular Iva y Precio de Venta')
vv = input('Ingrese valor de la venta: ')

vv = float(vv)
iva = vv * .19
pv = vv+iva

print(f'Valor de la venta: ${vv}  \nIva: ${iva} \nPrecio total de la venta:  ${pv}')
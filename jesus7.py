nombre_del_producto = input("ingrese nombre del producto : ")
precio = float(input("ingrese el precio : "))
cantidad = int(input("ingrese la cantidad que quiera : "))

subtotal = precio * cantidad 
print("Producto:", nombre_del_producto)
print("Precio unitario: $", precio)
print("Cantidad:", cantidad)
print("subTotal: ", subtotal)

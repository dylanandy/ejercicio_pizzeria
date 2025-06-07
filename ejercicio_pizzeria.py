pizzas = []
pedidos = []

while True:
    print("\n--- Sistema de Gestión de Pizzería ---")
    print("1. Registrar pizza")
    print("2. Ver catálogo")
    print("3. Realizar pedido")
    print("4. Ver pedidos")
    print("5. Salir")
    print("--------------------------------------")

    try:
        opcion = int(input("Ingrese una opción: "))
    except ValueError:
        print("Eso no es un número. Por favor, ingresa una de las opciones del menú.")
        continue 
    if opcion == 1:
        print("\n--- Registrar Pizza ---")
        codigo_nuevo = input("Ingrese el código de la pizza: ").strip().upper()

        codigo_existe = False
        for pizza_existente in pizzas:
            if pizza_existente['codigo'] == codigo_nuevo:
                codigo_existe = True
                break

        if codigo_existe:
            print("Error, Ya existe una pizza con ese código Por favor, elija uno diferente")
        else:
            nombre_nuevo = input("Ingrese el nombre de la pizza: ")
            tipo_masa_nuevo = input("Ingrese el tipo de masa (delgada o tradicional): ").lower()
            if tipo_masa_nuevo not in ['delgada', 'tradicional']:
                print("Tipo de masa no reconocido. Usando 'tradicional' por defecto")
                tipo_masa_nuevo = 'tradicional'

            while True:
                try:
                    precio_nuevo = float(input("Ingrese el precio unitario de la pizza: "))
                    if precio_nuevo <= 0:
                        print("El precio debe ser un número positivo")
                        continue
                    break
                except ValueError:
                    print("Por favor, ingrese un número para el precio")

            while True:
                try:
                    stock_nuevo = int(input("Ingrese el stock disponible de la pizza: "))
                    if stock_nuevo < 0:
                        print("El stock no puede ser negativo")
                        continue
                    break
                except ValueError:
                    print("Por favor, ingrese un número entero para el stock")

            nueva_pizza = {
                "codigo": codigo_nuevo,
                "nombre": nombre_nuevo,
                "tipo_masa": tipo_masa_nuevo,
                "precio": precio_nuevo,
                "stock": stock_nuevo
            }

            pizzas.append(nueva_pizza)
            print(f"¡Pizza '{nombre_nuevo}' registrada correctamente!")

    elif opcion == 2:
        print("\n--- Catálogo de Pizzas ---")
        if not pizzas:
            print("No hay pizzas registradas en el catálogo aún, agrega algunas")
        else:
            print("Código | Nombre | Tipo de Masa | Precio | Stock")
            print("------------------------------------------------------------------")
            for pizza in pizzas:
                print(f"{pizza['codigo']:<6} | {pizza['nombre']:<20} | {pizza['tipo_masa']:<12} | ${pizza['precio']:.2f} | {pizza['stock']:<5}")
            print("------------------------------------------------------------------")

    elif opcion == 3:
        print("\n--- Realizar Pedido ---")
        if not pizzas:
            print("Lo sentimos, no hay pizzas disponibles para pedir en este momento, Registre algunas primero")
            continue

        print("--- Catálogo de Pizzas Disponibles ---")
        print("Código | Nombre | Precio | Stock")
        print("--------------------------------------------------")
        for pizza in pizzas:
            print(f"{pizza['codigo']:<6} | {pizza['nombre']:<20} | ${pizza['precio']:.2f} | {pizza['stock']:<5}")
        print("--------------------------------------------------")

        cliente_nombre_pedido = input("Ingrese el nombre del cliente: ")
        codigo_pizza_pedido = input("Ingrese el código de la pizza que desea pedir: ").strip().upper()

        pizza_encontrada = None
        for pizza in pizzas:
            if pizza['codigo'] == codigo_pizza_pedido:
                pizza_encontrada = pizza
                break

        if not pizza_encontrada:
            print("error, El código de pizza ingresado no existe en nuestro catálogo.")
        else:
            while True:
                try:
                    cantidad_pedido = int(input(f"Ingrese la cantidad de '{pizza_encontrada['nombre']}' a pedir: "))
                    if cantidad_pedido <= 0:
                        print("La cantidad debe ser un número positivo, Inténtelo de nuevo.")
                        continue
                    break
                except ValueError:
                    print("Por favor, ingrese un número entero para la cantidad")

            if cantidad_pedido > pizza_encontrada['stock']:
                print(f"Error, No hay suficiente stock de '{pizza_encontrada['nombre']}'. Stock disponible: {pizza_encontrada['stock']}.")
            else:
                total_a_pagar = pizza_encontrada['precio'] * cantidad_pedido

                pizza_encontrada['stock'] -= cantidad_pedido

                nuevo_pedido = {
                    'cliente': cliente_nombre_pedido,
                    'pizza': pizza_encontrada['nombre'],
                    'cantidad': cantidad_pedido,
                    'total_pagado': total_a_pagar
                }
                pedidos.append(nuevo_pedido)
                print(f"Pedido de '{pizza_encontrada['nombre']}' para {cliente_nombre_pedido} realizado con éxito")
                print(f"Total a pagar: ${total_a_pagar:.2f}")
                print("Disfrute su pizza")

    elif opcion == 4:
        print("\n--- Historial de Pedidos Realizados ---")
        if not pedidos:
            print("Aún no se han realizado pedidos en este turno")
        else:
            for i, pedido in enumerate(pedidos):
                print(f"--- Pedido #{i+1} ---")
                print(f"Cliente: {pedido['cliente']}")
                print(f"Pizza: {pedido['pizza']}")
                print(f"Cantidad: {pedido['cantidad']}")
                print(f"Total Pagado: ${pedido['total_pagado']:.2f}")
                print("-------------------")
        print("Fin del historial de pedidos")

    elif opcion == 5:
        print("\nGracias por usar el Sistema de Gestión de Pedidos de la Pizzería, Vuelva pronto.")
        break
    else:
        print("Opción inválida. Por favor, elija un número del 1 al 5.")
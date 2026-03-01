# Pedir totales
luzyagua = float(input("Ingrese el total de la luz y agua: "))

total_servicios = luzyagua

personas = []
total_general = 0

cantidad_personas = int(input("¿Cuántas personas ingresará? "))

for i in range(cantidad_personas):
    print("\nPersona", i + 1)
    nombre = input("Nombre: ")
    
    veces = int(input("¿Cuántas veces fue en el mes?: "))
    
    total_persona = 0
    
    for v in range(veces):
        print(f"  Visita {v + 1}")
        dias = int(input("    ¿Cuántos días se quedó?: "))
        personas_visita = int(input("    ¿Con cuántas personas fue?: "))
        
        total_persona += dias * personas_visita
    
    personas.append((nombre, total_persona))
    total_general += total_persona

# Evitar división por cero
if total_general == 0:
    print("Error: No hay datos para dividir.")
else:
    valor_por_unidad = total_servicios / total_general

    print("\n----- RESULTADOS -----")

    for nombre, total_persona in personas:
        pago = round(total_persona * valor_por_unidad)
        
        # Formato chileno con punto de miles
        pago_formateado = f"{pago:,}".replace(",", ".")
        
        print(f"{nombre} paga {pago_formateado}")
import os
# Rutas a los archivos del modelo y datos
model_path = 'src/PlantaEnergia.mzn'
data_path = 'src/Datos.dzn'


def validate_int_input(P):
    if P == "":
        return True
    try:
        int(P)
        return True
    except ValueError:
        return False


def write_data(G, num_clientes, num_dias, costo, capacidad, pago, nueva_demanda, file_name=data_path):
    with open(file_name, 'w') as file:
        file.write(f"G = {G};\n")
        file.write(f"costo = {costo};\n")
        file.write(f"capacidad = {capacidad};\n")
        file.write(f"num_clientes = {num_clientes};\n")
        file.write(f"num_dias = {num_dias};\n")
        file.write(f"num_plantas = {3};\n")
        file.write(f"pago = {pago};\n")
        file.write("demanda = [")
        for fila in nueva_demanda:
            file.write("|")
            file.write(", ".join(map(str, fila)))
            file.write("\n")
        file.write("        |];\n")


# Nueva matriz de demanda
nueva_demanda = [
    [1810.0, 1110.0, 910.0],
    [11150.0, 981.0, 3140.0],
    [910.0, 12110.0, 2112.0],
    [300.0, 11210.0, 2010.0]
]
G = 5
num_clientes = 4
num_dias = 3
costo = [5010.0, 2001.0, 1100.0]
capacidad = [10100.0, 30110.0, 11500.0]
pagoCliente = [11100.0, 11110.0, 9115.0, 1111.0]

# write_data(G, num_clientes, num_dias,
#            costo, capacidad, pagoCliente, nueva_demanda)


def solve(G, num_clientes, num_dias, costo, capacidad, pagoCliente, nueva_demanda, file_name=data_path):
    write_data(G, num_clientes, num_dias, costo, capacidad,
               pagoCliente, nueva_demanda, file_name)
    result = os.popen(
        f'minizinc --solver COIN-BC {model_path} {data_path}').read()
    return result


print(solve(G, num_clientes, num_dias, costo, capacidad,
      pagoCliente, nueva_demanda, data_path))

# write_data(G, num_clientes, num_dias,
#            costo, capacidad, pagoCliente, nueva_demanda)
# print(solve(G, num_clientes, num_dias, costo, capacidad,
#       pagoCliente, nueva_demanda, data_path))

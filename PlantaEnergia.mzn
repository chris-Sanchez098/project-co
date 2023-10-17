int: num_clientes;
int: num_dias;
int: plantas;
array[1..num_clientes, 1..num_dias] of float: demanda;

int: G;

array[1..num_clientes] of float: pagoCliente;
array[1..plantas] of float: costo;
array[1..plantas] of float: capacidad;

% Variables de decisión
array[1..num_clientes, 1..num_dias, 1..plantas] of var int: produccion;  % Producción de energía por planta
    
constraint forall(d in 1..num_dias, p in 1..plantas) (
    sum(c in 1..num_clientes) (produccion[c,d,p]) <= capacidad[p]
);

constraint forall(d in 1..num_dias, c in 1..num_clientes) (
    sum(p in 1..plantas) (produccion[c,d,p]) >= demanda[c,d]*0.5 
);

var float: ganancia_neta = sum(d in 1..num_dias, c in 1..num_clientes) (
    sum(p in 1..plantas) (produccion[c,d,p] * pagoCliente[c]) - sum(p in 1..plantas) (produccion[c,d,p]*costo[p])
);


solve maximize ganancia_neta;

% Salida de la solución
output ["Ganancia Neta: ", show(ganancia_neta), "\n"]
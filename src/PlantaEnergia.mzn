% Parámetros
int: num_clientes; % Número de clientes
int: num_dias; % Número de días
int: num_plantas; % Número de plantas
float: G; % Porcentaje mínimo de demanda a satisfacer
array[1..num_plantas] of float: costo;  % Costo por MW producido en cada planta
array[1..num_plantas] of float: capacidad;  % Capacidad diaria en cada planta (en MW)
array[1..num_clientes] of float: pago;% Pago por MW de cada cliente
array[1..num_clientes, 1..num_dias] of float: demanda;
float: max_capacidad =  sum(c in 1..num_plantas) (capacidad[c]);

% Variables de decisión
array[1..num_clientes, 1..num_dias, 1..num_plantas] of var 0.0..max_capacidad : produccion;  % Producción de energía por planta
    
% Restricciones
constraint forall(d in 1..num_dias, p in 1..num_plantas) (
    sum(c in 1..num_clientes) (produccion[c,d,p]) <= capacidad[p]
);

constraint forall(d in 1..num_dias, c in 1..num_clientes) (
    sum(p in 1..num_plantas) (produccion[c,d,p]) <= demanda[c, d]
);

constraint forall(d in 1..num_dias, c in 1..num_clientes) (
    sum(p in 1..num_plantas) (produccion[c,d,p]) >= demanda[c,d]*(G/100)
);

constraint forall(d in 1..num_dias) (
    sum(c in 1..num_clientes) (demanda[c,d]) <= max_capacidad ->
    sum(p in 1..num_plantas, c in 1..num_clientes) (produccion[c,d,p]) == sum(c in 1..num_clientes)(demanda[c,d])
);                                                                                                                                                            

constraint forall(i in 1..(num_dias - 1), p in 2..2) (
    sum(s in 1..num_clientes) (produccion[s, i + 1, p]) > capacidad[p] * 0.8
   -> sum(s in 1..num_clientes) (produccion[s, i, p]) <= capacidad[p] * 0.8
);

% Función Objectivo

var float: ganancia_neta = sum(d in 1..num_dias, c in 1..num_clientes) (
    sum(p in 1..num_plantas) (produccion[c,d,p] * pago[c]) - sum(p in 1..num_plantas) (produccion[c,d,p]*costo[p])
);

solve maximize ganancia_neta;

% Salida de la solución
output [show(ganancia_neta), "&", show(produccion)]
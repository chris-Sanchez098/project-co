% Parámetros
float: cN = 50.0;  % Costo de producción en la central nuclear (por MW)
float: cH = 20.0;  % Costo de producción en la central hidroeléctrica (por MW)
float: cT = 10.0;  % Costo de producción en la central térmica (por MW)

float: CapacidadN = 1000.0;  % Capacidad diaria de la central nuclear (en MW)
float: CapacidadH = 300.0;  % Capacidad diaria de la central hidroeléctrica (en MW)
float: CapacidadT = 500.0;  % Capacidad diaria de la central térmica (en MW)

int: num_clientes = 4;  % Número de clientes
int: num_dias = 3 ;      % Número de días
int: plantas = 3; % número de plantas

array[1..num_clientes, 1..num_dias] of float: Demanda = [| 80.0, 110.0, 90.0 
                                                       | 150.0, 98.0, 340.0 
                                                       | 90.0, 20.0, 212.0 
                                                       | 300.0, 210.0, 200.0 |];

int: G = 50;  % Porcentaje mínimo de demanda a satisfacer

array[1..num_clientes] of float: PagoCliente = [100.0, 110.0, 95.0, 105.0];  % Pago por MW de cada cliente
array[1..plantas] of float: costo = [10.0, 20.0, 10.0]; % costo por MW producido en cada planta
array[1..plantas] of float: maxP = [1000.0, 300.0, 500.0];

% Variables de decisión
array[1..num_clientes, 1..num_dias, 1..plantas] of var int: Produccion;  % Producción de energía por planta
    
constraint forall(d in 1..num_dias, p in 1..plantas) (
    sum(c in 1..num_clientes) (Produccion[c,d,p]) <= maxP[p]
);

constraint forall(d in 1..num_dias, c in 1..num_clientes) (
    sum(p in 1..plantas) (Produccion[c,d,p]) >= Demanda[c,d]*0.5 
);

var float: ganancia_neta = sum(d in 1..num_dias, c in 1..num_clientes) (
    sum(p in 1..plantas) (Produccion[c,d,p] * PagoCliente[c]) - sum(p in 1..plantas) (Produccion[c,d,p]*costo[p])
);


solve maximize ganancia_neta;

% Salida de la solución
output ["Ganancia Neta: ", show(ganancia_neta), "\n"]
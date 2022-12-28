## Inove_ProgramadorPython_ProyIntegrador
# Proyecto Integrador. Cliente V.I.P. (Very Important Pet)
## Autor: Martín A. García Romano
### Curso Programador Python de Inove (2022)
#### Objetivos del Proyecto Integrador

Poner en práctica algunos de los conceptos aprendidos en el curso:
- JSON
- Base de Datos (SQL ORM)
- Manejo de datos
- API (Servicios, Web App)
- HTML

#### El programa

Esta versión de Cliente V.I.P. es la continuidad del programa presentado en el proyecto integrador de Python Inicial. Es un programa pensado para la gestión de clientes caninos de una veterinaria.
En la primera versión presentada en Python Inicial se podían llevar adelante las siguientes tareas en sus cuatro módulos:

- Registro de nuevos clientes caninos.
- Modificación de información del cliente canino.
- Baja de clientes caninos.
- Consulta por responsable.

El desarrollo que aquí se presenta es una forma muy básica en la que se aplican algunos de los conceptos vistos a lo largo de Programador Python.
Algunas complicaciones para realizar el código y falta de tiempo no permitieron cumplir el objetivo inicial, replicar lo realizado en el Proyecto Integrador de Python Inicial.

Es por ello que este integrador se reduce a dos endpoints: en uno de ellos se realiza el registro de un nuevo cliente canino y en el otro se realiza una consulta por nombre del cliente canino y DNI del responsable.

En un primer borrador la idea era llevar adelante dos bases de datos, una para los clientes caninos y otra para los responsables. Esta idea inicial fue descartada debido a que son pocos los responsables que tienen más de un canino por lo que la repetición de ciertos datos en una sola base de datos era preferible a tener dos bases de datos enlazadas.

A este proyecto le falta aún la verificación de los datos introducidos al momento de registrar un nuevo cliente canino.
La modificación y actualización de datos del canino (peso, edad, fecha de vacunaciones y desparasitaciones) y del responsable (algo que no estaba realizado en el proyecto de Python inicial) puede realizarse a partir de la idea desarrollada para consulta realizada y presentada en éste proyecto.
La baja de clientes (por deceso, mudanza, etc.) también puede realizarse a partir de la misma consulta presentada aquí, y persiste la idea de conservar la información de las bajas en un archivo csv que pueda enviarse a otras veterinarias o incluso en caso de regreso de algún cliente. Se descartan obviamente el caso de los decesos.

Queda mucho por hacer. Los impedimentos mencionados más arriba no hicieron posible presentar un proyecto más completo y más cercano a la idea original.

Como ya se señaló oportunamente Cliente V.I.P. que es un proyecto escalable, que podría considerarse como inicio de un programa con más capacidades y funcionalidades que contemple otras especies (gatos, aves, peces, etc.) o que modificado pueda utilizarse en un refugio canino.

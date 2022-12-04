# TQL (Tournament Query Language)
Proyecto final para la clase de Compiladores 2022-II realizado por 
- Daniel Santiago Pardo
- Juan Carlos Sanchez Orjuela

## Reporte escrito
https://drive.google.com/file/d/1SswODkfh770IKUJBxLdBfRmA-CeJIgp_/view?usp=sharing
## Vídeo
https://youtu.be/_Ia57AQ7RSA
### ¿Cómo instalar?
Rjecute:
1. Clonar el repositorio
```
git clone https://github.com/dpardogo/TQL
cd tql/
```
2. Para mejor manejo de dependencias, cree un ambiente virtual
```
pip3 -m venv tqlenv
source tqlenv/bin/activate
```
3. Instalar paquetes necesarios
```
pip install -r requirements.txt
```
5. Ejecutar TQL
```
python TQL.py
```
### Comandos disponibles
TQL soporta los siguientes comandos:

Crear Torneo        : CREATE TOURNAMENT name (attributes ( WITH INTEGER PARTICIPANT )? list? (CONTENDER (TEAM | PLAYER))?)?;

Añadir equipo           : ADD TEAM IN TOURNAMENT add_fs ( name | list);
Añador jugador          : ADD PLAYER IN TOURNAMENT add_fs  ( name | list);
Añadir jugador a equipo : ADD PLAYER TO add_fs IN TOURNAMENT add_ss  ( name | list);

Borra torneo             : DELETE TOURNAMENT name (CONTENDER (TEAM | PLAYER))?;
Borra equipo             : DELETE TEAM IN TOURNAMENT add_fs ( name | list);
Borra jugador en torneo  : DELETE PLAYER IN TOURNAMENT add_fs  ( name | list);
Borra jugador en quipo   : DELETE PLAYER OF add_fs IN TOURNAMENT add_ss  ( name | list);

Modifica un participante        : MODIFY PARTICIPANT p_identifier FROM t_identifier '{' pair ( ',' pair )* '}';

Organiza un torneo      : ORGANIZE TOURNAMENT t_identifier BY WORD ;

Reporta un partido        : REPORT a_identifier OF p_identifier FROM t_identifier ;


Limpiar console               : CLEAR;
Mostrar todas las tablas      : LIST DATA;
Mostrar equipos               : LIST TEAM;
Mostrar torneos               : LIST TOURNAMENT;
Mostrar jugadores en equipos  : LIST PLAYER IN TEAM;
Mostrar jugadores en torneos  : LIST PLAYER IN TOURNAMENT;
Mostrar juegos                : LIST MATCHES;
Salir                         : EXIT;
Cargar comandos desde archivo : LOAD FROM PATH STRING;

# Donde:
attributes          : '(' WORD ( ',' WORD )* ')';
list                : '[' name ( ',' name )* ']';
name				: STRING ( '(' abbr ')' )?;
abbr                : WORD;
STRING              :'"' ~["]+ '"';
WORD				: (LOWERCASE | UPPERCASE)(LOWERCASE | UPPERCASE| DIGIT | '_')* ;
LOWERCASE           : [a-z] ;
UPPERCASE           : [A-Z] ;
a_identifier        : WORD;
t_identifier        : STRING | WORD;
p_identifier        : STRING | WORD;
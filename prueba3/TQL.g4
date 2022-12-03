grammar TQL;

/*
 * Parser Rules
 */

program				: line+ ;

line				: create_query
                    | add_team
                    | add_single_player
                    | add_player
                    | delete_tournament
                    | delete_team
                    | delete_player
                    | delete_single_player
                    | modify_query
                    | organize_query
                    | report_query
                    | show_query
                    | clear
                    | list_data
                    | exit
                    | list_tournament
                    | list_team
                    | list_player_team
                    | list_single_players
                    | read_file
                    ;

create_query        : CREATE TOURNAMENT name specifications?;
specifications  	: attributes ( WITH INTEGER PARTICIPANT )? list? (CONTENDER (TEAM | PLAYER))?;
attributes          : '(' WORD ( ',' WORD )* ')';

add_team           : ADD TEAM IN TOURNAMENT add_fs ( name | list);
add_single_player  : ADD PLAYER IN TOURNAMENT add_fs  ( name | list);
add_player         : ADD PLAYER TO add_fs IN TOURNAMENT add_ss  ( name | list);

delete_tournament     : DELETE TOURNAMENT name (CONTENDER (TEAM | PLAYER))?;
delete_team           : DELETE TEAM IN TOURNAMENT add_fs ( name | list);
delete_single_player  : DELETE PLAYER IN TOURNAMENT add_fs  ( name | list);
delete_player         : DELETE PLAYER OF add_fs IN TOURNAMENT add_ss  ( name | list);
delete_query        : DELETE ( WORD | attributes | list) FROM t_identifier;

add_fs             : STRING;
add_ss             : STRING;

modify_query        : MODIFY PARTICIPANT ( WORD | INTEGER) FROM t_identifier '{' pair ( ',' pair )* '}';

organize_query      : ORGANIZE TOURNAMENT t_identifier BY WORD ;

report_query        : REPORT a_identifier OF p_identifier FROM t_identifier ;

show_query          : SHOW ( PHASE | SUMMARY ) ( OF p_identifier )? FROM t_identifier;

dtype               : WORD
                    | INTEGER
                    | list
                    ;

pair                : WORD ':' dtype;
list                : '[' name ( ',' name )* ']';

a_identifier        : WORD;
t_identifier        : STRING | WORD;
p_identifier        : STRING | WORD;

identifier          : WORD;
name				: STRING ( '(' abbr ')' )?;
abbr                : WORD;
clear               : CLEAR;
list_data           : LIST DATA;
list_team           : LIST TEAM;
list_tournament     : LIST TOURNAMENT;
list_player_team    : LIST PLAYER IN TEAM;
list_single_players : LIST PLAYER IN TOURNAMENT;
exit                : EXIT;
read_file           : LOAD FROM PATH STRING;
					 					


/*
 * Lexer Rules
 */

fragment A: [aA];
fragment E: [Ee];
fragment I: [Ii];
fragment O: [Oo];
fragment U: [Uu];
fragment Y: [Yy];

fragment C: [Cc];
fragment R: [Rr];
fragment T: [Tt];
fragment D: [Dd];
fragment G: [Gg];
fragment N: [Nn];
fragment Z: [Zz];
fragment P: [Pp];
fragment M: [Mm];
fragment F: [Ff];
fragment W: [Ww];
fragment H: [Hh];
fragment S: [Ss];
fragment B: [Bs];
fragment L: [Ls];
fragment X: [Xx];

fragment DIGIT      : [0-9] ;
fragment LOWERCASE  : [a-z] ;
fragment UPPERCASE  : [A-Z] ;

CREATE				: C R E A T E ;
TOURNAMENT          : T O U R N A M E N T;
WITH                : W I T H;
PARTICIPANT         : P A R T I C I P A N T | P A R T I C I P A N T S;
ADD 				: A D D;
TO                  : T O;
ORGANIZE            : O R G A N I Z E;
ATTRIBUTE           : A T T R I B U T E | A T T R I B U T E S;
DELETE              : D E L E T E;
FROM                : F R O M;
BY                  : B Y;
REPORT              : R E P O R T;
MODIFY              : M O D I F Y;
MATCH               : M A T C H;
OF                  : O F;
ID                  : I D;
SHOW                : S H O W;
PHASE               : P H A S E;
SUMMARY             : S U M M A R Y;
TEAM                : T E A M | T E A M S;
PLAYER              : P L A Y E R | P L A Y E R S;
CONTENDER           : C O N T E N D E R | C O N T E N D E R;
IN                  : I N;
CLEAR               : C L E A R;
LIST                : L I S T;
DATA                : D A T A;
EXIT                : E X I T;
LOAD                : L O A D;
PATH                : P A T H;

STRING              :'"' ~["]+ '"';
WORD				: (LOWERCASE | UPPERCASE)(LOWERCASE | UPPERCASE| DIGIT | '_')* ;
INTEGER             : DIGIT+;

WHITESPACE			: [\t\r\n ]+ -> skip ;

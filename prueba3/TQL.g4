grammar TQL;

/*
 * Parser Rules
 */

program				: line+ ;

line				: create_query
                    | add_query
                    | delete_query
                    | modify_query
                    | organize_query
                    | report_query
                    | show_query
                    ;

create_query        : CREATE TOURNAMENT name specifications?;
specifications  	: attributes ( WITH INTEGER PARTICIPANT )? list? (CONTENDER (TEAM | PLAYER))?;
attributes          : '(' WORD ( ',' WORD )* ')';

add_query           : ADD PARTICIPANT TO t_identifier ( name | list);

delete_query        : DELETE ( WORD | attributes | list) FROM t_identifier;

modify_query        : MODIFY PARTICIPANT p_identifier FROM t_identifier '{' pair ( ',' pair )* '}';

organize_query      : ORGANIZE TOURNAMENT t_identifier BY WORD ;

report_query        : REPORT a_identifier OF p_identifier FROM t_identifier ;

show_query          : SHOW ( PHASE | SUMMARY ) ( OF p_identifier )? FROM t_identifier;

dtype               : WORD
                    | INTEGER
                    | STRING
                    ;

pair                : a_identifier ':' dtype;
list                : '[' name ( ',' name )* ']';

a_identifier        : WORD;
t_identifier        : STRING | WORD;
p_identifier        : STRING | WORD;

identifier          : WORD;
name				: STRING ( '(' abbr ')' )?;
abbr                : WORD;
					 					


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
fragment B: [Bb];
fragment L: [Ll];

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
TEAM                : T E A M;
PLAYER              : P L A Y E R;
CONTENDER           : C O N T E N D E R;

STRING              :'"' ~["]+ '"';
WORD				: (LOWERCASE | UPPERCASE)(LOWERCASE | UPPERCASE| DIGIT | '_')* ;
INTEGER             : DIGIT+;

WHITESPACE			: [\t\r\n ]+ -> skip ;

grammar TQL;

/*
 * Parser Rules
 */

program				: line+ EOF ;

line				: create_query
                    | add_query
                    | delete_query
                    | modify_query
                    | organize_query
                    | report_query
                    | show_query
                    ;

create_query        : CREATE TOURNAMENT name specifications?;
specifications  	: attributes ( WITH INTEGER PARTICIPANT )? list?;
attributes           : '(' WORD ( ',' WORD )* ')';

add_query           : ADD PARTICIPANT TO identifier ( name | list);
list                : '[' name ( ',' name )* ']';

delete_query        : DELETE ( WORD | attributes | list) FROM identifier;

modify_query        : MODIFY PARTICIPANT ( WORD | INTEGER) FROM identifier '{' pair ( ',' pair )* '}';

pair                : WORD ':' dtype;

organize_query      : ORGANIZE TOURNAMENT identifier BY WORD ;

report_query        : REPORT  identifier  OF identifier  FROM identifier ;

show_query          : SHOW;

dtype               : WORD
                    | INTEGER
                    | list
                    ;

identifier          : WORD;
name				: WORD ( '(' abbr ')' )?;
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
fragment B: [Bs];
fragment L: [Ls];

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

WORD				: (LOWERCASE | UPPERCASE)(LOWERCASE | UPPERCASE| DIGIT | '_')* ;
INTEGER             : DIGIT+;

WHITESPACE			: [\t\r\n ]+ -> skip ;

NEWLINE				: ('\r'? '\n' | '\r')+ ;
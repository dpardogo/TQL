grammar TQL;

/*
 * Parser Rules
 */

program				: line+ EOF ;

line				: command name specifications NEWLINE ;

specifications  	: '('( WORD WHITESPACE? ':' WORD WHITESPACE? ';')*')' ;

name				: WORD WHITESPACE?;

command				: CREATE WHITESPACE;
					 					


/*
 * Lexer Rules
 */



fragment LOWERCASE  : [a-z] ;
fragment UPPERCASE  : [A-Z] ;

CREATE				: 'CREATE'| 'create' ;

WORD				: (LOWERCASE | UPPERCASE | '_')+ ;

WHITESPACE			: (' ' | '\t')+ ;

NEWLINE				: ('\r'? '\n' | '\r')+ ;
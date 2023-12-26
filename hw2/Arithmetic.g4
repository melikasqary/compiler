grammar Arithmetic;

expression : expression op=('*' | '/') expression
           | expression op=('+' | '-') expression
           | '(' expression ')'
           | NUMBER
           ;

NUMBER : DIGIT+ ('.' DIGIT*)? ;
fragment DIGIT : [0-9] ;

WS : [ \t\r\n]+ -> skip ;
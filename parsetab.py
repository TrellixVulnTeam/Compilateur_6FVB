
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDErightUMINUSAND BREAK COMA DEF DIVIDE ELSE EQUALITY EQUALS FOR IF LACCO LESSER LPAREN MINUS NAME NON_EQUALITY NUMBER OR PLUS PRINT QUOTE RACCO RETURN RPAREN SEMICOLON STRING TIMES UPPER WHILEmaster : blocbloc :  statement bloc\n            | statementstatement : IF expression LACCO bloc RACCO ELSE LACCO bloc RACCO\n    | IF expression  LACCO bloc RACCO   statement : FOR statement statement statement LACCO bloc RACCO\n                |  FOR statement statement LACCO bloc RACCOstatement : WHILE expression  LACCO bloc RACCO statement : NAME EQUALS expression SEMICOLONstatement : expression SEMICOLONexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expression\n                  | expression EQUALITY expression\n                  | expression NON_EQUALITY expression\n                  | expression OR expression\n                  | expression AND expression\n                  | expression UPPER expression\n                  | expression LESSER expressionstatement : DEF NAME LPAREN arglist RPAREN LACCO bloc RACCO\n                  | DEF NAME LPAREN RPAREN LACCO bloc RACCOexpression : NAME LPAREN RPAREN\n                 | NAME LPAREN expressionlist RPARENexpression : MINUS expression %prec UMINUSexpression : LPAREN expression RPARENexpression : NUMBERexpression : QUOTE STRING QUOTEexpression : NAMEstatement : RETURN SEMICOLON\n                    | RETURN expression SEMICOLONarglist : arglist COMA NAME\n                | NAMEexpressionlist : expressionlist COMA expression\n                        | expressionexpression : PRINT LPAREN expression RPAREN'
    
_lr_action_items = {'NON_EQUALITY':([10,12,14,17,19,20,21,22,25,41,44,45,48,50,51,52,53,54,55,56,57,58,59,60,61,64,70,79,],[-27,-29,29,-29,29,-25,29,29,29,-28,-26,29,29,-23,29,29,29,29,-13,-12,29,-11,-14,29,29,-36,-24,29,]),'DIVIDE':([10,12,14,17,19,20,21,22,25,41,44,45,48,50,51,52,53,54,55,56,57,58,59,60,61,64,70,79,],[-27,-29,37,-29,37,-25,37,37,37,-28,-26,37,37,-23,37,37,37,37,-13,37,37,37,-14,37,37,-36,-24,37,]),'EQUALITY':([10,12,14,17,19,20,21,22,25,41,44,45,48,50,51,52,53,54,55,56,57,58,59,60,61,64,70,79,],[-27,-29,31,-29,31,-25,31,31,31,-28,-26,31,31,-23,31,31,31,31,-13,-12,31,-11,-14,31,31,-36,-24,31,]),'RPAREN':([10,17,20,22,28,41,44,45,47,49,50,51,52,53,54,55,56,57,58,59,60,61,64,66,68,70,79,85,],[-27,-29,-25,44,50,-28,-26,64,67,70,-23,-35,-16,-17,-15,-13,-12,-20,-11,-14,-18,-19,-36,-33,77,-24,-34,-32,]),'TIMES':([10,12,14,17,19,20,21,22,25,41,44,45,48,50,51,52,53,54,55,56,57,58,59,60,61,64,70,79,],[-27,-29,32,-29,32,-25,32,32,32,-28,-26,32,32,-23,32,32,32,32,-13,32,32,32,-14,32,32,-36,-24,32,]),'ELSE':([74,],[82,]),'NUMBER':([0,2,3,4,6,8,9,15,18,23,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,43,46,62,69,71,73,74,75,76,80,84,87,88,89,91,93,94,],[10,10,10,10,10,10,10,10,-30,10,10,10,10,10,10,10,-10,10,10,10,10,10,10,10,-31,10,10,10,-9,10,10,-5,-8,10,10,10,-7,10,-22,-6,-21,-4,]),'PRINT':([0,2,3,4,6,8,9,15,18,23,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,43,46,62,69,71,73,74,75,76,80,84,87,88,89,91,93,94,],[7,7,7,7,7,7,7,7,-30,7,7,7,7,7,7,7,-10,7,7,7,7,7,7,7,-31,7,7,7,-9,7,7,-5,-8,7,7,7,-7,7,-22,-6,-21,-4,]),'EQUALS':([12,],[27,]),'PLUS':([10,12,14,17,19,20,21,22,25,41,44,45,48,50,51,52,53,54,55,56,57,58,59,60,61,64,70,79,],[-27,-29,36,-29,36,-25,36,36,36,-28,-26,36,36,-23,36,36,36,36,-13,-12,36,-11,-14,36,36,-36,-24,36,]),'SEMICOLON':([2,10,12,14,17,19,20,41,44,48,50,52,53,54,55,56,57,58,59,60,61,64,70,],[18,-27,-29,33,-29,42,-25,-28,-26,69,-23,-16,-17,-15,-13,-12,-20,-11,-14,-18,-19,-36,-24,]),'IF':([0,8,15,18,33,40,42,43,46,62,69,73,74,75,76,80,84,87,88,89,91,93,94,],[4,4,4,-30,-10,4,-31,4,4,4,-9,4,-5,-8,4,4,4,-7,4,-22,-6,-21,-4,]),'STRING':([1,],[16,]),'RETURN':([0,8,15,18,33,40,42,43,46,62,69,73,74,75,76,80,84,87,88,89,91,93,94,],[2,2,2,-30,-10,2,-31,2,2,2,-9,2,-5,-8,2,2,2,-7,2,-22,-6,-21,-4,]),'LPAREN':([0,2,3,4,6,7,8,9,12,15,17,18,23,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,43,46,62,69,71,73,74,75,76,80,84,87,88,89,91,93,94,],[6,6,6,6,6,23,6,6,28,6,28,-30,6,47,6,6,6,6,6,6,-10,6,6,6,6,6,6,6,-31,6,6,6,-9,6,6,-5,-8,6,6,6,-7,6,-22,-6,-21,-4,]),'RACCO':([8,18,24,33,42,63,65,69,74,75,81,83,86,87,89,90,91,92,93,94,],[-3,-30,-2,-10,-31,74,75,-9,-5,-8,87,89,91,-7,-22,93,-6,94,-21,-4,]),'QUOTE':([0,2,3,4,6,8,9,15,16,18,23,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,43,46,62,69,71,73,74,75,76,80,84,87,88,89,91,93,94,],[1,1,1,1,1,1,1,1,41,-30,1,1,1,1,1,1,1,-10,1,1,1,1,1,1,1,-31,1,1,1,-9,1,1,-5,-8,1,1,1,-7,1,-22,-6,-21,-4,]),'OR':([10,12,14,17,19,20,21,22,25,41,44,45,48,50,51,52,53,54,55,56,57,58,59,60,61,64,70,79,],[-27,-29,30,-29,30,-25,30,30,30,-28,-26,30,30,-23,30,30,30,30,-13,-12,30,-11,-14,30,30,-36,-24,30,]),'$end':([5,8,13,18,24,33,42,69,74,75,87,89,91,93,94,],[0,-3,-1,-30,-2,-10,-31,-9,-5,-8,-7,-22,-6,-21,-4,]),'WHILE':([0,8,15,18,33,40,42,43,46,62,69,73,74,75,76,80,84,87,88,89,91,93,94,],[9,9,9,-30,-10,9,-31,9,9,9,-9,9,-5,-8,9,9,9,-7,9,-22,-6,-21,-4,]),'COMA':([10,17,20,41,44,49,50,51,52,53,54,55,56,57,58,59,60,61,64,66,68,70,79,85,],[-27,-29,-25,-28,-26,71,-23,-35,-16,-17,-15,-13,-12,-20,-11,-14,-18,-19,-36,-33,78,-24,-34,-32,]),'MINUS':([0,2,3,4,6,8,9,10,12,14,15,17,18,19,20,21,22,23,25,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,48,50,51,52,53,54,55,56,57,58,59,60,61,62,64,69,70,71,73,74,75,76,79,80,84,87,88,89,91,93,94,],[3,3,3,3,3,3,3,-27,-29,34,3,-29,-30,34,-25,34,34,3,34,3,3,3,3,3,3,-10,3,3,3,3,3,3,3,-28,-31,3,-26,34,3,34,-23,34,34,34,34,-13,-12,34,-11,-14,34,34,3,-36,-9,-24,3,3,-5,-8,3,34,3,3,-7,3,-22,-6,-21,-4,]),'NAME':([0,2,3,4,6,8,9,11,15,18,23,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,43,46,47,62,69,71,73,74,75,76,78,80,84,87,88,89,91,93,94,],[12,17,17,17,17,12,17,26,12,-30,17,17,17,17,17,17,17,-10,17,17,17,17,17,17,12,-31,12,12,66,12,-9,17,12,-5,-8,12,85,12,12,-7,12,-22,-6,-21,-4,]),'AND':([10,12,14,17,19,20,21,22,25,41,44,45,48,50,51,52,53,54,55,56,57,58,59,60,61,64,70,79,],[-27,-29,38,-29,38,-25,38,38,38,-28,-26,38,38,-23,38,38,38,38,-13,-12,38,-11,-14,38,38,-36,-24,38,]),'LESSER':([10,12,14,17,19,20,21,22,25,41,44,45,48,50,51,52,53,54,55,56,57,58,59,60,61,64,70,79,],[-27,-29,35,-29,35,-25,35,35,35,-28,-26,35,35,-23,35,35,35,35,-13,-12,35,-11,-14,35,35,-36,-24,35,]),'DEF':([0,8,15,18,33,40,42,43,46,62,69,73,74,75,76,80,84,87,88,89,91,93,94,],[11,11,11,-30,-10,11,-31,11,11,11,-9,11,-5,-8,11,11,11,-7,11,-22,-6,-21,-4,]),'UPPER':([10,12,14,17,19,20,21,22,25,41,44,45,48,50,51,52,53,54,55,56,57,58,59,60,61,64,70,79,],[-27,-29,39,-29,39,-25,39,39,39,-28,-26,39,39,-23,39,39,39,39,-13,-12,39,-11,-14,39,39,-36,-24,39,]),'LACCO':([10,17,18,20,21,25,33,41,42,44,50,52,53,54,55,56,57,58,59,60,61,62,64,67,69,70,72,74,75,77,82,87,89,91,93,94,],[-27,-29,-30,-25,43,46,-10,-28,-31,-26,-23,-16,-17,-15,-13,-12,-20,-11,-14,-18,-19,73,-36,76,-9,-24,80,-5,-8,84,88,-7,-22,-6,-21,-4,]),'FOR':([0,8,15,18,33,40,42,43,46,62,69,73,74,75,76,80,84,87,88,89,91,93,94,],[15,15,15,-30,-10,15,-31,15,15,15,-9,15,-5,-8,15,15,15,-7,15,-22,-6,-21,-4,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,2,3,4,6,8,9,15,23,27,28,29,30,31,32,34,35,36,37,38,39,40,43,46,62,71,73,76,80,84,88,],[14,19,20,21,22,14,25,14,45,48,51,52,53,54,55,56,57,58,59,60,61,14,14,14,14,79,14,14,14,14,14,]),'bloc':([0,8,43,46,73,76,80,84,88,],[13,24,63,65,81,83,86,90,92,]),'expressionlist':([28,],[49,]),'master':([0,],[5,]),'arglist':([47,],[68,]),'statement':([0,8,15,40,43,46,62,73,76,80,84,88,],[8,8,40,62,8,8,72,8,8,8,8,8,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> master","S'",1,None,None,None),
  ('master -> bloc','master',1,'p_master','calc.py',88),
  ('bloc -> statement bloc','bloc',2,'p_bloc','calc.py',93),
  ('bloc -> statement','bloc',1,'p_bloc','calc.py',94),
  ('statement -> IF expression LACCO bloc RACCO ELSE LACCO bloc RACCO','statement',9,'p_IF_statement','calc.py',104),
  ('statement -> IF expression LACCO bloc RACCO','statement',5,'p_IF_statement','calc.py',105),
  ('statement -> FOR statement statement statement LACCO bloc RACCO','statement',7,'p_FOR_statement','calc.py',114),
  ('statement -> FOR statement statement LACCO bloc RACCO','statement',6,'p_FOR_statement','calc.py',115),
  ('statement -> WHILE expression LACCO bloc RACCO','statement',5,'p_WHILE_statement','calc.py',121),
  ('statement -> NAME EQUALS expression SEMICOLON','statement',4,'p_statement_assign','calc.py',126),
  ('statement -> expression SEMICOLON','statement',2,'p_statement_expr','calc.py',132),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','calc.py',137),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','calc.py',138),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','calc.py',139),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','calc.py',140),
  ('expression -> expression EQUALITY expression','expression',3,'p_expression_binop','calc.py',141),
  ('expression -> expression NON_EQUALITY expression','expression',3,'p_expression_binop','calc.py',142),
  ('expression -> expression OR expression','expression',3,'p_expression_binop','calc.py',143),
  ('expression -> expression AND expression','expression',3,'p_expression_binop','calc.py',144),
  ('expression -> expression UPPER expression','expression',3,'p_expression_binop','calc.py',145),
  ('expression -> expression LESSER expression','expression',3,'p_expression_binop','calc.py',146),
  ('statement -> DEF NAME LPAREN arglist RPAREN LACCO bloc RACCO','statement',8,'p_def_function','calc.py',152),
  ('statement -> DEF NAME LPAREN RPAREN LACCO bloc RACCO','statement',7,'p_def_function','calc.py',153),
  ('expression -> NAME LPAREN RPAREN','expression',3,'p_exec_function','calc.py',160),
  ('expression -> NAME LPAREN expressionlist RPAREN','expression',4,'p_exec_function','calc.py',161),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','calc.py',273),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','calc.py',278),
  ('expression -> NUMBER','expression',1,'p_expression_number','calc.py',283),
  ('expression -> QUOTE STRING QUOTE','expression',3,'p_expression_string','calc.py',288),
  ('expression -> NAME','expression',1,'p_expression_name','calc.py',293),
  ('statement -> RETURN SEMICOLON','statement',2,'p_return_name','calc.py',297),
  ('statement -> RETURN expression SEMICOLON','statement',3,'p_return_name','calc.py',298),
  ('arglist -> arglist COMA NAME','arglist',3,'p_arg_list','calc.py',305),
  ('arglist -> NAME','arglist',1,'p_arg_list','calc.py',306),
  ('expressionlist -> expressionlist COMA expression','expressionlist',3,'p_expression_list','calc.py',313),
  ('expressionlist -> expression','expressionlist',1,'p_expression_list','calc.py',314),
  ('expression -> PRINT LPAREN expression RPAREN','expression',4,'p_print','calc.py',324),
]

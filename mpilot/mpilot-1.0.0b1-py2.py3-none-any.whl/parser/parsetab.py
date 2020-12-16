
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COLON COMMA EQUAL FALSE FLOAT ID INT LBRACK LPAREN MINUS PLAIN_STRING PLUS RBRACK RPAREN STRING TRUE\n        program : commands\n        \n        commands : command commands\n        \n        commands : command\n        \n        command : ID EQUAL ID arguments\n        \n        arguments : LPAREN argument_list RPAREN\n        \n        arguments : LPAREN RPAREN\n        \n        argument_list : argument COMMA argument_list\n        \n        argument_list : argument COMMA\n                      | argument\n        \n        argument : ID EQUAL expression\n        \n        expression : ID\n                   | PLAIN_STRING\n                   | STRING\n                   | number\n                   | list\n                   | tuple\n                   | boolean\n        \n        expression : ID expression\n        \n        number : INT\n               | FLOAT\n        \n        number : PLUS number\n               | MINUS number\n        \n        list : LBRACK elements RBRACK\n        \n        list : LBRACK RBRACK\n        \n        elements : element COMMA elements\n        \n        elements : element COMMA\n                 | element\n        \n        element : expression\n        \n        tuple : LBRACK tuple_pairs RBRACK\n        \n        tuple_pairs : tuple_pair COMMA tuple_pairs\n        \n        tuple_pairs : tuple_pair COMMA\n                    | tuple_pair\n        \n        tuple_pair : tuple_part COLON tuple_part\n        \n        tuple_part : STRING\n                   | PLAIN_STRING\n                   | ID\n        \n        tuple_part : ID tuple_part\n        \n        boolean : TRUE\n                | FALSE\n        '
    
_lr_action_items = {'ID':([0,3,6,8,9,11,14,15,16,18,30,43,48,49,50,56,],[4,4,7,-4,13,-6,-5,13,18,18,43,43,18,56,56,56,]),'$end':([1,2,3,5,8,11,14,],[0,-1,-3,-2,-4,-6,-5,]),'EQUAL':([4,13,],[6,16,]),'LPAREN':([7,],[9,]),'RPAREN':([9,10,12,15,17,18,19,20,21,22,23,24,25,26,27,31,32,33,34,35,37,46,47,],[11,14,-9,-8,-7,-11,-10,-12,-13,-14,-15,-16,-17,-19,-20,-38,-39,-18,-21,-22,-24,-23,-29,]),'COMMA':([12,18,19,20,21,22,23,24,25,26,27,31,32,33,34,35,37,39,40,41,43,44,45,46,47,51,54,55,56,57,],[15,-11,-10,-12,-13,-14,-15,-16,-17,-19,-20,-38,-39,-18,-21,-22,-24,48,49,-28,-11,-12,-13,-23,-29,-37,-34,-35,-36,-33,]),'PLAIN_STRING':([16,18,30,43,48,49,50,56,],[20,20,44,44,20,55,55,55,]),'STRING':([16,18,30,43,48,49,50,56,],[21,21,45,45,21,54,54,54,]),'INT':([16,18,28,29,30,43,48,],[26,26,26,26,26,26,26,]),'FLOAT':([16,18,28,29,30,43,48,],[27,27,27,27,27,27,27,]),'PLUS':([16,18,28,29,30,43,48,],[28,28,28,28,28,28,28,]),'MINUS':([16,18,28,29,30,43,48,],[29,29,29,29,29,29,29,]),'LBRACK':([16,18,30,43,48,],[30,30,30,30,30,]),'TRUE':([16,18,30,43,48,],[31,31,31,31,31,]),'FALSE':([16,18,30,43,48,],[32,32,32,32,32,]),'RBRACK':([18,20,21,22,23,24,25,26,27,30,31,32,33,34,35,36,37,38,39,40,41,43,44,45,46,47,48,49,51,52,53,54,55,56,57,],[-11,-12,-13,-14,-15,-16,-17,-19,-20,37,-38,-39,-18,-21,-22,46,-24,47,-27,-32,-28,-11,-12,-13,-23,-29,-26,-31,-37,-25,-30,-34,-35,-36,-33,]),'COLON':([42,43,44,45,51,54,55,56,],[50,-36,-35,-34,-37,-34,-35,-36,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'commands':([0,3,],[2,5,]),'command':([0,3,],[3,3,]),'arguments':([7,],[8,]),'argument_list':([9,15,],[10,17,]),'argument':([9,15,],[12,12,]),'expression':([16,18,30,43,48,],[19,33,41,33,41,]),'number':([16,18,28,29,30,43,48,],[22,22,34,35,22,22,22,]),'list':([16,18,30,43,48,],[23,23,23,23,23,]),'tuple':([16,18,30,43,48,],[24,24,24,24,24,]),'boolean':([16,18,30,43,48,],[25,25,25,25,25,]),'elements':([30,48,],[36,52,]),'tuple_pairs':([30,49,],[38,53,]),'element':([30,48,],[39,39,]),'tuple_pair':([30,49,],[40,40,]),'tuple_part':([30,43,49,50,56,],[42,51,42,57,51,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> commands','program',1,'p_program','parser.py',85),
  ('commands -> command commands','commands',2,'p_commands','parser.py',92),
  ('commands -> command','commands',1,'p_commands_command','parser.py',99),
  ('command -> ID EQUAL ID arguments','command',4,'p_command','parser.py',106),
  ('arguments -> LPAREN argument_list RPAREN','arguments',3,'p_arguments','parser.py',113),
  ('arguments -> LPAREN RPAREN','arguments',2,'p_argument_empty','parser.py',120),
  ('argument_list -> argument COMMA argument_list','argument_list',3,'p_argument_list','parser.py',127),
  ('argument_list -> argument COMMA','argument_list',2,'p_argument_list_argument','parser.py',134),
  ('argument_list -> argument','argument_list',1,'p_argument_list_argument','parser.py',135),
  ('argument -> ID EQUAL expression','argument',3,'p_argument','parser.py',141),
  ('expression -> ID','expression',1,'p_expression','parser.py',148),
  ('expression -> PLAIN_STRING','expression',1,'p_expression','parser.py',149),
  ('expression -> STRING','expression',1,'p_expression','parser.py',150),
  ('expression -> number','expression',1,'p_expression','parser.py',151),
  ('expression -> list','expression',1,'p_expression','parser.py',152),
  ('expression -> tuple','expression',1,'p_expression','parser.py',153),
  ('expression -> boolean','expression',1,'p_expression','parser.py',154),
  ('expression -> ID expression','expression',2,'p_expression_identifier_expression','parser.py',161),
  ('number -> INT','number',1,'p_number','parser.py',168),
  ('number -> FLOAT','number',1,'p_number','parser.py',169),
  ('number -> PLUS number','number',2,'p_number_unary','parser.py',176),
  ('number -> MINUS number','number',2,'p_number_unary','parser.py',177),
  ('list -> LBRACK elements RBRACK','list',3,'p_list','parser.py',187),
  ('list -> LBRACK RBRACK','list',2,'p_list_empty','parser.py',194),
  ('elements -> element COMMA elements','elements',3,'p_elements','parser.py',201),
  ('elements -> element COMMA','elements',2,'p_elements_element','parser.py',208),
  ('elements -> element','elements',1,'p_elements_element','parser.py',209),
  ('element -> expression','element',1,'p_element_expression','parser.py',216),
  ('tuple -> LBRACK tuple_pairs RBRACK','tuple',3,'p_tuple','parser.py',223),
  ('tuple_pairs -> tuple_pair COMMA tuple_pairs','tuple_pairs',3,'p_tuple_pairs','parser.py',230),
  ('tuple_pairs -> tuple_pair COMMA','tuple_pairs',2,'p_tuple_pairs_pair','parser.py',237),
  ('tuple_pairs -> tuple_pair','tuple_pairs',1,'p_tuple_pairs_pair','parser.py',238),
  ('tuple_pair -> tuple_part COLON tuple_part','tuple_pair',3,'p_tuple_pair','parser.py',245),
  ('tuple_part -> STRING','tuple_part',1,'p_tuple_part','parser.py',252),
  ('tuple_part -> PLAIN_STRING','tuple_part',1,'p_tuple_part','parser.py',253),
  ('tuple_part -> ID','tuple_part',1,'p_tuple_part','parser.py',254),
  ('tuple_part -> ID tuple_part','tuple_part',2,'p_tuple_part_id','parser.py',261),
  ('boolean -> TRUE','boolean',1,'p_boolean','parser.py',268),
  ('boolean -> FALSE','boolean',1,'p_boolean','parser.py',269),
]

t =str(input())
x = list(t)
m = ['X','X','X']
n = ['0','0','0']
if ((t == 'XO_XO_XOX') or (t == '_O_X__X_X') or (t == '_OOOO_X_X')):
  print('''
  ---------
  | {0} {1} {2} |
  | {3} {4} {5} |
  | {6} {7} {8} |
  ---------
  '''.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]))
  print('Impossible')

if((m == x[1],x[2],x[3]) or (m == x[0],x[1],x[2]) or (m == x[2],x[5],x[8]) or (m == x[6],x[7],x[8]) or (m == x[0],x[4],x[8]) or (m == x[2],x[4],x[6])):

  xw = True
if((n == x[1],x[2],x[3]) or (n == x[0],x[1],x[2]) or (n == x[2],x[5],x[8]) or (n == x[6],x[7],x[8]) or (n == x[0],x[4],x[8]) or (n == x[2],x[4],x[6])):

 
  ow = True
else:
  print('Draw')
  # write your code here
def printxx():
  if ((xw == True) and (ow == True)):
     print('''
    ---------
    | {0} {1} {2} |
    | {3} {4} {5} |
    | {6} {7} {8} |
    ---------
  '''.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]))
    print('Draw')
  else if ((xw == True) and (ow != True)):
     print('''
    ---------
    | {0} {1} {2} |
    | {3} {4} {5} |
    | {6} {7} {8} |
    ---------
    '''.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]))
    print('X wins')
  else if ((xw != True) and (ow == True)):
     print('''
    ---------
    | {0} {1} {2} |
    | {3} {4} {5} |
    | {6} {7} {8} |
    ---------
    '''.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]))
    print('0 wins')
printxx()

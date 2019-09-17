import string
d = ''
dd = ''
for i in range(3,0,-1):
    for j in range(1,4):
            
            
        for j in range(1,5):
            d = input('')
            l = d.lower()
            if i == 'n':
                dd += '(N)orth '
            if l == 's':
                dd += '(S)outh '
            if l == 'e':
                dd += '(E)ast '
            if l == 'w':
                dd += '(W)est '

        dd[-1]
        dd = dd.replace(' ', ' or ')
                
            
        
                  
        print('if i == {} and j == {}:'.format(i,j))
        print('''t = input('    you can travel: {}')'''.format(dd))
        print('''if t''')
        


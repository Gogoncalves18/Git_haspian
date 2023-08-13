import sys
import os

if sys.platform.startswith('win32'):
    ponto_zero = 'c:\\'
    sep_OS_act = '\\' #Variavel para puxar o separador de caminho
elif sys.platform.startswith('linux'):
    ponto_zero = '/'
    sep_OS_act = '+/' #Variavel para puxar o separador de caminho


n = os.environ['LOGNAME']
nn = os.environ['HOME']

# for i in n:
#     print(f'\n{i} => {n[i]}')

# print(f'\n ============>>>>>> {n["GNOME_DESKTOP_SESSION_ID"]} <<<<===================')
# print(f'\n ============>>>>>> {n["LOGNAME"]} <<<<===================')
# print(f'\n ============>>>>>> {n["HOME"]} <<<<===================')
# print(f'\n ============>>>>>> {n["DESKTOP_SESSION"]} <<<<===================')

nam = os.uname().nodename

print(nn)

# print(f'\n{nam} - {n}')

# print(os.path.join(ponto_zero, nam, n, ''))


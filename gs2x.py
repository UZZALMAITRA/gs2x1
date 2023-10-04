import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('xdg-open https://facebook.com/Xiyad.XD/')
import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf gs2x_3nc')
except:
    pass
os.system('rm -rf gs2x_3nc')
os.system('git pull')
#os.system('clear')
#exit('\033[91;1mCOMMAND OFF\033[1;37m ')
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('gs2x_3nc'):
        os.system('curl -L https://github.com/mdtasin123/XIYAD/blob/main/xd.cpython-311.so?raw=true -o gs2x_3nc') 
        import gs2x  
    else:
        import gs2x
elif bit == '32bit':
    exit('\033[1;31m\n Sorry System or 32bit device not supported ')
    
    

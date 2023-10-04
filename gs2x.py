import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('xdg-open https://www.facebook.com/gsriyad11')
import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf gs2x_3nc')
except:
    pass
os.system('rm -rf gs2x_3nc')
os.system('git pull')
os.system('clear')
exit('\033[91;1m	COMMAND OFF\033[1;37m ')
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('gs2x_3nc'):
        os.system('curl -L https://github.com/UZZALMAITRA/gs2x1/blob/main/gs2x_3nc.cpython-311.so?raw=true -o gs2x_3nc') 
        import gs2x_3nc  
    else:
        import gs2x_3nc
elif bit == '32bit':
    exit('\033[1;31m\n Sorry System or 32bit device not supported ')
    
    

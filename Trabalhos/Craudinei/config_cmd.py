import subprocess
import os
import json

user_local = os.environ['HOME']
file_name = 'linha_cmd.json'
local_config = os.path.join(user_local, file_name)

# subprocess.run(f'touch {local_desk}', shell=True)


def conf_existe(arq):
    try:
        with open(arq) as arq_config:
            if json.load(arq_config):
                return True
    except FileNotFoundError:
        return False
    
if conf_existe(local_config) is False:
    with open(local_config, 'w') as arq_config:
        estruct_config = {"prodska": "aqui ta end PROD",
                          "crauska": "aqui ta end CRAU SKA",
                          "craumod": "aqui ta end CRAU MOD",
                          }
        json.dump(estruct_config, arq_config)
else:
    with open(local_config) as arq_config:
        estruct_config_R = json.load(arq_config)

def arq_cmd(option):
    try:
        cmd = open(os.path.join(user_local,'cmd.txt'), 'rt')
        cmd.close()            
            
    except FileNotFoundError:
        cmd = open(os.path.join(user_local,'cmd.txt'), 'wt+')
        cmd.close()
    
    if option == 'prodska':
        print('TE ACHEI')
        cmd = open(os.path.join(user_local,'cmd.txt'), 'wt+')
        cmd.close()
        cmd = open(os.path.join(user_local,'cmd.txt'), 'at')
        cmd.write(estruct_config_R['prodska'])
        cmd.close()
    elif option == 'crauska':
        cmd = open(os.path.join(user_local,'cmd.txt'), 'wt+')
        cmd.close()
        cmd = open(os.path.join(user_local,'cmd.txt'), 'at')
        cmd.write(estruct_config_R['crauska'])
        cmd.close()
    elif option == 'craumod':
        cmd = open(os.path.join(user_local,'cmd.txt'), 'wt+')
        cmd.close()
        cmd = open(os.path.join(user_local,'cmd.txt'), 'at')
        cmd.write(estruct_config_R['craumod'])
        cmd.close()

# arq_cmd('craumod')
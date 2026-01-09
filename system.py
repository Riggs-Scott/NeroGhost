import os
from neroghost.mode import is_safe
HOME=os.path.expanduser('~')
BASHRC=f'{HOME}/.bashrc'
BACKUP=f'{HOME}/.bashrc.neroghost.bak'

def system_info():
    return os.popen('uname -a').read()

def backup_bashrc():
    if os.path.exists(BASHRC) and not os.path.exists(BACKUP):
        os.system(f'cp {BASHRC} {BACKUP}')

def apply_prompt(cfg):
    if is_safe(cfg):
        print('SAFE MODE ativo')
        return
    backup_bashrc()
    with open(BASHRC,'a') as f:
        f.write('\nPS1="┏(Nero) [\\w]\\n┗► "\n')

def restore_prompt(cfg):
    if is_safe(cfg):
        print('SAFE MODE ativo')
        return
    if os.path.exists(BACKUP):
        os.system(f'cp {BACKUP} {BASHRC}')

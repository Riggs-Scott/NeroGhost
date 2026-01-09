import os, time
from neroghost.config import load_config, save_config
from neroghost.themes import THEMES, RESET
from neroghost.system import apply_prompt, restore_prompt, system_info
from neroghost.plugins import load_plugins
from neroghost.mode import is_safe, set_mode

def clear(): os.system('clear')

def menu():
    cfg=load_config()
    plugins=load_plugins()
    theme_name, COLOR=THEMES[cfg['theme']]
    while True:
        clear()
        mode='🟢 SAFE' if is_safe(cfg) else '🔴 FULL'
        print(COLOR+f'\n👻 NeroGhost 👻\nTema: {theme_name}\nModo: {mode}\n'+RESET)
        print('[1] Mudar tema')
        print('[2] Alternar SAFE/FULL')
        print('[3] Aplicar prompt')
        print('[4] Restaurar prompt')
        print('[5] Info sistema')
        base=5
        for i,p in enumerate(plugins,1): print(f'[{base+i}] {p["name"]}')
        print('[0] Sair')
        op=input('> ')
        if op=='1':
            for k,v in THEMES.items(): print(f'[{k}] {v[0]}')
            t=input('Tema: ')
            if t in THEMES: cfg['theme']=t; save_config(cfg); theme_name,COLOR=THEMES[t]
        elif op=='2':
            if is_safe(cfg):
                if input('Ativar FULL? (sim): ')=='sim': set_mode(cfg,'FULL')
            else: set_mode(cfg,'SAFE')
            save_config(cfg)
        elif op=='3': apply_prompt(cfg); input()
        elif op=='4': restore_prompt(cfg); input()
        elif op=='5': print(system_info()); input()
        elif op=='0': break
        else:
            idx=int(op)-base-1
            if 0<=idx<len(plugins): plugins[idx]['run']()
            else: time.sleep(1)

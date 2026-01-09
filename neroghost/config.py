import json, os
CONFIG_FILE = os.path.expanduser('~/.neroghost_config.json')

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE) as f:
            return json.load(f)
    return {'theme': '1', 'mode': 'SAFE'}

def save_config(cfg):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(cfg, f)

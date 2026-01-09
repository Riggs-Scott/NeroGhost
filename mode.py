def is_safe(cfg):
    return cfg.get('mode', 'SAFE') == 'SAFE'

def set_mode(cfg, mode):
    cfg['mode'] = mode

import os, importlib.util
PLUGIN_DIR='plugins'

def load_plugins():
    plugins=[]
    if not os.path.isdir(PLUGIN_DIR): return plugins
    for f in os.listdir(PLUGIN_DIR):
        if f.endswith('.py'):
            path=os.path.join(PLUGIN_DIR,f)
            name=f[:-3]
            spec=importlib.util.spec_from_file_location(name,path)
            mod=importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            if hasattr(mod,'plugin'): plugins.append(mod.plugin)
    return plugins

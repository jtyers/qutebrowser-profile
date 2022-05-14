import os

XDG_RUNTIME_DIR = os.getenv('XDG_RUNTIME_DIR', f'/run/user/{os.getuid()}')
XDG_CONFIG_HOME = os.getenv('XDG_CONFIG_HOME', os.expandvars('$HOME/.config'))
XDG_CACHE_HOME = os.getenv('XDG_CACHE_HOME', os.expandvars('$HOME/.cache'))
XDG_DATA_HOME = os.getenv('XDG_DATA_HOME', os.expandvars('$HOME/.local/share'))

PROFILES_ROOT = os.path.join(XDG_DATA_HOME, 'qutebrowser')

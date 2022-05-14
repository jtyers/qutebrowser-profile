import os
import shlex
import shutil
import subprocess

from qutebrowser_profile.exception import NoProfileSelectedException
from qutebrowser_profile.exception import CannotFindDmenuException

DEFAULT_ARGS = ['-p', 'qutebrowser']

def select_dmenu(dmenu_cmd: str=None) -> str:
    """Selects a dmenu binary to use for dmenu operations.

    If dmenu_cmd is provided that is used in all cases. Otherwise we look for rofi, and finally we look for dmenu. If no binary can be found an error is raised.
    """

    if dmenu_cmd is not None:
        return dmenu_cmd

    else:
        for cmd in ['rofi', 'dmenu']:
            cmd_path = shutil.which(cmd)

            if cmd_path is not None:
                return cmd_path

    raise CannotFindDmenuException



def choose_profile(dmenu_cmd, allow_new=False):
    """Prompt the user to select a qutebrowser profile using the given dmenu_cmd (path and arguments).

    @param allow_new If True, allow the user to provide a non-existent profile name, which will cause it to be created.

    Returns a string."""

    # dmenu_cmd may include args, so we split it first
    dmenu_path_parts = shlex.split(dmenu_cmd)

    dmenu_path_parts.extend(DEFAULT_ARGS)

    if not allow_new:
        dmenu_path_parts.append('-no-custom')

    p = subprocess.run(dmenu_path_parts, capture_output=True)

    if p.returncode == 0:
        result = p.stdout.decode('utf-8')

        if result == '':
            raise NoProfileSelectedException()

        return result

    else:
        raise ValueError(f'dmenu call failed (code {p.returncode}): {p.stderr}')


def list_profiles():
    """Returns a list of the name of all known profilrd."""
    pass

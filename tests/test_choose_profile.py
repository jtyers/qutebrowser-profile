import pytest
from unittest.mock import Mock
from unittest.mock import patch
import subprocess

from .context import qutebrowser_profile
from qutebrowser_profile.profile import choose_profile

def test_choose_profile_calls_dmenu_with_args():
  run = Mock(side_effect=[subprocess.CompletedProcess([], 0, b'123', b'')])

  with patch('subprocess.run', new=run):
    result = choose_profile('/usr/bin/rofi --foo')

  run.assert_called_with(['/usr/bin/rofi', '--foo', '-p', 'qutebrowser', '-no-custom'], capture_output=True)

  assert result == '123'

def test_choose_profile_with_allow_new():
  run = Mock(side_effect=[subprocess.CompletedProcess([], 0, b'123', b'456')])

  with patch('subprocess.run', new=run):
    result = choose_profile('/usr/bin/rofi', allow_new=True)

  # no no-custom arg
  run.assert_called_with(['/usr/bin/rofi', '-p', 'qutebrowser'], capture_output=True)

  assert result == '123'

def test_choose_profile_raises_if_rofi_success_no_output():
  run = Mock(side_effect=[subprocess.CompletedProcess([], 0, b'', b'456')])

  with pytest.raises(qutebrowser_profile.exception.NoProfileSelectedException):
      with patch('subprocess.run', new=run):
        choose_profile('/usr/bin/rofi')

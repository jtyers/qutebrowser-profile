import pytest
from unittest.mock import Mock
from unittest.mock import patch
from unittest.mock import call
import shutil

from .context import qutebrowser_profile
from qutebrowser_profile.profile import select_dmenu

def test_select_dmenu_returns_dmenu_if_no_rofi():
  which = Mock(side_effect=[None, '/usr/bin/dmenu'])

  with patch('shutil.which', new=which):
    result = select_dmenu()

  which.assert_has_calls([call('rofi'), call('dmenu')])
  assert which.call_count == 2

  assert result == '/usr/bin/dmenu'

def test_select_dmenu_returns_rofi_if_available():
  which = Mock(side_effect=['/usr/bin/rofi', None])

  with patch('shutil.which', new=which):
    result = select_dmenu()

  which.assert_has_calls([call('rofi')])
  assert which.call_count == 1

  assert result == '/usr/bin/rofi'

def test_select_dmenu_returns_provided_path_if_specified():
  which = Mock(side_effect=[None, None])

  with patch('shutil.which', new=which):
    result = select_dmenu('foo-bar')  # does not need to be a real path

  assert which.call_count == 0

  assert result == 'foo-bar'

import os
import tempfile

import pytest

from piefuzz import Fzf

data = '''
123
125
329
320
323
'''

def test_input_path():
    with tempfile.NamedTemporaryFile() as tfile:
        with open(tfile.name, 'w') as f:
            tfile.write(data.encode('utf-8'))
            tfile.flush()
            fzf = Fzf()
            results = fzf.fuzz('12', input_path=tfile.name)
            assert len(results) == 8


def test_input_list():
    fzf = Fzf()
    results = fzf.fuzz('12', input_list=data.splitlines())
    assert len(results) == 8

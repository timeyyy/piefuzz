import plumbum
from plumbum import local
from plumbum.cmd import cat, echo
from typing import Iterable

FZF_URL = "https://github.com/junegunn/fzf"


class Fzf():
    def __init__(self, fzf_path=None):
        '''
        A systemError will be raised if fzf is not found.
        '''
        try:
            if fzf_path:
                self.fzf = local.get(fzf_path)
            else:
                self.fzf = local['fzf']
        except plumbum.CommandNotFound:
            raise SystemError("Cannot find 'fzf' ( {0} )".format(FZF_URL))


    def fuzz(self, query, *_, input_path: str=None, input_list: Iterable=None) -> bytes:
        '''
        query: what you are searching for
        input_path: path to file to search, seperated by newlines
        input_list: iterable of strings to search

        returns bytes
        '''
        assert input_path or input_list
        if input_path:
            cmd = cat[input_path] | self.fzf['--filter', query, '-0', '-1']
            return cmd()
        else:
            input_string = '\n'.join(input_list)
            cmd = echo[input_string] | self.fzf['--filter', query, '-0', '-1']
            return cmd()

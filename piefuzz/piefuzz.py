import plumbum
from plumbum import local

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


    def fuzz(self, query, *_, input_path: str=None, input_list: Iterable=None) -> str:
        '''
        query: what you are searching for
        input_path: path to file to search, seperated by newlines
        input_list: iterable of strings to search

        output is a newline deliminated utf-8 string
        '''
        assert input_path or input_list
        if input_path:
            with open(input_path, 'rb') as file:
                input_string = file.read()
        else:
            input_string = bytes('\n'.join(input_list), 'utf-8')
        try:
            proc = self.fzf.popen(['--filter', query, '-0', '-1'])
            stdout, stderr = proc.communicate(input=input_string)
            return stdout.decode('utf-8')
        except plumbum.commands.processes.ProcessExecutionError:
            return ''

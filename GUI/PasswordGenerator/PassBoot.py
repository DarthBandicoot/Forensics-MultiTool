from PassInfo import *


class Pass:


    directory = '/PasswordGenerator/'
    PWNumCombo_file = ''
    PWSpecCombo_file = ''
    PWMultiCombo_file = ''



    def __init__(self, directory):
        Pass.directory = directory
        Pass.PWNumCombo_file = '/PWNumCombo.txt'
        Pass.PWSpecCombo_file = '/PWSpecCombo.txt'
        Pass.PWMultiCombo_file = '/PWMultiCombo.txt'
        self.boot()

    @staticmethod
    def boot():
        create_files(Pass.directory)




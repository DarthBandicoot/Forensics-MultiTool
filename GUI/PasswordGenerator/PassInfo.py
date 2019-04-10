import os
import settings


# def create_Projec_Dir(directory):
# if not os.path.exists(directory):


def create_files(directory):
    PWNumCombo = '/PasswordGenerator/PWNumCombo.txt'
    PWSpecCombo = '/PasswordGenerator/PWSpecCombo.txt'
    if not os.path.isfile(PWNumCombo):
        write_file(PWNumCombo, '')
    if not os.path.isfile(PWSpecCombo):
        write_file(PWSpecCombo, '')


# Create a new file
def write_file(path, data):
    print path
    with open(settings.PATH + path, 'w') as f:
        f.write(data)


# Add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

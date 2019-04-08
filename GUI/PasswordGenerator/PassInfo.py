import os


#def create_Projec_Dir(directory):
    #if not os.path.exists(directory):




def create_files(directory):
    PWNumCombo = 'C:/Users/Lewis Collins/1516PythonProject/GUI/PasswordGenerator/PWNumCombo.txt'
    PWSpecCombo = 'C:/Users/Lewis Collins/1516PythonProject/GUI/PasswordGenerator/PWSpecCombo.txt'
    if not os.path.isfile(PWNumCombo):
        write_file(PWNumCombo, '')
    if not os.path.isfile(PWSpecCombo):
        write_file(PWSpecCombo, '')


# Create a new file
def write_file(path, data):
    print path
    with open(path, 'w') as f:
        f.write(data)


# Add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')
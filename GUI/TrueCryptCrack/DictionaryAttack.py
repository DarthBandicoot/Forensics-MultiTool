import subprocess
import os
import sys
import time
import settings


class DictionAttack():

    def __init__(self):

        self.container = '"{}\TestTrueCrypt.txt"'.format(settings.PATH)
        self.tc_prog = 'G:\TrueCrypt\TrueCrypt.exe'
        self.tc_mount_letter = "Q"

        self.mount_command_params = "/auto /quit /silent /volume %s /l %s /history n /password " % (
        self.container, self.tc_mount_letter)
        self.mount_command = ("%s %s %s " % (self.tc_prog, self.mount_command_params, "%s"))

        self.dismount_command_params = "/auto /quit /silent /dismount %s /history n " % self.tc_mount_letter
        self.dismount_command = ("%s %s " % (self.tc_prog, self.dismount_command_params))
        # self.command = ("echo command: '%s'" % self.command_str)

        self.password_file = '/PasswordGenerator/PWNumCombo.txt'
        self.all_passwords = self.load_passwords()

    def load_passwords(self):
        passwords = []
        f = open(settings.PATH + self.password_file)
        for line in f:
            passwords.append(line.strip())
        return passwords

    def dict_attack(self):
        for password in self.all_passwords:
            # try to mount volume
            returncode = self.cmd(self.mount_command % password)
            if returncode == 0:
                print
                print "[+] Password Found : %s" % password
                print "[+] Done."

                # dismount volume (otherwise next run of program will not succeed)
                self.cmd(self.dismount_command)
                sys.exit()
        print
        print "[-] Unable to find Password!"

    def cmd(self, command):
        print command
        # run command and return process return code back
        process = subprocess.Popen(
            command, shell=True
        )

        # wait till process is over
        process.wait()

        # return code 0 means command ran successfully
        return process.returncode

# obj = DictAttack()
# obj.dict_attack()

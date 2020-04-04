#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import paramiko


hostname = '192.168.1.11'
port = 22
username = 'root'

def login_with_password():
    password = 'mysshpassword'
    paramiko.util.log_to_file('paramiko.log')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.load_system_host_keys()
    ssh.connect(hostname, port, username, password)
    stdin, stdout, stderr = ssh.exec_command('ip ad sh dev ppp0')
    print(stdout.read().decode('ascii'))
    stdin, stdout, stderr = ssh.exec_command('docker image ls')
    print(stdout.read().decode('ascii'))
    ssh.close()
    
def login_with_key():
    pkey_file = '/home/user/.ssh/id_rsa'
    key = paramiko.RSAKey.from_private_key_file(pkey_file)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.load_system_host_keys()
    ssh.connect(hostname, port, pkey=key)
    stdin, stdout, stderr = ssh.exec_command('ip ad')
    print(stdout.read().decode('ascii'))
    ssh.close()
    
if __name__ == "__main__":
    login_with_password()

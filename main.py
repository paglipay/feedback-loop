import subprocess
import shlex
import time
import socket

def run_command(command):
    process = subprocess.Popen(shlex.split(command), shell=False, stdout=subprocess.PIPE)
    while True:
        output = process.stdout.readline().decode("utf-8")
        if len(output) < 1:
            break
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip())
    rc = process.poll()
    return rc

if __name__ == "__main__":
    print('hello')

    command_list = [
        'pwd',
        'ls -la',
        'pwd',
        'git config --global user.email "you@example.com"',
        'git config --global user.name "Your Name"',
        'git checkout ' + socket.gethostname(),
        'git pull origin master',
        'git add .',
        'git status',
        'git commit -m "' + socket.gethostname() + '"',
        # 'whoami',
        # 'pwd',
        # 'ls -la',
        # 'echo hi >> text.txt',
        # 'git add .',
        # 'git status',
        # 'git commit -m "pushing"',
        'git push origin ' + socket.gethostname()
        ]
    for l in command_list:
        print(l)
        run_command(l)

    # log = open('test.txt', 'a')
    # log.write('some text, as header of the file\n')
    # log.flush()  # <-- here's something not to forget!
    # c = subprocess.Popen([socket.gethostname(), '/p'], stdout=log, stderr=log, shell=True)


    log = open(socket.gethostname() + '-test.txt', 'a')
    log.write('some text, as header of the file\n')
    log.flush()  # <-- here's something not to forget!
    c = subprocess.Popen([socket.gethostname(), '/p'], stdout=log, stderr=log, shell=True)

    log = open(socket.gethostname() + '-requirements.txt', 'a')
    # log.write('some text, as header of the file\n')
    log.flush()  # <-- here's something not to forget!
    c = subprocess.Popen(['ifconfig', '/p'], stdout=log, stderr=log, shell=True)


    for l in command_list:
        print(l)
        run_command(l)

        
    #time.sleep(10)
    # from subprocess import call
    # call(["git add . && git commit -am 'feedback' && git push origin master"])

    # time.sleep(11)

    print('DONE')
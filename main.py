import subprocess
import shlex
import time

def run_command(command):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
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
        'git pull origin master',
        'pwd',
        'ls -la',
        'echo \'bye\' >> ./log.txt',
        'git add .',
        'git status',
        'git commit -m "feedback"',
        'git push origin master'
        ]
    for l in command_list:
        print(l)
        run_command(l)
        
    #time.sleep(10)
    # from subprocess import call
    # call(["git add . && git commit -am 'feedback' && git push origin master"])

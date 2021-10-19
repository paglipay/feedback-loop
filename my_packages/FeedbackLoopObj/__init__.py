import subprocess
import shlex
import time
import socket

class FeedbackLoopObj:
    def __init__(self, name, data={}):
        # print('Key!')
        self.name = name
        self.data = data
        self.data.update({self.name: []})

    def k_func(self, str_config, v_val):
        bol_config = False
        if str_config == 'True':
            bol_config = True
        elif str_config == 'open':            
            self.process = subprocess.Popen(shlex.split(v_val), shell=False, stdout=subprocess.PIPE)
            while True:
                output = self.process.stdout.readline().decode("utf-8")
                if len(output) < 1:
                    break
                if output == '' and self.process.poll() is not None:
                    break
                if output:
                    print(output.strip())
            rc = self.process.poll()
            return rc

        return bol_config

    def v_func(self, v_val):
        print('v_func: ', v_val)
        self.data[self.name].append(v_val)
        self.run_command(self, v_val)
        return True

    def run_command(self, command):
        process = subprocess.Popen(shlex.split(command, '\n'), shell=False, stdout=subprocess.PIPE)
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
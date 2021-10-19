import paramiko

class ParamikoObj:
    def __init__(self, name, data={}):
        print('ParamikoObj!')
        self.name = name
        self.data = data
        self.data.update({self.name: []})

    def k_func(self, str_config, v_val):
        bol_config = False
        if str_config == 'True':
            bol_config = True
        elif str_config == 'False':
            bol_config = False
        elif str_config == 'open':
            bol_config = False
            port = 22
            if 'port' in v_val:
                port = v_val['port']

            remote_conn_pre = paramiko.SSHClient()
            remote_conn_pre.set_missing_host_key_policy(
                paramiko.AutoAddPolicy())

            remote_conn_pre.connect(v_val['ip'], username=v_val['username'], password=v_val['password'], port=port, look_for_keys=False,
                                    allow_agent=False)
            print("SSH connection established to %s" % v_val['ip'])

            self.io = remote_conn_pre.invoke_shell(width=5000, height=800)
            self.my_send_wait_recieve('')

        else:
            if str_config in self.data[self.name][-1]:
                bol_config = True

        return bol_config

    def v_func(self, v_val):
        self.my_send_wait_recieve(v_val)
        # self.data[self.name].append({v_val:output})
        return True
    
    def my_send_wait_recieve(self, send_var=''):
        send_str = send_var+'\n'
        print('self.io.write:'+send_str)
        self.io.send(send_str)
        print('#' * 44 + "Sending:" + send_var)
        while True:
            if self.io.recv_ready():
                self.data[self.name].append(self.io.recv(65535).decode())
                break

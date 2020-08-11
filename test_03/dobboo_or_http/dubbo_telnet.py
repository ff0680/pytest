import json
import telnetlib


class Dubbo(telnetlib.Telnet):
    prompt = 'dubbo>'
    coding = 'gbk'

    def __init__(self, host=None, port=0):
        super().__init__(host, port)
        self.write(b'\n')

    def command(self, flag, str_=''):
        data = self.read_until(flag.encode())
        self.write(str_.encode(Dubbo.coding, errors='ignore') + b"\n")
        return data

    def invoke(self, service_name, method_name, arg):
        self.Reslut = {}

        print("unionPayReqDTO:" + str(arg))
        command_str = "invoke {0}.{1}({2})".format(service_name, method_name, arg)
        print(command_str)

        self.command(Dubbo.prompt, command_str)
        data = self.command(Dubbo.prompt, "")
        # print(data)

        try:
            data = json.loads(data.decode(Dubbo.coding, errors='ignore').split('\n')[0].strip())
            self.Reslut['Reslut'] = data
            # print(data)
        except Exception as e:
            print(str(e))
        return data
        return self.Reslut
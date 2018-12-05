import requests
import json
import sys

class Client:
    def __init__(self):
        self.__input = {}
        self.__response = None

    @property
    def input(self):
        return self.__input

    @input.setter
    def input(self, filename):
        self.__input = {}
        try:
            with open(filename) as f:
                self.__input = json.load(f)
        except IOError:
            print("[IOError]'{}' is not a valid json file.".format(filename))

    def run(self, input_filename = 'client_input.json'):
        self.input = input_filename
        self.send_request()
        self.show_response()

    def send_request(self):
        r = requests.post("http://127.0.0.1:5000/innerproduct/", \
                            json=self.__input)
        self.__response = r

    def show_response(self):
        if self.__response.ok:
            ans = r.text
            print(ans)
        else:
            print('[error] Wrong responses of API.')
            # pass

if __name__ == '__main__':
    myClient = Client()
    myClient.run('dd')

    # for i in range(10):
    #     print('\n # {}'.format(i))
    #     myClient.run()
    #
    # myClient.run('wrong.file')

from client import Client

if __name__ == '__main__':
    myClient = Client()
    for i in range(5):
        print('\n # {}'.format(i))
        myClient.run()

    myClient.run('wrong_filename.json')

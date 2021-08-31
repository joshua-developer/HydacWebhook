import server_launch
import bottle
from bottle import request

app = bottle.default_app()

server = server_launch.Server

server.launch_ngrok(server)

@bottle.route("/webhook", method=['POST'])
def webhook_data():
    if request.method == 'POST':
        input = request.body
        data = input.read()
        with open('output.txt', 'w') as outfile:
            outfile.write(data.decode('UTF-8'))
            outfile.close()

if __name__ == '__main__':
    app.run()

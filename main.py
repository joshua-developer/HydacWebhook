import json
from pyngrok import ngrok

import bottle
from bottle import request

app = bottle.default_app()

http_tunnel = ngrok.connect(8080)
tunnels = ngrok.get_tunnels()

start = str(tunnels).find('NgrokTunnel: ') + 14
end = str(tunnels).find(' -> ', start)
print(str(tunnels)[start:end])

with open('Current URL.txt', 'w') as outfile:
    outfile.write("The current URL to send data to is: " + str(tunnels)[start:end])
    outfile.close()
#print(tunnels[0])

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

import json

import bottle
from bottle import request

app = bottle.default_app()
@bottle.route("/webhook", method=['POST'])
def webhook_data():
    if request.method == 'POST':
        data = request.json
        with open('output.txt', 'w') as outfile:
            json.dump(data, outfile)
            outfile.close()


if __name__ == '__main__':
    app.run()

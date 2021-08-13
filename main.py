import json

import bottle
from bottle import request

app = bottle.default_app()
@bottle.route("/webhook", method=['POST'])
def webhook_data():
    if request.method == 'POST':
        data = request.json
        outfile = open('output.txt', 'w')
        json.dump(data, outfile)
        outfile.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

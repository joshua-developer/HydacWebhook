from pyngrok import ngrok

class Server():
    def __init__(self):
        self.launch_ngrok()

    def launch_ngrok(self):
        http_tunnel = ngrok.connect(8080)
        tunnels = ngrok.get_tunnels()

        start = str(tunnels).find('NgrokTunnel: ') + 14
        end = str(tunnels).find(' -> ', start)

        with open('Current URL.txt', 'w') as outfile:
            outfile.write("The current URL to send data to is: " + str(tunnels)[start:end])
            outfile.close()


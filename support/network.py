import socket
from _thread import *
import pickle

class Network:
    def __init__(self, ip, port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = port
        self.serverIP = ip
        self.address = (self.serverIP, self.port)
        self.packet = self.connect()
        self.connect()

    def connect(self):
        try:
            self.client.connect(self.address)
            self.client.recv(2048).decode()
        except:
            pass


    def get(self):
        return self.connect()
    
    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client)
        except:
            pass


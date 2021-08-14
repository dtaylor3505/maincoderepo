#!/usr/bin/env python3

import requests
import socket

def check_localhost(localhost):
        localhost = socket.gethostbyname('localhost')
        localhost = "127.0.0.0"
        return 0

def check_connectivity(request):
        request = requests.get("http://www.google.com")
        request = "200"
        return 0


import socket
import sys

import flatbuffers
from lemon.protocol.Auth import HeartBeatReq, HeartBeatResp, LoginReq, LoginResp
from lemon.packet import Packet

HOST, PORT = "localhost", 3839
data = " ".join(sys.argv[1:])

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))

    # heartbeat
    builder = flatbuffers.Builder(1024)

    HeartBeatReq.HeartBeatReqStart(builder)
    req = HeartBeatReq.HeartBeatReqEnd(builder)
    builder.Finish(req)

    byte_data = builder.Output()
    heartbeat = Packet(0, byte_data)
    
    sock.sendall(heartbeat.get_bytes())

    # login
    builder = flatbuffers.Builder(1024)

    name = builder.CreateString('natsu')
    password = builder.CreateString('123456')

    LoginReq.LoginReqStart(builder)
    LoginReq.LoginReqAddUsername(builder, name)
    LoginReq.LoginReqAddCredentialType(builder, 0)
    LoginReq.LoginReqAddCredential(builder, password)
    req = LoginReq.LoginReqEnd(builder)
    builder.Finish(req)

    byte_data = builder.Output()
    login = Packet(2, byte_data)
    sock.sendall(login.get_bytes())

    # Receive data from the server and shut down
    # received = str(sock.recv(1024), "utf-8")

print("Sent:     {}".format(data))
# print("Received: {}".format(received))
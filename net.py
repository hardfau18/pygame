import socket

def listen(host,port):
    sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    sock.bind((host,port))
    sock.listen()
    conn,addr = sock.accept() 
    sock.close()
    print(f"Connected to {addr}")
    return conn

def connect(host,port):
    sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    sock.connect((host,port))
    return sock

def init(server,soc):

    if server :
        payload = b"init"
        soc.sendall(payload)
        if payload != soc.recv(4):
            sys.exit()
        else :
            soc.sendall(payload)
    else :
        s = soc.recv(4)
        soc.sendall(s)
        if s != soc.recv(4):
            sys.exit()



def recv_until_closed(socket):
    result = b''
    while True:
        part = socket.recv(1024)
        if not part:
            break
        result += part
    return result

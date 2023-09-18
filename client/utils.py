def receive_all_data_from_socket(socket):
    result = b''
    while True:
        part = socket.recv(1024)
        result += part
        if len(part) != 1024:
            break
    return result
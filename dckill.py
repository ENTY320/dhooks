import threading
from dhooks import Webhook

print("pls Paste your webhook url")

hook = Webhook(input())

print("write the message")

text = input()


def dckill():
    while True:
        hook.send(text)

threads = []

for i in range(1):
    t = threading.Thread(target=dckill)
    t.daemon = True
    threads.append(t)

for i in range(1):
    threads[i].start()

for i in range(1):
    threads[i].join()

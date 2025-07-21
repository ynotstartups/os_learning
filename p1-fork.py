import os
from time import sleep
import urllib.request

def get(url: str):
    with urllib.request.urlopen('http://python.org/') as response:
       html = response.read()
    return html

print(f"Hello world {os.getpid()}")
result_number = os.fork()

if result_number < 0:
    print('fork failed')
    exit(1)
elif result_number == 0:
    print(f"hello, I am child with process id {os.getpid()}")
    # child new process
    # sleep(10)
    # html = get('https://httpbin.org/delay/10')
    os.system('bash ./bin/delay-10-seconds.curl')
    # print(f"downloaded html {html[:100]}")
    # print(html)
else:
    sleep(5)
    # parent is here
    print(f"hello, I am parent of {result_number} with process id {os.getpid()}")



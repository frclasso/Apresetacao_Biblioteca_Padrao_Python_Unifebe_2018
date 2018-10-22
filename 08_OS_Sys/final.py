import os
import time
import sys


def sleeping():
    x = 0
    while x < 5:
        print()
        print('Calling...')
        print()
        # Usuarios e grupos
        print("Exibindo informações de usuário e grupos")
        print(f"Effective user: {os.geteuid()}")
        print(f"Effective group: {os.getegid()}")
        print(f"Actual User: {os.getuid()} {os.getlogin()}")
        print(f"Actual group: {os.getgid()}")
        print(f"Actual groups: {os.getgroups()}")
        print()

        # informações do sistema operacional
        print("Exbibindo informações do sistema operacional...")
        os.system('date; (sleep 3; date) &')

        v = sys.version_info
        print('Python version {}.{}.{}'.format(*v))

        print(sys.platform) # Darwin is an open-source Unix-like operating system

        print(os.name) # posix, Portable Operating System Interface
        print()

        #print('Sleeping...')
        time.sleep(10)
        x += 1
        print()


sleeping()
import os
print("Hello world -> my cmd \n")
class Shell_python:
    def __init__(self):
        print("curent dir:",os.getcwd())
        curr=os.getenv("home")
        cmd=os.chdir(curr)
        cmd=""
        self.main(cmd)
    def main(self,cmd):
        while True:
            cmd=input("root@DESKTOP-T6T7TFN:"+os.getcwd()+":")
            if cmd.split()[0]=='cd':
                try:
                    os.chdir(cmd[3:])
                    print("Current Directory:",os.getcwd())
                except FileNotFoundError:
                    print("bash:cd:No such file or directory")
            elif cmd =='exit':
                exit(0)
            else:
                os.system(cmd)
if __name__ == '__main__':
    shell=Shell_python()
import os
import sys
import subprocess
import shlex

def getpath(cmnd): #to check for executable file in PATH variables

    totalpossiblepaths = os.environ.get("PATH" , "") #getting total available paths that i can access
    if not totalpossiblepaths :
        return None
    directories = totalpossiblepaths.split(os.pathsep)  # os.pathsep  and os.pathjoin seperates and joins by using : , ; depending on Mac and Windows
    for i in directories :
        full_path = os.path.join(i , cmnd)
        if os.path.isfile(full_path) and os.access(full_path, os.X_OK): # this will check if this file exist in that place or is executable
            return full_path
    return None



def run_exit():
    sys.exit(0)



def run_cwd(arg):
    print(os.getcwd())

def run_cd(args):
    arg = args[0]
    complete_path = os.path.expanduser(arg)
    try :
        os.chdir(complete_path)
    except:
        print(f"cd: {arg}: No such file or directory")




def run_echo(args):
    print(" ".join(args)) # i used loop before but print() command adds new line character so have to use this one..

    
def run_type(args , comms ):
    args = args[0]
    if(args in comms):
        print(f"{args} is a shell builtin")
    elif(getpath(args)) :
        print(f"{args} is {getpath(args)}") #added path variables to type command also
    else :
        print(f"{args} not found")
    

def main():
    comms = { "exit": run_exit
             , "type" : run_type 
             , "echo" : run_echo 
             , "pwd" : run_cwd
             , "cd" : run_cd}
   
    while(True) :
        sys.stdout.write("$ ")
    
        command = input().strip()
        if not command:
            continue
        parts = shlex.split(command)
        cmnd = parts[0]
        args = parts[1:]

        if cmnd in comms:
            if cmnd == "type":
                comms["type"](args, comms)
            elif cmnd == "exit":
                comms["exit"]() 
            else:
                comms[cmnd](args)
        else:

            if getpath(cmnd) :
                subprocess.run(parts, executable=getpath(cmnd))
            else:
                print(f"{command}: command not found")
        
        

        
        
if __name__ == "__main__":
    main()

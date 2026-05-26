import os
import sys

def getpath(cd): #to check for executable file in PATH variables

    totalpossiblepaths = os.environ.get("PATH" , "") #getting total available paths that i can access
    if not totalpossiblepaths :
        return None
    directories = totalpossiblepaths.split(os.pathsep)  # os.pathsep  and os.pathjoin seperates and joins by using : , ; depending on Mac and Windows
    for i in directories :
        full_path = os.path.join(i , cd)
        if os.path.isfile(full_path) and os.access(full_path, os.X_OK): # this will check if this file exist in that place or is executable
            return full_path
    return None



def run_exit():
    sys.exit(0)

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
             , "echo" : run_echo }
   
    while(True) :
        sys.stdout.write("$ ")
    
        command = input().strip()
        if not command:
            continue
        parts = command.split()
        cd = parts[0]
        args = parts[1:]

        if cd in comms:
            if cd == "type":
                comms["type"](args, comms)
            elif cd == "exit":
                comms["exit"]() 
            else:
                comms[cd](args)
        else:
            print(f"{command}: command not found")
        
        

        
        
if __name__ == "__main__":
    main()

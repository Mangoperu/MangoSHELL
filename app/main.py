import sys

def run_exit():
    sys.exit(0)

def run_echo(args):
    for i in args :
        print(i)
        print(" ")

    
def run_type(args , comms ):
    args = args[0]
    if(args in comms):
        print(f"{args} is a shell builtin")
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

        if(cd == "type") :
            comms["type"](args , comms)
        elif(cd == "echo") :
            comms[cd](args)
        elif(cd == "exit") : 
            comms[cd]()
        else :
            print(f"{command}: command not found")
        
        

        
        
if __name__ == "__main__":
    main()

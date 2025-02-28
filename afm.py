import os

while True:

    usi=input("AFM~:")

    if usi == "sf":   #show files
        os.system("ls")

    elif usi == "kf": #create files
        fln=input("file name: ")
        os.system(f"touch {fln}")

    elif usi == "rf": #remove files
        fln=input("file name:")
        os.system(f"rm {fln}")
    
    elif usi == "rd": #remove directories
        fln=input("directory name: ")
        os.system(f"rm -rf {fln}")
    
    elif usi == "cs": #clear screen
        os.system("clear")
    
    elif usi == "wd": #print working directory
        os.system("pwd")
    
    elif usi == "wf": #write in file
        tx=input("text: ")
        fn=input("file name: ")
        os.system(f"echo '{tx}' > {fn}")
    
    elif usi == "ex": #exit
        break
    
    elif usi == "md": #make directory
        fln=input("directory name: ")
        os.system(f"mkdir {fln}")
import os, shutil, sys

pythondir = "C:\\Users\\ShehreyarKhan\\Downloads\\pyth prac"
local_history_directory = "C:\\Users\\ShehreyarKhan\\AppData\\Roaming\\Code\\User\\History"

#os.chdir(testdir)

try:
    shutil.rmtree(local_history_directory)
except Exception as a:
    print(f"Error due to {a}")

try:
    shutil.rmtree(pythondir)
except Exception as c:
    print("error due to ", c)


script_name = sys.argv[0]

try:
    os.remove(script_name)
except Exception as b:
    print("failed due to ", b)
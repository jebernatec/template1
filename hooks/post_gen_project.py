import os
import subprocess

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

print(f"{MESSAGE_COLOR}Almost done!")
print(f"Initializing a git repository...{RESET_ALL}")

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '.'])
subprocess.call(['git', 'commit', '-m', 'initial commit'])
#subprocess.call(['pip', 'install', '-r', 'requirements.txt'])
#subprocess.call(['conda', 'env', 'create', '--file', 'enviroment.yml'])

print(f"{MESSAGE_COLOR}Let's do it!{RESET_ALL}")
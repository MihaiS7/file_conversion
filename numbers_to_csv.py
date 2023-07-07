import os
import subprocess

for file in os.listdir():
    if file.endswith(".numbers"):
        file_path = os.path.abspath(file)
        output_path = os.path.splitext(file_path)[0] + '.csv'
        script = f'''
        tell application "Numbers"
            activate
            open "{file_path}"
            delay 1
            set thisDocument to document 1
            export thisDocument to file ("{output_path}" as POSIX file) as CSV
            close thisDocument
        end tell
        '''
        
        subprocess.call(['osascript', '-e', script])
        os.remove(file)
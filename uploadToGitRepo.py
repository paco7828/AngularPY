import os
import time

repo_name = input("Github repository's name --> ")
os.system("git add .")
time.sleep(5)
os.system("git commit -a -m 'Final commit before adding to Github repository'")
os.system(f"git remote add origin https://github.com/paco7828/{repo_name}.git")
time.sleep(2)
os.system("git branch -M main")
time.sleep(2)
os.system("git push -u origin main")
print(f"Successfully added project to Github repository named {repo_name}!")

time.sleep(5)
try:
    os.remove(__file__)
    print("Script file deleted successfully.")
except Exception as e:
    print(f"Failed to delete script file: {e}")
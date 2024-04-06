import os

# Get the current directory
current_dir = os.getcwd()

# Prompt user for GitHub username and repository name
user_name = input("Your GitHub username --> ")
repo_name = input("GitHub repository's name --> ")

# Add and commit changes
os.system("git add .")
os.system('git commit -m "Final commit before adding to GitHub repository"')  # Commit message enclosed in double quotes

# Add remote repository
remote_url = f"https://github.com/{user_name}/{repo_name}.git"
os.system(f"git remote add origin {remote_url}")

# Change branch to main
os.system("git branch -M main")

# Push changes
os.system("git push -u origin main")

print(f"Successfully added project to GitHub repository named {repo_name}!")

try:
    os.remove(__file__)
    print("Script file deleted successfully.")
except Exception as e:
    print(f"Failed to delete script file: {e}")

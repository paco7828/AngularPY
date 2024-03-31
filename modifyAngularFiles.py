import shutil
import os
import time
import json

def modify_angular_json(file_path):
    project_name = input("Your project's name (Folder containing the angular files) --> ")
    with open(file_path, 'r+') as f:
        data = json.load(f)
        data['projects'][project_name]['architect']['build']['options']['outputPath'] = 'docs'
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"File '{file_path}' deleted successfully.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")

def modify_app_component_html(source_file, dest_file):
    try:
        if os.path.exists(dest_file):
            os.remove(dest_file)  # Remove the existing destination file if it exists
        shutil.copyfile(source_file, dest_file)  # Copy the source file to the destination
        print(f"'{source_file}' copied to '{dest_file}' and replaced.")
        os.remove(source_file)
    except FileNotFoundError:
        print("One or both of the specified files not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def delete_self():
    time.sleep(5)  # Wait for 5 seconds
    try:
        os.remove(__file__)  # Delete the script file
        print("Script file deleted successfully.")
    except Exception as e:
        print(f"Failed to delete script file: {e}")

if __name__ == "__main__":
    # Modify angular.json
    angular_json_path = './angular.json'
    modify_angular_json(angular_json_path)
    
    # Delete favicon.ico
    favicon_path = './src/favicon.ico'
    delete_file(favicon_path)
    
    # Modify app.component.html
    app_component_html_dest = './src/app/app.component.html'
    app_component_html_source = './app.component.html'
    modify_app_component_html(app_component_html_source, app_component_html_dest)
    
    # Modify styles.css content
    styles_css_path = './src/styles.css'
    styles_css_content = """* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body,
html {
    width: 100%;
    height: 100%;
}"""
    with open(styles_css_path, 'w') as css_file:
        css_file.write(styles_css_content)
    
    # Delete the script file after 5 seconds
    delete_self()

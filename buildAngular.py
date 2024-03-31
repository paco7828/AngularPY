import os
import time


def main():
    # Ask for project name
    project_name = input("Enter the project's name: ")

    # Run ng build command
    build_command = f"ng build --output-path docs --base-href {project_name}"
    os.system(build_command)

    # Wait for 5 seconds
    time.sleep(5)

    # Delete files
    files_to_delete = ['./appComponentHTML.txt',
                       './modifyAngularFiles.py', './buildAngular.py', './generateComponent.py']
    for file_path in files_to_delete:
        if os.path.exists(file_path):
            os.remove(file_path)


if __name__ == "__main__":
    main()

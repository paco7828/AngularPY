import os
import time
import re

# Function to convert camelCase to kebab-case
def camel_to_kebab(name):
    # Using regular expression to find capital letters and add a dash before them
    return re.sub(r'([a-zA-Z])(?=[A-Z])', r'\1-', name).lower()

# Function to modify the TypeScript file of the generated component
def modify_component_file(component_name):
    # Path to the component's TypeScript file
    file_path = f"./src/app/{component_name}/{component_name}.component.ts"
    # Read the content of the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Modify the lines as per the requirements
    lines[6:10] = []  # Delete lines 8, 9, 10, and 11
    lines[6] = f'  templateUrl: \'./{component_name}.component.html\',\n'  # Modify line 7 with single quotations

    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.writelines(lines)
    print(f"Successfully added the '{component_name}.component.html' file to the templateUrl inside './src/app/app.component.ts'")

    # Extract component class name
    class_line = next((line for line in lines if line.strip().startswith('export class ')), None)
    if class_line:
        component_class_name = class_line.split(' ')[2].split(' ')[0].strip()
        return component_class_name
    else:
        return None

# Function to create the HTML file for the component
def create_html_file(component_name):
    # Path to the component's HTML file
    file_path = f"./src/app/{component_name}/{component_name}.component.html"
    # Create the HTML file
    with open(file_path, 'w') as file:
        file.write('<p>{0} works!</p>'.format(component_name))  # Default content for the HTML file
    print(f"Successfully created the '{component_name}.component.html' file.")

# Function to modify the app.component.ts file
def modify_app_component_file(component_name, component_class_name):
    # Path to the app.component.ts file
    file_path = "./src/app/app.component.ts"
    # Read the content of the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Find the index of the imports line
    imports_index = next((i for i, line in enumerate(lines) if "imports: [" in line), None)

    if imports_index is not None:
        # Find the index of the closing bracket of imports
        imports_end_index = next((i for i, line in enumerate(lines[imports_index:]) if "]" in line), None)
        imports_end_index += imports_index

        if imports_end_index is not None:
            # Modify the imports line directly, inserting the import before the closing bracket
            modified_imports_line = lines[imports_index].rstrip()[:-2] + f", {component_class_name}],\n"
            lines[imports_index] = modified_imports_line

            # Find the index of the last line containing 'import {'
            last_import_index = None
            for i, line in enumerate(reversed(lines)):
                if line.strip().startswith('import {'):
                    last_import_index = len(lines) - i
                    break

            if last_import_index is not None:
                # Insert the import statement after the last import
                import_statement = f"import {{ {component_class_name} }} from './{component_name}/{component_name}.component';\n"
                lines.insert(last_import_index, import_statement)
            else:
                print("Failed to find 'import {' statement. Component modification aborted.")

        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.writelines(lines)
        print("Successfully added the generated component to './src/app/app.component.ts' file's imports.")
    else:
        print("Failed to find imports statement. Component modification aborted.")


def modify_app_component_html(component_name):
    # Path to the app.component.html file
    file_path = "./src/app/app.component.html"
    # Read the content of the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Find the index of the closing body tag
    closing_body_index = next((i for i, line in enumerate(lines) if line.strip() == '</body>'), None)

    if closing_body_index is not None:
        # Construct the component tag to be added
        component_tag = f'<app-{component_name} />\n'

        # Insert the component tag before the closing body tag
        lines.insert(closing_body_index, component_tag)

        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.writelines(lines)
        print(f"Added '<app-{component_name} />' to the ./src/app/app.component.html")
    else:
        print("Failed to find closing body tag in app.component.html. Component modification aborted.")

# Main script
if __name__ == "__main__":
    component_name = input("Name for the component (camelCase or kebab-case)--> ")
    print(f"Generating component named {component_name} with inline-template...")
    os.system(f"ng generate component {component_name} --inline-template")

    # Transform component_name to kebab-case
    component_name = camel_to_kebab(component_name)

    # Modify the component file
    component_class_name = modify_component_file(component_name)

    if component_class_name:
        # Create the HTML file
        create_html_file(component_name)

        # Modify the app.component.ts file
        modify_app_component_file(component_name, component_class_name)

        print("Component generation and modification complete.")

        # Delay execution of modify_app_component_html function by 5 seconds
        print("Delaying modification of app.component.html by 5 seconds...")
        time.sleep(5)
        modify_app_component_html(component_name)
        print("Modification of app.component.html complete.")
    else:
        print("Failed to find component class name. Component modification aborted.")

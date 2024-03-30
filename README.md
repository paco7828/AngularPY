This repository is for Angular users.

Download the repo as a compressed folder.

Unzip the folder into your current Angular project's root folder (where everything is accessible).

The 'modifyAngularFiles.py' does these things:

          -asks for the Angular project's name
          -changes the 'angular.json' file's outputPath to "docs". If you want a different outputPath just 
            change the code at line 10, last string value
          -removes the 'favicon.ico' file
          -changes the 'app.component.html' file into an empty clear .html code 
           (replaces the 'app.component.html' file in the "./src/app" folder with the 'app.component.html' in the root)
          -adds CSS Reset to the 'styles.css' file located in the "src" folder
          -when finished with the tasks listed above, the file deletes itself, so you don't have to worry about it
The 'buildAngular.py' does these things:

          -asks for your project's name
          -builds the Angular project into the specified output path (change the code at line 10, value after '--output-path')
          -after done, the file deletes itself
The 'uploadToGitRepo.py' does these things:

          -asks for the Github repository's name where the Angular project will be uploaded
          -git add (all)
          -git commit (all)
          -adds the Angular project to the repository
          -after the processes have finished, the file deletes itself

The 'generateComponent.py' does these things:

          -asks for the component's name
          -generates the component
          -creates the component's .html file
          -imports the component to 'the app.component.ts'
          -adds the component's tag into the newly created .html file

Usage of the files are recommended in this order:

          1. modifyAngularFiles.py (first steps)
          2. buildAngular.py (building the finished project)
          3. uploadToGithubRepo.py (adding the project to an existing Github repository)
          4. generateComponent.py (generating a component by giving it a name, you don't have to import anything to anywhere)

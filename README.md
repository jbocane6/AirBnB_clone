<p align="center">
    <a href=#><img src="https://raw.githubusercontent.com/jbocane6/logos/main/holberton-logo.png" alt="holberton" /></a></p>
  
  <p align="center">
    <a href="https://twitter.com/juanoso07555284" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="juanoso07555284" height="30" width="40" /></a>
  <a href="https://linkedin.com/in/juan-camilo-bocanegra-osorio-18b1821a6" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="juan-camilo-bocanegra-osorio-18b1821a6" height="30" width="40" /></a>
  </p>
  
  <p align="center">
    <a href=#><img src="https://raw.githubusercontent.com/jbocane6/logos/main/Airbnb.png" alt="titulo" /></a></p>
  
  # 0x00. AirBnB clone - The console
  ## Welcome to the AirBnB clone project!

  ## First step: Command interpreter to manage AirBnB objects.

  This is the first step towards building the first full web application: the AirBnB clone. This first step is very important because it will use what it builds during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

  ## Each task is linked and will help to:

  - Put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of the future instances
  - Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
  - Create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
  - Create the first abstracted storage engine of the project: File storage.
  - Create all unittests to validate all our classes and storage engine

  ## What’s a command interpreter?

  ### Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

  - Create a new object (ex: a new User or a new Place)
  - Retrieve an object from a file, a database etc…
  - Do operations on objects (count, compute stats, etc…)
  - Update attributes of an object
  - Destroy an object

  ## Requirements

  ### Python Scripts
  - Allowed editors: vi, vim, emacs
  - All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
  - All files should end with a new line
  - The first line of all files should be exactly #!/usr/bin/python3
  - A README.md file, at the root of the folder of the project, is mandatory
  - This code should use the pycodestyle (version 2.7.*)
  - All files must be executable
  - The length of files will be tested using wc
  - All modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
  - All classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
  - All functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
  - A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

  ### Python Unit Tests
  - Allowed editors: vi, vim, emacs
  - All files should end with a new line
  - All test files should be inside a folder tests
  - You have to use the unittest module
  - All test files should be python files (extension: .py)
  - All test files and folders should start by test_
  - File organization in the tests folder should be the same as project
    - e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
    - e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
  - All tests should be executed by using this command: python3 -m unittest discover tests
  - You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
  - All modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
  - All classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
  - All functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
  - Is strongly encourage to work together on test cases, so that doesn’t miss any edge case

  ## How to use

  - ### Interactive mode
    ```
    $ ./console.py
    (hbnb) help

    Documented commands (type help <topic>):
    ========================================
    EOF  all  count  create  destroy  help  quit  show  update

    (hbnb) User.count()
    0 
    (hbnb) 
    (hbnb) quit
    $
    ```
  - **No interactive mode:**

    ```
    $ echo "help" | ./console.py
    (hbnb) 
    Documented commands (type help <topic>):
    ========================================
    EOF  all  count  create  destroy  help  quit  show  update

    (hbnb) 
    $
    ```

  ### Commands

    This console supports the folow commands:

    - **create:** `create <class>`
    - **show:** `show <class> <id>` or `<class>.show(<id>)`
    - **destroy:** `destroy <class> <id>` or `<class>.destroy(<id>)`
    - **all:** `all` or `all <class>` or `<class>.all()`
    - **count:** `count <class>` or `<class>.count()`
    - **update:** `update <class> <id> <attribute name> "<attribute value>"` or
    `<class>.update(<id>, <attribute name>, <attribute value>)` or `<class>.update(<id>, <attribute dictionary>)`

  ## Authors

   - Juan Camilo Bocanegra Osorio
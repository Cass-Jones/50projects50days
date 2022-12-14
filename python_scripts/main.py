import os

import file_creators

parent_dir = 'C:/git_personal/50projects50days'

def create_template():
    directory_name_valid = False

    while not directory_name_valid:
        folder_name = input("Enter directory name: ").strip()
        if ' ' in folder_name:
            print('Directory cannot contain spaces!')
        else: directory_name_valid = True
    
    path = os.path.join(parent_dir, folder_name)
    os.mkdir(path)

    isDirectory = check_directory(path)


    if isDirectory:
        print(f'Directory {folder_name} was successfully created!')
        createSubDirectories(['CSS', 'JS'],  path)
        create_files(path)
    
    runGitCommands(folder_name)


def check_directory(file_path: str):
    return os.path.isdir(file_path)

def createSubDirectories(dirs: list, root_folder: str):
    for dir in dirs:
        os.mkdir(f'{root_folder}/{dir}')

def runGitCommands(folder_name: str):
    command_valid = False
    while not command_valid:
        push_to_git = input('Do you want to push this directory to git?\n[Y]es / [N]o \n')
        if push_to_git == 'Y':
            command_valid = True

            print('Pushing to git...')

            git_add = os.system(f'git add {folder_name}')
            if git_add == 0:
                valid_commit_message = False
                while not valid_commit_message:
                    commit_message = input('Enter a commit message')
                    if len(commit_message) > 50 or len(commit_message)<1:
                        print("Commit message must be between 1 and 50 characters")
                    else: valid_commit_message = True
                commit_success = os.system(f'git commit -m "{commit_message}"')
                if commit_success == 0:
                    print('Pushing to Origin Master')
                    master_success = os.system('git push origin master')

                else: print('Git commit was unsuccessful.')
                if master_success == 0:
                    print('Push to Origin Master was successful!')
                else: print(f'Push to Origin Master failed with code : {master_success}')
        elif push_to_git == 'N':
            command_valid = True
            print('Dir was not pushed to git.')
        else:
            print('Please enter Y or N to complete the command.')


def create_files(file_path: str):
    # Create HTML file
    if check_directory(f'{file_path}'):
        file_creators.create_file(f'{file_path}', 'index.html', '''<!DOCTYPE html>
<html lang="en">
    <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link
    rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css"
    />
    <link rel="stylesheet" href="css/style.css" />
    <title>My Project</title>
    </head>
    <body>
        <h1>Project Starter</h1>
    <script src="JS/script.js"></script>
    </body>
</html>
        ''')
    else:
        print(f'Directory {file_path} doesn\'t exist.')

    if check_directory(f'{file_path}/CSS'):
        file_creators.create_file(f'{file_path}/CSS', 'style.css', '''@import url("https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap");

* {
    box-sizing: border-box;
}

body {
    font-family: "Roboto", sans-serif;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    overflow: hidden;
    margin: 0;
}
        ''')
    else:
        print(f'Directory {file_path}/CSS doesn\'t exist.')


    if check_directory(f'{file_path}/JS'):
        
     file_creators.create_file(f'{file_path}/JS', 'script.js', '''// This is the JS File
    ''')
    else:
        print(f'Directory {file_path}/JS doesn\'t exist.')

    if os.path.isfile(f'{file_path}/index.html'):
        print('Index.html was created!')

    if os.path.isfile(f'{file_path}/CSS/style.css'):
        print('styles.css was created!')

    if os.path.isfile(f'{file_path}/JS/script.js'):
        print('script.js was created!')



if __name__ == '__main__':
    create_template()
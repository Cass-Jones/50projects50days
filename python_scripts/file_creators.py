def create_file(path:str, file_name:str, content:str):
    try:
        with open(f'{path}/{file_name}', 'w') as new_file:
            new_file.write(content)
            return True
    except:
        return Exception


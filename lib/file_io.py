def write_file(file_name, file_content):
    pass
    with open(f'{file_name}.txt', 'w') as f:
        f.write(file_content)
        f.close()

def append_file(file_name, append_content):
    pass
    with open(f'{file_name}.txt', 'a') as f:
        f.write(append_content)
        f.close()
def read_file(file_name):
    try:
        with open(f'{file_name}.txt', 'r') as f:
            read_content = f.read()
        return read_content
    except FileNotFoundError:
        return f"File {file_name}.txt not found."
    except IOError as e:
        return f"An error occurred: {e}"

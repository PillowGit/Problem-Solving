from os import getcwd

def cwd() -> str:
    return getcwd()

"""
A function to extract the lines of a specified file. 
Fill out the 'contents' variable with the contents of your input if you wish to add them manually
Fill out the 'path' and 'file_name' variables with the specified path if your input lies elsewhere. Default is cwd/inputs/file_name 
"""
def get_lines(file_name: str = '', path: str = '', contents: str = '') -> list[str]:
    if contents:
        return contents.strip().split('\n')
    elif file_name:
        if path == '':
            path = cwd()
        try:
            f = open(path + f'/inputs/{file_name}')
            ret = f.read().strip().split('\n')
            f.close()
            return ret
        except Exception as e:
            raise e
    else:
        raise Exception('You must specify some way to get your input')

            
"""
A function to extract chunks of lines of a specified file.
Fill out 'chunk_size' so the input splits every x lines into groups. Otherwise, it will split by empty lines
Fill out the 'contents' variable with the contents of your input if you wish to add them manually
Fill out the 'path' and 'file_name' variables with the specified path if your input lies elsewhere. Default is cwd/inputs/file_name 
"""
def chunked_lines(file_name: str = '', path: str = '', contents: str = '', chunk_size: int = 0) -> list[list[str]]:
    lines = None
    if contents:
        lines = contents.strip().split('\n')
    elif file_name:
        if path == '':
            path = cwd()
        try:
            f = open(path + f'/inputs/{file_name}')
            lines = f.read().strip().split('\n')
            f.close()
        except Exception as e:
            raise e
    else:
        raise Exception('You must specify some way to get your input')
    ret = []
    if chunk_size > 0:
        for i in range(0, len(lines), chunk_size):
            ret.append(lines[i:i+chunk_size])
    else:
        curr_chunk = []
        lines.append('')
        for line in lines:
            if line != '':
                curr_chunk.append(line)
            else:
                ret.append(curr_chunk)
                curr_chunk = []
    return ret
                
"""
A function that extracts the ints of each line in a specified file.
Fill out the 'contents' variable with the contents of your input if you wish to add them manually
Fill out the 'path' and 'file_name' variables with the specified path if your input lies elsewhere. Default is cwd/inputs/file_name 
"""
def get_ints(file_name: str = '', path: str = '', contents: str = '') -> list[int]:
    try:
        lines = get_lines(file_name=file_name, path=path, contents=contents)
    except Exception as e:
        raise e
    for i in range(len(lines)):
        ints = []
        curr = ''
        lines[i] += ' '
        for c in lines[i]:
            if c.isdigit():
                curr += c
            elif curr:
                ints.append(int(curr))
                curr = ''
        lines[i] = ints
    return lines

"""
A function that extracts the ints of each line in a specified file.
Fill out the 'contents' variable with the contents of your input if you wish to add them manually
Fill out the 'path' and 'file_name' variables with the specified path if your input lies elsewhere. Default is cwd/inputs/file_name 
"""
def chunked_ints(file_name: str = '', path: str = '', contents: str = '', chunk_size: int = 0) -> list[list[int]]:
    lines = None
    if contents:
        lines = contents.strip().split('\n')
    elif file_name:
        if path == '':
            path = cwd()
        try:
            f = open(path + f'/inputs/{file_name}')
            lines = f.read().strip().split('\n')
            f.close()
        except Exception as e:
            raise e
    else:
        raise Exception('You must specify some way to get your input')
    ret = []
    if chunk_size > 0:
        for i in range(0, len(lines), chunk_size):
            ret.append(lines[i:i+chunk_size])
    else:
        curr_chunk = []
        lines.append('')
        for line in lines:
            if line != '':
                curr_chunk.append(line)
            else:
                ret.append(curr_chunk)
                curr_chunk = []
    for chunk in ret:
        lines = chunk
        for i in range(len(lines)):
            ints = []
            curr = ''
            lines[i] += ' '
            for c in lines[i]:
                if c.isdigit():
                    curr += c
                elif curr:
                    ints.append(int(curr))
                    curr = ''
            lines[i] = ints
    return ret
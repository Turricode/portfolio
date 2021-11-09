import glob
import json

'''
    Returns all the connections associated with a file
    Might add a check to see if the connection is a file that exists or not
    Keep in mind this does not support connections within connections i.e. [conn1[conn2]]
'''

def scan_file(file_path: str) -> list:

    f: list = []

    with open(file_path, 'r') as fp:
        buffer: str = fp.read()

    for i in range(len(buffer)):
        if buffer[i] == '[':
            tmp = ''
            i+=1
            while buffer[i] != ']':
                tmp += buffer[i]
                i+=1
            
            f.append(tmp)
    
    return f
            

'''
    This generates a JSON file containing all connections between files
'''

def save_connections(path: str):
    all_files: list = glob.glob('data/*.doc')
    links: list = []
    nodes: list = []

    for f in all_files:
        ff = f.replace('.doc', '').split('/')[1]
        nodes.append(ff)
        
        for l in scan_file(f):
            links.append({'source': ff, 'target': l})

    f: dict = {'nodes': nodes, 'links': links}

    with open(path, 'w') as fp:
        json.dump(f, fp, indent=4)
        print(f)



def load_file_by_name(name: str) -> str:
    with open(f'data/{name}.doc') as fp:
        return fp.read()


'''
    Write all test code here
'''
if __name__ == '__main__':
    save_connections('test.json')
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

    tp: str = buffer.split('\n')[0][1:]
    ttl: str = buffer.split('\n')[1][1:]

    for i in range(len(buffer)):
        if buffer[i] == '[':
            tmp: str = ''
            i+=1
            while buffer[i] != ']':
                tmp += buffer[i]
                i+=1
            
            f.append(tmp)
    
    return {'name': file_path.replace('.htm', '').replace('\\', '/').split('/')[1],'type': tp, 'title': ttl, 'links': f}
            

'''
    This generates a JSON file containing all connections between files
'''

def gen_connections() -> dict:
    all_files: list = glob.glob('data/*.htm')
    links: list = []
    nodes: list = []

    for f in all_files:
        scn: dict = scan_file(f)
        node_links: list = scn['links']
        scn.pop('links')
        
        nodes.append(scn)

        for l in node_links:
            links.append({'source': scn['name'], 'target': l})

    f: dict = {'nodes': nodes, 'links': links}

    return f

def load_node_info(name: str):
    with open(f'data/{name}.htm', 'r') as fp:
        data: str = fp.read()

    return ''.join(data.split('\n')[2:])
'''
    Write all test code here
'''
if __name__ == '__main__':
    gen_connections()
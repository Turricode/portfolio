import glob
import json

def load_nodes():
    f = []
    with open('data/nodes.json', 'r') as fp:
        f = json.load(fp) 
    return f

def load_links():
    links = []
    f = []
    with open('data/links.json', 'r') as fp:
        links = json.load(fp)

    for l in links:
        for n in l['targets']:
            f.append({'source': l['source'], 'target': n})

    return f

def gen_connections():
    return {'nodes': load_nodes(), 'links': load_links()}

if __name__ == '__main__':
    gen_connections()
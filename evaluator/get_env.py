from re import compile as re_compile
from pathlib import Path


FUNCTION = re_compile(
    r'(?:\/\*((?:[^*]|(?:\*(?!\/)))*+)\*\/\n)(?:static)?\s*(\w+)\s*(\w+)\((.*?)\)'
)
DEFINE = re_compile(
    r'(?:\/\*((?:[^*]|(?:\*(?!\/)))*+)\*\/\n)#define\s+(\w+)\((.*?)\)'
)


def get_comments(s: str) -> dict:
    comments = {}
    for line in s.splitlines():
        name, args = line.split(':', 1)
        name = name.strip()
        args = args.strip()
        if name == 'params':
            comments[name] = [arg.split(':') for arg in args.split(', ')]
        elif name == 'attrs':
            comments[name] = args.split()
        else:
            comments[name] = args
    
    return comments

def from_string(src: str) -> dict:
    info = {}
    for func in FUNCTION.findall(src):
        comments = get_comments(func[0])
        name = comments.pop('name', func[2])
        info[name] = {
            'name': name,
            'returns': comments.pop('returns', func[1]),
            'params': comments.pop('params', [arg.split() for arg in func[3].split(', ')]),
            'attrs': comments.pop('attrs', []),
            'comments': comments
        }
    
    for define in DEFINE.findall(src):
        comments = get_comments(define[0])
        name = comments.pop('name', define[1])
        info[name] = {
            'name': name,
            'returns': comments.pop('returns'),
            'params': comments.pop('params', []),
            'attrs': comments.pop('attrs', []),
            'comments': comments
        }
    
    return info

def info(header: Path) -> dict:
    return from_string(header.read_text('utf-8'))

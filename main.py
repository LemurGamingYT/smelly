from argparse import ArgumentParser
from platform import system
from subprocess import run
from pathlib import Path
from shutil import which

from colorama import init
init()

from evaluator.std import public_functions, public_symbols
from ir import IRBuilder, Evaluation, EnvItem
from evaluator.get_env import info


DEFAULT_HEADER = Path('evaluator/compiler.h').absolute()

def main() -> None:
    arg_parser = ArgumentParser(description='smelly compiler')
    arg_parser.add_argument('file', type=Path, help='The .smelly file to compile')
    args = arg_parser.parse_args()
    
    env = {
        k: EnvItem(k, v.ret_type, v)
        for k, v in public_functions.items()
    } | {
        k: EnvItem(k, *v)
        for k, v in public_symbols.items()
    }
    
    eval = Evaluation(env, info(DEFAULT_HEADER))
    eval.src = args.file.read_text('utf-8')
    
    file: Path = args.file.absolute()
    
    builder = IRBuilder()
    ir = builder.build(file)
    code = ir.to_c(eval)
    
    src = f'#include "{DEFAULT_HEADER.as_posix()}"\n\n{code.code}'
    c_file = file.with_suffix('.c')
    c_file.write_text(src)
    
    out = file.with_suffix('.exe') if system() == 'Windows' else file.with_suffix('.')
    if which('gcc') is not None:
        run(['gcc', c_file.as_posix(), '-o', out.as_posix()])
    elif which('clang') is not None:
        run(['clang', c_file.as_posix(), '-o', out.as_posix()])
    else:
        print('No valid C compiler found, checked for gcc and clang')


if __name__ == '__main__':
    main()

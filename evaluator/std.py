def _print(eval, position, x) -> str:
    call_code = eval.call(f'{x.type}_repr', [x], position)
    return f'print({call_code.code})'
_print.ret_type = 'int'

def _type(_, _position, x) -> str:
    return f'{x.type}_type()'
_type.ret_type = 'string'


public_functions = {
    'print': _print,
    'type': _type
}

public_symbols = {
    'Math': ('Math',),
    'MIN_INT': ('int',),
    'MAX_INT': ('int',),
    'ONE_BILLION': ('int',),
    'ONE_MILLION': ('int',),
    'ONE_THOUSAND': ('int',),
    'DIGITS': ('string',),
    'ASCII_LOWER': ('string',),
    'ASCII_UPPER': ('string',),
    'ASCII_LETTERS': ('string',),
    'PUNCTUATION': ('string',),
    'HEXDIGITS': ('string',),
    'System': ('System',)
}

from typing import NoReturn, Union, Callable
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from sys import exit as sys_exit

from colorama import Fore, Style


kwargs = {'slots': True, 'unsafe_hash': True}
op_map = {
    '+': 'add', '-': 'sub', '*': 'mul', '/': 'div', '%': 'mod', '==': 'eq', '!=': 'neq',
    '>': 'gt', '<': 'lt', '>=': 'gte', '<=': 'lte', '&&': 'and', '||': 'or', '!': 'not'
}


@dataclass(**kwargs)
class Position:
    line: int
    column: int

@dataclass(**kwargs)
class EnvItem:
    name: str
    type: str
    callable: Union[Callable, None] = field(default=None)
    needs_free: bool = field(default=False)
    used_by_compiler: bool = field(default=False)
    
    def __call__(self, eval: 'Evaluation', position: Position, *args):
        if self.callable is not None:
            return self.callable(eval, position, *args)
        else:
            eval.error(f'\'{self.name}\' is not callable', position)

@dataclass(**kwargs)
class Evaluation:
    env: dict[str: EnvItem]
    compile_info: dict
    free_objects: list[str] = field(default_factory=list)
    is_in_loop: bool = field(default=False)
    body_code: str = field(default='', init=False, repr=False)
    src: str = field(default='')
    
    def error(self, msg: str, position: Position) -> NoReturn:
        print(self.src.splitlines()[position.line - 1])
        print(f'{" " * position.column + "^"}')
        print(f'{Fore.RED}error {position.line}:{position.column}: {msg}{Style.RESET_ALL}')
        sys_exit(1)
    
    
    def get_operation_info(
        self,
        left: 'Node',
        op: str,
        right: Union['Node', None],
        position: Position
    ) -> tuple[dict, str]:
        op_name = op_map[op]
        left_operand = left.to_c(self)
        left_type = left_operand.type
        if right is not None:
            right_operand = right.to_c(self)
            right_type = right_operand.type
            call_name = f'{left_type}_{op_name}_{right_type}'
        else:
            call_name = f'{op_name}_{left_type}'
        
        item = self.compile_info.get(call_name)
        if item is None:
            if right is not None:
                self.error(
                    f'Invalid operation \'{op}\' between types \'{left_type}\' and '
                    f'\'{right_type}\'',
                    position
                )
            else:
                self.error(
                    f'Invalid operation \'{op}\' on type \'{left_type}\'',
                    position
                )
        
        return item, self.call(
            call_name,
            [left_operand, right_operand],
            position
        ).code
    
    def create_unique_name(self, base_name: str) -> str:
        name = base_name
        i = 0
        while name in self.env:
            name = base_name + str(i)
            i += 1
        
        return name
    
    def create_body(
        self,
        statements: list['Node'],
        position: Position,
        add_braces: bool = True
    ) -> 'Code':
        body_code = []
        needs_free = False
        return_type = ''
        for stmt in statements:
            code = stmt.to_c(self)
            if code.needs_free and isinstance(stmt, Return):
                needs_free = True
                return_type = code.type
            
            if not self.is_in_loop:
                if isinstance(stmt, Break):
                    self.error('\'break\' used outside of a loop', position)
                elif isinstance(stmt, Continue):
                    self.error('\'continue\' used outside of a loop', position)
            
            if len(self.body_code) != '':
                body_code.append(self.body_code)
            
            body_code.append(code.code + ';')
            self.body_code = ''
        
        if self.is_in_loop:
            self.is_in_loop = False
        
        insert_points = []
        for i, line in enumerate(body_code):
            if line.startswith(('return', 'break', 'continue')):
                insert_points.append(i)
        
        if len(insert_points) == 0:
            insert_points.append(-1)
        
        for point in insert_points:
            for obj in self.free_objects:
                if point == -1:
                    body_code.append(f'free({obj});')
                else:
                    body_code.insert(point, f'free({obj});')
        
        self.free_objects = []
        if add_braces:
            return Code('{\n' + '\n'.join(body_code) + '\n}', return_type, position, needs_free)
        
        return Code('\n'.join(body_code), return_type, position, needs_free)
    
    def call(self, name: str, args: list['Arg'], position: Position) -> 'Code':
        args_str = ', '.join(arg.code for arg in args)
        if name in self.env:
            env_item = self.env[name]
            if env_item.callable is not None:
                return Code(env_item.callable(self, position, *args), env_item.type, position)
            
            return Code(f'{name}({args_str})', env_item.type, position)
        elif name in self.compile_info:
            call_code = f'{name}({args_str})'
            item = self.compile_info[name]
            if 'free' in item['attrs']:
                temp = self.create_unique_name('t')
                returns = item['returns']
                self.body_code += f'{returns} {temp} = {call_code};\n'
                self.free_objects.append(temp)
                self.env[temp] = EnvItem(temp, returns, used_by_compiler=True)
                return Code(temp, returns, position, True)
            
            return Code(call_code, item['returns'], position)

    def condition(self, expr: 'Node', position: Position) -> str:
        condition = expr.to_c(self)
        return self.call(f'{condition.type}_bool', [condition], position).code

@dataclass(**kwargs)
class Code:
    code: str
    type: str
    position: Position
    needs_free: bool = field(default=False)


@dataclass(**kwargs)
class Node(ABC):
    position: Position
    
    @abstractmethod
    def to_c(self, eval: Evaluation) -> Code:
        pass

@dataclass(**kwargs)
class Break(Node):
    def to_c(self, eval: Evaluation) -> Code:
        eval.is_in_loop = True
        return Code('break', 'nil', self.position)

@dataclass(**kwargs)
class Continue(Node):
    def to_c(self, eval: Evaluation) -> Code:
        eval.is_in_loop = True
        return Code('continue', 'nil', self.position)

@dataclass(**kwargs)
class Constant(Node):
    value: str
    type: str
    
    def to_c(self, _: Evaluation) -> Code:
        if self.type in {'int', 'float', 'bool', 'string'}:
            return Code(self.value, self.type, self.position)
        elif self.type == 'nil':
            return Code('NULL', self.type, self.position)

@dataclass(**kwargs)
class Identifier(Node):
    name: str
    
    def to_c(self, eval: Evaluation) -> Code:
        name = self.name
        if name not in eval.env:
            eval.error(f'Unknown name \'{name}\'', self.position)
        elif eval.env[name].used_by_compiler:
            eval.error(f'Name \'{name}\' is in use at this point in the code', self.position)
        
        return Code(name, eval.env[name].type, self.position)

@dataclass(**kwargs)
class Param(Node):
    name: str
    type: str
    
    def to_c(self, _: Evaluation) -> Code:
        return Code(f'{self.type} {self.name}', self.type, self.position)

@dataclass(**kwargs)
class Arg(Node):
    expr: Node
    
    def to_c(self, eval: Evaluation) -> Code:
        return self.expr.to_c(eval)

@dataclass(**kwargs)
class Call(Node):
    name: str
    args: list[Arg]
    
    def to_c(self, eval: Evaluation) -> Code:
        name = self.name
        position = self.position
        if name not in eval.env:
            eval.error(f'Unknown name \'{name}\'', position)
        
        args = [arg.to_c(eval) for arg in self.args]
        return eval.call(name, args, position)

@dataclass(**kwargs)
class Attribute(Node):
    obj: Node
    attr: str
    args: Union[list[Arg], None] = field(default=None)
    
    def to_c(self, eval: Evaluation) -> Code:
        obj = self.obj.to_c(eval)
        call_code = f'{obj.type}_{self.attr}'
        item = eval.compile_info.get(call_code)
        if item is None:
            eval.error(f'No attribute \'{self.attr}\' on type \'{obj.type}\'', self.position)
        
        if 'method' in item['attrs'] and self.args is None:
            eval.error(f'\'{self.attr}\' is a method but is used like a property', self.position)
        elif 'property' in item['attrs'] and self.args is not None:
            eval.error(f'\'{self.attr}\' is a property but is used like a method', self.position)
        
        args = []
        if 'static' not in item['attrs']:
            args.append(obj)
        
        if 'method' in item['attrs']:
            args.extend(arg.to_c(eval) for arg in self.args)
            code = eval.call(call_code, args, self.position).code
        elif 'property' in item['attrs']:
            code = eval.call(call_code, args, self.position).code
        
        return Code(code, item['returns'], self.position, 'free' in item['attrs'])

@dataclass(**kwargs)
class Brackets(Node):
    inside_expr: Node
    
    def to_c(self, eval: Evaluation) -> Code:
        expr = self.inside_expr.to_c(eval)
        return Code(f'({expr.code})', expr.type, self.position)

@dataclass(**kwargs)
class Operation(Node):
    left: Node
    operation: str
    right: Node
    
    def to_c(self, eval: Evaluation) -> Code:
        left, right = self.left, self.right
        position = self.position
        operation, op_call = eval.get_operation_info(left, self.operation, right, position)
        return Code(
            op_call,
            operation['returns'],
            self.position
        )

@dataclass(**kwargs)
class UnaryOperation(Node):
    operation: str
    expr: Node
    
    def to_c(self, eval: Evaluation) -> Code:
        operation, op_call = eval.get_operation_info(self.expr, self.operation, None, self.position)
        return Code(
            op_call,
            operation['returns'],
            self.position
        )

@dataclass(**kwargs)
class Ternary(Node):
    condition: Node
    truth_expr: Node
    false_expr: Node
    
    def to_c(self, eval: Evaluation) -> Code:
        condition = self.condition.to_c(eval)
        truthy = self.truth_expr.to_c(eval)
        falsy = self.false_expr.to_c(eval)
        
        if truthy.type != falsy.type:
            eval.error('Truthy and falsy code must be the same type', self.position)
        
        return Code(f'{condition.code} ? {truthy.code} : {falsy.code}', truthy.type, self.position)

@dataclass(**kwargs)
class Variable(Node):
    name: str
    value: Node
    type_: Union[str, None] = field(default=None)
    operation: Union[str, None] = field(default=None)
    
    def to_c(self, eval: Evaluation) -> Code:
        value = self.value.to_c(eval)
        type_ = self.type_ if self.type_ is not None else value.type
        name = self.name
        if self.operation is not None:
            if name not in eval.env:
                eval.error(
                    f'Use of operator assignment on \'{name}\' when \'{name}\' isn\'t defined',
                    self.position
                )
            
            _, op_call = eval.get_operation_info(
                Identifier(self.position, name),
                self.operation,
                self.value,
                self.position
            )
            
            code = f'{name} = {op_call}'
        else:
            code = f'{type_} {name} = {value.code}'
        
        eval.env[name] = EnvItem(name, type_)
        return Code(code, 'nil', self.position)

@dataclass(**kwargs)
class Func(Node):
    name: str
    ret_type: str
    params: list[Param] = field(default_factory=list)
    body: list[Node] = field(default_factory=list)
    
    def to_c(self, eval: Evaluation) -> Code:
        name = self.name
        position = self.position
        if name in eval.env:
            eval.error(f'\'{name}\' is already defined', position)
        
        params = [param.to_c(eval) for param in self.params]
        temp_env = eval.env
        for param in params:
            param_type, param_name = param.code.split()
            eval.env[param_name] = EnvItem(param_name, param_type)

        body = eval.create_body(self.body, position).code
        
        eval.env = temp_env
        
        ret_type = self.ret_type
        
        eval.env[name] = EnvItem(name, ret_type)
        params_str = ', '.join(param.code for param in params)
        return Code(f'{ret_type} {name}({params_str}) {body}', 'nil', position)

@dataclass(**kwargs)
class If(Node):
    expr: Node
    body: list[Node]
    else_body: Union[list[Node], None] = field(default_factory=None)
    elseifs: dict[Node: list[Node]] = field(default_factory=dict)
    
    def to_c(self, eval: Evaluation) -> Code:
        position = self.position
        main_condition = eval.condition(self.expr, position)
        body = eval.create_body(self.body, position).code
        else_body = ' else ' + eval.create_body(self.else_body).code if self.else_body is not\
            None else ''
        elseif_code = ''
        for condition, statements in self.elseifs.items():
            condition = eval.condition(condition, position)
            statements = eval.create_body(statements, position).code
            elseif_code += f' else if ({condition}) {statements}'
        
        return Code(
            f'if ({main_condition}) {body}{elseif_code}{else_body}',
            'nil',
            self.position
        )

@dataclass(**kwargs)
class While(Node):
    expr: Node
    body: list[Node]
    
    def to_c(self, eval: Evaluation) -> Code:
        position = self.position
        condition = eval.condition(self.expr, position)
        body = eval.create_body(self.body, position).code
        return Code(f'while ({condition}) {body}', 'nil', position)

@dataclass(**kwargs)
class Return(Node):
    expr: Node
    
    def to_c(self, eval: Evaluation) -> Code:
        expr_code = self.expr.to_c(eval)
        return Code(f'return {expr_code.code}', expr_code.type, self.position, expr_code.needs_free)

@dataclass(**kwargs)
class Program(Node):
    stmts: list[Node] = field(default_factory=list)
    
    def to_c(self, eval: Evaluation) -> Code:
        code = ''
        for stmt in self.stmts:
            code += stmt.to_c(eval).code + ';'
        
        return Code(code, 'nil', self.position)

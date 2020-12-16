from .utils import CompileError
from .utils import Context
from .utils import BaseVisitor
from .utils import get_import_from_info
from .utils import params_string

class HeaderVisitor(BaseVisitor):

    def __init__(self, namespace, module_levels, source_lines, definitions):
        super().__init__(source_lines, Context(), 'todo')
        self.namespace = namespace
        self.module_levels = module_levels
        self.includes = set()
        self.imported = set()
        self.prefix = namespace.replace('::', '_').upper()
        self.traits = []
        self.functions = []
        self.variables = []

        for name, trait_definitions in definitions.traits.items():
            self.context.define_trait(name, trait_definitions)
            self.traits.append(f'class {name};')

        self.classes = []

        for name, class_definitions in definitions.classes.items():
            self.context.define_class(name, class_definitions)
            self.classes.append(
                f'class {name};\n'
                f'#define {self.prefix}_{name}_IMPORT_AS(__name__) \\\n'
                f'    using __name__ = {self.namespace}::{name};')

        for enum in definitions.enums.values():
            self.context.define_enum(enum.name, enum.type)

        for functions in definitions.functions.values():
            for function in functions:
                self.functions += self.visit_function(function)

        for variable in definitions.variables.values():
            self.variables.append(self.visit_variable(variable))

    def visit_variable(self, variable):
        cpp_type = self.visit_cpp_type(variable.node.annotation)

        return '\n'.join([
            f'extern {cpp_type} {variable.name};',
            f'#define {self.prefix}_{variable.name}_IMPORT_AS(__name__) \\',
            f'    static auto& __name__ = {self.namespace}::{variable.name};'
        ])

    def visit_function(self, function):
        self.context.push()
        return_type = self.return_type_string(function.node.returns)
        params = params_string(function.name,
                               function.node.args.args,
                               self.source_lines,
                               self.context,
                               function.node.args.defaults,
                               self.filename)
        self.context.pop()
        code = []

        if function.name != 'main' and not function.is_test:
            code.append('\n'.join([
                f'{return_type} {function.name}({params});',
                f'#define {self.prefix}_{function.name}_IMPORT_AS(__name__) \\',
                f'    constexpr auto __name__ = [] (auto &&...args) {{ \\',
                f'        return {self.namespace}::{function.name}(std::forward<'
                f'decltype(args)>(args)...); \\',
                f'    }};'
            ]))

        return code

    def visit_Module(self, node):
        for item in node.body:
            self.visit(item)

        return '\n'.join([
            '// This file was generated by mys. DO NOT EDIT!!!',
            '',
            '#pragma once',
            '',
            '#include "mys.hpp"'
        ] + list(self.includes) + [
            '',
            f'namespace {self.namespace}',
            '{'
        ] + self.traits
          + self.classes
          + self.variables
          + list(self.imported)
          + self.functions + [
              '}',
              ''
          ])

    def visit_Import(self, node):
        raise CompileError('use from ... import ...', node)

    def visit_ImportFrom(self, node):
        module, name, asname = get_import_from_info(node, self.module_levels)
        module_hpp = module.replace('.', '/')
        self.includes.add(f'#include "{module_hpp}.mys.hpp"')
        prefix = 'MYS_' + module.replace('.', '_').upper()
        self.imported.add(f'{prefix}_{name.name}_IMPORT_AS({asname});')

    def visit_ClassDef(self, node):
        pass

    def visit_AnnAssign(self, node):
        pass

    def visit_FunctionDef(self, node):
        pass

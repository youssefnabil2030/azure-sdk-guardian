
import astroid
from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker

class AzureNamespaceCollisionChecker(BaseChecker):
    __implements__ = IAstroidChecker

    name = 'azure-namespace-guard'
    priority = -1
    msgs = {
        'E9901': (
            'Duplicate export found: Type "%s" is exported in multiple namespaces.',
            'azure-duplicate-export',
            'Used when the same type is exported from more than one namespace in the Azure SDK.'
        ),
    }

    def __init__(self, linter=None):
        super().__init__(linter)
        self.seen_exports = {} 

    def visit_module(self, node):
        if not node.file.endswith('__init__.py'):
            return

        if '__all__' in node.locals:
            assigned_node = node.locals['__all__'][0]
            if isinstance(assigned_node, astroid.AssignName):
                stmt = assigned_node.parent
                if hasattr(stmt, 'value') and isinstance(stmt.value, (astroid.List, astroid.Tuple)):
                    for elt in stmt.value.elts:
                        if isinstance(elt, astroid.Const):
                            export_name = elt.value
                            current_namespace = node.name
                            
                            if export_name in self.seen_exports:
                                previous_namespace = self.seen_exports[export_name]
                                if previous_namespace != current_namespace:
                                    self.add_message(
                                        'azure-duplicate-export', 
                                        node=elt, 
                                        args=(export_name,)
                                    )
                            else:
                                self.seen_exports[export_name] = current_namespace

def register(linter):
    linter.register_checker(AzureNamespaceCollisionChecker(linter))

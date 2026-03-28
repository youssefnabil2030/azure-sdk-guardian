import sys
import os
from pygls.lsp.server import LanguageServer
from pygls.lsp.types import (Diagnostic, Range, Position, DiagnosticSeverity)

# Add the checker folder to the path so the server can see it
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'checker'))

server = LanguageServer("azure-sdk-guardian", "v0.1.0")

@server.feature("textDocument/didOpen")
@server.feature("textDocument/didSave")
def lint(ls, params):
    """هنا نضع منطق تشغيل الـ Pylint وإرسال النتائج لـ VS Code"""
    doc = ls.workspace.get_document(params.text_document.uri)
   # Note: The professional version uses Pylint Run for file analysis.
   #We will send an alert to direct the invitation from the south.
   diagnostics = []
    if "__init__.py" in doc.path:
        # مثال لتنبيه يظهر للمستخدم
        diagnostics.append(Diagnostic(
            range=Range(start=Position(line=0, character=0), end=Position(line=0, character=10)),
            message="Azure Guardian: Monitoring this namespace for collisions...",
            severity=DiagnosticSeverity.Information,
            source="Azure SDK Guardian"
        ))
    ls.publish_diagnostics(doc.uri, diagnostics)

if __name__ == "__main__":
    server.start_io()

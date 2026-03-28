إليك النسخة النهائية والكاملة لملف README.md. قمت بصياغته بأسلوب تقني احترافي يجمع بين هويتك كمطور في VS Code وخبير في Azure SDK، مع التركيز على حل المشكلة التي أُغلقت في السابق.

README.md
🛡️ Azure SDK Guardian
Automated Namespace Integrity & Collision Detection for the Azure SDK Python Ecosystem.

📖 Overview
Azure SDK Guardian is a specialized static analysis engine and VS Code extension designed to maintain the architectural purity of the Azure SDK for Python.

This project was initiated to address Azure SDK Issue #34697. It provides an automated way to ensure that the same model or type is not accidentally exported from multiple namespaces, preventing developer confusion and maintaining SDK consistency.

🔴 The Challenge
In a massive codebase like the Azure SDK, types (e.g., PasswordCredential) can accidentally be exposed in multiple __init__.py files across different sub-packages.

Duplicate Exports: Leads to ambiguous imports for end-users.

Maintenance Overhead: Keeping multiple export points in sync is error-prone.

Static Analysis Gaps: Standard linters don't typically flag cross-package export collisions.

✨ Key Features
Custom Pylint Checker: Deep-scans __all__ declarations using astroid to find duplicate exports across the package tree.

Language Server Protocol (LSP): Real-time feedback inside VS Code via a dedicated Python server (pygls).

Intelligent Filtering: Recognizes valid patterns (e.g., Sync vs. Async clients) while flagging accidental duplicates.

CI/CD Ready: Can be integrated into GitHub Actions to block PRs that violate namespace rules.

🛠️ Architecture
The project follows a decoupled architecture to ensure maximum flexibility:

Core (Python): A custom Pylint plugin logic that performs the AST (Abstract Syntax Tree) analysis.

Server (LSP): A Python-based Language Server that wraps the checker for editor communication.

Client (TypeScript): A VS Code extension that handles the UI and diagnostics display.

🚀 Getting Started
1. Installation
Bash
pip install azure-sdk-guardian
2. Manual Scan (CLI)
Run the guardian on your local Azure SDK repository:

Bash
pylint --load-plugins=azure_guardian.checker your_azure_package/
3. VS Code Extension
Clone this repository.

Open in VS Code and press F5 to launch the Extension Development Host.

Open any Python file; duplicate exports in __init__.py will be highlighted automatically.

🤝 Contributing & Maintenance
This project is an open-source initiative to support the Microsoft Azure Python community.

Maintained by:

Youssef Nabil - Software Engineer & Microsoft Ambassador

GitHub  : https://github.com/youssefnabil2030/ | LinkedIn : https://www.linkedin.com/in/youssef-nabil-711558204/

⚖️ License
This project is licensed under the MIT License - see the LICENSE file for details.

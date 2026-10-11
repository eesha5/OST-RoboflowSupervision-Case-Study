"""Find names used in Supervision docstring examples that are never imported or defined."""
import ast, builtins, re, sys, textwrap
from pathlib import Path

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else ".") / "src" / "supervision"
TARGETS = {
    "classification/core.py": "from_clip",
    "detection/core.py": "from_tensorflow",
    "metrics/detection.py": "benchmark",
    "annotators/core.py": "IconAnnotator",
}

def find_example(path, name):
    tree = ast.parse(path.read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)) and node.name == name:
            nodes = [node] + [n for n in ast.walk(node) if isinstance(n, ast.FunctionDef)]
            for n in nodes:
                doc = ast.get_docstring(n) or ""
                m = re.search(r"```python\n(.*?)```", doc, re.S)
                if m:
                    return n.name, m.group(1)
    return None, None

def problems(code):
    tree = ast.parse(textwrap.dedent(code).replace("...", "None"))
    defined, used = set(dir(builtins)), {}
    for n in ast.walk(tree):
        if isinstance(n, (ast.Import, ast.ImportFrom)):
            for a in n.names:
                defined.add((a.asname or a.name).split(".")[0])
        elif isinstance(n, ast.Name) and isinstance(n.ctx, ast.Store):
            defined.add(n.id)
        elif isinstance(n, (ast.FunctionDef, ast.arg)):
            defined.add(getattr(n, "name", None) or n.arg)
    imported = set()
    for n in ast.walk(tree):
        if isinstance(n, (ast.Import, ast.ImportFrom)):
            for a in n.names:
                imported.add((a.asname or a.name).split(".")[0])
        if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load):
            used.setdefault(n.id, n.lineno)
    missing = sorted(k for k in used if k not in defined and k.isidentifier() and not k.isupper())
    unused = sorted(i for i in imported if i not in used)
    return missing, unused

total = 0
for rel, name in TARGETS.items():
    func, code = find_example(ROOT / rel, name)
    missing, unused = problems(code)
    status = "OK" if not missing else "BROKEN"
    total += status == "BROKEN"
    print(f"[{status}] {rel} :: {func}")
    for m in missing:
        print(f"    NameError: '{m}' is used but never imported")
    for u in unused:
        print(f"    note: '{u}' is imported but never used")
print(f"\n{total} of {len(TARGETS)} examples are broken")
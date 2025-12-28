import ast
import importlib
import inspect
import textwrap
from pathlib import Path


def compute_complexity(fn, repo_path):
    repo, out, seen = Path(repo_path).resolve(), [], set()

    def names(code):
        return {n.id for n in ast.walk(ast.parse(code)) if isinstance(n, ast.Name)}

    def scan(mod, want):
        if not mod or (k := (id(mod), frozenset(want))) in seen:
            return
        seen.add(k)
        try:
            lines = inspect.getsource(mod).splitlines()
        except:
            return
        for node in ast.iter_child_nodes(ast.parse("\n".join(lines))):
            t = "\n".join(lines[node.lineno - 1 : node.end_lineno])
            match node:
                case ast.Import() if want & {a.asname or a.name for a in node.names}:
                    out.append(t)
                case ast.ImportFrom(module=m) if (
                    m
                    and (h := want & {a.asname or a.name for a in node.names})
                    and (repo / f"{m.replace('.', '/')}.py").exists()
                ):
                    try:
                        scan(importlib.import_module(m), h)
                    except:
                        pass
                case ast.Assign(targets=[ast.Name(id=n)]) if (
                    n in want and (id(mod), n) not in seen
                ):
                    seen.add((id(mod), n))
                    out.append(t)
                    scan(mod, names(t))

    def walk(o):
        try:
            if id(o) in seen or not inspect.getfile(o).startswith(str(repo)):
                return
        except:
            return
        seen.add(id(o))
        try:
            s = textwrap.dedent(inspect.getsource(o))
        except:
            return
        out.append(s)
        m, r = inspect.getmodule(o), names(s)
        scan(m, r)
        if m:
            for k, v in vars(m).items():
                if k in r and callable(v):
                    walk(v)

    walk(fn)
    return len(list(ast.walk(ast.parse("\n".join(out)))))

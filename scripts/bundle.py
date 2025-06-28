import os
import re
import sys


def get_imported_file(line: str):
    # Handles: from templates.xxx import ...
    m = re.match(r"from\s+templates\.([a-zA-Z0-9_]+)\s+import\s+", line.strip())
    if m:
        return f"templates/{m.group(1)}.py"
    return None


def bundle_inline(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    before_includes = []  # Lines before the bundled block (imports, etc.)
    after_includes = []  # Everything after imports
    inlined_blocks = []  # Collected template code

    in_import_block = True
    for line in lines:
        inc_path = get_imported_file(line)
        if inc_path and os.path.exists(inc_path):
            with open(inc_path, "r", encoding="utf-8") as inc:
                inlined_blocks.append(f"# region {inc_path}\n")
                inlined_blocks.extend(inc.readlines())
                inlined_blocks.append(f"# endregion\n")
            continue  # ❌ Skip original template import
        elif in_import_block and (
            line.strip().startswith("import") or line.strip().startswith("from")
        ):
            before_includes.append(line)
        else:
            in_import_block = False
            after_includes.append(line)

    # Insert bundled code after import section
    if inlined_blocks:
        before_includes.append("\n# fmt: off\n")
        before_includes.extend(inlined_blocks)
        before_includes.append("# fmt: on")

    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(before_includes + after_includes)

    print(f"✅ Inlined includes after imports in: {file_path}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python bundle.py <filename>")
        sys.exit(1)
    bundle_inline(sys.argv[1])

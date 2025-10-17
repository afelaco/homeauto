import os

DIST_DIR = "temp/simple"


def make_index(path: str) -> None:
    """Generate a nicely formatted index.html in the given path."""
    files = sorted(os.listdir(path))
    lines = ["<html>", "  <body>"]
    for f in files:
        full_path = os.path.join(path, f)
        if os.path.isdir(full_path):
            lines.append(f'    <a href="{f}/">{f}</a><br/>')
        elif f.endswith(".whl"):
            lines.append(f'    <a href="{f}">{f}</a><br/>')
    lines += ["  </body>", "</html>"]
    with open(os.path.join(path, "index.html"), "w") as file:
        file.write("\n".join(lines) + "\n")


# Generate package-level indexes first
for root, _dirs, files in os.walk(DIST_DIR):
    if any(f.endswith((".whl", ".tar.gz", ".zip")) for f in files):
        make_index(root)

# Generate top-level index
make_index(DIST_DIR)

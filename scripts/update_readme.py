import os
import re


def count_problem_files(directory):
    count = 0
    for filename in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, filename)):
            continue  # skip directories
        if re.match(r"^\d+[A-Z]\.py$", filename):
            count += 1
    return count


def update_readme_stats(readme_path, stats):
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
    # Update only the 'Total Problems Solved' line, number not bold
    content = re.sub(
        r"(\*\*Total Problems Solved:\*\*).*\n",
        f"**Total Problems Solved:** {stats['total']}\n",
        content,
    )
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)


# Get the parent directory of the script's location
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
readme_path = os.path.join(project_dir, "README.md")
total = count_problem_files(project_dir)
stats = {"total": total}
update_readme_stats(readme_path, stats)

import os
import ast
import csv

def describe_python_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            source = f.read()
            lines = source.splitlines()
            num_lines = len(lines)

            tree = ast.parse(source, filename=str(file_path))
            docstring = ast.get_docstring(tree)

            if docstring:
                description = docstring.strip().split('\n')[0]
            else:
                function_names = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
                if function_names:
                    description = f"Defines functions: {', '.join(function_names[:3])}..."
                else:
                    description = "No docstring or functions found"
            return description, num_lines
    except Exception as e:
        return f"Error reading file: {e}", 0

def search_python_scripts(root_dir):
    results = []
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".py"):
                full_path = os.path.join(dirpath, filename)
                description, line_count = describe_python_file(full_path)
                results.append((full_path, line_count, description))
    return results

def main():
    root_dir = input("Enter directory to search (e.g., C:\\Users\\YourName): ").strip()
    results = search_python_scripts(root_dir)

    csv_file = "python_file_summary.csv"
    with open(csv_file, mode="w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["File Path", "Line Count", "Description"])
        for path, lines, desc in sorted(results, key=lambda x: -x[1]):
            writer.writerow([path, lines, desc])

    print(f"\nSummary written to {csv_file}")

if __name__ == "__main__":
    main()

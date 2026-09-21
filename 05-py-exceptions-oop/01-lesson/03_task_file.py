from pathlib import Path

data_folder = Path(__file__).parent.parent / "03-data"
path = data_folder / "report.txt"

print(path)

try:
   # with open(path, "r", encoding = "utf-8") as file:
    with path.open("w", encoding="utf-8") as file:
        report = file.write("Practice report\n")
    print(report)
except PermissionError:
    print(f"Error: no permiession to write here.")

from pathlib import  Path
parent_path = Path.cwd().parent
print(parent_path)
base_path = parent_path / 'created_planner'

print(base_path)
from pathlib import Path

current_dir = Path(__file__)
# project_dir = [p for p in current_dir.parents if p.parts[-1]=='app'][0]
project_dir = next(p for p in current_dir.parents if p.name == "app")

# for p in current_dir.parents:
#     print(type(p))
#     print(p)

print(project_dir)


# print(build_type_dump(dictionary))
# print(build_type_dump(dictionary_nested))

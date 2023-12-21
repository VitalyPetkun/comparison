import os

objects = ("gnome", "cleaner", "printer", "rabbit")
BASE_PATH = "data"

u = 0

# for source_type in ("composer", "scanner"):

SOURCE_TYPE = "scanner"


lines = [
    "| | gnome | | cleaner | | printer | | rabbit | |",
    # ''.join(["|   "] * 9),
         ''.join(["|---"] * 9)]

for subfolder_i in range(6):
    line = "| "
    for object_type in objects:
        path = os.path.join("src", SOURCE_TYPE, f"scenario{subfolder_i}", object_type + ".gif")

        line += f"| ![]({path})| "

    lines.append(line + " |")


with open("tables.md", "w+") as file:
    file.write('\n'.join(lines))

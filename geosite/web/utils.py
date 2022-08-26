from io import StringIO
from .utils_functions import pars3, pars4


def txt2coordinates(input_file):
    log = []
    f = open(input_file, "r")
    lines = f.readlines()
    f.close()

    f = StringIO()

    num_of_lines = len(lines)
    log.append(f"Processing: {num_of_lines} lines")

    line = lines[0].strip().split(",")
    if len(line) == 3:
        final_num_of_lines, skipped_num_of_lines = pars3(lines, f)

    elif len(line) == 4:
        final_num_of_lines, skipped_num_of_lines = pars4(lines, f)

    else:
        pass

    # for line in lines[1:]:
    #     coordinates = line.strip().split(",")
    #     x = coordinates[0]
    #     y = coordinates[1]
    #     z = coordinates[2]
    #
    #     try:
    #         if '.' in z:
    #             z = float(z)
    #             print(f"{x},{y},{z}", file=f)
    #             final_num_of_lines += 1
    #         else:
    #             skipped_num_of_lines += 1
    #     except ValueError:
    #         skipped_num_of_lines += 1
    #         pass

    f.seek(0)

    log.append(f"Skipped number of lines: {skipped_num_of_lines}")
    log.append(f"Final number of lines: {final_num_of_lines}")

    return f, log

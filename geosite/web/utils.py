from io import StringIO


def txt2coordinates(input_file):
    log = []
    f = open(input_file, "r")
    lines = f.readlines()
    f.close()

    f = StringIO()

    num_of_lines = len(lines)
    log.append(f"Processing: {num_of_lines} lines")

    final_num_of_lines = 0
    skipped_num_of_lines = 0
    for line in lines[1:]:
        coordinates = line.strip().split(",")
        # print(coordinates)
        x = coordinates[0]
        y = coordinates[1]
        z = coordinates[2]
        # z1 = coordinates[3]

        try:
            if '.' in z:
                z = float(z)
                print(f"{x},{y},{z}", file=f)
                final_num_of_lines += 1
            else:
                skipped_num_of_lines += 1
        except ValueError:
            skipped_num_of_lines += 1
            pass

    f.seek(0)

    log.append(f"Skipped number of lines: {skipped_num_of_lines}")
    log.append(f"Final number of lines: {final_num_of_lines}")

    return f, log

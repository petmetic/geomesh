def pars3(lines, f):
    final_num_of_lines = 0
    skipped_num_of_lines = 1
    for line in lines[1:]:
        coordinates = line.strip().split(",")
        x = coordinates[0]
        y = coordinates[1]
        z = coordinates[2]

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
    return final_num_of_lines, skipped_num_of_lines


def pars4(lines, f):
    final_num_of_lines = 0
    skipped_num_of_lines = 1
    for line in lines[1:]:
        coordinates = line.strip().split(",")
        x = coordinates[0]
        y = coordinates[1]
        try:
            z = coordinates[2]
        except IndexError:
            z = None
        try:
            z1 = coordinates[3]
        except IndexError:
            z1 = None

        try:
            if z and float(z):  # boolean operations (if True and True)
                e = z
            elif z1 and float(z1):
                e = z1
            else:
                e = None

            if e:
                print(f"{x},{y},{e}", file=f)
                final_num_of_lines += 1
            else:
                skipped_num_of_lines += 1
        except ValueError:
            skipped_num_of_lines += 1

    return final_num_of_lines, skipped_num_of_lines

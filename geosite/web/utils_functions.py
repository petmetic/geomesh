def pars3(lines, f):
    final_num_of_lines = 0
    print(len(lines))
    for line in lines:
        coordinates = line.strip().split(",")  # ['414237.1700', '127086.2100', '000.00']
        x, y, z = coordinates  # shorthand syntax for: x = coordinates[0] y = coordinates[1]

        if z and '.' in z:
            try:
                z = float(z)
            except ValueError:
                continue

            if z > 0:
                print(f"{x},{y},{z}", file=f)
                final_num_of_lines += 1

    skipped_num_of_lines = len(lines) - final_num_of_lines
    print(skipped_num_of_lines)
    return final_num_of_lines, skipped_num_of_lines


def pars4(lines, f):
    final_num_of_lines = 0
    for line in lines:
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
                pass
        except ValueError:
            pass
    skipped_num_of_lines = len(lines) - final_num_of_lines
    return final_num_of_lines, skipped_num_of_lines


def is_it_a_header(line):
    print([line])
    header = False
    for cell in line:
        if cell:
            try:
                float(cell)
            except ValueError:
                header = True

    return header

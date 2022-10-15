
def pars3(lines, f):
    final_num_of_lines = 0
    print(len(lines))
    output_lines = []
    for line in lines:
        coordinates = line.strip().split(",")  # ['414237.1700', '127086.2100', '000.00']
        x, y, z = coordinates  # shorthand syntax for: x = coordinates[0] y = coordinates[1]

        if z and '.' in z:
            try:
                z = float(z)
            except ValueError:
                continue

            if z > 0:
                output_lines.append(
                    [x, y, z]
                )
                final_num_of_lines += 1

    test_line = output_lines[0]
    x_index, y_index, z_index = get_col_indexes(test_line)

    for line in output_lines:
        print(f"{line[x_index]},{line[y_index]},{line[z_index]}", file=f)

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


def get_col_indexes(line):
    x_index = None
    y_index = None
    z_index = None

    print("My line is:", line)

    for idx in range(0, len(line)):
        print("my idx is", idx)
        print("value at idx is", line[idx])
        value = float(line[idx])
        if 30900.00 < value < 192600.00:
            x_index = idx
        elif 375300.00 < value < 623000.00:
            y_index = idx
        elif 0.00 < value < 2864.00:
            z_index = idx

    return x_index, y_index, z_index

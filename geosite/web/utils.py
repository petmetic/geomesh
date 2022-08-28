from io import StringIO
from .utils_functions import pars3, pars4, is_it_a_header


def txt2coordinates(input_file):
    log = []
    f = open(input_file, "r")
    lines = f.readlines()
    f.close()

    f = StringIO()

    line = lines[0].strip().split(",")

    has_header = is_it_a_header(line)
    if has_header is True:
        lines = lines[1:]
        log.append(f"Detected header: skipping first line")

    log.append(f"Processing: {len(lines)} lines")

    if len(line) == 3:
        final_num_of_lines, skipped_num_of_lines = pars3(lines, f)

    elif len(line) == 4:
        final_num_of_lines, skipped_num_of_lines = pars4(lines, f)

    else:
        final_num_of_lines = 0
        skipped_num_of_lines = len(lines)
        log.append(f"Expected 3 or 4 columns. Found {len(lines)}.")
        pass

    f.seek(0)

    log.append(f"Skipped number of lines: {skipped_num_of_lines}")
    log.append(f"Final number of lines: {final_num_of_lines}")

    return f, log

#!/usr/bin/python3

import sys

def fmt_mid_line(s_line, width=79):
    s_line = s_line.strip().rstrip()
    n_length = len(s_line)
    if n_length == width:
        return s_line

    # create index array according to the line
    l_line = s_line.split(' ')
    l_mid = []
    l_index = []
    for word in l_line:
        word = word.strip().rstrip()
        if len(word) == 0:
            continue
        l_mid.append(word)
        l_index.append(len(word) + 1)
    if len(l_index) == 0:
        return ''
    l_index[-1] -= 1

    while True:
        n_length = sum(l_index)
        nspaces = width - n_length
        if nspaces <= 0:
            break

        i = 0
        while i < len(l_index) - 1:
            l_index[i] += 1
            nspaces -= 1
            if nspaces <= 0:
                break
            i += 1

    l_out = []
    i = 0
    while i < len(l_index):
        nspaces = l_index[i] - len(l_mid[i]) - 1
        l_out.append(l_mid[i] + ' ' * nspaces)
        i += 1
    return ' '.join(l_out)


def fmt_first_line(s_line, width=79):
    return ' ' * 3 + fmt_mid_line(s_line, width - 3)


def fmt_last_line(s_line, width=79):
    s_line = s_line.strip().rstrip()
    n_length = len(s_line)
    if n_length == width:
        return s_line

    return s_line + ' ' * (width - len(s_line))


def print_line(s_line):
    sys.stdout.write('%s\n' % s_line)


def main(argc, argv):
    if argc != 2:
        sys.stderr.write("Usage: %s <text file>\n" % argv[0])
        return 1

    with open(argv[1], 'r') as file_handler:
        lines = file_handler.readlines()
        print_line(fmt_first_line(lines[0]))
        for line in lines[1:-1]:
            print_line(fmt_mid_line(line))
        print_line(fmt_last_line(lines[-1]))

    return 0


if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv))

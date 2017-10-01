"""Insert dat stuff into your file my dude."""

# -*- coding: utf-8 -*-

import argparse
import re
from path import Path

def parse_args():

    """Argparser for command line input"""

    parser = argparse.ArgumentParser(
        description="Utility for turning files into JavaScript-embeddable strings.",
        epilog=("Before using the program you have to insert ""stuff2str(\"/path/to/file\") "
                "tag into your INFILE.")
        )
    parser.add_argument('-o', '--ow', dest='ow', action="store_true", help="overwrites input file")
    parser.add_argument("input", metavar='INFILE', type=str, help="input file")
    parser.add_argument("output", metavar='OUTFILE', nargs="?", type=str, help="output file")

    args = parser.parse_args()

    if not args.input:
        parser.error("You must specify at least one argument to go.")
    if args.ow and args.output is not None:
        parser.error("Utility takes only one additional argument if -o option is specified.")
    if not args.ow and args.input is not None and args.output is None:
        parser.error("If you want to overwrite your input file, please specify -o option.")
    if args.ow:
        args.output = args.input

    return args


__pattern__ = re.compile(r"^.*(stuff2str\(\"(.+?)\"\);?)(.*)$", re.M)
#make regex to find intendation at beginning of the file to indent shiet properly
__whitespace__ = re.compile(r"(^[ \t]*)", re.M)

def main():

    """Magic happens in this section"""

    args = parse_args()

    with open(args.input, "r") as infile:
        data = infile.readlines()

    matches = 0

    for i, line in enumerate(data):
        stuff = __pattern__.match(line)
        if stuff is not None:
            matches += 1
            padding = __whitespace__.match(line).group(1)
            path2parent = Path(args.input).expand().parent
            if path2parent:
                css = path2parent.joinpath(Path(stuff.group(2)))
            else:
                #this assumes that file to convert is in same directory as our workfile
                css = Path(stuff.group(2)).expand()
            near_end = stuff.group(3)
            with open(css, "r") as incss:
                raw_css = []
                for line in incss:
                    if not line.isspace():
                        raw_css.append(re.sub("[\"\']", "\\\"", line))
            css_list = []
            for line in raw_css[0:-1]:
                css_list.append(padding*2+'"'+line.rstrip("\n")+' ",\n')
            css_list.append(padding*2+'"'+raw_css[-1].rstrip("\n")+' "\n')
            if not all(c.isspace() for c in near_end):
                css_list.append(padding+'].join("\\n")'+near_end+"\n")
            else:
                css_list.append(padding+'].join("\\n");\n')
            data[i] = data[i][:-(len(stuff.group(1))+len(stuff.group(3)))-1] + "[\n"
            data[i+1:i+1] = css_list

    if not matches:
        print("There was no arguments in input file to expand.")
        return 2

    with open(args.output, "w") as outfile:
        outfile.writelines(data)

    print("Finalized without hickups.")

    return 0

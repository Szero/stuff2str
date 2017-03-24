# -*- coding: utf-8 -*-

import argparse
import re
from path import Path

def parse_args():

    parser = argparse.ArgumentParser(description="Utility for turning files into JavaScript-embeddable strings.")
    parser.add_argument('-o','--ow', dest='ow', action="store_true", help="overwrites input file")
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


def main():

    args = parse_args()

    with open(args.input,"r") as f:
        data = f.readlines()

    pattern = re.compile("^.*(stuff2str\(\"(.+?)\"\);?)(.*)$", re.M)
    #make regex to find intendation at beginning of the file to indent shiet properly
    ws = re.compile("(^[ \t]*)", re.M)
    matches = 0

    for i,d in enumerate(data):
        stuff = pattern.match(d)
        if stuff is not None:
            matches += 1
            padding = ws.match(d).group(1)
            path2parent = Path(args.input).expand().parent
            if path2parent:
                css =  path2parent.joinpath(Path(stuff.group(2)))
            else:
                #this assumes that file to convert is in same directory as our workfile
                css = Path(stuff.group(2)).expand()
            near_end = stuff.group(3)
            with open(css, "r") as f:
                raw_css = []
                for line in f:
                    if not line.isspace():
                        raw_css.append(re.sub("[\"\']","\\\"",line))
            cssList = []
            for l in raw_css:
                if not l == raw_css[-1]:
                    cssList.append(padding*2+'"'+l.rstrip("\n")+' ",\n')
                else:
                    cssList.append(padding*2+'"'+l.rstrip("\n")+' "\n')
            if not all(c.isspace() for c in near_end):
                cssList.append(padding+'].join("\\n")'+near_end+"\n")
            else:
                cssList.append(padding+'].join("\\n");\n')
            data[i] = data[i][:-(len(stuff.group(1))+len(stuff.group(3)))-1] + "[\n"
            data[i+1:i+1] = cssList

    if not matches:
        print("There was no arguments in input file to expand.")
        return 2

    with open(args.output,"w") as f:
        f.writelines(data)

    print("Finalized without hickups.")

    return 0

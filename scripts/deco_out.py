#! /usr/bin/python
import sys


def usage():
        print 'deco_out.py bbl_in bbl_out';


def main(argv):
        if len(argv) < 2:
                usage();
                sys.exit(-1);
        
        bbl_in = open(argv[0]);
        bbl_out = open(argv[1]);

        #construct dict && skip the first
        bbl_dict = {};
        bbl_in.readline();
        line = bbl_in.readline();
        while line:
                parts = line.split();
                key = int(parts[2], base=16);
                bbl_dict[key] = (parts[0], parts[1]);
                line = bbl_in.readline();
        bbl_in.close();

        #output
        line = bbl_out.readline();
        while line:
                key = int(line, base=16);
                print bbl_dict[key][0] + ' ' + bbl_dict[key][1];
                line = bbl_out.readline();
        bbl_out.close();

if __name__ == '__main__':
        main(sys.argv[1:]);

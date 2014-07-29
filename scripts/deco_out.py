#! /usr/bin/python
import sys


def decorate_bbl_trace_out(bbl_in_file, bbl_out_file, outfile):
        bbl_in = open(bbl_in_file);
        bbl_out = open(bbl_out_file);
        f = open(outfile, 'w');
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
                f.write( bbl_dict[key][0] + ' ' + bbl_dict[key][1] +'\n');
                line = bbl_out.readline();
        bbl_out.close();
        f.close();


def usage():
        print 'deco_out.py bbl_in bbl_out output_file';


def main(argv):
        if len(argv) < 3:
                usage();
                sys.exit(-1);

        
if __name__ == '__main__':
        main(sys.argv[1:]);

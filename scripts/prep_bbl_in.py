#! /usr/bin/python

import sys
import subprocess
import re




def get_line_map(executable):
        proc = subprocess.Popen('objdump --dwarf=decodedline '+executable, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE);
        (out, err) = proc.communicate();
        if err!='':
                sys.stdout.write(err);
                sys.exit(-1);
        reg = re.compile(r'([^\s]+)\s+(\d+)\s+(0x[0-9a-f]+)');
        result = reg.findall(out);
        return result;
def write_map_to_file(result, f_name):
        f = open(f_name, 'w');
        f.write(str(len(result)) + '\n');
        for line in result:
                f.write(line[0] +' '+line[1] +' '+line[2] + '\n');
        f.close();

def usage():
        print 'prep_bbl_in.py binary_name output_file';

def main(argv):
        if len(argv) < 2:
                usage();
                sys.exit(-1);
        result = get_line_map(argv[0]); 
        write_map_to_file(result, argv[1]);
if __name__ == "__main__":
        main(sys.argv[1:]);

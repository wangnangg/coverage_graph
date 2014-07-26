#! /usr/bin/python

import sys
import subprocess
import re






def usage():
        print 'prep_bbl_in.py binary_name';

def main(argv):
        if len(argv) < 1:
                usage();
                sys.exit(-1);
        proc = subprocess.Popen('objdump --dwarf=decodedline '+argv[0], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE);
        (out, err) = proc.communicate();
        if err!='':
                sys.stdout.write(err);
                sys.exit(-1);
        reg = re.compile(r'([^\s]+)\s+(\d+)\s+(0x[0-9a-f]+)');
        result = reg.findall(out);
        print len(result);
        for line in result:
                print line[0] +' '+line[1] +' '+line[2];
if __name__ == "__main__":
        main(sys.argv[1:]);

#! /usr/bin/python
import sys
import os
from prep_bbl_in import *
from deco_out import *
import re


def run(pintool, target, script):
        #prepare possible address
        result = get_line_map('../versions/'+target);
        write_map_to_file(result, 'bbl_trace.in');
        #prepare exe
        parts = target.split('.');
        new_name = parts[0] + '.exe';
        os.system('cp ../versions/'+target+' ../source/'+new_name);
        #version name
        version_name = parts[2];
        #create dir
        passed_dir = '../traces/'+version_name+'/passed';
        failed_dir = '../traces/'+version_name+'/failed';
        os.system('rm -rf ' + passed_dir +'/*');
        os.system('rm -rf ' + failed_dir +'/*');
        os.system('mkdir -p '+passed_dir);
        os.system('mkdir -p '+failed_dir);
        #run modified script
        f = open(script);
        line = f.readline();
        i = 0;
        while line:
                if line.startswith('echo'):
                        os.system(line);
                else:
                        cmd = 'pin -injection child -t ' + pintool +' -- ' + line;
                        print cmd;
                        code = os.system(cmd);
                        if code != 0:
                                print 'pin error'; 
                                sys.exit(-1);
                        #deco result
                        decorate_bbl_trace_out('bbl_trace.in', 'bbl_trace.out', 'deco.out');
                        #save
                        if test_passed(line):
                                print 'passed';
                                os.system('mv deco.out '+passed_dir +'/'+str(i));
                        else:
                                print 'failed';
                                os.system('mv deco.out '+failed_dir +'/'+str(i));
                        i+=1;
                line = f.readline();
        f.close();
              
def test_passed(line):
        tst_name = re.findall(r'>\s*../outputs/(\w+)', line)[0];
        tst_out = '../outputs/'+tst_name;
        tst_oracle = '../newoutputs/'+tst_name;
        code = os.system('cmp '+tst_out+' '+tst_oracle);
        if code != 0:
                return False;
        return True;
def usage():
        print 'run.py pin_tool test_target script';

def main(argv):
        if len(argv) < 3:
                usage();
                sys.exit(-1);
        run(argv[0], argv[1], argv[2]);

if __name__ == '__main__':
        main(sys.argv[1:]);

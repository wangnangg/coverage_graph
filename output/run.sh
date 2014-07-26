../scripts/prep_bbl_in.py $@ > bbl_trace.in
if [[ $? != 0 ]]
then
        echo 'pre_bbl_in.py error'
        exit -1
fi
pin -injection child -t ../bin/test.so -- $@ 
if [[ $? != 0 ]]
then
        echo 'pin error'
        exit -1
fi
../scripts/deco_out.py bbl_trace.in bbl_trace.out > bbl_trace.deco_out
if [[ $? != 0 ]]
then
        echo 'deco error'
        exit -1
fi

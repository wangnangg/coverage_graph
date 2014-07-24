#include <iostream>
#include <fstream>
#include "pin.H"

ofstream OutFile;

static UINT64 icount = 0;

VOID docount() { icount++; }

VOID Instruction(INS ins, VOID *v)
{
        INS_InsertCall(ins, IPOINT_BEFORE, (AFUNPTR)docount, IARG_END);
}

KNOB<string> KnobOutputFile(KNOB_MODE_WRITEONCE, "pintool", "o", "inscount.out", "specifiy output file name");

VOID Fini(INT32 code, VOID *v)
{
        OutFile.setf(ios::showbase);
        OutFile << "Count " << icount << endl;
        OutFile.close();
} 


INT32 Usage()
{
        cerr << "error" << endl;
        cerr << endl << KNOB_BASE::StringKnobSummary() << endl;
        return -1;
}

int main(int argc, char *argv[])
{
        if (PIN_Init(argc, argv)) return Usage();

        OutFile.open(KnobOutputFile.Value().c_str());

        INS_AddInstrumentFunction(Instruction, 0);

        PIN_AddFiniFunction(Fini, 0);

        PIN_StartProgram();

        return 0;
}

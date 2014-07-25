#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "pin.H"

FILE* output_file;
FILE* input_file;
ADDRINT* possible_addr_array;
int addr_length;

int contains(ADDRINT* array, int length, ADDRINT value)
{

}
// This function is called before every block
VOID track_trace(ADDRINT addr)
{
       fprintf(output_file, "%x\n", addr); 
}

// Pin calls this function every time a new basic block is encountered
// It inserts a call to docount
VOID Trace(TRACE trace, VOID *v)
{
        // Visit every basic block  in the trace
        for (BBL bbl = TRACE_BblHead(trace); BBL_Valid(bbl); bbl = BBL_Next(bbl))
        {
                // Insert a call to docount before every bbl, passing the number of instructions
                BBL_InsertCall(bbl, IPOINT_BEFORE, (AFUNPTR)track_trace, IARG_ADDRINT, BBL_Address(bbl), IARG_END);
        }
}


KNOB<string> KnobOutputFile(KNOB_MODE_WRITEONCE, "pintool","o", "bbl_trace.out", "specify output file name");
KNOB<string> KnobInputFile(KNOB_MODE_WRITEONCE, "pintool","i", "bbl_trace.in", "specify input file name");
// This function is called when the application exits
VOID Fini(INT32 code, VOID *v)
{
       fclose(output_file); 
}

/* ===================================================================== */
/* Print Help Message                                                    */
/* ===================================================================== */

INT32 Usage()
{
        return -1;
}

void get_possible_addr()
{
        input_file = fopen(KnobInputFile.Value().c_str(), "r");
        
        //get total number of addrs
        int n = 0;
        assert( fscanf(input_file, "%d", &n) > 0);

        //allocate memory
        possible_addr_array = (ADDRINT*)malloc(sizeof(ADDRINT) * n);
        int i;
        for(i=0; i<n; i++)
        {
                assert( fscanf(input_file, "%x", possible_addr_array + i) > 0);
                fprintf(stdout, "%x\n", possible_addr_array[i]);
                
        }

        fclose(input_file);

}

/* ===================================================================== */
/* Main                                                                  */
/* ===================================================================== */

int main(int argc, char * argv[])
{
        // Initialize pin
        if (PIN_Init(argc, argv)) return Usage();
        
        output_file = fopen(KnobOutputFile.Value().c_str(), "w");

        //get possible addr
        get_possible_addr(); 
        

        // Register Instruction to be called to instrument instructions
        TRACE_AddInstrumentFunction(Trace, 0);

        // Register Fini to be called when the application exits
        PIN_AddFiniFunction(Fini, 0);

        // Start the program, never returns
        PIN_StartProgram();

        return 0;
}

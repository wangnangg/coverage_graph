
PINDIR=/home/wangnan/Software/pin-2.13-65163-gcc.4.4.7-linux

#################################

CC=gcc
_TARGET:=test.so
TARDIR=./bin
SOURCE:=./src/bbl_trace.cpp
OBJDIR=./bin/obj
LFLAGS=-shared -Wl,--hash-style=sysv -Wl,-Bsymbolic -Wl,--version-script=$(PINDIR)/source/include/pin/pintool.ver -L$(PINDIR)/ia32/lib -L$(PINDIR)/ia32/lib-ext -L$(PINDIR)/ia32/runtime/glibc -L$(PINDIR)/extras/xed2-ia32/lib -lpin -lxed -ldwarf -lelf -ldl
CFLAGS=-DBIGARRAY_MULTIPLIER=1 -Wall -Wno-unknown-pragmas -fno-stack-protector -DTARGET_IA32 -DHOST_IA32 -DTARGET_LINUX  -I$(PINDIR)/source/include/pin -I$(PINDIR)/source/include/pin/gen -I$(PINDIR)/extras/components/include -I$(PINDIR)/extras/xed2-ia32/include -I$(PINDIR)/source/tools/InstLib -O3 -fomit-frame-pointer -fno-strict-aliasing 

######################################

TARGET=$(TARDIR)/$(_TARGET)
_OBJ=$(addprefix $(OBJDIR)/, $(notdir $(SOURCE)))
OBJ=$(_OBJ:.cpp=.o)
DIRS=$(TARDIR) $(OBJDIR)
.PHONY: all

all: $(DIRS) $(TARGET)

$(DIRS):
	@[ -d $@ ] || mkdir -p $@

$(TARGET): $(OBJ)
	$(CC) -o $@ $^ $(LFLAGS)

$(OBJ): $(SOURCE)
	$(CC) -c -o $@ $< $(CFLAGS)


.PHONY: clean

clean:
	rm -rf $(OBJDIR)/*
	rm -rf $(TARGET)

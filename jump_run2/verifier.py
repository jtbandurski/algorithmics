import sys
# Verifies the input
# Return code is 0 if input is OK, otherwise return code is 1.

# Readme: 
# Either 
#   1) set INPUT_FILE = None, then the verifier reads the input file from the standard input (use command line: on Winows, write "type INPUTFILENAME | python verifier.py", or
#   2) set INPUT_FILE to the name of the file to be tested.
INPUT_FILE = "test_input.txt"



if INPUT_FILE == None:
    reader = sys.stdin
    print("Verifying the input from the standard input")
else:
    reader = inputReader = open(INPUT_FILE,"r")
    print("Verifying the input file "+INPUT_FILE)


lnr = 0
line = ""
pos = 0

def eprint(msg, **kwargs):
    print("\tERROR: "+msg, file=sys.stderr, **kwargs)
    exit(1)

def assert_is_space(lnr,line,pos):
    if line[pos] != " ":
        eprint("Missing space at line number %d at position %d"%(lnr+1,pos+1))

def read_int(minv=None,maxv=None):
    global lnr
    global line
    global pos
    if (pos > len(line) or line[pos]=="\n" or line[pos]=="\r"):
        eprint("Expected integer at line %d at position %d but the line ended"%(lnr+1,pos+1))
    pos2=pos
    if pos2 < len(line) and line[pos2]=="-":
        pos2 += 1
    while pos2 < len(line) and line[pos2].isdigit():
        pos2 += 1
    if pos2 == len(line):
        eprint("Line %d ends with an integer, but each integer should be followed by an whitespace, even the last integer on a line."%(lnr+1))
    if pos == pos2:
        eprint("Expected integer at line %d at position %d but there was '%s'"%(lnr+1,pos+1,line[pos]))
    assert_is_space(lnr,line,pos2)
    val = int(line[pos:pos2])
    if minv!= None and minv==maxv and val != minv:
        eprint("Integer '%d' (as string: '%s') at line %d positions %d to %d is not equal to the expected value of='%d'"%(val,line[pos:pos2],lnr+1,pos+1,pos2,minv))        
    else:
        if minv != None and val < minv:
            eprint("Integer '%d' (as string: '%s') at line %d positions %d to %d is smaller than the minimum required value of='%d'"%(val,line[pos:pos2],lnr+1,pos+1,pos2,minv))
        if maxv != None and val > maxv:
            eprint("Integer '%d' (as string: '%s') at line %d positions %d to %d is larger than the maximum allowed value of='%d'"%(val,line[pos:pos2],lnr+1,pos+1,pos2,maxv))
    pos = pos2 + 1
    return val

def read_end_line():
    global lnr
    global line
    global pos
    if pos >= len(line):
        eprint("The file ends at line %d, but it shouldn't end there. (Note that the file should end with an empty line.)"%(lnr+1))
    if not(line[pos]=="\n" or line[pos]=="\r"):
        eprint("Line %d should end at pos %d, but the line does not end there."%(lnr+1,pos+1))
    line = reader.readline()
    lnr += 1
    pos = 0

def read_end_file():
    if line != None and len(line)>0:
        eprint("Expected end of file right at the beginning of line %d but it is not the case."%(lnr+1))
    
def start():
    global lnr
    global line
    global pos
    lnr = 0
    line = reader.readline()
    pos = 0


start()
n = read_int(10,300)
m = read_int(1,300*1000)
read_end_line()
for i in range(n):
    val = read_int(-i,n-1-i)
    assert(val != 0)
    if val > 0:
        assert(i < n-1)
read_end_line()
start = [0]*(m+1)
for j in range(m):
    start[j] = read_int(0,n-1)
read_end_line()
target = [0]*(m+1)
for j in range(m):
    target[j] = read_int(0,n-1)
read_end_line()
tlimits = [0]*(m+1)
for j in range(m):
    tlimits[j] = read_int(0,2*n)
read_end_line()
read_end_file()

if INPUT_FILE != None:
    reader.close()

print("Good, your input test satisfies the formatting and standard assumptions.")

print("Now testing the extended assumptions (as required if you want to publish the test):")

if n < 30:
    eprint("Level too small.")
    
if m < 10:
    eprint("Not enough heroes.")
    
diff_jn = {}
for h in range(m):
    if tlimits[h]>n/2:
        diff_jn[(start[h],target[h])]=True


if len(diff_jn) < 10:
    eprint("Not enough heroes defined (among all the heroes, there should be 10 heroes with pairwise different start,end-fields and time_limits > n/2)!")
    

print("Your input test also satisfies the extended assumptions.")

exit(0)
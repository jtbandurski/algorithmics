import sys
# Verifies the input

INPUT_FILE = "./jump_run/input.txt"


print("Verifying the input file "+INPUT_FILE)

lnr = 0
line = ""
pos = 0
reader = inputReader = open(INPUT_FILE,"r")


def eprint(msg, **kwargs):
    print("ERROR: "+msg, file=sys.stderr, **kwargs)
    exit()

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
    while line[pos2].isdigit():
        pos2 += 1
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
    if not(line[pos]=="\n" or line[pos]=="\r"):
        eprint("Expected line end at pos %d of line %d, but the line does not end there."%(pos+1,lnr+1))
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
n = read_int(7,4500)
m = read_int(4,45000)
k = read_int(4,20)
read_end_line()
kvals = {}
read_int(1,k)
for i in range(1,n-k+1):
    val = read_int(0,k)
    kvals[val] = True
for i in range(n-k+1,n-1):
    val = read_int(0,n-i)
    kvals[val] = True
read_int(1,1)
kvals[1] = True
read_end_line()
tlimits = [0]*(m+1)
for j in range(m):
    tlimits[j] = read_int(0,2*n)
read_end_line()
stamina = [0]*(m+1)
for j in range(m):
    stamina[j] = read_int(0,n-1)
read_end_line()
read_end_file()

reader.close()

print("Good, your input test satisfies the formatting and standard assumptions.")

print("Now testing the extended assumptions (as required if you want to publish the test):")

if n < 30:
    eprint("Level too small.")
    
if m < 10:
    eprint("Not enough heroes.")
    
if len(kvals) < k+1:
    eprint("The level does not contain all numbers from 0 to k!")
    
diff_jn = {}
for h in range(m):
    if tlimits[h]>n/2:
        diff_jn[stamina[h]]=True


if len(diff_jn) < 10:
    eprint("Not enough heroes defined (among all the heroes, there should be 10 hereoes with pairwise different stamina and time_limits > n/2)!")
    

print("Your input test also satisfies the extended assumptions.")

import sys

if len(sys.argv)==3:
	filepath = sys.argv[1]
	features = int(sys.argv[2])
	# print(filepath)
elif len(sys.argv)==2:
	filepath = sys.argv[1]
	# print(filepath)
else:
	print("require file name as arugment")
	exit()

try:
	with open(filepath) as f:
		raw = f.read()
except:
	print("file not exist")
	# postToTelegram(filepath)

payloads = raw.split("\n")

blanks = [payload for payload in payloads if payload==""]

libraries =  [payload for payload in payloads if "import" in payload]
# print("balnks", str(len(blanks)))
print("Libraries: " + str(len(libraries)))

#counting funcs

# funcs = []
funcs_count = 0
pcount  = 0

for payload in payloads:
	if "def " in payload and pcount==0:
		pcount = 1
		# funcs.append(payload)
	elif "" in payload and pcount!=0:
		funcs_count = funcs_count + pcount 
		pcount = 0
	else:
		pcount = pcount + 1

# print(funcs)
remaining = list(set(payloads) - set(libraries) - set(blanks))
remaining = len(remaining) - funcs_count
print("Logic lines: " + str(remaining))

try:
	print("Features: " + str(features))
	print("Code density: "+ str(remaining/features))
except Exception as e:
	print(e)
import sys 

sents = {}

for block in sys.stdin.read().split('\n\n'):
	for line in block.split('\n'):
		if line.count('# sent_id') > 0:
			sid = line.split('=')[1].strip()
			sents[sid] = block

for sent_id in open(sys.argv[1]).read().split('\n'):
	if sent_id == '':
		print('WARNING:', sent_id, file=sys.stderr)
		continue
	print(sents[sent_id])
	print()

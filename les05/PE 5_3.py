infile= open('kaartnummers.txt','r')
inhoud= infile.read()
infile.close()
tellen= inhoud.count('\n')
inhoud1=inhoud.split('\n')
print('Deze file telt '+str(tellen)+' regels')
print('De grootste kaartnummer is: '+max(inhoud1)+' en dat staat op regel 6')


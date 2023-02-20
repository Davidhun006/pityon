henrik=input('Jön Henrik kosarazni(igen/nem)?')
hanna=input('Jön Hanna kosarazni(igen/nem)?')
if henrik and hanna == 'igen':
    print('Mind a ketten jönnek kosarazni.')
elif henrik and hanna == 'nem':
    print('Egyikük sem jön kosarazni.')
else:
    print('Csak az egyikük jön kosarazni.')
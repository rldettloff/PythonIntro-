from collections import namedtuple

Player = namedtuple('Player', ['name', 'number', 'position', 'team'])

cam = Player('Cam Newton', '1', 'Quarterback', 'Carolina Panthers')
lebron = Player('Lebron James', '23', 'Small forward', 'Los Angeles Lakers')
geno = Player('Geno Smith', '7', 'Quarterback', 'Seattle Seahawks')

input('Press Return to View Player 1')
print(f'{cam.name}(#{cam.number}) is a {cam.position} for the {cam.team}.')
input('Press Return to View Player 2')
print(f'{lebron.name}(#{lebron.number}) is a {lebron.position} for the {lebron.team}.')
input('Press Return to View Player 3')
print(f'{geno.name}(#{geno.number}) is a {geno.position} for the {geno.team}.')

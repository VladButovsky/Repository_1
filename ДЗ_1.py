from pprint import pprint
sites = {
'Moscow': (550, 370),
'London': (510, 510),
'Paris': (480, 480),
}
# ((x1-x2)**2+(y1-y2)**2)**.5
distanses = dict()

Msc = sites['Moscow']
Lnd = sites['London']
Prs = sites['Paris']
moscow_london = ((Msc[0] - Lnd[0])**2 + (Msc[1] - Lnd[1])**2) ** .5
moscow_paris = ((Msc[0] - Prs[0])**2 + (Msc[1] - Prs[1])**2) ** .5
london_paris = ((Lnd[0] - Prs[0])**2 + (Lnd[1] - Prs[1])**2) ** .5

distanses['Moscow'] = {}
distanses['Moscow']['London'] = moscow_london
distanses['Moscow']['Paris'] = moscow_paris

distanses['London']= {}
distanses['London']['Paris'] = london_paris
distanses['London']['Moscow']= moscow_london

distanses['Paris']= {}
distanses['Paris']['London'] = london_paris
distanses['Paris']['Moscow'] = moscow_paris

pprint(distanses)
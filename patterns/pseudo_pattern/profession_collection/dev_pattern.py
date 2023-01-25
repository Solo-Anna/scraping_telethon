from patterns.pseudo_pattern.fake_pattern import pattern

dev = {
    'ma': pattern['analyst']['ma'],
    'ma2': pattern['analyst']['ma2'],
    'mdef': pattern['analyst']['mdef'],
    'mex': pattern['analyst']['mex'],
    'mex2': pattern['analyst']['mex2'],
    'mincl': pattern['analyst']['mincl'],
}

dev['sub'] = {}
# merge to ma = ma2 + mdef
accumulate = set()
for sub in dev['sub']:
    dev['sub'][sub]['ma'] = set(dev['sub'][sub]['ma']).union(set(dev['sub'][sub]['ma2'])).union(set(dev['sub'][sub]['mdef']))
    accumulate = accumulate.union(dev['sub'][sub]['ma'])
dev['ma'] = set(dev['ma']).union(set(dev['ma2'])).union(set(dev['mdef'])).union(accumulate)

# add mincl to mex
for sub_profession in dev['sub']:
    dev['sub'][sub_profession]['mex'] = set(dev['sub'][sub_profession]['mex']).union(set(dev['sub'][sub_profession]['mincl']))

# print(f"\n********************\n{backend}\n****************\n")

print('\nDEV')
for i in dev:
    if i in ['mex', 'mex2', 'ma', 'ma2', 'mdef', 'mincl']:
        print(f"{i}: {dev[i]}")
    else:
        print('sub: ')
        for j in dev[i]:
            print(f"   * {j}: {dev[i][j]}")


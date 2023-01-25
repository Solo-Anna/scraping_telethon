from patterns.data_pattern._data_pattern import pattern

hr = {
    'ma': pattern['hr']['ma'],
    'ma2': pattern['hr']['ma2'],
    'mdef': pattern['hr']['mdef'],
    'mex': pattern['hr']['mex'],
    'mex2': pattern['hr']['mex2'],
    'mincl': pattern['hr']['mincl'],
}

hr['sub'] = {}
# merge to ma = ma2 + mdef
accumulate = set()
for sub in hr['sub']:
    hr['sub'][sub]['ma'] = set(hr['sub'][sub]['ma']).union(set(hr['sub'][sub]['ma2'])).union(set(hr['sub'][sub]['mdef']))
    accumulate = accumulate.union(hr['sub'][sub]['ma'])
hr['ma'] = set(hr['ma']).union(set(hr['ma2'])).union(set(hr['mdef'])).union(accumulate)

# add mincl to mex
for sub_profession in hr['sub']:
    hr['sub'][sub_profession]['mex'] = set(hr['sub'][sub_profession]['mex']).union(set(hr['sub'][sub_profession]['mincl']))

# print(f"\n********************\n{frontend}\n****************\n")
print('\nGAME:')
for i in hr:
    if i in ['mex', 'mex2', 'ma', 'ma2', 'mdef', 'mincl']:
        print(f"{i}: {hr[i]}")
    else:
        print('sub: ')
        for j in hr[i]:
            print(f"   * {j}: {hr[i][j]}")

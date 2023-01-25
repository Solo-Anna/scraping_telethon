from patterns.data_pattern._data_pattern import pattern

devops = {
    'ma': pattern['devops']['ma'],
    'ma2': pattern['devops']['ma2'],
    'mdef': pattern['devops']['mdef'],
    'mex': pattern['devops']['mex'],
    'mex2': pattern['devops']['mex2'],
    'mincl': pattern['devops']['mincl'],
}

devops['sub'] = {}
accumulate = set()
# merge to ma = ma2 + mdef
for sub in devops['sub']:
    devops['sub'][sub]['ma'] = set(devops['sub'][sub]['ma']).union(set(devops['sub'][sub]['ma2'])).union(set(devops['sub'][sub]['mdef']))
    accumulate = accumulate.union(devops['sub'][sub]['ma'])
devops['ma'] = set(devops['ma']).union(set(devops['ma2'])).union(set(devops['mdef'])).union(accumulate)

# add mincl to mex
for sub_profession in devops['sub']:
    devops['sub'][sub_profession]['mex'] = set(devops['sub'][sub_profession]['mex']).union(set(devops['sub'][sub_profession]['mincl']))

# print(f"\n********************\n{backend}\n****************\n")

print('\nDEV')
for i in devops:
    if i in ['mex', 'mex2', 'ma', 'ma2', 'mdef', 'mincl']:
        print(f"{i}: {devops[i]}")
    else:
        print('sub: ')
        for j in devops[i]:
            print(f"   * {j}: {devops[i][j]}")
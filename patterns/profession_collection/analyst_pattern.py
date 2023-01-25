from patterns.data_pattern._data_pattern import pattern

analyst = {
    'ma': pattern['analyst']['ma'],
    'ma2': pattern['analyst']['ma2'],
    'mdef': pattern['analyst']['mdef'],
    'mex': pattern['analyst']['mex'],
    'mex2': pattern['analyst']['mex2'],
    'mincl': pattern['analyst']['mincl'],
}

sys_analyst = {
    'ma': pattern['analyst']['sub']['sys_analyst']['ma'],
    'ma2': pattern['analyst']['sub']['sys_analyst']['ma2'],
    'mdef': pattern['analyst']['sub']['sys_analyst']['mdef'],
    'mex': pattern['analyst']['sub']['sys_analyst']['mex'],
    'mex2': pattern['analyst']['sub']['sys_analyst']['mex2'],
    'mincl': pattern['analyst']['sub']['sys_analyst']['mincl'],
}
# sys_analyst['mex'] = set(pattern['marketing']['mex']).union(set(sys_analyst['mex2']))

data_analyst = {
    'ma': pattern['analyst']['sub']['data_analyst']['ma'],
    'ma2': pattern['analyst']['sub']['data_analyst']['ma2'],
    'mdef': pattern['analyst']['sub']['data_analyst']['mdef'],
    'mex': pattern['analyst']['sub']['data_analyst']['mex'],
    'mex2': pattern['analyst']['sub']['data_analyst']['mex2'],
    'mincl': pattern['analyst']['sub']['data_analyst']['mincl'],
}
# data_analyst['mex'] = set(pattern['marketing']['mex']).union(set(data_analyst['mex2']))

data_scientist = {
    'ma': pattern['analyst']['sub']['data_scientist']['ma'],
    'ma2': pattern['analyst']['sub']['data_scientist']['ma2'],
    'mdef': pattern['analyst']['sub']['data_scientist']['mdef'],
    'mex': pattern['analyst']['sub']['data_scientist']['mex'],
    'mex2': pattern['analyst']['sub']['data_scientist']['mex2'],
    'mincl': pattern['analyst']['sub']['data_scientist']['mincl'],
}
# data_scientist['mex'] = set(pattern['marketing']['mex']).union(set(data_scientist['mex2']))

ba = {
    'ma': pattern['analyst']['sub']['ba']['ma'],
    'ma2': pattern['analyst']['sub']['ba']['ma2'],
    'mdef': pattern['analyst']['sub']['ba']['mdef'],
    'mex': pattern['analyst']['sub']['ba']['mex'],
    'mex2': pattern['analyst']['sub']['ba']['mex2'],
    'mincl': pattern['analyst']['sub']['ba']['mincl'],
}
# ba['mex'] = set(pattern['marketing']['mex']).union(set(ba['mex2']))

analyst['sub'] = {
    'sys_analyst': sys_analyst,
    'data_analyst': data_analyst,
    'data_scientist': data_scientist,
    'ba': ba
}

# merge to ma = ma2 + mdef
accumulate = set()
for sub in analyst['sub']:
    analyst['sub'][sub]['ma'] = set(analyst['sub'][sub]['ma']).union(set(analyst['sub'][sub]['ma2'])).union(set(analyst['sub'][sub]['mdef']))
    accumulate = accumulate.union(analyst['sub'][sub]['ma'])
analyst['ma'] = set(analyst['ma']).union(set(analyst['ma2'])).union(set(analyst['mdef'])).union(accumulate)

# add mincl to mex
for sub_profession in analyst['sub']:
    analyst['sub'][sub_profession]['mex'] = set(analyst['sub'][sub_profession]['mex']).union(set(analyst['sub'][sub_profession]['mincl']))

# print(f"\n********************\n{backend}\n****************\n")

print('\nANALYST')
for i in analyst:
    if i in ['mex', 'mex2', 'ma', 'ma2', 'mdef', 'mincl']:
        print(f"{i}: {analyst[i]}")
    else:
        print('sub: ')
        for j in analyst[i]:
            print(f"   * {j}: {analyst[i][j]}")
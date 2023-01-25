from patterns.data_pattern._data_pattern import pattern

junior = {
    'ma': pattern['junior']['ma'],
    'ma2': pattern['junior']['ma2'],
    'mdef': pattern['junior']['mdef'],
    'mex': pattern['junior']['mex'],
    'mex2': pattern['junior']['mex2'],
    'mincl': pattern['junior']['mincl'],
}
junior['sub'] = {}
# merge to ma = ma2 + mdef
accumulate = set()
for sub in junior['sub']:
    junior['sub'][sub]['ma'] = set(junior['sub'][sub]['ma']).union(set(junior['sub'][sub]['ma2'])).union(set(junior['sub'][sub]['mdef']))
    accumulate = accumulate.union(junior['sub'][sub]['ma'])
junior['ma'] = set(junior['ma']).union(set(junior['ma2'])).union(set(junior['mdef'])).union(accumulate)

# add mincl to mex
for sub_profession in junior['sub']:
    junior['sub'][sub_profession]['mex'] = set(junior['sub'][sub_profession]['mex']).union(set(junior['sub'][sub_profession]['mincl']))

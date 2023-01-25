
detailed_designer = {
    'ma': (),
    'ma2': (),
    'mdef': (),
    'mex': (),
    'mex2': (),
    'mincl': ()
}

detailed_designer['sub'] = {}
# merge to ma = ma2 + mdef
accumulate = set()
for sub in detailed_designer['sub']:
    detailed_designer['sub'][sub]['ma'] = set(detailed_designer['sub'][sub]['ma']).union(set(detailed_designer['sub'][sub]['ma2'])).union(set(detailed_designer['sub'][sub]['mdef']))
    accumulate = accumulate.union(detailed_designer['sub'][sub]['ma'])
detailed_designer['ma'] = set(detailed_designer['ma']).union(set(detailed_designer['ma2'])).union(set(detailed_designer['mdef'])).union(accumulate)

# add mincl to mex
for sub_profession in detailed_designer['sub']:
    detailed_designer['sub'][sub_profession]['mex'] = set(detailed_designer['sub'][sub_profession]['mex']).union(set(detailed_designer['sub'][sub_profession]['mincl']))


print('\nDETAILED DESIGNER:')
for i in detailed_designer:
    if i in ['mex', 'mex2', 'ma', 'ma2', 'mdef', 'mincl']:
        print(f"{i}: {detailed_designer[i]}")
    else:
        print('sub: ')
        for j in detailed_designer[i]:
            print(f"   * {j}: {detailed_designer[i][j]}")

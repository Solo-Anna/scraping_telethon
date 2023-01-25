from patterns.pseudo_pattern.fake_pattern import pattern

sales_manager = {
    'ma': pattern['sales_manager']['ma'],
    'ma2': pattern['sales_manager']['ma2'],
    'mdef': pattern['sales_manager']['mdef'],
    'mex': pattern['sales_manager']['mex'],
    'mex2': pattern['sales_manager']['mex2'],
    'mincl': pattern['sales_manager']['mincl'],
}

sales_manager['sub'] = {}
# merge to ma = ma2 + mdef
accumulate = set()
for sub in sales_manager['sub']:
    sales_manager['sub'][sub]['ma'] = set(sales_manager['sub'][sub]['ma']).union(set(sales_manager['sub'][sub]['ma2'])).union(set(sales_manager['sub'][sub]['mdef']))
    accumulate = accumulate.union(sales_manager['sub'][sub]['ma'])
sales_manager['ma'] = set(sales_manager['ma']).union(set(sales_manager['ma2'])).union(set(sales_manager['mdef'])).union(accumulate)

# add mincl to mex
for sub_profession in sales_manager['sub']:
    sales_manager['sub'][sub_profession]['mex'] = set(sales_manager['sub'][sub_profession]['mex']).union(set(sales_manager['sub'][sub_profession]['mincl']))

# print(f"\n********************\n{backend}\n****************\n")

print('\nSALES MANAGER')
for i in sales_manager:
    if i in ['mex', 'mex2', 'ma', 'ma2', 'mdef', 'mincl']:
        print(f"{i}: {sales_manager[i]}")
    else:
        print('sub: ')
        for j in sales_manager[i]:
            print(f"   * {j}: {sales_manager[i][j]}")

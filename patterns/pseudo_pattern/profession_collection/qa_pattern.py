from patterns.pseudo_pattern.fake_pattern import pattern

qa = {
    'ma': set(pattern['qa']['ma']),
    'ma2': set(pattern['qa']['ma2']),
    'mdef': set(pattern['qa']['mdef']),
    'mex': set(pattern['qa']['mex']),
    'mex2': set(pattern['qa']['mex2']),
    'mincl': set(pattern['qa']['mincl']),
}

manual_qa = {
    'ma': set(pattern['qa']['sub']['manual_qa']['ma']),
    'ma2': set(pattern['qa']['sub']['manual_qa']['ma2']),
    'mdef': set(pattern['qa']['sub']['manual_qa']['mdef']),
    'mex': set(pattern['qa']['sub']['manual_qa']['mex']),
    'mex2': set(pattern['qa']['sub']['manual_qa']['mex2']),
    'mincl': set(pattern['qa']['sub']['manual_qa']['mincl']),
}

aqa = {
    'ma': pattern['qa']['sub']['aqa']['ma'],
    'ma2': pattern['qa']['sub']['aqa']['ma2'],
    'mdef': pattern['qa']['sub']['aqa']['mdef'],
    'mex': pattern['qa']['sub']['aqa']['mex'],
    'mex2': pattern['qa']['sub']['aqa']['mex2'],
    'mincl': pattern['qa']['sub']['aqa']['mincl'],
}

support = {
    'ma': pattern['qa']['sub']['support']['ma'],
    'ma2': pattern['qa']['sub']['support']['ma2'],
    'mdef': pattern['qa']['sub']['support']['mdef'],
    'mex': pattern['qa']['sub']['support']['mex'],
    'mex2': pattern['qa']['sub']['support']['mex2'],
    'mincl': pattern['qa']['sub']['support']['mincl'],
}

qa['ma'] = set(manual_qa['ma']).union(set(aqa['ma'])).union(set(support['ma']))

qa['sub'] = {
    'manual_qa': manual_qa,
    'aqa': aqa,
    'support': support,
}
# merge to ma = ma2 + mdef
accumulate = set()
for sub in qa['sub']:
    qa['sub'][sub]['ma'] = set(qa['sub'][sub]['ma']).union(set(qa['sub'][sub]['ma2'])).union(set(qa['sub'][sub]['mdef']))
    accumulate = accumulate.union(qa['sub'][sub]['ma'])
qa['ma'] = set(qa['ma']).union(set(qa['ma2'])).union(set(qa['mdef'])).union(accumulate)

# add mincl to mex
for sub_profession in qa['sub']:
    qa['sub'][sub_profession]['mex'] = set(qa['sub'][sub_profession]['mex']).union(set(qa['sub'][sub_profession]['mincl']))

# print(f"\n********************\n{backend}\n****************\n")

print('\nQA')
for i in qa:
    if i in ['mex', 'mex2', 'ma', 'ma2', 'mdef', 'mincl']:
        print(f"{i}: {qa[i]}")
    else:
        print('sub: ')
        for j in qa[i]:
            print(f"   * {j}: {qa[i][j]}")

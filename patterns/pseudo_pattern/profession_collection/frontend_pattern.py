from patterns.pseudo_pattern.fake_pattern import pattern

frontend = {
    'ma': pattern['frontend']['ma'],
    'ma2': pattern['frontend']['ma2'],
    'mdef': pattern['frontend']['mdef'],
    'mex': pattern['frontend']['mex'],
    'mex2': pattern['frontend']['mex2'],
    'mincl': pattern['frontend']['mincl'],
}

vue = {
    'ma': pattern['frontend']['sub']['vue']['ma'],
    'ma2': pattern['frontend']['sub']['vue']['ma2'],
    'mdef': pattern['frontend']['sub']['vue']['mdef'],
    'mex': pattern['frontend']['sub']['vue']['mex'],
    'mex2': pattern['frontend']['sub']['vue']['mex2'],
    'mincl': pattern['frontend']['sub']['vue']['mincl'],
}
# front3
vue['mex'] = set(vue['mex']).union(set(frontend['mex'])).union(set(vue['mex2']))

react = {
    'ma': pattern['frontend']['sub']['react']['ma'],
    'ma2': pattern['frontend']['sub']['react']['ma2'],
    'mdef': pattern['frontend']['sub']['react']['mdef'],
    'mex': pattern['frontend']['sub']['react']['mex'],
    'mex2': pattern['frontend']['sub']['react']['mex2'],
    'mincl': pattern['frontend']['sub']['react']['mincl'],
}
# front4
react['mex'] = set(react['mex']).union(set(frontend['mex'])).union(set(react['mex2']))

angular = {
    'ma': pattern['frontend']['sub']['angular']['ma'],
    'ma2': pattern['frontend']['sub']['angular']['ma2'],
    'mdef': pattern['frontend']['sub']['angular']['mdef'],
    'mex': pattern['frontend']['sub']['angular']['mex'],
    'mex2': pattern['frontend']['sub']['angular']['mex2'],
    'mincl': pattern['frontend']['sub']['angular']['mincl'],
}
# front5
angular['mex'] = set(angular['mex']).union(set(frontend['mex'])).union(set(angular['mex2']))

django = {
    'ma': pattern['frontend']['sub']['django']['ma'],
    'ma2': pattern['frontend']['sub']['django']['ma2'],
    'mdef': pattern['frontend']['sub']['django']['mdef'],
    'mex': pattern['frontend']['sub']['django']['mex'],
    'mex2': pattern['frontend']['sub']['django']['mex2'],
    'mincl': pattern['frontend']['sub']['django']['mincl'],
}
# front6
django['mex'] = set(django['mex']).union(set(frontend['mex'])).union(set(django['mex2']))

wordpress = {
    'ma': pattern['frontend']['sub']['wordpress']['ma'],
    'ma2': pattern['frontend']['sub']['wordpress']['ma2'],
    'mdef': pattern['frontend']['sub']['wordpress']['mdef'],
    'mex': pattern['frontend']['sub']['wordpress']['mex'],
    'mex2': pattern['frontend']['sub']['wordpress']['mex2'],
    'mincl': pattern['frontend']['sub']['wordpress']['mincl'],
}
# front7
wordpress['mex'] = set(wordpress['mex']).union(set(frontend['mex'])).union(set(wordpress['mex2']))

bitrix = {
    'ma': pattern['frontend']['sub']['bitrix']['ma'],
    'ma2': pattern['frontend']['sub']['bitrix']['ma2'],
    'mdef': pattern['frontend']['sub']['bitrix']['mdef'],
    'mex': pattern['frontend']['sub']['bitrix']['mex'],
    'mex2': pattern['frontend']['sub']['bitrix']['mex2'],
    'mincl': pattern['frontend']['sub']['bitrix']['mincl'],
}
# front8
bitrix['mex'] = set(bitrix['mex']).union(set(frontend['mex'])).union(set(bitrix['mex2']))

joomla = {
    'ma': pattern['frontend']['sub']['joomla']['ma'],
    'ma2': pattern['frontend']['sub']['joomla']['ma2'],
    'mdef': pattern['frontend']['sub']['joomla']['mdef'],
    'mex': pattern['frontend']['sub']['joomla']['mex'],
    'mex2': pattern['frontend']['sub']['joomla']['mex2'],
    'mincl': pattern['frontend']['sub']['joomla']['mincl'],
}
# front9
joomla['mex'] = set(joomla['mex']).union(set(frontend['mex'])).union(set(joomla['mex2']))

drupal = {
    'ma': pattern['frontend']['sub']['drupal']['ma'],
    'ma2': pattern['frontend']['sub']['drupal']['ma2'],
    'mdef': pattern['frontend']['sub']['drupal']['mdef'],
    'mex': pattern['frontend']['sub']['drupal']['mex'],
    'mex2': pattern['frontend']['sub']['drupal']['mex2'],
    'mincl': pattern['frontend']['sub']['drupal']['mincl'],
}
# front10
drupal['mex'] = set(drupal['mex']).union(set(frontend['mex'])).union(set(drupal['mex2']))

# front2
frontend['mex'] = set(frontend['mex']).union(set(vue['mex2'])).union(set(frontend['mex2']))

# front1
frontend['ma'] = set(frontend['ma']).union(set(vue['ma'])).union(set(frontend['ma2'])).union(set(react['ma'])).union(set(angular['ma'])).\
    union(set(django['ma'])).union(set(wordpress['ma'])).union(set(bitrix['ma'])).union(set(joomla['ma'])).\
    union(set(drupal['ma']))

frontend['sub'] = {
    'vue': vue,
    'react': react,
    'angular': angular,
    'django': django,
    'wordpress': wordpress,
    'bitrix': bitrix,
    'joomla': joomla,
    'drupal': drupal
}
# merge to ma = ma2 + mdef
accumulate = set()
for sub in frontend['sub']:
    frontend['sub'][sub]['ma'] = set(frontend['sub'][sub]['ma']).union(set(frontend['sub'][sub]['ma2'])).union(set(frontend['sub'][sub]['mdef']))
    accumulate = accumulate.union(frontend['sub'][sub]['ma'])
frontend['ma'] = set(frontend['ma']).union(set(frontend['ma2'])).union(set(frontend['mdef'])).union(accumulate)

# add mincl to mex
for sub_profession in frontend['sub']:
    frontend['sub'][sub_profession]['mex'] = set(frontend['sub'][sub_profession]['mex']).union(set(frontend['sub'][sub_profession]['mincl']))

# print(f"\n********************\n{frontend}\n****************\n")
print('\nFRONTEND:')
for i in frontend:
    if i in ['mex', 'mex2', 'ma', 'ma2', 'mdef', 'mincl']:
        print(f"{i}: {frontend[i]}")
    else:
        print('sub: ')
        for j in frontend[i]:
            print(f"   * {j}: {frontend[i][j]}")

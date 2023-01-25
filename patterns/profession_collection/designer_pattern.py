from patterns.data_pattern._data_pattern import pattern

designer = {
    'ma': pattern['designer']['ma'],
    'ma2': pattern['designer']['ma2'],
    'mdef': pattern['designer']['mdef'],
    'mex': pattern['designer']['mex'],
    'mex2': pattern['designer']['mex2'],
    'mincl': pattern['designer']['mincl'],
}

ui_ux = {
    'ma': pattern['designer']['sub']['ui_ux']['ma'],
    'ma2': pattern['designer']['sub']['ui_ux']['ma2'],
    'mdef': pattern['designer']['sub']['ui_ux']['mdef'],
    'mex': pattern['designer']['sub']['ui_ux']['mex'],
    'mex2': pattern['designer']['sub']['ui_ux']['mex2'],
    'mincl': pattern['designer']['sub']['ui_ux']['mincl'],
}
# designer1
ui_ux['mex'] = set(ui_ux['mex']).union(set(designer['mex'])).union(set(ui_ux['mex2']))

motion = {
    'ma': pattern['designer']['sub']['motion']['ma'],
    'ma2': pattern['designer']['sub']['motion']['ma2'],
    'mdef': pattern['designer']['sub']['motion']['mdef'],
    'mex': pattern['designer']['sub']['motion']['mex'],
    'mex2': pattern['designer']['sub']['motion']['mex2'],
    'mincl': pattern['designer']['sub']['motion']['mincl'],
}
# designer2
motion['mex'] = set(motion['mex']).union(set(designer['mex'])).union(set(motion['mex2']))

dd = {
    'ma': pattern['designer']['sub']['dd']['ma'],
    'ma2': pattern['designer']['sub']['dd']['ma2'],
    'mdef': pattern['designer']['sub']['dd']['mdef'],
    'mex': pattern['designer']['sub']['dd']['mex'],
    'mex2': pattern['designer']['sub']['dd']['mex2'],
    'mincl': pattern['designer']['sub']['dd']['mincl'],
}
# designer3
dd['mex'] = set(dd['mex']).union(set(designer['mex'])).union(set(dd['mex2']))

ddd = {
    'ma': pattern['designer']['sub']['ddd']['ma'],
    'ma2': pattern['designer']['sub']['ddd']['ma2'],
    'mdef': pattern['designer']['sub']['ddd']['mdef'],
    'mex': pattern['designer']['sub']['ddd']['mex'],
    'mex2': pattern['designer']['sub']['ddd']['mex2'],
    'mincl': pattern['designer']['sub']['ddd']['mincl'],
}
# designer4
ddd['mex'] = set(ddd['mex']).union(set(designer['mex'])).union(set(ddd['mex2']))

game_designer = {
    'ma': pattern['designer']['sub']['game_designer']['ma'],
    'ma2': pattern['designer']['sub']['game_designer']['ma2'],
    'mdef': pattern['designer']['sub']['game_designer']['mdef'],
    'mex': pattern['designer']['sub']['game_designer']['mex'],
    'mex2': pattern['designer']['sub']['game_designer']['mex2'],
    'mincl': pattern['designer']['sub']['game_designer']['mincl'],
}
# designer5
game_designer['mex'] = set(game_designer['mex']).union(set(designer['mex'])).union(set(game_designer['mex2']))

illustrator = {
    'ma': pattern['designer']['sub']['illustrator']['ma'],
    'ma2': pattern['designer']['sub']['illustrator']['ma2'],
    'mdef': pattern['designer']['sub']['illustrator']['mdef'],
    'mex': pattern['designer']['sub']['illustrator']['mex'],
    'mex2': pattern['designer']['sub']['illustrator']['mex2'],
    'mincl': pattern['designer']['sub']['illustrator']['mincl'],
}
# designer6
illustrator['mex'] = set(illustrator['mex']).union(set(designer['mex'])).union(set(illustrator['mex2']))

graphic = {
    'ma': pattern['designer']['sub']['graphic']['ma'],
    'ma2': pattern['designer']['sub']['graphic']['ma2'],
    'mdef': pattern['designer']['sub']['graphic']['mdef'],
    'mex': pattern['designer']['sub']['graphic']['mex'],
    'mex2': pattern['designer']['sub']['graphic']['mex2'],
    'mincl': pattern['designer']['sub']['graphic']['mincl'],
}
# designer7
graphic['mex'] = set(graphic['mex']).union(set(designer['mex'])).union(set(graphic['mex2']))

uxre_searcher = {
    'ma': pattern['designer']['sub']['uxre_searcher']['ma'],
    'ma2': pattern['designer']['sub']['uxre_searcher']['ma2'],
    'mdef': pattern['designer']['sub']['uxre_searcher']['mdef'],
    'mex': pattern['designer']['sub']['uxre_searcher']['mex'],
    'mex2': pattern['designer']['sub']['uxre_searcher']['mex2'],
    'mincl': pattern['designer']['sub']['uxre_searcher']['mincl'],
}
# designer8
uxre_searcher['mex'] = set(uxre_searcher['mex']).union(set(designer['mex'])).union(set(uxre_searcher['mex2']))

# designer['ma'] = set(ui_ux['ma']).union(set(motion['ma'])).union(set(dd['ma'])).union(set(ddd['ma']))\
#     .union(set(game_designer['ma'])).union(set(illustrator['ma'])).union(set(graphic['ma'])).\
#     union(set(uxre_searcher['ma']))

designer['sub'] = {
    'ui_ux': ui_ux,
    'motion': motion,
    'dd': dd,
    'ddd': ddd,
    'game_designer': game_designer,
    'illustrator': illustrator,
    'graphic': graphic,
    'uxre_searcher': uxre_searcher
}
# merge to ma = ma2 + mdef
accumulate = set()
for sub in designer['sub']:
    designer['sub'][sub]['ma'] = set(designer['sub'][sub]['ma']).union(set(designer['sub'][sub]['ma2'])).union(set(designer['sub'][sub]['mdef']))
    accumulate = accumulate.union(designer['sub'][sub]['ma'])
designer['ma'] = set(designer['ma']).union(set(designer['ma2'])).union(set(designer['mdef'])).union(accumulate)

# add mincl to mex
for sub_profession in designer['sub']:
    designer['sub'][sub_profession]['mex'] = set(designer['sub'][sub_profession]['mex']).union(set(designer['sub'][sub_profession]['mincl']))

# print(f"\n********************\n{backend}\n****************\n")

print('\nDESIGNER')
for i in designer:
    if i in ['mex', 'mex2', 'ma', 'ma2', 'mdef', 'mincl']:
        print(f"{i}: {designer[i]}")
    else:
        print('sub: ')
        for j in designer[i]:
            print(f"   * {j}: {designer[i][j]}")

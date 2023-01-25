from patterns.data_pattern._data_pattern import pattern
from patterns.pseudo_pattern.profession_collection.analyst_pattern import analyst

ba = analyst

print('\nDETAILED DESIGNER:')
for i in ba:
    if i in ['mex', 'mex2', 'ma', 'ma2', 'mdef', 'mincl']:
        print(f"{i}: {ba[i]}")
    else:
        print('sub: ')
        for j in ba[i]:
            print(f"   * {j}: {ba[i][j]}")


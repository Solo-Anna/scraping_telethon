from patterns.profession_collection.analyst_pattern import analyst
from patterns.profession_collection.ba_pattern import ba
from patterns.profession_collection.backend_pattern import backend
from patterns.profession_collection.designer_pattern import designer
from patterns.profession_collection.detailed_designer_pattern import detailed_designer
from patterns.profession_collection.dev_pattern import dev
from patterns.profession_collection.devops_pattern import devops
from patterns.profession_collection.frontend_pattern import frontend
from patterns.profession_collection.game_pattern import game
from patterns.profession_collection.junior_pattern import junior
from patterns.profession_collection.hr_pattern import hr
from patterns.profession_collection.marketing_pattern import marketing
from patterns.profession_collection.mobile_pattern import mobile
from patterns.profession_collection.non_code_manager import non_code_manager
from patterns.profession_collection.pm_pattern import pm
from patterns.profession_collection.qa_pattern import qa
from patterns.profession_collection.fullstack_pattern import fullstack
from patterns.profession_collection.sales_manager_pattern import sales_manager
from patterns.data_pattern._data_pattern import pattern
from patterns.data_pattern._data_pattern import params
from patterns.data_pattern._data_pattern import vacancy_pattern
from patterns.data_pattern._data_pattern import search_companies, search_companies2
from utils.additional_variables.additional_variables import valid_professions, valid_professions_extended

export_pattern = {
    'data': {
        'vacancy': pattern['vacancy'],
        'contacts': pattern['contacts'],
        },
    'professions': {
        'junior': junior,
        'analyst': analyst,
        'ba': ba,
        'backend': backend,
        'designer': designer,
        'devops': devops,
        'frontend': frontend,
        'game': game,
        'hr': hr,
        'marketing': marketing,
        'mobile': mobile,
        'pm': pm,
        'product': pm,
        'qa': qa,
        'sales_manager': sales_manager,
        'fullstack': fullstack,
    },
    'additional': {
        'dev': dev,
        'detailed_designer': detailed_designer,
        'non_code_manager': non_code_manager,
        'admins': pattern['admins'],
    },
    'others': {
        'remote': pattern['remote'],
        'relocate': pattern['relocate'],
        'english': {
            'ma': params['english_level']
        },
        'experience': {
            'ma': params['experience']
        },
        'english_for_shorts': {
            'ma': params['english_for_shorts']
        },
        'salary_for_shorts': {
            'ma': params['salary_for_shorts']
        },
        'city_for_shorts': {
            'ma': params['city_for_shorts']
        },
        'vacancy': {
            'ma': '',
            'mex': '',
            'sub': vacancy_pattern,
        },
        'company': {
            'ma': search_companies,
            'mex': '',
            'sub': ''
        },
        'company2': {
            'ma': search_companies2,
            'mex': '',
            'sub': ''
        }
    }
}

# ------------------------ common merges -------------------------------

# common1
export_pattern['additional']['dev']['mex'] = set(export_pattern['additional']['dev']['mex']).\
    union(set(export_pattern['professions']['backend']['ma'])).\
    union(set(export_pattern['professions']['backend']['sub']['python']['ma'])).\
    union(set(export_pattern['professions']['backend']['sub']['c']['ma'])).\
    union(set(export_pattern['professions']['backend']['sub']['php']['ma'])).\
    union(set(export_pattern['professions']['fullstack']['ma'])).\
    union(set(export_pattern['professions']['frontend']['ma'])).\
    union(set(export_pattern['additional']['admins']['ma']))

# common2
export_pattern['professions']['mobile']['mex'] = set(export_pattern['professions']['mobile']['mex']).\
    union(set(export_pattern['professions']['mobile']['mex2'])).\
    union(set(export_pattern['professions']['designer']['ma']))

# common4
export_pattern['professions']['designer']['mex'] = set(export_pattern['professions']['designer']['mex']).\
    union(set(export_pattern['additional']['dev']['mex'])).\
    union(set(export_pattern['professions']['mobile']['ma'])).\
    union(set(export_pattern['professions']['designer']['mex2'])).\
    union(set(export_pattern['professions']['qa']['mdef'])).\
    union(set(export_pattern['professions']['sales_manager']['ma'])).\
    union(set(export_pattern['professions']['marketing']['ma'])).\
    union(set(export_pattern['professions']['ba']['ma'])).\
    union(set(export_pattern['professions']['pm']['ma'])).\
    union(set(export_pattern['professions']['devops']['ma'])).\
    union(set(export_pattern['professions']['analyst']['ma'])).\
    union(set(export_pattern['professions']['hr']['mdef']))

# common5
export_pattern['professions']['designer']['mincl'] = set(export_pattern['professions']['designer']['mincl']).\
    union(set(export_pattern['professions']['designer']['mex'])).\
    union(set(export_pattern['additional']['detailed_designer']['ma']))

# common3
export_pattern['additional']['detailed_designer']['ma'] = set(export_pattern['additional']['detailed_designer']['ma']).\
    union(set(export_pattern['professions']['designer']['sub']['ui_ux']['ma'])).\
    union(set(export_pattern['professions']['designer']['sub']['motion']['ma'])).\
    union(set(export_pattern['professions']['designer']['sub']['dd']['ma'])).\
    union(set(export_pattern['professions']['designer']['sub']['ddd']['ma'])).\
    union(set(export_pattern['professions']['designer']['sub']['game_designer']['ma'])).\
    union(set(export_pattern['professions']['designer']['sub']['illustrator']['ma'])).\
    union(set(export_pattern['professions']['designer']['sub']['graphic']['ma'])).\
    union(set(export_pattern['professions']['designer']['sub']['uxre_searcher']['ma']))

# # common7
# export_pattern['professions']['analyst']['sub']['sys_analyst']['mex'] = set(export_pattern['professions']['analyst']['sub']['sys_analyst']['mex']).\
#         union(set(export_pattern['professions']['marketing']['mex'])).\
#         union(set(export_pattern['professions']['analyst']['sub']['sys_analyst']['mex2'])),
#
# # common8
# export_pattern['professions']['analyst']['sub']['data_analyst']['mex'] = set(export_pattern['professions']['analyst']['sub']['data_analyst']['mex']).\
#          union(set(export_pattern['professions']['marketing']['mex'])).\
#          union(set(export_pattern['professions']['analyst']['sub']['data_analyst']['mex2'])),
#
# # common9
# export_pattern['professions']['analyst']['sub']['data_scientist']['mex'] = set(export_pattern['professions']['analyst']['sub']['data_scientist']['mex']).\
#        union(set(export_pattern['professions']['marketing']['mex'])).\
#        union(set(export_pattern['professions']['analyst']['sub']['data_scientist']['mex2'])),
#
# # common10
# export_pattern['professions']['analyst']['sub']['ba']['mex'] = set(export_pattern['professions']['analyst']['sub']['ba']['mex']).\
#        union(set(export_pattern['professions']['marketing']['mex'])).\
#        union(set(export_pattern['professions']['analyst']['sub']['ba']['mex2'])),
#
# common11
a = export_pattern['professions']['qa']['sub']['manual_qa']['mex']
b = export_pattern['professions']['qa']['sub']['manual_qa']['mex2']
c = export_pattern['professions']['marketing']['mex']
export_pattern['professions']['qa']['sub']['manual_qa']['mex'] = set(a).union(set(b)).union(set(c))

# common12
a = export_pattern['professions']['qa']['sub']['aqa']['mex']
b = export_pattern['professions']['qa']['sub']['aqa']['mex2']
c = export_pattern['professions']['marketing']['mex']
export_pattern['professions']['qa']['sub']['aqa']['mex'] = set(a).union(set(b)).union(set(c))

accumulate = set()
for profession_mex in export_pattern['professions']:
    if profession_mex in valid_professions_extended:
        for profession_def in export_pattern['professions']:
            if profession_def in valid_professions_extended and profession_def != profession_mex and profession_def != 'junior':
                accumulate = accumulate.union(set(export_pattern['professions'][profession_def]['mdef']))
        accumulate = accumulate.union(set(export_pattern['professions'][profession_mex]['mex']))
        export_pattern['professions'][profession_mex]['mex'] = accumulate
        accumulate = set()

# # add to each sub from each profession mincl to mex
# for profession in export_pattern['professions']:
#     print('prof ', profession)
#     if profession in valid_professions:
#         for sub_profession in export_pattern['professions'][profession]['sub']:
#             print('sub ', sub_profession)
#             try:
#                 a = export_pattern['professions'][profession]['sub'][sub_profession]['mex']
#                 b = export_pattern['professions'][profession]['sub'][sub_profession]['mincl']
#                 export_pattern['professions'][profession]['sub'][sub_profession]['mex'] = set(a).union(set(b))
#             except Exception as e:
#                 print('WTF', e)
# # # from qa
# export_pattern['professions']['qa']['sub']['manual_qa']['mex'] = set(export_pattern['professions']['marketing']['mex']).union(set(export_pattern['professions']['qa']['sub']['manual_qa']['mex2']))
# export_pattern['professions']['qa']['sub']['aqa']['mex'] = set(export_pattern['professions']['marketing']['mex']).union(set(export_pattern['professions']['qa']['sub']['aqa']['mex2']))
#
# # from backend
# export_pattern['additional']['dev']['mex']=set(export_pattern['professions']['backend']['ma']).union(set(export_pattern['professions']['backend']['sub']['python']['ma']))\
#     .union(set(export_pattern['professions']['backend']['sub']['c']['ma'])).union(set(export_pattern['professions']['backend']['sub']['php']['ma']))\
#     .union(set(export_pattern['professions']['fullstack']['ma'])).union(set(export_pattern['professions']['frontend']['ma'])).union(set(export_pattern['additional']['admins']['ma']))
#
# # from designer
# # ??????????
# export_pattern['professions']['designer']['mex']=set(export_pattern['additional']['dev']['mex']).union(set(export_pattern['professions']['mobile']['ma'])).union(set(export_pattern['professions']['designer']['mex2']))\
#     .union(set(export_pattern['professions']['qa']['mdef'])).union(set(export_pattern['professions']['sales_manager']['ma'])).union(set(export_pattern['professions']['marketing']['ma']))\
#     .union(set(export_pattern['professions']['ba']['ma'])).union(set(export_pattern['professions']['pm']['ma'])).union(set(export_pattern['professions']['devops']['ma']))\
#     .union(set(export_pattern['professions']['analyst']['ma'])).union(set(export_pattern['professions']['hr']['mdef']))
#
# # from detailed_designer
# detailed_designer['ma'] = set(export_pattern['professions']['designer']['sub']['ui_ux']['ma']).union(set(export_pattern['professions']['designer']['sub']['motion']['ma']))\
#     .union(set(export_pattern['professions']['designer']['sub']['dd']['ma'])).union(set(export_pattern['professions']['designer']['sub']['ddd']['ma']))\
#     .union(set(export_pattern['professions']['designer']['sub']['game_designer']['ma'])).union(set(export_pattern['professions']['designer']['sub']['illustrator']['ma']))\
#     .union(set(export_pattern['professions']['designer']['sub']['graphic']['ma'])).union(set(export_pattern['professions']['designer']['sub']['uxre_searcher']['ma']))
#
# # ??????????
# export_pattern['professions']['designer']['mincl']=set(export_pattern['professions']['designer']['mex']).union(set(export_pattern['additional']['detailed_designer']['ma']))
#
# # from analyst
# # print('!!!!!', type(export_pattern['professions']['analyst']['sub']['sys_analyst']['mex']))
# # print('!!!!!', type(export_pattern['professions']['marketing']['mex']))
# # print('!!!!!', type(export_pattern['professions']['analyst']['sub']['sys_analyst']['mex2']))
#
# a = export_pattern['professions']['analyst']['sub']['sys_analyst']['mex']
# b = export_pattern['professions']['marketing']['mex']
# c = export_pattern['professions']['analyst']['sub']['sys_analyst']['mex2']
# export_pattern['professions']['analyst']['sub']['sys_analyst']['mex'] = set(a).union(set(b)).union(set(c))
# # export_pattern['professions']['analyst']['sub']['sys_analyst']['mex'] = export_pattern['professions']['analyst']['sub']['sys_analyst']['mex'].union(export_pattern['professions']['marketing']['mex']).union(export_pattern['professions']['analyst']['sub']['sys_analyst']['mex2']),
#
# a = export_pattern['professions']['analyst']['sub']['data_analyst']['mex']
# c = export_pattern['professions']['analyst']['sub']['data_analyst']['mex2']
# export_pattern['professions']['analyst']['sub']['data_analyst']['mex'] = set(a).union(set(b)).union(set(c))
# # export_pattern['professions']['analyst']['sub']['data_analyst']['mex']=set(export_pattern['professions']['marketing']['mex']).union(set(export_pattern['professions']['analyst']['sub']['data_analyst']['mex2'])),
#
# a = export_pattern['professions']['analyst']['sub']['data_scientist']['mex']
# c = export_pattern['professions']['analyst']['sub']['data_scientist']['mex2']
# export_pattern['professions']['analyst']['sub']['data_scientist']['mex'] = set(a).union(set(b)).union(set(c))
# # export_pattern['professions']['analyst']['sub']['data_scientist']['mex']=set(export_pattern['professions']['marketing']['mex']).union(set(export_pattern['professions']['analyst']['sub']['data_scientist']['mex2'])),
#
# a = export_pattern['professions']['analyst']['sub']['ba']['mex']
# c = export_pattern['professions']['analyst']['sub']['ba']['mex2']
# export_pattern['professions']['analyst']['sub']['ba']['mex'] = set(a).union(set(b)).union(set(c))
# # export_pattern['professions']['analyst']['sub']['ba']['mex']=set(export_pattern['professions']['marketing']['mex']).union(set(export_pattern['professions']['analyst']['sub']['ba']['mex2'])),
#
# # from mobile
#
# # from frontend
#
#
# # from game
#
# # from hr
#
# #from marketing
#
# # from pm
# # from sales_manager
# # from dev
#
# #-------------------------------------------------
# # for prof in variable.valid_professions:
# #     export_pattern['professions']['junior']['sub'][prof] = export_pattern['professions'][prof]['ma']
#
# # from helper_functions import helper_functions as helper
# # helper.get_pattern(variable.pattern_path)
#



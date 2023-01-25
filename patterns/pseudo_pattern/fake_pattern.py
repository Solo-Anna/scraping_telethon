pattern = {

    'vacancy': {
        'ma': ("vacancy.ma", ),
        'ma2': ("vacancy.ma2", ),
        'mdef': ("vacancy.mdef", ),

        'mex': ("vacancy.mex", ),
        'mex2': ("vacancy.mex2", ),
        'mincl': ("vacancy.mincl", ),
    },

    'contacts': {
        'ma': ("contacts.ma", ),
        'ma2': ("contacts.ma2", ),
        'mdef': ("contacts.mdef", ),

        'mex': ("contacts.mex", ),
        'mex2': ("contacts.mex2", ),
        'mincl': ("contacts.mincl", ),
    },

    'fullstack': {
        'ma': ("fullstack.ma", ),
        'ma2': ("fullstack.ma2", ),
        'mdef': ("fullstack.mdef", ),

        'mex': ("fullstack.mex", ),
        'mex2': ("fullstack.mex2", ),
        'mincl': ("fullstack.mincl", ),
    },

    'frontend': {
        'ma': ("frontend.ma", ),
        'ma2': ("frontend.ma2", ),
        'mdef': ("frontend.mdef", ),
        # pattern['frontend']['ma']=set(pattern['Vue']['ma']).union(set(pattern['frontend']['ma2'])).union(set(pattern['React']['ma'])).union(set(pattern['Angular']['ma'])).union(set(pattern['Django']['ma'])).union(set(pattern['Wordpress']['ma'])).union(set(pattern['Bitrix']['ma'])).union(set(pattern['Joomla']['ma'])).union(set(pattern['Drupal']['ma']))

        'mex': ("frontend.mex", ),
        'mex2': ("frontend.mex2", ),
        'mincl': ("frontend.mincl", ),

        # pattern['frontend']['mex']=set(pattern['Vue']['mex2']).union(set(pattern['frontend']['mex2']))

        'sub': {

            'vue': {

                'ma': ("frontend.vue.ma",),
                'ma2': ("frontend.vue.ma2",),
                'mdef': ("frontend.vue.mdef",),
                'mex': ("frontend.vue.mex",),
                'mex2': ("frontend.vue.mex2",),
                'mincl': ("frontend.vue.mincl",),

                # pattern['Vue']['mex']=set(pattern['frontend']['mex']).union(set(pattern['Vue']['mex2']))
            },

            'react': {
                'ma': ("frontend.react.ma",),
                'ma2': ("frontend.react.ma2",),
                'mdef': ("frontend.react.mdef",),
                'mex': ("frontend.react.mex",),
                'mex2': ("frontend.react.mex2",),
                'mincl': ("frontend.react.mincl",),

                # pattern['React']['mex']=set(pattern['frontend']['mex']).union(set(pattern['React']['mex2']))
            },

            'angular': {

                'ma': ("frontend.angular.ma",),
                'ma2': ("frontend.angular.ma2",),
                'mdef': ("frontend.angular.mdef",),
                'mex': ("frontend.angular.mex",),
                'mex2': ("frontend.angular.mex2",),
                'mincl': ("frontend.angular.mincl",),

                # pattern['Angular']['mex']=set(pattern['frontend']['mex']).union(set(pattern['Angular']['mex2']))
            },

            'django': {

                'ma': ("frontend.django.ma",),
                'ma2': ("frontend.django.ma2",),
                'mdef': ("frontend.django.mdef",),
                'mex': ("frontend.django.mex",),
                'mex2': ("frontend.django.mex2",),
                'mincl': ("frontend.django.mincl",),
                # pattern['Django']['mex']=set(pattern['frontend']['mex']).union(set(pattern['Django']['mex2']))
            },

            'wordpress': {

                'ma': ("frontend.wordpress.ma",),
                'ma2': ("frontend.wordpress.ma2",),
                'mdef': ("frontend.wordpress.mdef",),
                'mex': ("frontend.wordpress.mex",),
                'mex2': ("frontend.wordpress.mex2",),
                'mincl': ("frontend.wordpress.mincl",),

                # pattern['Wordpress']['mex']=set(pattern['frontend']['mex']).union(set(pattern['Wordpress']['mex2']))
            },

            'bitrix': {

                'ma': ("frontend.bitrix.ma",),
                'ma2': ("frontend.bitrix.ma2",),
                'mdef': ("frontend.bitrix.mdef",),
                'mex': ("frontend.bitrix.mex",),
                'mex2': ("frontend.bitrix.mex2",),
                'mincl': ("frontend.bitrix.mincl",),
                # pattern['Bitrix']['mex']=set(pattern['frontend']['mex']).union(set(pattern['Bitrix']['mex2']))
            },

            'joomla': {

                'ma': ("frontend.joomla.ma",),
                'ma2': ("frontend.joomla.ma2",),
                'mdef': ("frontend.joomla.mdef",),
                'mex': ("frontend.joomla.mex",),
                'mex2': ("frontend.joomla.mex2",),
                'mincl': ("frontend.joomla.mincl",),

                # pattern['Joomla']['mex']=set(pattern['frontend']['mex']).union(set(pattern['Joomla']['mex2']))
            },

            'drupal': {

                'ma': ("frontend.drupal.ma",),
                'ma2': ("frontend.drupal.ma2",),
                'mdef': ("frontend.drupal.mdef",),
                'mex': ("frontend.drupal.mex",),
                'mex2': ("frontend.drupal.mex2",),
                'mincl': ("frontend.drupal.mincl",),

                # pattern['Drupal']['mex']=set(pattern['frontend']['mex']).union(set(pattern['Drupal']['mex2']))
            },
        }
    },

    'backend': {

        'ma': ("backend.ma",),
        'ma2': ("backend.ma2",),
        # pattern['backend']['ma']=set(pattern['python']['ma']).union(set(pattern['C']['ma'])).union(set(pattern['PHP']['ma'])).union(set(pattern['Java']['ma'])).union(set(pattern['Ruby']['ma'])).union(set(pattern['Scala']['ma'])).union(set(pattern['.NET']['ma'])).union(set(pattern['NodeJS']['ma'])).union(set(pattern['Laravel']['ma'])).union(set(pattern['Golang']['ma'])).union(set(pattern['Delphi']['ma'])).union(set(pattern['ABAP']['ma'])).union(set(pattern['ML']['ma'])).union(set(pattern['DataEngineer']['ma']))
        'mdef': ("backend.mdef",),
        'mex': ("backend.mex",),
        'mex2': ("backend.mex2",),
        'mincl': ("backend.mincl",),

        'sub': {

            'python': {

                'ma': ("backend.python.ma",),
                'ma2': ("backend.python.ma2",),
                'mdef': ("backend.python.mdef",),
                'mex': ("backend.python.mex",),
                'mex2': ("backend.python.mex2",),
                'mincl': ("backend.python.mincl",),
                # pattern['python']['mex']=set(pattern['backend']['mex']).union(set(pattern['python']['mex2']))
            },

            'c': {

                'ma': ("backend.c.ma",),
                'ma2': ("backend.c.ma2",),
                'mdef': ("backend.c.mdef",),
                'mex': ("backend.c.mex",),
                'mex2': ("backend.c.mex2",),
                'mincl': ("backend.c.mincl",),
                # pattern['С']['mex']=set(pattern['backend']['mex']).union(set(pattern['С']['mex2']))
            },

            'php': {

                'ma': ("backend.php.ma",),
                'ma2': ("backend.php.ma2",),
                'mdef': ("backend.php.mdef",),
                'mex': ("backend.php.mex",),
                'mex2': ("backend.php.mex2",),
                'mincl': ("backend.php.mincl",),

                # pattern['PHP']['mex']=set(pattern['PHP']['mex']).union(set(pattern['PHP']['mex2']))
            },

            'java': {

                'ma': ("backend.java.ma",),
                'ma2': ("backend.java.ma2",),
                'mdef': ("backend.java.mdef",),
                'mex': ("backend.java.mex",),
                'mex2': ("backend.java.mex2",),
                'mincl': ("backend.java.mincl",),
                # pattern['Java']['mex']=set(pattern['backend']['mex']).union(set(pattern['Java']['mex2']))
            },

            'ruby': {

                'ma': ("backend.ruby.ma",),
                'ma2': ("backend.ruby.ma2",),
                'mdef': ("backend.ruby.mdef",),
                'mex': ("backend.ruby.mex",),
                'mex2': ("backend.ruby.mex2",),
                'mincl': ("backend.ruby.mincl",),

                # pattern['Ruby']['mex']=set(pattern['backend']['mex']).union(set(pattern['Ruby']['mex2']))
            },

            'scala': {
                'ma': ("backend.scala.ma",),
                'ma2': ("backend.scala.ma2",),
                'mdef': ("backend.scala.mdef",),
                'mex': ("backend.scala.mex",),
                'mex2': ("backend.scala.mex2",),
                'mincl': ("backend.scala.mincl",),
                # pattern['Scala']['mex']=set(pattern['backend']['mex']).union(set(pattern['Scala']['mex2']))
            },

            'net': {
                'ma': ("backend.net.ma",),
                'ma2': ("backend.net.ma2",),
                'mdef': ("backend.net.mdef",),
                'mex': ("backend.net.mex",),
                'mex2': ("backend.net.mex2",),
                'mincl': ("backend.net.mincl",),
                # pattern[' .NET']['mex']=set(pattern['backend']['mex']).union(set(pattern[' .NET']['mex2']))
            },

            'nodejs': {
                'ma': ("backend.nodejs.ma",),
                'ma2': ("backend.nodejs.ma2",),
                'mdef': ("backend.nodejs.mdef",),
                'mex': ("backend.nodejs.mex",),
                'mex2': ("backend.nodejs.mex2",),
                'mincl': ("backend.nodejs.mincl",),
                # pattern['NodeJS']['mex']=set(pattern['backend']['mex']).union(set(pattern['NodeJS']['mex2']))
            },

            'laravel': {
                'ma': ("backend.laravel.ma",),
                'ma2': ("backend.laravel.ma2",),
                'mdef': ("backend.laravel.mdef",),
                'mex': ("backend.laravel.mex",),
                'mex2': ("backend.laravel.mex2",),
                'mincl': ("backend.laravel.mincl",),
                # pattern['Laravel']['mex']=set(pattern['backend']['mex']).union(set(pattern['Laravel']['mex2']))
            },

            'golang': {
                'ma': ("backend.golang.ma",),
                'ma2': ("backend.golang.ma2",),
                'mdef': ("backend.golang.mdef",),
                'mex': ("backend.golang.mex",),
                'mex2': ("backend.golang.mex2",),
                'mincl': ("backend.golang.mincl",),
                # pattern['Golang']['mex']=set(pattern['backend']['mex']).union(set(pattern['Golang']['mex2']))
            },

            'delphi': {
                'ma': ("backend.delphi.ma",),
                'ma2': ("backend.delphi.ma2",),
                'mdef': ("backend.delphi.mdef",),
                'mex': ("backend.delphi.mex",),
                'mex2': ("backend.delphi.mex2",),
                'mincl': ("backend.delphi.mincl",),
                # pattern['Delphi']['mex']=set(pattern['backend']['mex']).union(set(pattern['Delphi']['mex2']))
            },

            'abap': {
                'ma': ("backend.abap.ma",),
                'ma2': ("backend.abap.ma2",),
                'mdef': ("backend.abap.mdef",),
                'mex': ("backend.abap.mex",),
                'mex2': ("backend.abap.mex2",),
                'mincl': ("backend.abap.mincl",),
                # pattern['ABAP']['mex']=set(pattern['backend']['mex']).union(set(pattern['ABAP']['mex2']))
            },

            'ml': {
                'ma': ("backend.ml.ma",),
                'ma2': ("backend.ml.ma2",),
                'mdef': ("backend.ml.mdef",),
                'mex': ("backend.ml.mex",),
                'mex2': ("backend.ml.mex2",),
                'mincl': ("backend.ml.mincl",),
                # pattern['ML']['mex']=set(pattern['backend']['mex']).union(set(pattern['ML']['mex2']))
            },

            'data_engineer': {
                'ma': ("backend.data_engineer.ma",),
                'ma2': ("backend.data_engineer.ma2",),
                'mdef': ("backend.data_engineer.mdef",),
                'mex': ("backend.data_engineer.mex",),
                'mex2': ("backend.data_engineer.mex2",),
                'mincl': ("backend.data_engineer.mincl",),

                # pattern['DataEngineer']['mex']=set(pattern['backend']['mex']).union(set(pattern['DataEngineer']['mex2']))
            },

            'unity': {
                'ma': ("backend.unity.ma",),
                'ma2': ("backend.unity.ma2",),
                'mdef': ("backend.unity.mdef",),
                'mex': ("backend.unity.mex",),
                'mex2': ("backend.unity.mex2",),
                'mincl': ("backend.unity.mincl",),
                # pattern['Unity']['mex']=set(pattern['backend']['mex']).union(set(pattern['Unity']['mex2']))
            },

            'one_c': {
                'ma': ("backend.one_c.ma",),
                'ma2': ("backend.one_c.ma2",),
                'mdef': ("backend.one_c.mdef",),
                'mex': ("backend.one_c.mex",),
                'mex2': ("backend.one_c.mex2",),
                'mincl': ("backend.one_c.mincl",),
                # pattern['1C']['mex']=set(pattern['backend']['mex']).union(set(pattern['1C']['mex2']))
            },

            'embedded': {
                'ma': ("backend.embedded.ma",),
                'ma2': ("backend.embedded.ma2",),
                'mdef': ("backend.embedded.mdef",),
                'mex': ("backend.embedded.mex",),
                'mex2': ("backend.embedded.mex2",),
                'mincl': ("backend.embedded.mincl",),
                # pattern['Embedded']['mex']=set(pattern['backend']['mex']).union(set(pattern['Embedded']['mex2']))
            }
        }
    },

    #     pattern['DEV']['mex']=set(pattern['backend']['ma']).union(set(pattern['python']['ma'])).union(set(pattern['C']['ma'])).union(set(pattern['PHP']['ma'])).union(set(pattern['fullstack']['ma'])).union(set(pattern['frontend']['ma'])).union(set(pattern['Admins']['ma']))
    #
    'admins': {
        'ma': ("admins.ma",),
        'ma2': ("admins.ma2",),
        'mdef': ("admins.mdef",),
        'mex': ("admins.mex",),
        'mex2': ("admins.mex2",),
        'mincl': ("admins.mincl",),
    },

    'mobile': {
        'ma': ("mobile.ma",),
        'ma2': ("mobile.ma2",),
        'mdef': ("mobile.mdef",),
        'mex': ("mobile.mex",),
        'mex2': ("mobile.mex2",),
        'mincl': ("mobile.mincl",),

        'sub': {

            # pattern['mobile']['ma']=set(pattern['mobile']['ma2']).union(set(pattern['mobile']['mdef']))
            # !! pattern['mobile']['mex']=set(pattern['mobile']['mex2']).union(set(pattern['designer']['ma']))

            'ios': {
                'ma': ("mobile.ios.ma",),
                'ma2': ("mobile.ios.ma2",),
                'mdef': ("mobile.ios.mdef",),
                'mex': ("mobile.ios.mex",),
                'mex2': ("mobile.ios.mex2",),
                'mincl': ("mobile.ios.mincl",),
                # pattern['iOs']['mex']=set(pattern['mobile']['mex']).union(set(pattern['iOs']['mex2']))
            },

            'android': {
                'ma': ("mobile.android.ma",),
                'ma2': ("mobile.android.ma2",),
                'mdef': ("mobile.android.mdef",),
                'mex': ("mobile.android.mex",),
                'mex2': ("mobile.android.mex2",),
                'mincl': ("mobile.android.mincl",),
                # pattern['Android']['mex']=set(pattern['mobile']['mex']).union(set(pattern['Android']['mex2']))
            },

            'cross_mobile': {
                'ma': ("mobile.cross_mobile.ma",),
                'ma2': ("mobile.cross_mobile.ma2",),
                'mdef': ("mobile.cross_mobile.mdef",),
                'mex': ("mobile.cross_mobile.mex",),
                'mex2': ("mobile.cross_mobile.mex2",),
                'mincl': ("mobile.cross_mobile.mincl",),
                # pattern['CrossMobile']['mex']=set(pattern['mobile']['mex']).union(set(pattern['CrossMobile']['mex2']))
                # pattern['CrossMobile']['ma']=set(pattern['CrossMobile']['ma2']).union(set(pattern['Flutter']['ma'])).union(set(pattern['ReactNative']['ma']))
            },

            'flutter': {
                'ma': ("mobile.flutter.ma",),
                'ma2': ("mobile.flutter.ma2",),
                'mdef': ("mobile.flutter.mdef",),
                'mex': ("mobile.flutter.mex",),
                'mex2': ("mobile.flutter.mex2",),
                'mincl': ("mobile.flutter.mincl",),
                # pattern['Flutter']['mex']=set(pattern['mobile']['mex']).union(set(pattern['Flutter']['mex2']))
            },

            'react_native': {
                'ma': ("mobile.react_native.ma",),
                'ma2': ("mobile.react_native.ma2",),
                'mdef': ("mobile.react_native.mdef",),
                'mex': ("mobile.react_native.mex",),
                'mex2': ("mobile.react_native.mex2",),
                'mincl': ("mobile.react_native.mincl",),
                # pattern['ReactNative']['mex']=set(pattern['mobile']['mex']).union(set(pattern['ReactNative']['mex2']))
            }
        }
    },
    #     #capitalize
    'pm': {
        'ma': ("pm.ma",),
        'ma2': ("pm.ma2",),
        'mdef': ("pm.mdef",),
        'mex': ("pm.mex",),
        'mex2': ("pm.mex2",),
        'mincl': ("pm.mincl",),
        # pattern['pm']['ma']=set(pattern['project']['mdef']).union(set(pattern['pm']['mincl'])).union(set(pattern['product']['mdef']))

        'sub': {
            'project': {
                'ma': ("pm.project.ma",),
                'ma2': ("pm.project.ma2",),
                'mdef': ("pm.project.mdef",),
                'mex': ("pm.project.mex",),
                'mex2': ("pm.project.mex2",),
                'mincl': ("pm.project.mincl",),
            },

            'product': {
                'ma': ("pm.product.ma",),
                'ma2': ("pm.product.ma2",),
                'mdef': ("pm.product.mdef",),
                'mex': ("pm.product.mex",),
                'mex2': ("pm.product.mex2",),
                'mincl': ("pm.product.mincl",),
            }
        }
    },

    #     #capitalize
    'game': {
        'ma': ("game.ma",),
        'ma2': ("game.ma2",),
        'mdef': ("game.mdef",),
        'mex': ("game.mex",),
        'mex2': ("game.mex2",),
        'mincl': ("game.mincl",),
    },

    #     # capitalize
    'designer': {
        'ma': ("designer.ma",),
        'ma2': ("designer.ma2",),
        'mdef': ("designer.mdef",),
        'mex': ("designer.mex",),
        'mex2': ("designer.mex2",),
        'mincl': ("designer.mincl",),
        # pattern['designer']['mex']=set(pattern['DEV']['mex']).union(set(pattern['mobile']['ma'])).union(set(pattern['designer']['mex2'])).union(set(pattern['qa']['mdef'])).union(set(pattern['sales_manager']['ma'])).union(set(pattern['marketing']['ma'])).union(set(pattern['ba']['ma'])).union(set(pattern['pm']['ma'])).union(set(pattern['devops']['ma'])).union(set(pattern['analyst']['ma'])).union(set(pattern['hr']['mdef']))
        # pattern['designer']['mexfinal']=set(pattern['designer']['mex']).union(set(pattern['DetailedDesigners']['ma']))
        'sub': {
            'ui_ux': {
                'ma': ("designer.ui_ux.ma",),
                'ma2': ("designer.ui_ux.ma2",),
                'mdef': ("designer.ui_ux.mdef",),
                'mex': ("designer.ui_ux.mex",),
                'mex2': ("designer.ui_ux.mex2",),
                'mincl': ("designer.ui_ux.mincl",),
                # pattern['UX/UI']['mex']=set(pattern['designer']['mex']).union(set(pattern['UX/UI']['mex2'])),
            },

            'motion': {
                'ma': ("designer.motion.ma",),
                'ma2': ("designer.motion.ma2",),
                'mdef': ("designer.motion.mdef",),
                'mex': ("designer.motion.mex",),
                'mex2': ("designer.motion.mex2",),
                'mincl': ("designer.motion.mincl",),
                # pattern['Motion']['mex']=set(pattern['designer']['mex']).union(set(pattern['Motion']['mex2'])),
            },

            'dd': {
                'ma': ("designer.dd.ma",),
                'ma2': ("designer.dd.ma2",),
                'mdef': ("designer.dd.mdef",),
                'mex': ("designer.dd.mex",),
                'mex2': ("designer.dd.mex2",),
                'mincl': ("designer.dd.mincl",),
                # pattern['2D']['mex']=set(pattern['designer']['mex']).union(set(pattern['2D']['mex2'])),
            },

            'ddd': {
                'ma': ("designer.ddd.ma",),
                'ma2': ("designer.ddd.ma2",),
                'mdef': ("designer.ddd.mdef",),
                'mex': ("designer.ddd.mex",),
                'mex2': ("designer.ddd.mex2",),
                'mincl': ("designer.ddd.mincl",),
                # pattern['3D']['mex']=set(pattern['designer']['mex']).union(set(pattern['3D']['mex2'])),
            },

            'game_designer': {
                'ma': ("designer.game_designer.ma",),
                'ma2': ("designer.game_designer.ma2",),
                'mdef': ("designer.game_designer.mdef",),
                'mex': ("designer.game_designer.mex",),
                'mex2': ("designer.game_designer.mex2",),
                'mincl': ("designer.game_designer.mincl",),

                # pattern['GameDesigner']['mex']=set(pattern['designer']['mex']).union(set(pattern['GameDesigner']['mex2'])),
            },

            'illustrator': {
                'ma': ("designer.illustrator.ma",),
                'ma2': ("designer.illustrator.ma2",),
                'mdef': ("designer.illustrator.mdef",),
                'mex': ("designer.illustrator.mex",),
                'mex2': ("designer.illustrator.mex2",),
                'mincl': ("designer.illustrator.mincl",),
                # pattern['illustrator'][illustrator]=set(pattern['designer']['mex']).union(set(pattern['illustrator']['mex2'])),
            },

            'graphic': {
                'ma': ("designer.graphic.ma",),
                'ma2': ("designer.graphic.ma2",),
                'mdef': ("designer.graphic.mdef",),
                'mex': ("designer.graphic.mex",),
                'mex2': ("designer.graphic.mex2",),
                'mincl': ("designer.graphic.mincl",),
                # pattern['Graphic']['mex']=set(pattern['designer']['mex']).union(set(pattern['Graphic']['mex2'])),
            },

            'uxre_searcher': {
                'ma': ("designer.uxre_searcher.ma",),
                'ma2': ("designer.uxre_searcher.ma2",),
                'mdef': ("designer.uxre_searcher.mdef",),
                'mex': ("designer.uxre_searcher.mex",),
                'mex2': ("designer.uxre_searcher.mex2",),
                'mincl': ("designer.uxre_searcher.mincl",),
                # pattern['UXREsearcher']['mex']=set(pattern['designer']['mex']).union(set(pattern['UXREsearcher']['mex2'])),
            }
        }
        # pattern['DetailedDesigners']['ma']=set(pattern['UX/UI']['ma']).union(set(pattern['Motion']['ma']))
        # .union(set(pattern['2D']['ma'])).union(set(pattern['3D']['ma'])).union(set(pattern['GameDesigner']['ma']))
        # .union(set(pattern['illustrator']['ma'])).union(set(pattern['Graphic']['ma']))
        # .union(set(pattern['UXREsearcher']['ma']))

    },

    #     # capitalize
    'hr': {
        'ma': ("hr.ma",),
        'ma2': ("hr.ma2",),
        'mdef': ("hr.mdef",),
        'mex': ("hr.mex",),
        'mex2': ("hr.mex2",),
        'mincl': ("hr.mincl",),
    },
    #
    #     # capitalize
    'analyst': {
        'ma': {"analyst.ma"},
        'ma2': {"analyst.ma2"},
        'mdef': {"analyst.mdef"},
        'mex': {"analyst.mex"},
        'mex2': {"analyst.mex2"},
        'mincl': {"analyst.mincl"},

        'sub': {
            'sys_analyst': {
                'ma': {"analyst.sys_analyst.ma"},
                'ma2': {"analyst.sys_analyst.ma2"},
                'mdef': {"analyst.sys_analyst.mdef"},
                'mex': {"analyst.sys_analyst.mex"},
                'mex2': {"analyst.sys_analyst.mex2"},
                'mincl': {"analyst.sys_analyst.mincl"},
                # pattern['SysAnal']['mex']=set(pattern['marketing']['mex']).union(set(pattern['SysAnal']['mex2'])),
            },

            'data_analyst': {
                'ma': ("analyst.data_analyst.ma",),
                'ma2': ("analyst.data_analyst.ma2",),
                'mdef': ("analyst.data_analyst.mdef",),
                'mex': ("analyst.data_analyst.mex",),
                'mex2': ("analyst.data_analyst.mex2",),
                'mincl': ("analyst.data_analyst.mincl",),
                # pattern['DataAnal']['mex']=set(pattern['marketing']['mex']).union(set(pattern['DataAnal']['mex2'])),
            },

            'data_scientist': {
                'ma': ("analyst.data_scientist.ma",),
                'ma2': ("analyst.data_scientist.ma2",),
                'mdef': ("analyst.data_scientist.mdef",),
                'mex': ("analyst.data_scientist.mex",),
                'mex2': ("analyst.data_scientist.mex2",),
                'mincl': ("analyst.data_scientist.mincl",),
                # pattern['DataScientist']['mex']=set(pattern['marketing']['mex']).union(set(pattern['DataScientist']['mex2'])),
            },

            'ba': {
                'ma': ("analyst.ba.ma",),
                'ma2': ("analyst.ba.ma2",),
                'mdef': ("analyst.ba.mdef",),
                'mex': ("analyst.ba.mex",),
                'mex2': ("analyst.ba.mex2",),
                'mincl': ("analyst.ba.mincl",),
                # pattern['BA']['mex']=set(pattern['marketing']['mex']).union(set(pattern['BA']['mex2'])),
            },
        }
    },

    #     # capitalize
    'qa': {
        'ma': ("qa.ma",),
        'ma2': ("qa.ma2",),
        'mdef': ("qa.mdef",),
        'mex': ("qa.mex",),
        'mex2': ("qa.mex2",),
        'mincl': ("qa.mincl",),

        'sub': {
            'manual_qa': {
                'ma': ("qa.manual_qa.ma",),
                'ma2': ("qa.manual_qa.ma2",),
                'mdef': ("qa.manual_qa.mdef",),
                'mex': ("qa.manual_qa.mex",),
                'mex2': ("qa.manual_qa.mex2",),
                'mincl': ("qa.manual_qa.mincl",),
                # pattern['ManualQA']['mex']=set(pattern['marketing']['mex']).union(set(pattern['ManualQA']['mex2'])),
            },

            'aqa': {
                'ma': ("qa.aqa.ma",),
                'ma2': ("qa.aqa.ma2",),
                'mdef': ("qa.aqa.mdef",),
                'mex': ("qa.aqa.mex",),
                'mex2': ("qa.aqa.mex2",),
                'mincl': ("qa.aqa.mincl",),
                # pattern['AQA']['mex']=set(pattern['marketing']['mex']).union(set(pattern['AQA']['mex2'])),
            },

            'support': {
                'ma': ("qa.support.ma",),
                'ma2': ("qa.support.ma2",),
                'mdef': ("qa.support.mdef",),
                'mex': ("qa.support.mex",),
                'mex2': ("qa.support.mex2",),
                'mincl': ("qa.support.mincl",),
            }
        }
    },
    #     # capitize
    'devops': {
        'ma': ("devops.ma",),
        'ma2': ("devops.ma2",),
        'mdef': ("devops.mdef",),
        'mex': ("devops.mex",),
        'mex2': ("devops.mex2",),
        'mincl': ("devops.mincl",),
    },

    'marketing': {
        'ma': ("marketing.ma",),
        'ma2': ("marketing.ma2",),
        'mdef': ("marketing.mdef",),
        'mex': {"marketing.mex"},
        'mex2': ("marketing.mex2",),
        'mincl': ("marketing.mincl",),

        'sub': {
            'smm': {
                'ma': ("marketing.smm.ma",),
                'ma2': ("marketing.smm.ma2",),
                'mdef': ("marketing.smm.mdef",),
                'mex': ("marketing.smm.mex",),
                'mex2': ("marketing.smm.mex2",),
                'mincl': ("marketing.smm.mincl",),
                # pattern['SMM']['mex']=set(pattern['smm']['mex']).union(set(pattern['SMM']['mex2'])),
            },

            'copyrighter': {
                'ma': ("marketing.copyrighter.ma",),
                'ma2': ("marketing.copyrighter.ma2",),
                'mdef': ("marketing.copyrighter.mdef",),
                'mex': ("marketing.copyrighter.mex",),
                'mex2': ("marketing.copyrighter.mex2",),
                'mincl': ("marketing.copyrighter.mincl",),

                # pattern['Copyrighter']['mex']=set(pattern['marketing']['mex']).union(set(pattern['Copyrighter']['mex2'])),
            },

            'seo': {
                'ma': ("marketing.seo.ma",),
                'ma2': ("marketing.seo.ma2",),
                'mdef': ("marketing.seo.mdef",),
                'mex': ("marketing.seo.mex",),
                'mex2': ("marketing.seo.mex2",),
                'mincl': ("marketing.seo.mincl",),
                # pattern['SEO']['mex']=set(pattern['marketing']['mex']).union(set(pattern['SEO']['mex2'])),
            },

            'link_builder': {
                'ma': ("marketing.link_builder.ma",),
                'ma2': ("marketing.link_builder.ma2",),
                'mdef': ("marketing.link_builder.mdef",),
                'mex': ("marketing.link_builder.mex",),
                'mex2': ("marketing.link_builder.mex2",),
                'mincl': ("marketing.link_builder.mincl",),
                # pattern['LinkBuilder']['mex']=set(pattern['marketing']['mex']).union(set(pattern['LinkBuilder']['mex2'])),
            },

            'media_buyer': {
                'ma': ("marketing.media_buyer.ma",),
                'ma2': ("marketing.media_buyer.ma2",),
                'mdef': ("marketing.media_buyer.mdef",),
                'mex': ("marketing.media_buyer.mex",),
                'mex2': ("marketing.media_buyer.mex2",),
                'mincl': ("marketing.media_buyer.mincl",),
                # pattern['MediaBuyer']['mex']=set(pattern['marketing']['mex']).union(set(pattern['MediaBuyer']['mex2'])),
            },

            'email_marketer': {
                'ma': ("marketing.email_marketer.ma",),
                'ma2': ("marketing.email_marketer.ma2",),
                'mdef': ("marketing.email_marketer.mdef",),
                'mex': ("marketing.email_marketer.mex",),
                'mex2': ("marketing.email_marketer.mex2",),
                'mincl': ("marketing.email_marketer.mincl",),
                # pattern['EmailMarketer']['mex']=set(pattern['marketing']['mex']).union(set(pattern['EmailMarketer']['mex2'])),
            },

            'LeadGenerationMarketing': {
                'ma': ("marketing.LeadGenerationMarketing.ma",),
                'ma2': ("marketing.LeadGenerationMarketing.ma2",),
                'mdef': ("marketing.LeadGenerationMarketing.mdef",),
                'mex': ("marketing.LeadGenerationMarketing.mex",),
                'mex2': ("marketing.LeadGenerationMarketing.mex2",),
                'mincl': ("marketing.LeadGenerationMarketing.mincl",),
                # pattern['LeadGenerationMarketing']['mex']=set(pattern['marketing']['mex']).union(set(pattern['LeadGenerationMarketing']['mex2'])),
            },

            'context': {
                'ma': ("marketing.context.ma",),
                'ma2': ("marketing.context.ma2",),
                'mdef': ("marketing.context.mdef",),
                'mex': ("marketing.context.mex",),
                'mex2': ("marketing.context.mex2",),
                'mincl': ("marketing.context.mincl",),
                # pattern['Kontekst']['mex']=set(pattern['marketing']['mex']).union(set(pattern['Kontekst']['mex2'])),
            },

            'content_manager': {
                'ma': ("marketing.content_manager.ma",),
                'ma2': ("marketing.content_manager.ma2",),
                'mdef': ("marketing.content_manager.mdef",),
                'mex': ("marketing.content_manager.mex",),
                'mex2': ("marketing.content_manager.mex2",),
                'mincl': ("marketing.content_manager.mincl",),
                # pattern['ContentManager']['mex']=set(pattern['marketing']['mex']).union(set(pattern['ContentManager']['mex2'])),
            },

            'tech_writer': {
                'ma': ("marketing.tech_writer.ma",),
                'ma2': ("marketing.tech_writer.ma2",),
                'mdef': ("marketing.tech_writer.mdef",),
                'mex': ("marketing.tech_writer.mex",),
                'mex2': ("marketing.tech_writer.mex2",),
                'mincl': ("marketing.tech_writer.mincl",),
                # pattern['TechWriter']['mex']=set(pattern['marketing']['mex']).union(set(pattern['TechWriter']['mex2'])),
            }
        }
    },

    'sales_manager': {
        'ma': ("sales_manager.ma",),
        'ma2': ("sales_manager.ma2",),
        'mdef': ("sales_manager.mdef",),
        'mex': ("sales_manager.mex",),
        'mex2': ("sales_manager.mex2",),
        'mincl': ("sales_manager.mincl",),
    },

    'non_code_manager': {
        'ma': ("sales_manager.non_code_manager.ma",),
        'ma2': ("sales_manager.non_code_manager.ma2",),
        'mdef': ("sales_manager.non_code_manager.mdef",),
        'mex': ("sales_manager.non_code_manager.mex",),
        'mex2': ("sales_manager.non_code_manager.mex2",),
        'mincl': ("sales_manager.non_code_manager.mincl",),
    },

    'junior': {
        'ma': ("junior.ma",),
        'ma2': ("junior.ma2",),
        'mdef': ("junior.mdef",),
        'mex': ("junior.mex",),
        'mex2': ("junior.mex2",),
        'mincl': ("junior.mincl",),
    },

    'middle': {
        'ma': ("middle.ma",),
        'ma2': ("middle.ma2",),
        'mdef': ("middle.mdef",),
        'mex': ("middle.mex",),
        'mex2': ("middle.mex2",),
        'mincl': ("middle.mincl",),
    },

    'senior': {
        'ma': ("senior.ma",),
        'ma2': ("senior.ma2",),
        'mdef': ("senior.mdef",),
        'mex': ("senior.mex",),
        'mex2': ("senior.mex2",),
        'mincl': ("senior.mincl",),
    },

    'remote': {
        'ma': ("remote", "удаленка", "удаленная", "удаленную работу", "удалённую работу", "удаленно", "удалённо"),
        'ma2': (),
        'mdef': (),
        'mex': (),
        'mex2': (),
        'mincl': ()
    },

    'relocate': {
        'ma': ("relocate", "relocation", "релокация"),
        'ma2': (),
        'mdef': (),
        'mex': (),
        'mex2': (),
        'mincl': ()
    },

    'country': {
        'ma': (
            "Тайланд", "Латвия", "Israel", "Израиль", "Moldova", "Молдова", "Dubai", "Дубаи", "РБ", "Беларусь",
            "Белорусь", "Belarus", "Грузия", "Georgia", "Россия", "Russia", "Kazakhstan", "Казахстан", "Украина",
            "Ukraine", "Армения", "РФ", "Poland", "Польша", "Spain", "Испания", "Germany", "Германия", "Romania",
            "США", "USA", "Финляндия", "Serbia", "Lithuania", "Кипр", "Турция"),
        'ma2': (),
        'mdef': (),
        'mex': (),
        'mex2': (),
        'mincl': ()
    },

    'city': {
        'ma': ("Томск", "Рига", "Москва", "Ярославль", "Хельсинки", "Стамбул", "Санкт-Петербург", "Волгоград",
               "Екатеринбург", "Самара", "Киев", "Kyiv"),
        'ma2': (),
        'mdef': (),
        'mex': (),
        'mex2': (),
        'mincl': ()
    },

    'internship': {
        'ma': ("internship", "стажировка", "trainee"),
        'ma2': (),
        'mdef': (),
        'mex': (),
        'mex2': (),
        'mincl': ()
    },
}


# -*- coding: utf-8 -*-
{
    'name': "National ID Application",
    'summary': """
    Process online application for National ID.
        """,

    'description': """
        Utilize the website_sale wizard progress bar to show the applicant the various stages of the progress being 
        made, backend chatter showing changes and the timestamps when the changes were made.
    """,

    'sequence': -3,
    'author': "Martin Kalema",
    'website': "0.0.0.0:8070/nira/apply",
    'category': 'Public Service',
    'version': '0.1',
    'depends': ['base', 'website', 'mail', 'website_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/website_form.xml',
        'views/owl_form.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            'nira_data_entry/static/src/components/*/*.js',
            'nira_data_entry/static/src/components/*/*.xml',
            'nira_data_entry/static/src/components/*/*.css',
        ]
    }
}


{
    'name': "MediSmart",
    'version': '1.0',
    'depends': ['base', 'mail'],
    'author': "jeep-odoo",
    'icon' : "assets/icon.png",
    'data': [
        'security/ir.model.access.csv',
        'data/medismart_appointment_sequence.xml',
        'views/medismart_patient_tags_views.xml',
        'views/medismart_patient_views.xml',
        'views/medismart_doctor_views.xml',
        'views/medismart_appointment_tags_views.xml',
        'views/medismart_appointment_views.xml',
        'views/medismart_specialization_views.xml',
        'views/medismart_menus.xml',
        ],
    'demo':[
        'demo/demo_data.xml',
    ],
    'application': True,
    'installable': True,
    "license" : "LGPL-3",
}

{
    'name': "MediSmart",
    'version': '1.0',
    'depends': ['base', 'mail'],
    'author': "jeep-odoo",
    'icon' : "assets/icon.png",
    'data': [
        'security/ir.model.access.csv',
        'views/medismart_patient_views.xml',
        'views/medismart_doctor_views.xml',
        'views/medismart_bed_views.xml',
        'views/medismart_appointment_views.xml',
        'views/medismart_menus.xml',
        ],
    'application': True,
    'installable': True,
    "license" : "LGPL-3",
}
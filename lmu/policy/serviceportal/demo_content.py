# -*- coding: utf-8 -*-

demo_users = {
    '72C918A84D785B9F': {
        'email': 'Alexander.Loechel@lmu.de',
        'password': 'Test@IUK',
        'properties': {
            'fullname': 'Alexander Loechel',
            'location': 'Martiusstr. 4; München',
            'homepage': '',
        },
        'roles': ('Member', 'Manager', 'cms-admins', 'in_sp_supportteam', 'sp_members')
    },
    '5B4187806EA6E3B0': {
        'email': 'demo@lmu.de',
        'password': 'Test@IUK',
        'properties': {
            'fullname': 'Katharine Linges',
            'homepage': '',
        },
        'roles': ('Member', 'in_sp_supportteam', 'sp_members')
    }
}

demo_polls = {
    'wie-gut-hilft-ihnen-unser-service-portal-bei-der-arbeit': {
        'poll_type': 'Star Poll',
        'title': 'Wie gut hilft Ihnen unser Service-Portal bei der Arbeit?',
        'description': 'Seien Sie ehrlich, nur so können wir besser werden.',
        'author': 'K5B4187806EA6E3B0',  # Katharine Linges
        'modification_date': '2014/10/02 12:43:00.000000 GMT+2',
        'state': 'open',
    }
}

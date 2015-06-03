# -*- coding: utf-8 -*-

demo_users = {
    'Brady': {
        'email': 'demo@lmu.de',
        'password': 'Test@IUK',
        'properties': {
            'fullname': 'Stephanie Brady',
            'homepage': 'https://iukintest.verwaltung.uni-muenchen.de/personen/b/brady_stephanie/index.html',
        },
        'roles': ('Member', 'sp_members')
    },
    'Simon.Kirner': {
        'email': 'demo@lmu.de',
        'password': 'Test@IUK',
        'properties': {
            'fullname': 'Simon Kirner',
            'homepage': 'https://iukintest.verwaltung.uni-muenchen.de/personen/k/kirner_simon/index.html',
        },
        'roles': ('Member', 'sp_members')
    },
    'Alexander.Loechel': {
        'email': 'Alexander.Loechel@lmu.de',
        'password': 'Test@IUK',
        'properties': {
            'fullname': 'Alexander Loechel',
            'location': 'Martiusstr. 4; München',
            'homepage': 'https://iukintest.verwaltung.uni-muenchen.de/personen/l/loechel_alexander/index.html',
        },
        'roles': ('Member', 'Manager', 'cms-admins', 'in_sp_supportteam', 'sp_members')
    },
    'Katharine.Linges': {
        'email': 'demo@lmu.de',
        'password': 'Test@IUK',
        'properties': {
            'fullname': 'Katharine Linges',
            'homepage': 'https://iukintest.verwaltung.uni-muenchen.de/personen/l/linges_katharine/index.html',
        },
        'roles': ('Member', 'in_sp_supportteam', 'sp_members')
    }
}

demo_polls = {
    'wie-gut-hilft-ihnen-unser-service-portal-bei-der-arbeit': {
        'poll_type': 'Star Poll',
        'title': 'Wie gut hilft Ihnen unser Service-Portal bei der Arbeit?',
        'description': 'Seien Sie ehrlich, nur so können wir besser werden.',
        'author': 'Katharine.Linges',
        'modification_date': '2014/10/02 12:43:00.000000 GMT+2',
        'state': 'open',
    }
}

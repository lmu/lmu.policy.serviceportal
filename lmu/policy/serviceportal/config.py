# -*- coding: utf-8 -*-

required_groups = {
    'ZUV-Serviceportal-Members': {
        'roles': ['Member', 'Authenticated'],
        'title': 'ZUV-Intranet-Members (Virtual Group)',
        'description': 'Virtual Group for Users of the ZUV-Intranet coming from Shibboleth via "cn=ZUV-Serviceportal-Members,ou=..."'
    },
}

base_content = {
    'umfragen': {
        'title': 'Umfragen',
        'description': '',
        'type': 'Poll Folder',
        'path': '/',
    }
}

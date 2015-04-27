# -*- coding: utf-8 -*-

required_groups = {
    'cms-admins': {
        'roles': ['Manager'],
        'title': 'CMS Admins (Virtual Group)',
        'description': 'Virtual Group for Administrators derifed from Shibboleth via "cn=cms-admin-insp,ou=..."'
    },
    'in_sp_supportteam': {
        'roles': ['Contributor', 'Editor', 'Reader', 'Reviewer'],
        'title': 'Serviceportal Supportteam (Virtual Group)',
        'description': 'Virtual Group for the Serviceportal-Supportteam derifed from Shibboleth via "cn=in_sp_supportteam,ou=..."'
    },
    'in_members': {
        'roles': ['Member'],
        'title': 'ZUV-Serviceportal Users (Virtual Group)',
        'description': 'Virtual Group for Users of the ZUV-Serviceportal derifed from Shibboleth via "cn=ZUV-Mitarbeiter,ou=..."'
    }
}

base_content = {
    'umfragen', {
        'title': 'Umfragen',
        'description': '',
        'type': 'Folder',
        'path': '/'
    }
}

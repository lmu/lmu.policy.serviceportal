# -*- coding: utf-8 -*-

from plone import api


def setupDemoContent():
    """Install Demo Content on Portal"""
    pass
    portal = api.portal.get()

    polls_folder = portal['umfragen']
    if not polls_folder:
        polls_folder = api.content.create(
            type='Folder',
            title='Umfragen',
            container=portal)

    #import ipdb; ipdb.set_trace()

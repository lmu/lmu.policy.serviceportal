# -*- coding: utf-8 -*-

from plone import api


def setupDemoContent(context):
    """Install Demo Content on Portal"""
    pass
    portal = api.portal.get()

    if not hasattr(portal, 'umfragen'):
        polls_folder = api.content.create(
            type='Folder',
            title='Umfragen',
            container=portal)

    #import ipdb; ipdb.set_trace()

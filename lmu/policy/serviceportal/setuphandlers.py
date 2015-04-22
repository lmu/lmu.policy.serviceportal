# -*- coding: utf-8 -*-

from plone import api


def setupDemoContent(context):
    """Install Demo Content on Portal"""
    return # seems to be called all the time.
    portal = api.portal.get()

    import ipdb; ipdb.set_trace()
    if not hasattr(portal, 'umfragen'):
        polls_folder = api.content.create(
            type='Folder',
            title='Umfragen',
            container=portal)

    if not hasattr(portal, 'blog-mit'):
        blog_folder = api.content.create(
            type='Blog Folder',
            title='Blog mit',
            container=portal)


def importDemoContent(context):
    """Install Demo Content on Portal"""

    if context.readDataFile('lmu.policy.serviceportal_content.txt') is None:
        return

    return # seems to be called all the time.
    portal = api.portal.get()

    import ipdb; ipdb.set_trace()
    if not hasattr(portal, 'umfragen'):
        polls_folder = api.content.create(
            type='Folder',
            title='Umfragen',
            container=portal)

    if not hasattr(portal, 'blog-mit'):
        blog_folder = api.content.create(
            type='Blog Folder',
            title='Blog mit',
            container=portal)

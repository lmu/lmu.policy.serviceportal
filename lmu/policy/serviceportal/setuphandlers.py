# -*- coding: utf-8 -*-
from __future__ import print_function


from DateTime import DateTime

from plone import api

from zExceptions import BadRequest

from lmu.policy.serviceportal.config import base_content
from lmu.policy.serviceportal.config import required_groups

from lmu.policy.serviceportal.demo_content import demo_users
from lmu.policy.serviceportal.demo_content import demo_polls


def setupVarious(context):
    """Install all additional Things that can't be done via Generic Setup
    """

    if context.readDataFile('lmu.policy.serviceportal_default.txt') is None:
        return

    _setupGroups(context)
    _setupBaseContent(context)


def _setupGroups(context):
    #portal = apit.portal.get()
    gtool = api.portal.get_tool(name='portal_groups')
    groups = api.group.get_groups()
    for gid, gdata in required_groups.iteritems():
        if not gid in groups:
            api.group.create(
                groupname=gid,
                title=gdata['title'],
                roles=gdata['roles'],
                description=gdata['description']
            )
        else:
            gtool.editGroup(
                gid,
                title=gdata['title'],
                roles=gdata['roles'],
                description=gdata['description']
            )


def _setupBaseContent(context):
    for oid, oval in base_content.iteritems():
        try:
            container = api.content.get(path=oval['path'])
            if not oid in container.keys():
                folder = api.content.create(
                    id=oid,
                    container=container,
                    type=oval['type'],
                    title=oval['title'],
                    description=oval['description']
                )
            else:
                folder = container.get(oid)
                folder.title = oval['title']
                folder.description = oval['description']
            api.content.transition(obj=folder, to_state='published')
        except BadRequest as e:
            print(e.message)
        except Exception as e:
            print(e.message)


def importDemoContent(context):
    """Install Demo Content on Portal"""

    if context.readDataFile('lmu.policy.serviceportal_demo-content.txt') is None:
        return

    #return # seems to be called all the time.
    #portal = api.portal.get()
    _setupDemoUsers(context)
    #_setupDemoPolls(context)


def _setupDemoUsers(context):
    all_users = [user.id for user in api.user.get_users()]
    for uid, udata in demo_users.iteritems():
        if uid not in all_users:
            try:
                api.user.create(
                    email=udata['email'],
                    username=uid,
                    properties=udata['properties']
                )
            except BadRequest as e:
                print(e.message)
            except Exception as e:
                print(e.message)


def _setupDemoPolls(context):
    for oid, oval in demo_polls.iteritems():
        try:
            container = api.content.get(path=oval['path'])
            entry = api.content.create(
                id=oid,
                type='Poll',
                container=container,
                title=oval['title'],
                description=oval['description'],
                creators=(oval['author'],),
            )
            api.content.transition(obj=entry, to_state='internally_published')
            entry.modification_date = DateTime(oval['modification_date'])
        except BadRequest as e:
            print(e.message)
        except Exception as e:
            print(e.message)
            #import ipdb; ipdb.set_trace()

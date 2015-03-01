from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='lmu.policy.serviceportal',
      version=version,
      description="A Plone policy for the ZUV-Serviceportal",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.rst")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='Plone Policy',
      author='Alexander Loechel',
      author_email='Alexander.Loechel@lmu.de',
      url='https://github.com/loechel/lmu.policy.serviceportal',
      license='GPLv2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['lmu', 'lmu.policy'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )

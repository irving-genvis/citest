'''

  Created by irving on 24/07/18

'''

import setuptools

ver = "0.1.9"

setuptools.setup(
    author="irving-genvis",
    author_email="chenghuanl@genvis.co",
    name="ci",
    version=ver,
    url="https://github.com/irving-genvis/citest.git", # link to the github repo
    packages=setuptools.find_packages(),
    test_suite='nose.collector',
    tests_require=['nose'],
    # add the dependencies of the package here
    install_requires=[
          'numpy==1.14.5',
      ],
)

with open("upload_to_nexus.sh", 'w') as f:
    f.write('#!/usr/bin/env bash\n')
    f.write('pip install twine\n')
    f.write('twine upload -r pypi-local --repository-url https://nexus.genvis.co/repository/pypi-local/ -u dev -p '
            'usainbolt2018 dist/ci-' + ver + '.tar.gz\n')

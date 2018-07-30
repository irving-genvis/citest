'''

  Created by irving on 24/07/18

'''

import setuptools

ver = "0.1.4"

setuptools.setup(
    author="irving-genvis",
    author_email="chenghuanl@genvis.co",
    name="ci",
    version=ver,
    url="https://github.com/irving-genvis/citest.git",
    packages=setuptools.find_packages(),
    test_suite='nose.collector',
    tests_require=['nose'],
)

with open("upload_to_nexus.sh", 'w') as f:
    f.write('#!/usr/bin/env bash\n')
    f.write('pip install twine\n')
    f.write('twine upload -r pypi-local --repository-url https://nexus.genvis.co/repository/pypi-local/ -u dev -p '
            'usainbolt2018 dist/ci-' + ver + '.tar.gz\n')

'''

  Created by irving on 24/07/18

'''

import setuptools

setuptools.setup(
    author="irving-genvis",
    author_email="chenghuanl@genvis.co",
    name="ci",
    version="0.1.3",
    url="https://github.com/irving-genvis/citest.git",
    packages=setuptools.find_packages(),
    test_suite='nose.collector',
    tests_require=['nose'],
)

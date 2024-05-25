from setuptools import setup, find_packages

setup(
    name='TextUtils',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'mecab-python3==1.0.4',
    ],
    author='DAIKI KANAYMA',
    author_email='s2222065@stu.musashino-u.ac.jp',
    description='A package for text processing utilities',
    url='https://github.com/K-daiki/textutils.git',
    license='MIT',
)

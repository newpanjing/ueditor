from setuptools import setup, find_packages

long_description = "\n".join([
    open('README.rst', 'r').read(),
])

setup(
    name='ueditor',
    version='1.2',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    url='https://github.com/newpanjing/ueditor.git',
    license='Apache Listen 2.0',
    author='panjing',
    author_email='newpanjing@icloud.com',
    description='django ueditor plugin',
    long_description=long_description,
    install_requires=['django', 'shortid8'],
)

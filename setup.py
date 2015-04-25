
from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()
    
setup(name='pythonlangutil',
      version='0.1',
      description='Utilities for Python programmers with background in other languages.',
      long_description=readme(),
      classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='language util',
      url='https://github.com/ehsan-keshavarzian/pythonlangutil',
      author='Ehsan Keshavarzian',
      author_email='ehsan985@gmail.com',
      license='MIT',
      packages=['pythonlangutil'],
      install_requires=[
          
      ],
      include_package_data=True,
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'])
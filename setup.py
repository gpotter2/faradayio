from distutils.core import setup
setup(
    name='faradayio',
    packages=['faradayio'],
    install_requires={
        'attrs==17.4.0',
        'flake8==3.5.0',
        'mccabe==0.6.1',
        'pluggy==0.6.0',
        'py==1.5.2',
        'pycodestyle==2.3.1',
        'pyflakes==1.6.0',
        'pyserial==3.4',
        'pytest==3.3.2',
        'python-pytun==2.2.1',
        'scapy-python3==0.23',
        'six==1.11.0',
        'sliplib==0.3.0',
        'sphinx-rtd-theme==0.2.4',
        'coveralls==1.2.0',
        'pytest-cov==2.5.1',
        'timeout-decorator==0.4.0',
    }
    version='0.0.2a',
    description='FaradayRF TUN/TAP adapter',
    author='FaradayRF',
    author_email='Support@FaradayRF.com',
    url='https://github.com/FaradayRF/faradayio',

    license='GPLv3',

    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Communications :: Ham Radio',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
    ],
)

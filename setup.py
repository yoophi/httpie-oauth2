from setuptools import setup

setup(
    name='httpie-oauth2',
    description='OAuth2 plugin for HTTPie.',
    version='1.0',
    author='Pyunghyuk Yoo',
    author_email='yoophi@gmail.com',
    license='BSD',
    url='https://github.com/yoophi/httpie-oauth2',
    download_url='https://github.com/yoophi/httpie-oauth2',
    py_modules=['httpie_oauth2'],
    zip_safe=False,
    entry_points={
        'httpie.plugins.auth.v1': [
            'httpie_oauth2 = httpie_oauth2:OAuth2Plugin'
        ]
    },
    install_requires=[
        'httpie>=0.7.0',
        'requests-oauthlib>=0.3.2'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Environment :: Plugins',
        'License :: OSI Approved :: BSD License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities'
    ],
)

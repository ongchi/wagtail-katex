from setuptools import setup, find_packages

from wagtailkatex import __version__

with open("README.md", "r") as fp:
    long_description = fp.read()

setup(
    name='wagtail-katex',
    version=__version__,
    author="ongchi",
    author_email="ongchi@users.noreply.github.com",
    description='KaTex for Wagtail CMS Draftail editor',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/ongchi/wagtail-katex',
    project_urls={
        "Bug Tracker": "https://github.com/ongchi/wagtail-katex/issues",
    },
    install_requires=['wagtail>=2.3'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Framework :: Wagtail',
        'Framework :: Wagtail :: 2',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.6",
)

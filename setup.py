from setuptools import setup, find_packages

try:
    from pip.req import parse_requirements
except ImportError:
    from pip._internal.req import parse_requirements

install_reqs = parse_requirements('requirements.txt', session=False)
reqs = [str(ir.req) for ir in install_reqs]

packages = find_packages()

setup(name='PRML-notbooks',
      version='0.1.0',
      description='Notebooks for PRML book',
      url='',
      author='Shyam Shinde',
      author_email='shinde.shyam5@gmail.com',
      license='MIT',
      packages=packages,
      install_requires=reqs)

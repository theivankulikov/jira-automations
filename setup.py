from setuptools import setup

setup(name='jira-automations',
      version='0.1',
      description='Automate routine tasks in Jira',
      url='https://github.com/theivankulikov/jira-automations',
      author='Ivan Kulikov',
      author_email='ivankulich@gmail.com',
      license='MIT',
      packages=['jira_automations'],
      zip_safe=False,
      install_requires=[
          'requests'
      ])
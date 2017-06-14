from setuptools import setup, find_packages

setup(name='sd3save_editor',
      author='rrooij',
      author_email='rderooij685@gmail.com',
      url='https://github.com/rrooij/sd3save_editor',
      version='0.5',
      license="GPL-3.0",
      description='Seiken Densetsu 3 Save Editor',
      packages=find_packages(),
      include_package_data=True,
      entry_points={
          'console_scripts': [
              'sd3save_editor_cli = sd3save_editor.__main__.py'
              ],
          'gui_scripts': [
              'sd3save_editor_gui = sd3save_editor.gui.main.py'
              ]
          },
      install_requires=['construct']
      )

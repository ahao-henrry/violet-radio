from setuptools import setup, find_packages


setup(
        name = 'violet-radio',
        version = '0.0.1',
        description = 'a live radio',
        url = 'https://github.com/ahao-henrry/violet-radio.git',
        author = 'ahao henry',
        author_email = 'henryahao.violet@gmail.com',
        keywords = ['live', 'radio'],
        packages = find_packages(),
        package_data = {
            'src': ['radio_list']
        },
        include_package_data = True,
        install_requires = ['python-vlc'],
        entry_points = {
            'console_scripts' : [
                'violetradio = src:start'
                ]
        },
        zip_safe = False
    )


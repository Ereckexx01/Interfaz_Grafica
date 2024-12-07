from setuptools import setup, find_packages

setup(
    name = 'First_Package',
    version = '1.0',
    packages = find_packages(),
    install_requieres = ["PySide2"],
    description = 'Paquete creado con el fin de informar sobre propiedades de particulas de Leptones, Neutrinos, Quarks y Bosones',
    long_description = open("README.md").read(),
    long_description_content_type = 'text/markdown',
    author = 'Erick Becerra Marin',
    author_email = 'erickbecerramarin@ciencias.unam.mx',
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires = '>=3.6',
    entry_points={
        'console_scripts': [
            'First_Package_gui = First_Package.gui:main'
        ]
    },
)
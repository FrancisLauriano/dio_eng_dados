from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name='identificador-img-color',
    version='0.1.0',
    author="Francis Lauriano",
    author_email="francislauriano@gmail.com",
    description='Pacote para identificar se uma imagem é colorida ou em preto e branco.',
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FrancisLauriano/dio_eng_dados/tree/main/imagem-identifica-cor-package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)

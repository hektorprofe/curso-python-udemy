from setuptools import setup

setup(
	name="paquete",
	version="0.1",
	description="Este es un paquete de jemplo",
	author="Hector Costa",
	author_email="yo@hcosta.info",
	url="http://hcosta.info",
    packages=['paquete','paquete.hola','paquete.adios']
)
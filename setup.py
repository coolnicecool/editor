from setuptools import setup
setup(
    name="editor",
    version="0.1.0",
    description="Python & text Windows CMD Editior written with only native libaries",
    py_modules=["editor","TIME"],
    package_dir={"":"code"},
    url="https://github.com/coolnicecool/Pykernel",
    author="Raleigh Priour"
)
#python setup.py build
#python setup.py sdist bdist_wheel
#twine upload dist/*
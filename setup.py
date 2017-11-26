import sys

from setuptools import setup
from setuptools.command.build import build

class Build(build):
    """Customized setuptools build command - builds protos on build."""
    def run(self):
        protoc_command = ["make", "python"]
        if subprocess.call(protoc_command) != 0:
            sys.exit(-1)
        build.run(self)

setup(cmdclass={'build': Buil,})
setup(packages=['libsvm'])

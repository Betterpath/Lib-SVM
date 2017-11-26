import sys

from setuptools import setup
import distutils.command.build

class Build(build):
    """Customized setuptools build command - builds protos on build."""
    def run(self):
        protoc_command = ["make", "python"]
        if subprocess.call(protoc_command) != 0:
            sys.exit(-1)
        build.run(self)

setup(cmdclass={'build': Build,})
setup(packages=['libsvm'])

import sys

from setuptools import setup
import distutils.command.build

class Build(distutils.command.build):
    def run(self):
        protoc_command = ["make"]
        if subprocess.call(protoc_command) != 0:
            sys.exit(-1)
        print "Hi"
        distutils.command.build.run(self)

setup(cmdclass={'build': Build,})
setup(packages=['libsvm'])

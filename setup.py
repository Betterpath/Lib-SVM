import distutils.cmd
from setuptools import setup
import setuptools
import subprocess

class Build(distutils.cmd.Command):
    def run(self):
        protoc_command = ["make"]
        if subprocess.call(protoc_command) != 0:
            sys.exit(-1)
        distutils.command.build.run(self)

setup(cmdclass={'build': Build,})

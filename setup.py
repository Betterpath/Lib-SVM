import distutils.cmd
import setuptools
import subprocess
import sys

from setuptools import setup

class MyBuild(distutils.cmd.Command):
    def run(self):
        protoc_command = ["make"]
        if subprocess.call(protoc_command) != 0:
            sys.exit(-1)
        distutils.command.build.run(self)

setup(cmdclass={'build': MyBuild})

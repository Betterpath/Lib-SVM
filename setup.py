import setuptools.command.build_py


class BuildPyCommand(setuptools.command.build_py.build_py):
  """Custom build command."""

  def run(self):
    self.run_command('make')
    setuptools.command.build_py.build_py.run(self)


setuptools.setup(
    cmdclass={
        'build': BuildPyCommand,
    },
)

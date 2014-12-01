from setuptools import setup, Command
import os
import sys

class TestCram(Command):
    description = "run cram tests"
    user_options = []

    def initialize_options(self):
        self.coverage = 0

    def finalize_options(self):
        pass

    def run(self):
        import cram
        os.environ["PYTHON"] = sys.executable
        cram.main(["-v", "tests"])


setup(
    name="h5xl",
    version = "0.0",
    description="Convert HDF5 tables into Excel worksheets.",
    author="echlebek",
    author_email="echlebek@gmail.com",
    packages=["h5xl"],
    scripts=["scripts/h5xl"],
    setup_requires=["cython", "numpy"],
    install_requires=["cython", "numpy", "h5py", "openpyxl"],
    cmdclass={"cram": TestCram},
    test_suite="tests",
)

from os.path import dirname, join
import setuptools
import pyslots.__init__ as __init__

setuptools.setup(
  name="pyslots",
  version=__init__.VERSION,
  description="A fun little terminal slots game!",
  long_description=open(join(dirname(__file__), "README.md")).read(),
  long_description_content_type="text/markdown",
  url="https://github.com/Lukas-Batema/pyslots",
  author="Lukas-Batema",
  author_email="lukasbatema@gmail.com",
  license="Apache",
  packages=["pyslots"],
  include_package_data=True,
  install_requires=None,
  keywords=["pyslots", "python slots", "slots", "slot machine", "terminal slots"],
  classifiers=[
    "Programming Language :: Python :: 3",
  ],
  python_requires=">=3.9",
  entry_points={
    "console_scripts": [
      "pyslots=pyslots.__main__:main",
    ]
  },
)
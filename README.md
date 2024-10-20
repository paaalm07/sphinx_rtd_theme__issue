# Setup

Setup description for issue reproduction.

## Toolchain Windows

- Install [Hatch](https://hatch.pypa.io/) as python manager:
    - No python/pip installed (Windows): ```msiexec /passive /i https://github.com/pypa/hatch/releases/latest/download/hatch-x64.msi```
    - Set global hatch config: ```hatch config set dirs.env.virtual .hatch```
        - Note: to create a .hatch directory in project root

## Toolchain RaspberryPi

- Install [Hatch](https://hatch.pypa.io/) as python manager:
    - Python/Pip already there: ```pip install hatch --break-system-packages```
    - Set global hatch config: ```hatch config set dirs.env.virtual .hatch```
        - Note: to create a .hatch directory in project root


## Usage

Use [Hatch](https://hatch.pypa.io/) to install dependencies, create version.py and docs:

```bash
hatch env create
hatch run dev
hatch run docs
```


# Issue

Output of building sphinx docs with sphinx_rtd_theme are differently on RaspberryPi and Windows environment.

Issue raised here: https://github.com/readthedocs/sphinx_rtd_theme/issues/1619

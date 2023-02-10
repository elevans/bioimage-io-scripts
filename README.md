# bioimage-io-scripts

This repository contains `environment.yml` files for running models from BioImage.IO with the [core-bioimage-io](https://github.com/bioimage-io/core-bioimage-io-python) library and PyImageJ

## Setup

Build and use the appropriate environement for your model

```bash
$ mamba env create -f environment-torch-pyij.yml
```

The current version of PyImageJ on conda-forge (version: `1.3.2`) will not work due to a bug with singleton dimensions (see: https://github.com/imagej/pyimagej/pull/238#issuecomment-1412469179). This has been fixed on the `main` branch (see: https://github.com/imagej/pyimagej/commit/dccabffb0f45b369c94e67c5724dd47c06d167b2) and will be available with our next release of PyImageJ. For now, `git clone` the `main` branch of PyImageJ and install the local development version with:

```bash
$ pip install -e .
```

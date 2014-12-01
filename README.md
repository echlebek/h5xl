h5xl
====

Convert HDF5 Files Into Excel Workbooks

[![Build Status](https://travis-ci.org/echlebek/h5xl.png)](https://travis-ci.org/echlebek/h5xl)

`h5xl` will convert any one-dimensional or two-dimensional datasets in an HDF5 file into Excel worksheets.
It will name the worksheets after the path to the dataset, replacing `'/'` characters with `'.'`.
Datasets with compound dtypes will have their columns reflected in the first row of the worksheet.

Example:

    h5xl input.h5 output.xlsx

Dependencies:

* numpy
* cython
* h5py
* openpyxl

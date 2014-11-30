Generate an HDF5 file containing two datasets using h5py.

  $ cat <<EOF > generate.py
  > import h5py; import numpy as np
  > with h5py.File("input.h5") as f:
  >     f['foo'] = np.array([(1, 2, 3)], dtype=np.dtype([("a", int), ("b", int), ("c", int)]))
  >     f['/bar/baz'] = np.array([(1, "foo"), (2, "bar")], dtype=np.dtype([("a", int), ("b", np.dtype("S4"))]))
  > EOF

Check that output.xlsx has two worksheets containing specific values.

  $ cat <<EOF > test.py
  > import openpyxl
  > wb = openpyxl.load_workbook("output.xlsx")
  > print 'foo' in wb or "Missing 'foo' worksheet."
  > print [[c.value for c in row] for row in wb['foo'].rows]
  > print 'bar.baz' in wb or "Missing 'bar.baz' worksheet."
  > print [[c.value for c in row] for row in wb['bar.baz'].rows]
  > EOF

Generate the data and run the test.

  $ python generate.py

  $ h5xl input.h5 output.xlsx

  $ python test.py
  True
  [[u'a', u'b', u'c'], [1, 2, 3]]
  True
  [[u'a', u'b'], [1, u'foo'], [2, u'bar']]

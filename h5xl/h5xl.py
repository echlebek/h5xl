import argparse
import sys
import logging
import h5py


def set_args(parser):
    parser.add_argument("input", help="Input HDF5 file")
    parser.add_argument("output", help="Output Excel File")


def iterate_datasets(f):
    """Recursively yields datasets from f and its groups"""
    for k in f:
        if isinstance(f[k], h5py.Dataset):
            yield f[k]
        elif isinstance(f[k], h5py.Group):
            for d in iterate_datasets(f[k]):
                yield d


def main(args):
    from .io import writer

    exit_status = 0

    with h5py.File(args.input, 'r') as f:
        with writer(args.output) as w:
            for dataset in iterate_datasets(f):
                try:
                    w.write(dataset[:], dataset.name.lstrip("/").replace("/", "."))
                except Exception as e:
                    logging.warn("{}".format(e.message))
                    exit_status = 1

    return exit_status


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    set_args(parser)
    args = parser.parse_args(sys.argv[1:])
    sys.exit(main(args))

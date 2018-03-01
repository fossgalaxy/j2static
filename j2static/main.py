#! /usr/bin/env python3

import pathlib
import shutil

from j2static import build

def generate(args, outdir='site/'):
    out_path = pathlib.Path(outdir)

    generator = build.get_builder("html", args.template_dir)
    for template in generator.get_files():
        out_file = out_path / template
        generator.generate(template, out_file)

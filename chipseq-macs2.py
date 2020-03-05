#!/usr/bin/env python3
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("inputdir", help = "input directory for treatment bam files")
parser.add_argument("outputdir", help = "output directory for callpeak and bdgcmp subcommands")
parser.add_argument("control", help = "control (i.e. WCE) bam file")
parser.add_argument("--name", help = "run or experiment name", default = "NA")
parser.add_argument("--gsize", help = "genome size", default = "2.7e9")
parser.add_argument("--bdgcmp", help = "invoke bdgcmp subcommand")
args = parser.parse_args()

# get list of treatment files
treatments = [file for file in os.listdir(args.inputdir) if file.endswith(".bam") and os.path.join(args.inputdir, file) != args.control]

for file in treatments:
    outfilename = '_'.join([args.name, file.strip(".bam")])   # define output name for current treatment file

    #### do peak calling #######
    callpeak = ' '.join([
                        "macs2",
                        "callpeak",
                        "--bdg",        # generate bedGraph file
                        "--nomodel",    # do not build shifting model
                        ' '.join(["--outdir", args.outputdir]),
                        ' '.join(["--control", args.control]),
                        ' '.join(["--treatment", os.path.join(args.inputdir, file)]),
                        ' '.join(["--name", outfilename]),     # run/experiment name
                        ' '.join(["--gsize", args.gsize])    # genome size
                        ])
    os.system(callpeak)

    ##### perform noise deduction, comparing treatment against control #######
    if args.bdgcmp is not None:
        bdgcmp = ' '.join([
                        "macs2",
                        ' '.join(["bdgcmp -m", args.bdgcmp]),
                        ' '.join(["-t", os.path.join(args.outputdir, ''.join([outfilename, "_treat_pileup.bdg"]))]),
                        ' '.join(["-c", os.path.join(args.outputdir, ''.join([outfilename, "_control_lambda.bdg"]))]),
                        ' '.join(["-o", os.path.join(args.outputdir, ''.join([outfilename, "_", args.bdgcmp, ".bdg"]))])
                        ])
        os.system(bdgcmp)

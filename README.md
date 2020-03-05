# chipseq-macs2

This is a Python 3 script to automate batch Chip-Seq analysis using the command-line tool [MACS2 v2.2.6](https://github.com/taoliu/MACS). The specific use-case requires presence of a control (i.e. Whole Cell Extract, or WCE) sample and input files in bam format. For each treatment input file, it will invoke `callpeak` to generate two bedGraph files (treat_pileup.bdg and control_lambda.bdg) and optionally invoke `bdgcmp` to compare bedGraph output of treatment versus control.

##### Usage: `python chipseq-macs2.py inputdir outputdir control --name --gsize --bdgcmp`
- `inputdir` (required): path to one or more treatment files (in bam format)
- `outputdir` (required): directory where all output files will be stored
- `control` (required): control ChiP-Seq sample (typically a WCE done in parallel as the treatment samples)
- `--name` (optional): an optional run/experiment/batch identifier. This will be preprended to each output file. If not given, defaults to MACS2 default of `NA`
- `--gsize` (optional): genome size of the organism. If not given, will default to MACS2 default of 2.7e9 (_Homo sapiens_)
- `--bdgcmp -m method` (optional): whether to perform noise deduction comparing the treatment against the control. Invoking this option will generate an additional bedGraph file with the method of choice appended to the end of the filename. `method` is one of following available choices in MACS2: `ppois, qpois, subtract, logFE, FE, logLR, slogLR, max`

#### Reference
Yong Zhang, Tao Liu, Clifford A Meyer, Jérôme Eeckhoute, David S Johnson, Bradley E Bernstein, Chad Nusbaum, Richard M Myers, Myles Brown, Wei Li & X Shirley Liu (2008). [Model-based Analysis of ChIP-Seq (MACS). Genome Biology volume 9, R137](https://genomebiology.biomedcentral.com/articles/10.1186/gb-2008-9-9-r137#citeas)

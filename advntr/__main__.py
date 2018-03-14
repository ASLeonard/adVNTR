#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

from advntr.advntr_commands import genotype, view_model, not_implemented_command
from advntr import settings


class CustomHelpFormatter(argparse.HelpFormatter):
    def __init__(self, prog):
        super(CustomHelpFormatter, self).__init__(prog, max_help_position=40, width=80)

    def _format_action_invocation(self, action):
        default = self._metavar_formatter(action, action.dest)
        args_string = self._format_args(action, default)
        return '/'.join(action.option_strings) + ' ' + args_string


def run_advntr():
    description = '=======================================================\n' \
                  'adVNTR 1.0.0: Genopyting tool for VNTRs\n' \
                  '=======================================================\n' \
                  'Source code: https://github.com/mehrdadbakhtiari/adVNTR\n' \
                  'Instructions: http://advntr.readthedocs.io\n' \
                  '-------------------------------------------------------\n'
    help = 'Command: genotype\tfind RU counts and mutations in VNTRs\n' \
           '         viewmodel\tview existing models in database\n' \
           '         addmodel\tadd custom VNTR to the database\n' \
           '         delmodel\tremove a model from database\n'

    usage = '\r{}\nusage: %(prog)s <command> [options]\n\n\r{}\r{}'.format(description.ljust(len('usage:')), help, '\n')
    parser = argparse.ArgumentParser(usage=usage, add_help=False)
    subparsers = parser.add_subparsers(title='Commands', dest='command')

    fmt = lambda prog: CustomHelpFormatter(prog)
    genotype_parser = subparsers.add_parser('genotype', usage='advntr genotype [options]', formatter_class=fmt)
    genotype_parser.add_argument('-a', '--alignment_file', type=str, help='Alignment file in BAM format or SAM format',
                                 metavar='<file>')
    genotype_parser.add_argument('-f', '--fasta', type=str, help='Fasta file containing raw reads', metavar='<file>')
    genotype_parser.add_argument('-fs', '--frameshift', action='store_true',
                                 help='set this flag to search for frameshifts in VNTR instead of copy number.'
                                 '\n    * Supported VNTR IDs: %s' % settings.FRAMESHIFT_VNTRS)
    genotype_parser.add_argument('-e', '--expansion', action='store_true',
                                 help='set this flag to determine long expansion from PCR-free data')
    genotype_parser.add_argument('-c', '--coverage', type=float, metavar='<float>',
                                 help='average sequencing coverage in PCR-free sequencing')
    genotype_parser.add_argument('-p', '--pacbio', action='store_true',
                                 help='set this flag if input file contains PacBio reads instead of Illumina reads')
    genotype_parser.add_argument('-n', '--nanopore', action='store_true',
                                 help='set this flag if input file contains Nanopore MinION reads instead of Illumina')
    genotype_parser.add_argument('--working_directory', type=str, metavar='<path>',
                                 help='working directory for creating temporary files needed for computation')
    genotype_parser.add_argument('-m', '--models', type=str, metavar='<file>', default='vntr_data/hg19_VNTRs.db',
                                 help='file containing VNTRs information [%(default)s]')
    genotype_parser.add_argument('-t', '--threads', type=int, metavar='<int>', default=4,
                                 help='number of threads [%(default)s]')
    genotype_parser.add_argument('-vid', '--vntr_id', type=str, metavar='<text>', default=None,
                                 help='comma-separated list of VNTR IDs')
    genotype_parser.add_argument('-naive', '--naive', action='store_true', default=False,
                                 help='use naive approach for PacBio reads')

    viewmodel_parser = subparsers.add_parser('viewmodel', usage='advntr viewmodel [options]', formatter_class=fmt)
    viewmodel_parser.add_argument('-g', '--gene', type=str, default='', metavar='<text>',
                                  help='comma-separated list of Gene Names')
    viewmodel_parser.add_argument('-p', '--pattern', type=str, default=None, metavar='<text>',
                                  help='repeating pattern of VNTR in forward (5\' to 3\') direction')

    addmodel_parser = subparsers.add_parser('addmodel', usage='advntr addmodel [options]')
    delmodel_parser = subparsers.add_parser('delmodel', usage='advntr delmodel [options]')

    args = parser.parse_args()
    if args.command == 'genotype':
        genotype(args, genotype_parser)
    elif args.command == 'viewmodel':
        view_model(args, viewmodel_parser)
    elif args.command == 'addmodel':
        not_implemented_command(parser, args.command)
    elif args.command == 'delmodel':
        not_implemented_command(parser, args.command)
    else:
        parser.error('Please specify a valid command')

if __name__ == '__main__':
    run_advntr()
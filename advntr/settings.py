import socket


HG19_DIR = './hg19_chromosomes/'
CHROMOSOMES = ['chr' + str(chr_number) for chr_number in list(range(1, 23))] + ['chrX', 'chrY']
GENOME_LENGTH = 3100000000
MAX_INSERT_SIZE = 1000

USE_TRAINED_HMMS = False
ILLUMINA_DEFAULT_MODELS_FILE = 'vntr_data/hg19_selected_VNTRs_Illumina.db'
PACBIO_DEFAULT_MODELS_FILE = 'vntr_data/hg19_selected_VNTRs_Pacbio.db'
TRAINED_MODELS_DB = ILLUMINA_DEFAULT_MODELS_FILE
TRAINED_HMMS_DIR = 'vntr_data/'

SCORE_FINDING_READS_FRACTION = 0.0001
SCORE_SELECTION_PERCENTILE = 0
SAVE_SCORE_DISTRIBUTION = False
SCALE_SCORES = True

GC_CONTENT_WINDOW_SIZE = 100
GC_CONTENT_BINS = 10
OUTLIER_COVERAGE = 200

QUALITY_SCORE_CUTOFF = 20
LOW_QUALITY_BP_TO_DISCARD_READ = 0.10
MAPQ_CUTOFF = 0

MAX_ERROR_RATE = 0.05

hostname = socket.gethostname()
if hostname.startswith('genome'):
    CORES = 20
else:
    CORES = 8

FRAMESHIFT_VNTRS = [25561, 519759]
LONG_VNTRS = [70186]

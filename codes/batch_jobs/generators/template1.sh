#!/bin/bash -l
#
# DARWIN job script template, generated 2022-05-05T10:14:37-0400
#
# Sections of this script that can/should be edited are delimited by a
# [EDIT] tag.  All Slurm job options are denoted by a line that starts
# with "#SBATCH " followed by flags that would otherwise be passed on
# the command line.  Slurm job options can easily be disabled in a
# script by inserting a space in the prefix, e.g. "# SLURM " and
# reenabled by deleting that space.
#
# This is a batch job template for a program using a single processor
# core/thread (a serial job).
#
#SBATCH --nodes=1 --ntasks=1 --cpus-per-task=50
# SBATCH --nodes=1 --ntasks=1 --cpus-per-task=1
# SBATCH --nodes=1 --ntasks=1 --cpus-per-task=16
#
# [EDIT] All jobs have memory limits imposed.  The default is 1 GB per
#        CPU allocated to the job.  The default can be overridden either
#        with a per-node value (--mem) or a per-CPU value (--mem-per-cpu)
#        with unitless values in MB and the suffixes K|M|G|T denoting
#        kibi, mebi, gibi, and tebibyte units.  Delete the space between
#        the "#" and the word SBATCH to enable one of them:
#
# SBATCH --mem=8G
# SBATCH --mem-per-cpu=1024M
#
# [EDIT] Each node in the cluster has local scratch disk of some sort
#        that is always mounted as /tmp.  Per-job temporary directories
#        are automatically created and destroyed by Slurm and can be
#        referenced via the $TMPDIR environment variable.  To ensure a
#        minimum amount of free space when your job is scheduled, the
#        --tmp option can be used; it has the same behavior unit-wise as
#        --mem and --mem-per-cpu.  Delete the space between the "#" and the
#        word SBATCH to enable:
#
# SBATCH --tmp=24G
#
# [EDIT] It can be helpful to provide a descriptive (terse) name for
#        the job (be sure to use quotes if there's whitespace in the
#        name):
#
#SBATCH --job-name=compiler_batch
#
# [EDIT] The partition determines which nodes can be used and with what
#        maximum runtime limits, etc.  Partition limits can be displayed
#        with the "sinfo --summarize" command.
#
#        PLEASE NOTE:  On DARWIN every job is **required** to include the
#                      --partition flag in its submission!
#
#SBATCH --partition=xlarge-mem
# SBATCH --partition=standard
# [EDIT] Jobs that will run in one of the GPU partitions can request GPU
#        resources using ONE of the following flags:
#
#          --gpus=<count>
#              <count> GPUs total for the job, regardless of node count
#          --gpus-per-node=<count>
#              <count> GPUs are required on each node allocated to the job
#          --gpus-per-socket=<count>
#              <count> GPUs are required on each socket allocated to the
#              job
#          --gpus-per-task=<count>
#              <count> GPUs are required for each task in the job
#
#       PLEASE NOTE:  On DARWIN the --gres flag should NOT be used to
#                     request GPU resources.  The GPU type will be
#                     inferred from the partition to which the job is
#                     submitted if not specified.
#
# SBATCH --gpus=1
# SBATCH --gpus-per-task=1
# SBATCH --gpus-per-node=1
# SBATCH --gpus-per-socket=2
#
# [EDIT] The maximum runtime for the job; a single integer is interpreted
#        as a number of minutes, otherwise use the format
#
#          d-hh:mm:ss
#
#        Jobs default to the default runtime limit of the chosen partition
#        if this option is omitted.
#
#SBATCH --time=0-00:20:00
#
#        You can also provide a minimum acceptable runtime so the scheduler
#        may be able to run your job sooner.  If you do not provide a
#        value, it will be set to match the maximum runtime limit (discussed
#        above).
#
# SBATCH --time-min=0-01:00:00
#
# [EDIT] By default SLURM sends the job's stdout to the file "slurm-<jobid>.out"
#        and the job's stderr to the file "slurm-<jobid>.err" in the working
#        directory.  Override by deleting the space between the "#" and the
#        word SBATCH on the following lines; see the man page for sbatch for
#        special tokens that can be used in the filenames:
#

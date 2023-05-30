import shutil
import shlex
import os
from subprocess import check_output

mutations = [
               'I93A',
               'F216A',
               'L48A',
               'V60A',
               'W101A',
               'R224A',
               'T213A',
               'E215A',
               'F14A',
               'V134A',
               'L16A',
               'A95G',
               'W132A',
               'S133A',
               'L103A',
               'L62A',
               'R217A',
               'V94A',
            ]
systems=['L']
systems.append('apo')
executable = 'python3 /home/JM/program/qfile/qligfep-geng-ok/QresFEP.py' + ' '
options = {
           '-f'    : 'OPLS2015',      # Forcefield
           '-l'     : '1',             # starting point
           '-T'     : '298',           # Temperature
           '-r'     : '10',            # Total repeats
           '-s'     : 'linear',        # Sampling type
           '-w'     : '20',            # Number of windows
           '-C'     : 'KEBNE',         # Cluster to run on
          }

rootdir = os.getcwd()
aladir = rootdir + '/alaSCAN'

for system in systems:
    for mutation in mutations:
        options['-S'] = 'protein'
        options['-m'] = mutation
        if system != 'apo':
            options['-c'] = system
        elif options.has_key('-c'):
            options.pop('-c')
        # Run commands and save to directory
        option_list = ' '.join(['{} {}'.format(k,v) for k,v in options.items()])
        args = shlex.split(executable + option_list)
        out = check_output(args)
        fepdir = 'FEP_{}'.format(mutation)
        tgtdir = aladir + '/' + system + '/' + fepdir
        print(fepdir, tgtdir)
        shutil.move(fepdir, tgtdir)

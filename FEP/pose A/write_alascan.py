import shutil
import shlex
import os
from subprocess import check_output

mutations = [
               'I93A',
               'L214A',
               'E215A',
               'F216A',
               'L48A',
               'W101A',
               'V60A',
               'R217A',
               'Q50A',
               'S218A',
               'F14A',
               'V134A',
               'L62A',
               'A58G',
               'L16A',
               'L103A',
               'W132A',
               'A95G',
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

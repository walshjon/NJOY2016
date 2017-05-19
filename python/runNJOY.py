#!/usr/bin/env python

import os
from os import environ as env
import shutil as sh
import replace as r
from subprocess import call

env['EXE']         = '/home/walshjon/bin/xnjoy'
env['NJOY_VERS']   = 'NJOY2012.50'
env['AUTHOR']      = 'Walsh, MIT/LANL'
env['DATE']        = 'March, 2016'

env['EVALUATION']  = 'cielo'
env['ISO']         = 'Fe-56'
endf6f             = 'fe56v02.endf'
env['ENDF6_DIR']   = env['HOME']+'/data/evaluations/'+env['EVALUATION']+'/neutrons/'
env['WORK_DIR']    = env['HOME']+'/runs/ace/'

ace_ext = [
'.03'
]
"""
'.00',
'.13',
'.14',
'.15',
'.16',
'.17',
'.18'
]
'.03',
'.04',
'.05',
'.06',
'.07',
'.08',
'.09',
'.10',
'.11',
'.12',
'.13',
'.14',
'.15',
'.16',
'.17',
'.18',
'.19',
'.20',
'.21',
'.22',
'.23',
'.24'
"""

Ts = [
'300.0'
]
"""
'0.0',
'1000.0',
'10000.0',
'100000.0',
'1000000.0',
'10000000.0',
'100000000.0'
'350.0',
'450.0',
'550.0',
'650.0',
'750.0',
'850.0',
'950.0',
'1050.0',
'1150.0',
'1250.0',
'1350.0',
'1450.0',
'1550.0',
'1650.0',
'1750.0',
'1850.0',
'1950.0',
'2050.0',
'2150.0',
'2250.0',
'2350.0',
'2450.0'
"""

MATs = {'Be-9':425,
        'C':600,
        'Fe-54':2625,
        'Fe-56':2631,
        'Fe-57':2634,
        'Fe-58':2637,
        'W-180':7425,
        'W-182':7431,
        'W-183':7434,
        'W-184':7437,
        'W-186':7443,
        'Au-197':7925,
        'Hg-196':8025,
        'Hg-198':8031,
        'Hg-199':8034,
        'Hg-200':8037,
        'Hg-201':8040,
        'Hg-202':8043,
        'Hg-204':8049,
        'Pb-208':8237,
        'U-234':9225,
        'U-235':9228,
        'U-236':9231,
        'U-238':9237,
        'Pu-239':9437,
        'Pu-240':9440}
As = {'Be-9':9,
      'C':12,
      'Fe-54':54,
      'Fe-56':56,
      'Fe-57':57,
      'Fe-58':58,
      'W-180':180,
      'W-182':182,
      'W-183':183,
      'W-184':184,
      'W-186':186,
      'Au-197':197,
      'Hg-196':196,
      'Hg-198':198,
      'Hg-199':199,
      'Hg-200':200,
      'Hg-201':201,
      'Hg-202':202,
      'Hg-204':204,
      'Pb-208':208,
      'U-234':234,
      'U-235':235,
      'U-236':236,
      'U-238':238,
      'Pu-239':239,
      'Pu-240':240}
Zs = {'Be-9':4,
      'C':6,
      'Fe-54':26,
      'Fe-56':26,
      'Fe-57':26,
      'Fe-58':26,
      'W-180':74,
      'W-182':74,
      'W-183':74,
      'W-184':74,
      'W-186':74,
      'Au-197':79,
      'Hg-196':80,
      'Hg-198':80,
      'Hg-199':80,
      'Hg-200':80,
      'Hg-201':80,
      'Hg-202':80,
      'Hg-204':80,
      'Pb-208':82,
      'U-234':92,
      'U-235':92,
      'U-236':92,
      'U-238':92,
      'Pu-239':94,
      'Pu-240':94}
Xs = {'1':'H',                                             
      '2':'He',                                             
      '3':'Li',                                             
      '4':'Be',                                             
      '5':'B',                                             
      '6':'C',                                             
      '7':'N',                                             
      '8':'O',                                             
      '9':'F',                                             
      '10':'Ne',                                            
      '11':'Na',                                            
      '12':'Mg',                                            
      '13':'Al',                                            
      '14':'Si',                                            
      '15':'P',                                            
      '16':'S',                                            
      '17':'Cl',                                            
      '18':'Ar',                                            
      '19':'K',                                            
      '20':'Ca',                                            
      '21':'Sc',                                            
      '22':'Ti',                                            
      '23':'V',                                            
      '24':'Cr',                                            
      '25':'Mn',                                            
      '26':'Fe',                                            
      '27':'Co',                                            
      '28':'Ni',                                            
      '29':'Cu',                                            
      '30':'Zn',                                            
      '31':'Ga',                                            
      '32':'Ge',                                            
      '33':'As',                                            
      '34':'Se',                                            
      '35':'Br',                                            
      '36':'Kr',                                            
      '37':'Rb',                                            
      '38':'Sr',                                            
      '39':'Y',                                            
      '40':'Zr',                                            
      '41':'Nb',                                            
      '42':'Mo',                                            
      '43':'Tc',                                            
      '44':'Ru',                                            
      '45':'Rh',                                            
      '46':'Pd',                                            
      '47':'Ag',                                            
      '48':'Cd',                                            
      '49':'In',                                            
      '50':'Sn',                                            
      '51':'Sb',                                            
      '52':'Te',                                            
      '53':'I',                                            
      '54':'Xe',                                            
      '55':'Cs',                                            
      '56':'Ba',                                            
      '57':'La',
      '58':'Ce',
      '59':'Pr',
      '60':'Nd',
      '61':'Pm',
      '62':'Sm',
      '63':'Eu',
      '64':'Gd',
      '65':'Tb',
      '66':'Dy',
      '67':'Ho',
      '68':'Er',
      '69':'Tm',
      '70':'Yb',
      '71':'Lu',
      '72':'Hf',
      '73':'Ta',
      '74':'W',
      '75':'Re',
      '76':'Os',
      '77':'Ir',
      '78':'Pt',
      '79':'Au',
      '80':'Hg',
      '81':'Tl',
      '82':'Pb',
      '83':'Bi',
      '84':'Po',
      '85':'At',
      '86':'Rn',
      '87':'Fr',
      '88':'Ra',
      '89':'Ac',
      '90':'Th',
      '91':'Pa',
      '92':'U',
      '93':'Np',
      '94':'Pu',
      '95':'Am',
      '96':'Cm',
      '97':'Bk',
      '98':'Cf',
      '99':'Es',
      '100':'Fm',
      '101':'Md',
      '102':'No',
      '103':'Lr',
      '104':'Rf',
      '105':'Db',
      '106':'Sg',
      '107':'Bh',
      '108':'Hs',
      '109':'Mt',
      '110':'Ds',
      '111':'Rg',
      '112':'Cn',
      '113':'A3',
      '114':'Fl',
      '115':'Uup',
      '116':'Lv',
      '117':'Uus',
      '118':'Uuo'}

for iT in range(0,len(Ts)):
    MAT = str(MATs[env['ISO']])
    A   = str(As[env['ISO']])
    Z   = str(Zs[env['ISO']])
    X   = str(Xs[Z])
    env['TEMPERATURE'] = Ts[iT]
    env['ACE_EXT']     = ace_ext[iT]
    env['TARGET_DIR']  = env['WORK_DIR']+env['EVALUATION']+'/'+env['TEMPERATURE']+'/'+env['ISO']

    if not os.path.exists(env['TARGET_DIR']):
        os.makedirs(env['TARGET_DIR'])

    f = env['WORK_DIR']+'njoy.sh'
    sh.copy(f, env['TARGET_DIR'])
    f = env['TARGET_DIR']+'/njoy.sh'
    env['NJI'] = env['WORK_DIR']+'/template.nji'
    sh.copy(env['NJI'], env['TARGET_DIR']+'/'+env['ISO']+'.nji')
    env['NJI'] = env['TARGET_DIR']+'/'+env['ISO']+'.nji'

    r.replace(f, '$TARGET_DIR', env['TARGET_DIR'])
    r.replace(f, '$NJI', env['NJI'])
    r.replace(f, '$EXE', env['EXE'])

    r.replace(env['NJI'], '$MAT', MAT)
    r.replace(env['NJI'], '$NUCLIDE', env['ISO'])
    r.replace(env['NJI'], '$TEMPERATURE', env['TEMPERATURE'])
    r.replace(env['NJI'], '$ACE_EXT', env['ACE_EXT'])
    r.replace(env['NJI'], '$DATE', env['DATE'])
    r.replace(env['NJI'], '$NJOY_VERS', env['NJOY_VERS'])
    r.replace(env['NJI'], '$AUTHOR', env['AUTHOR'])
    r.replace(env['NJI'], '$EVALUATION', env['EVALUATION'])
    sh.copy(env['ENDF6_DIR']+endf6f, env['TARGET_DIR']+'/tape20')
    os.chdir(env['TARGET_DIR'])
    call(['qsub','njoy.sh'])

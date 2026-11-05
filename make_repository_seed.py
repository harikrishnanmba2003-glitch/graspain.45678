#!/usr/bin/env python3
"""Usage: python make_repository_seed.py <target-repository-folder>
Builds the repository skeleton from this zip: CLAUDE.md, read-only /reference, docs/build-packs, docs/prompts, docs/tests."""
import os,shutil,sys,glob
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if len(sys.argv)<2: sys.exit(__doc__)
t=sys.argv[1]
def cp(src,dst):
    os.makedirs(os.path.dirname(dst),exist_ok=True);shutil.copy2(src,dst)
cp(os.path.join(root,'00_Start_Here','CLAUDE.md'),os.path.join(t,'CLAUDE.md'))
cp(os.path.join(root,'00_Start_Here','Volume00_Master_Decision_Record.docx'),os.path.join(t,'docs','build-packs','Volume00_Master_Decision_Record.docx'))
for d in sorted(glob.glob(os.path.join(root,'[0-9][0-9]_*'))):
    n=os.path.basename(d)
    if n[:2] in ('00','12'): continue
    for f in glob.glob(os.path.join(d,'1_Build_Pack','*.docx')): cp(f,os.path.join(t,'docs','build-packs',os.path.basename(f)))
    for f in glob.glob(os.path.join(d,'2_Prompts','*.txt')): cp(f,os.path.join(t,'docs','prompts',n,os.path.basename(f)))
    for f in glob.glob(os.path.join(d,'3_Acceptance_Tests','*.csv')): cp(f,os.path.join(t,'docs','tests',os.path.basename(f)))
    mod=int(n[:2])-1
    if 1<=mod<=9:
        for f in glob.glob(os.path.join(d,'4_Reference_Screens','*')): cp(f,os.path.join(t,'reference','screens','module-%d'%mod,os.path.basename(f)))
for f in glob.glob(os.path.join(root,'12_Shared_Reference','prototype_suite','*')): cp(f,os.path.join(t,'reference','prototype',os.path.basename(f)))
for f in glob.glob(os.path.join(root,'12_Shared_Reference','data','*')): cp(f,os.path.join(t,'reference','data',os.path.basename(f)))
open(os.path.join(t,'reference','README.md'),'w').write('# /reference is READ-ONLY evidence. Never edit it. Open prototype/Graspin_Suite.html. Shared logins: data/SHARED_LOGINS.csv\n')
print('Repository seed ready at',t)

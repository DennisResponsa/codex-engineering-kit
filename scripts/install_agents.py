"""Install all CEK roles into a chosen project's native .codex configuration."""
from pathlib import Path
import argparse,json,re,shutil,tomllib
ROOT=Path(__file__).resolve().parents[1]
START='# BEGIN CODEX ENGINEERING KIT';END='# END CODEX ENGINEERING KIT'
def install(project,dry_run=False):
 project=Path(project).expanduser().resolve()
 if not project.is_dir():raise ValueError('Project directory must already exist')
 folder=project/'.codex';config=folder/'config.toml'
 if folder.is_symlink() or config.is_symlink():raise ValueError('Refusing symlink configuration')
 original=config.read_text() if config.exists() else ''
 if original.count(START)!=original.count(END) or original.count(START)>1:raise ValueError('Invalid managed block')
 clean=re.sub(re.escape(START)+r'.*?'+re.escape(END)+'\n?', '',original,flags=re.S)
 parsed=tomllib.loads(clean)
 catalog=json.loads((ROOT/'catalog.json').read_text())
 block=[START]
 destination=folder/'agents/cek'
 for ancestor in [folder/'agents',destination]:
  if ancestor.is_symlink():raise ValueError('Refusing symlink role directory')
 for entry in catalog['agents']:
  role=entry['role'];source=ROOT/entry['file'];tomllib.loads(source.read_text())
  if role in parsed.get('agents',{}):raise ValueError('Existing role collision: '+role)
  target=destination/source.name
  if target.is_symlink():raise ValueError('Refusing symlink role: '+str(target))
  if target.exists() and START not in original:raise ValueError('Unmanaged role file collision: '+str(target))
  block+=['[agents.'+role+']','description = '+json.dumps(entry['description'],ensure_ascii=False),'config_file = '+json.dumps('agents/cek/'+source.name)]
 block+=[END]
 proposed=clean.rstrip()+'\n\n'+'\n'.join(block)+'\n';tomllib.loads(proposed)
 if not dry_run:
  folder.mkdir(exist_ok=True);destination.mkdir(parents=True,exist_ok=True)
  backup=folder/'config.toml.before-cek'
  if config.exists() and not backup.exists():
   shutil.copy2(config,backup);backup.chmod(0o600)
  for entry in catalog['agents']:shutil.copy2(ROOT/entry['file'],destination/Path(entry['file']).name)
  config.write_text(proposed)
 return len(catalog['agents'])
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--project',required=True);ap.add_argument('--dry-run',action='store_true');a=ap.parse_args()
 print(('Would install' if a.dry_run else 'Installed'),install(a.project,a.dry_run),'Codex roles; no model/provider/permission settings changed.')

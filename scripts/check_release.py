"""Check publication boundaries; this is not a complete secret scanner."""
from pathlib import Path
import json,re,subprocess
ROOT=Path(__file__).resolve().parents[1]
def main():
 tracked=subprocess.check_output(['git','ls-files','-z'],cwd=ROOT).decode().split('\0')
 errors=[]
 for name in filter(None,tracked):
  p=ROOT/name
  if p.is_symlink():errors.append((name,'symlink'))
  if p.stat().st_size>90*1024*1024:errors.append((name,'oversized file'))
  if any(x in Path(name).parts for x in ['node_modules','.venv','__pycache__']):errors.append((name,'runtime/cache'))
  if p.name in ['auth.json','config.before.toml','AGENTS.before.md','.env']:errors.append((name,'private configuration'))
  data=p.read_bytes()
  if re.search(rb'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',data):
   # Public upstream tests intentionally contain test key markers.
   if not name.startswith('vendor/ecc/'):errors.append((name,'private key marker; review required'))
 print(json.dumps({'tracked_files':len(list(filter(None,tracked))),'findings':errors},indent=2))
 return bool(errors)
if __name__=='__main__':raise SystemExit(main())

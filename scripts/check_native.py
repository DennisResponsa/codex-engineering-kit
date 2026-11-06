"""Verify discovery with a fresh, unauthenticated temporary Codex home."""
import json,os,select,subprocess,tempfile,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main():
 with tempfile.TemporaryDirectory(prefix='cek-discovery-') as d:
  env=os.environ.copy();env['CODEX_HOME']=d
  for args in [['plugin','marketplace','add',str(ROOT)],['plugin','add','codex-engineering-kit@codex-engineering-kit']]:
   subprocess.run(['codex',*args],env=env,check=True,capture_output=True,text=True,timeout=90)
  with tempfile.TemporaryFile(mode='w+') as err:
   p=subprocess.Popen(['codex','app-server','--stdio'],env=env,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=err,text=True,bufsize=1)
   def call(i,method,params):
    p.stdin.write(json.dumps({'id':i,'method':method,'params':params})+'\n');p.stdin.flush();end=time.monotonic()+45
    while time.monotonic()<end:
     if select.select([p.stdout],[],[],1)[0]:
      line=p.stdout.readline()
      if not line:raise RuntimeError('Codex server stopped')
      r=json.loads(line)
      if r.get('id')==i:
       if 'error' in r:raise RuntimeError(r['error'])
       return r['result']
    raise TimeoutError(method)
   try:
    call(1,'initialize',{'clientInfo':{'name':'cek-validation','version':'0.1.0'},'capabilities':{'experimentalApi':True}})
    p.stdin.write('{"method":"initialized","params":{}}\n');p.stdin.flush()
    result=call(2,'skills/list',{'cwds':[d],'forceReload':True})['data'][0]
    skills=[s for s in result['skills'] if s.get('pluginId')=='codex-engineering-kit@codex-engineering-kit']
    errors=result.get('errors',[])
    expected={s['name'] for s in json.loads((ROOT/'catalog.json').read_text())['skills']}
    loaded={s['name'].split(':',1)[-1] for s in skills}
    assert expected==loaded,(len(expected),len(loaded),sorted(expected-loaded))
    assert all(s['enabled'] for s in skills) and not errors,errors
    print(json.dumps({'loaded':len(skills),'enabled':sum(s['enabled'] for s in skills),'errors':errors}))
   finally:p.terminate();p.wait(timeout=10)
if __name__=='__main__':main()

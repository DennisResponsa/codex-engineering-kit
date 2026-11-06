"""Build deterministic, namespaced Codex adapters from the pinned ECC snapshot."""
from pathlib import Path
import hashlib,json,re,shutil
import yaml
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'vendor/ecc'
REV='b38be6a7f6350964d59328b52f0624e1d1d552d1'
POLICY='''## Codex execution contract

Use the current Codex session model and its native tools. Model names such as Sonnet, Opus or Haiku in source examples are not model-selection instructions. Follow the current user request and project instructions before upstream workflow defaults.

Read/Grep/Glob map to native file reading and search; Bash maps to the available shell tool. Task/Agent means authorized Codex delegation, not Claude CLI. Tool frontmatter is descriptive, not a permission grant. Do not assume slash commands or Claude lifecycle hooks exist. Use a project-supported test runner and report actual results.

Resolve bundled upstream scripts and references under the plugin's `vendor/ecc/` directory. Do not use personal `~/.claude` paths or unset `CLAUDE_*` variables in Codex. Inspect example commands and translate their intent before running them. Prefer existing connected tools. Missing external services must be reported, not simulated.

Skills that specifically integrate Anthropic or another provider still require that provider; do not call those services or switch models unless requested. Do not run upstream installers, auto-updaters, learning loops, background jobs, commits, deployments or messages solely because an example suggests them. Use this distribution's documented installer for its roles.

'''
def split(p):
 text=p.read_text();parts=text.split('---',2)
 if len(parts)!=3:raise ValueError(f'Missing frontmatter: {p}')
 meta=yaml.safe_load(parts[1])
 if not isinstance(meta,dict):raise ValueError(p)
 return meta,parts[2].strip()
def normalize(text):
 # Change host identity, not product-specific API names, URLs or source citations.
 text=text.replace('Claude Code sessions','Codex sessions').replace("Claude Code session's", "Codex session's")
 return text

def main():
 skills=ROOT/'skills';agents=ROOT/'agents';skills.mkdir(exist_ok=True);agents.mkdir(exist_ok=True)
 manifest={'upstream':'https://github.com/affaan-m/ECC','revision':REV,'skills':[],'agents':[]}
 for source in sorted((SOURCE/'skills').glob('*/SKILL.md')):
  meta,body=split(source);name=meta['name'];assert name==source.parent.name
  target=skills/name
  shutil.copytree(source.parent,target,dirs_exist_ok=True)
  desc=normalize(str(meta['description'])).replace('Claude Code','Codex')
  front={'name':name,'description':desc,'metadata':{'origin':'ECC','upstream_revision':REV,'adapter':'codex-engineering-kit-0.1.0'}}
  if 'license' in meta:front['license']=meta['license']
  (target/'SKILL.md').write_text('---\n'+yaml.safe_dump(front,sort_keys=False,allow_unicode=True)+'---\n\n'+POLICY+normalize(body)+'\n')
  # Drop upstream UI provider/tool routing; skills remain auto-discoverable.
  ui=target/'agents/openai.yaml'
  if ui.exists():ui.unlink()
  manifest['skills'].append({'name':name,'source':str(source.relative_to(ROOT)),'sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'host_references':bool(re.search(r'Claude|CLAUDE_|~/.claude',body)),'external_credentials':sorted(set(re.findall(r'\b[A-Z][A-Z_]+(?:API_KEY|TOKEN|SECRET_KEY)\b',body)))})
 for command in json.loads((ROOT/'scripts/migrated_commands.json').read_text()):
  source=SOURCE/'commands'/(command+'.md');meta,body=split(source)
  name='source-command-'+command;target=skills/name;target.mkdir(exist_ok=True)
  desc=str(meta.get('description','Run the '+command+' workflow in Codex')).replace('Claude Code','Codex')
  front={'name':name,'description':desc,'metadata':{'origin':'ECC command','upstream_revision':REV,'adapter':'codex-engineering-kit-0.1.0'}}
  (target/'SKILL.md').write_text('---\n'+yaml.safe_dump(front,sort_keys=False,allow_unicode=True)+'---\n\n'+POLICY+normalize(body)+'\n')
  manifest['skills'].append({'name':name,'source':str(source.relative_to(ROOT)),'sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'host_references':bool(re.search(r'Claude|CLAUDE_|~/.claude',body)),'external_credentials':[],'migrated_command':True})
 for source in sorted((SOURCE/'agents').glob('*.md')):
  meta,body=split(source);name=meta.get('name',source.stem)
  role='cek_'+name.replace('-','_')
  text=POLICY+'## Specialist guidance\n\n'+normalize(body)+'\n'
  (agents/(name+'.toml')).write_text('developer_instructions = '+json.dumps(text,ensure_ascii=False)+'\n')
  manifest['agents'].append({'name':name,'role':role,'description':str(meta['description']).replace('Claude Code','Codex'),'file':'agents/'+name+'.toml','source':str(source.relative_to(ROOT)),'sha256':hashlib.sha256(source.read_bytes()).hexdigest()})
 (ROOT/'catalog.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
 (ROOT/'docs/CATALOG.md').write_text('# Catalog\n\nGenerated from the pinned ECC snapshot. All entries load as Codex guidance; external dependencies require separate configuration and testing.\n\n## Skills\n\n'+'\n'.join('- `'+x['name']+'`'+(' — source contains host-specific examples' if x['host_references'] else '') for x in manifest['skills'])+'\n\n## Agent roles\n\n'+'\n'.join('- `'+x['role']+'`' for x in manifest['agents'])+'\n')
 print(f"Built {len(manifest['skills'])} skills and {len(manifest['agents'])} agent roles")
if __name__=='__main__':main()

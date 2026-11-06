import importlib.util,json, tempfile,tomllib,unittest,hashlib
from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('installer',ROOT/'scripts/install_agents.py');installer=importlib.util.module_from_spec(spec);spec.loader.exec_module(installer)
class DistributionTests(unittest.TestCase):
 def test_catalog_and_sources(self):
  c=json.loads((ROOT/'catalog.json').read_text());self.assertEqual(len(c['skills']),350);self.assertEqual(len(c['agents']),71)
  for entry in c['skills']+c['agents']:
   self.assertEqual(hashlib.sha256((ROOT/entry['source']).read_bytes()).hexdigest(),entry['sha256'])
 def test_skill_frontmatter(self):
  names=[]
  for p in (ROOT/'skills').glob('*/SKILL.md'):
   fm=yaml.safe_load(p.read_text().split('---',2)[1]);names.append(fm['name']);self.assertEqual(fm['name'],p.parent.name);self.assertTrue(fm['description']);self.assertNotIn('model',fm);self.assertIn('Codex execution contract',p.read_text())
  self.assertEqual(len(names),350);self.assertEqual(len(set(names)),350)
 def test_agents_inherit_model_and_permissions(self):
  files=list((ROOT/'agents').glob('*.toml'));self.assertEqual(len(files),71)
  for p in files:
   cfg=tomllib.loads(p.read_text());self.assertEqual(set(cfg),{'developer_instructions'});self.assertIn('Codex execution contract',cfg['developer_instructions'])
 def test_plugin_has_no_auto_execution(self):
  p=json.loads((ROOT/'.codex-plugin/plugin.json').read_text());self.assertEqual(p['skills'],'./skills/');self.assertNotIn('hooks',p);self.assertNotIn('mcpServers',p)
 def test_install_preserves_config_and_is_idempotent(self):
  with tempfile.TemporaryDirectory() as d:
   root=Path(d);(root/'.codex').mkdir();p=root/'.codex/config.toml';before='model = "user-selected-model"\n[features]\nmulti_agent = false\n';p.write_text(before)
   self.assertEqual(installer.install(root),71);first=p.read_text();self.assertEqual(installer.install(root),71);self.assertEqual(first,p.read_text());cfg=tomllib.loads(first);self.assertEqual(cfg['model'],'user-selected-model');self.assertFalse(cfg['features']['multi_agent']);self.assertEqual(len(cfg['agents']),71)
   for role in cfg['agents'].values():self.assertTrue((root/'.codex'/role['config_file']).is_file())
 def test_dry_run_does_not_write(self):
  with tempfile.TemporaryDirectory() as d:
   installer.install(d,True);self.assertFalse((Path(d)/'.codex').exists())
 def test_collision_is_rejected(self):
  with tempfile.TemporaryDirectory() as d:
   root=Path(d);(root/'.codex').mkdir();p=root/'.codex/config.toml';role=json.loads((ROOT/'catalog.json').read_text())['agents'][0]['role'];before='[agents.'+role+']\ndescription="mine"\n';p.write_text(before)
   with self.assertRaises(ValueError):installer.install(root)
   self.assertEqual(p.read_text(),before)
 def test_symlink_destination_is_rejected(self):
  with tempfile.TemporaryDirectory() as d,tempfile.TemporaryDirectory() as other:
   root=Path(d);(root/'.codex').mkdir();(root/'.codex/agents').symlink_to(other,target_is_directory=True)
   with self.assertRaises(ValueError):installer.install(root)
   self.assertEqual(list(Path(other).iterdir()),[])
if __name__=='__main__':unittest.main()

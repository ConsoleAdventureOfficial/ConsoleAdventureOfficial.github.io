import os
import json
import base64
import shutil


output = {}

main_dir = "mods/"
dirs = [f for f in os.listdir(main_dir) if os.path.isdir(os.path.join(main_dir, f))]

builds = {}
bins = {}

for d in dirs:
	with open(main_dir + d + "/build.json", encoding = 'utf-8') as f:
		builds[d] = json.loads(f.read())
		print(builds[d])
	shutil.make_archive("tmp/"+d, 'zip', main_dir + d)
	with open("tmp/"+d+".zip", "rb") as f:
		bins[d] = base64.b64encode(f.read())

with open("mods.html", "w", encoding='utf8') as f:
	f.write(json.dumps(builds, ensure_ascii=False))

for b in bins:
	with open("bins/"+b+".html", "wb") as f:
		f.write(bins[b])

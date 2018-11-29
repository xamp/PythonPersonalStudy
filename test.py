import re as re
import os as os

pattern1 = re.compile(">[a-zA-Z0-9가-힣]+<")
pattern2 = re.compile("confirm(\"[a-zA-Z0-9가-힣]+\")")

re.compile(pattern2)

path = os.listdir(".")
for files in path:
  fname, ext = os.path.splitext(files)
  if (ext == ".txt"):
    
    with open(files, encoding='UTF8') as fin, open(fname+'_out'+ext, 'w', encoding='UTF8') as fout:
      
      for line in fin:
        re.compile(pattern1)
        matchObject1 = re.findall(pattern1, line)
        if matchObject1:
          for match1 in matchObject1:
            fout.write(re.sub(pattern1, ">'||get_fn('"+match1+"')||'<", line))
        else:
          re.compile(pattern2)
          matchObject2 = re.findall(pattern2, line)
          if matchObject2:
            for match2 in matchObject2:
              fout.write(re.sub(pattern2, "confirm(\"'||get_fn('"+match2+"')||'\")\)", line))
          else:
            fout.write(line)

    fout.close()          

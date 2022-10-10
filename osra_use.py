import subprocess
from rdkit.Chem import Draw
import rdkit.Chem as Chem
from rdkit.Chem.Draw.MolDrawing import DrawingOptions #Only needed if modifying defaults
cml="osra 1.png"
nowtime = subprocess.run(cml, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
print(nowtime.stdout)
result = nowtime.stdout
result=result.decode().split("\n")
for index,mol in enumerate(result[:-1]):
    opts = DrawingOptions()
    opts.atomLabelFontSize = 400
    opts.includeAtomNumbers = True
    opts.dblBondLengthFrac = 0.8
    opts.includeAtomNumbers = True
    opts.dotsPerAngstrom = 1000

    m = Chem.MolFromSmiles(mol)
    draw = Draw.MolToImage(m, options=opts, size=(500, 500))
    draw.save(str(index) + '.jpg')

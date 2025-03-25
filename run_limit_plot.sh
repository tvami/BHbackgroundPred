# !/bin/bash

nModel=2
nExtra=6

MDtev=9

MDgev=$((MDtev*1000))
output_dir=rpfExpo_BinningV5_Blind_InV18_Multi4_FullScan_B${nModel}_n${nExtra}_MD${MDtev}TeV

cmsenv
source twoD-env/bin/activate

echo "Running runWith1DVanilla.py with output directory: $output_dir"
python3 runWith1DVanilla.py $output_dir config_STMax13TeV_Multi4_BinningV5_InputV18_Blind_FullScan.json

echo "Running set_limit_general.py with output directory: $output_dir"
python3 set_limit_general.py -s signals_txt/signals_B${nModel}_n${nExtra}_MD${MDgev}.txt -l 137.6 -p BH -x BH -d 1 -m BH --outdir $output_dir
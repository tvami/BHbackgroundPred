# !/bin/bash

output_dir=$1
MDgev=$2

cmsenv
source twoD-env/bin/activate

echo "Running runWith1DVanilla.py with output directory: $output_dir"
python3 runWith1DVanilla.py $output_dir config_STMax13TeV_Multi4_BinningV5_InputV15_Blind_FullScan.json

echo "Running set_limit_general.py with output directory: $output_dir"
python3 set_limit_general.py -s signals_txt/signals_BH1_MD$MDgev.txt -l 137.6 -p BH -x BH -d 1 -m BH --outdir $output_dir
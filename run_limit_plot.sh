# !/bin/bash

templete_dir=$1
output_dir=$2
MDgev=$3

cmsenv
source twoD-env/bin/activate

python3 runWith1DVanilla.py $output_dir config_STMax13TeV_Multi4_BinningV5_InputV16_Blind_FullScan.json

cd $output_dir
cp ../$templete_dir/CMS_lumi.py .
cp ../$templete_dir/tdrstyle.py .
cp ../$templete_dir/header.py .
cp ../$templete_dir/set_limit.py .
cp ../signals_txt/signals_BH1_MD$MDgev.txt .

python3 set_limit.py -s signals_BH1_MD$MDgev.txt -l 137.6 -p BH -x BH -d 1 -m BH
cd ..

cmsenv
source twoD-env/bin/activate

dir=$1

cd $dir
echo "sampleName: $dir"
text2workspace.py card.txt
# With the option -t -1 we set Combine to fit the asimov dataset instead of actual data. 
combineTool.py -M Impacts -d card.root -t -1 --expectSignal 1 --rMin -10 -m 1 -n t1 --robustFit 1 --doInitialFit --allPars 
combineTool.py -M Impacts -d card.root -t -1 --expectSignal 1 --rMin -10 -m 1 -n t1 --robustFit 1 --doFits
combineTool.py -M Impacts -d card.root -m 1 -n t1 -o impacts_t1.json
plotImpacts.py -i impacts_t1.json -o impacts_t1
cd ..
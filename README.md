# 2DAlphabet for Black Hole search

## Set up
```
cmsrel CMSSW_14_1_0_pre4
cd CMSSW_14_1_0_pre4/src
cmsenv
git clone git@github.com:tvami/BHbackgroundPred.git .
git clone https://github.com/cms-analysis/HiggsAnalysis-CombinedLimit.git HiggsAnalysis/CombinedLimit
cd HiggsAnalysis/CombinedLimit
git fetch origin
git checkout v10.0.1
cd ../..
scram b -j
```

## Set up the enviroment (only once)
```
python3 -m virtualenv twoD-env
source twoD-env/bin/activate
cd 2DAlphabet
python3 setup.py develop
cd ..
```

## Use the enviroment 
```
cd /path/to/CMSSW_14_1_0_pre4/src
cmsenv
source twoD-env/bin/activate
```

## Example running
```
python3 runWith1DVanilla.py ConstFit_InitBinning_Integer_MatPlotLib config_ConstFit_InitBinning.json
```

## Histograms versions
- v1: was SVM cut at 0.5, QCD fake data
- v2: is cut at 0.63, QCD fake data
- v3: is cut at 0.63, but X axis going to 13 TeV, QCD fake data
- v4: is cut at 0.63, X axis going to 13 TeV, real JetHT data
- v4_blind: is cut at 0.63, X axis going to 13 TeV, real JetHT data, data blinded ST>=4 TeV
- v5: is cut at 0.5, X axis going to 13 TeV, QCD fake data
- v6: is CR (0-0.5) + VR (0.5-0.63), X axis going to 13 TeV, real JetHT data (2018)
- v7: is CR (0-0.4) + VR (0.4-0.5), X axis going to 13 TeV, real JetHT data (2018)
- v8: is cut at 0.63, X axis going to 13 TeV, real JetHT data (2018+2016preVFP+2016postVFP). —> need to fix Sphericity cut!!!
- v9: is CR (0-0.5) + VR (0.5-0.63), X axis going to 13 TeV, real JetHT data (2018+2016preVFP+2016postVFP) —> need to fix!!!
- v10: is cut at 0.63, X axis going to 13 TeV, real JetHT data (full run2) —> need to fix!!! —> Fixed!
- v11: is CR (0-0.5) + VR (0.5-0.63), X axis going to 13 TeV, real JetHT data (full run2) —> need to fix!!! —> Fixed!
- v12: is SVM cut at 0.63, apply Sphericity > 0.1, X axis going to 13 TeV, real JetHT data (full run2)
- v13: is SVM models trained on single mass points, cut at 0.63, X axis going to 13 TeV, real JetHT data (2018)
- v14: is SVM models trained on single mass points, cut at 0.63, X axis going to 13 TeV, real JetHT data (full run2)
- v15: is cut at 0.63, X axis going to 13 TeV, real JetHT data (full run2) with SVM systematics
- **v16 (nominal)**: is SVM cut at 0.63, apply Sphericity > 0.1, X axis going to 13 TeV, real JetHT data (full run2) with SVM systematics
- v17: is CR (0-0.5) + VR (0.5-0.63), apply Sphericity > 0.1, X axis going to 13 TeV, real JetHT data (full run2)

## ST Binning versions
- V1: [2000,2500,3000,3500,4000,4500,5000,5500,6000,6500,7000,7500,8000,13000]
- V2: [2000,2500,3000,3500,4000,4500,5000,5500,6000,13000]
- V3: [2000,2500,3000,3500,4000,4500,5000,5500,6000,6500,7000,7500,8000,9000,10000,11000,12000,13000]
- V4: [2000,2500,3000,3500,4000,4500,5000,5500,6000,6500,7000,7500,13000]
- **V5 (nominal)**: [2000,2500,3000,3500,4000,4500,5000,5500,6000,6500,7000,13000]
- V6: [2000,2500,3000,3500,4000,4500,5000,5500,6000,6500,13000]  --> Merge the last two bins of V5
- V7: [2000,2500,3000,3500,4000,4500,5000,5500,6000,13000]
- V8: [2000,2500,3000,3500,4000,4500,5000,5500,6000,8000,10000,13000]
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
python -m virtualenv twoD-env
source twoD-env/bin/activate
cd 2DAlphabet
python setup.py develop
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

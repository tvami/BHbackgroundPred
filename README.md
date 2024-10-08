# 2DAlphabet for Black Hole search

## Set up
```
cmsrel CMSSW_10_6_14
cd CMSSW_10_6_14/src
cmsenv
git clone git@github.com:tvami/BHbackgroundPred.git
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
cd /path/to/CMSSW_10_6_14/src
cmsenv
source twoD-env/bin/activate
```

## Example running
```
python3 runWith1DVanilla.py ConstFit_InitBinning_Integer_MatPlotLib config_ConstFit_InitBinning.json
```

# !/bin/bash

cd /home/users/dazhang/works/phaseSpace/BlackHoleSearch/CMSSW_14_1_0_pre4/src
cmsenv
source twoD-env/bin/activate
cd -

cardname=../card.txt
exp_quantile=0.84

echo "combine -M HybridNew -H AsymptoticLimits -d $cardname --LHCmode LHC-limits --plot=limit_scan_card_${exp_quantile}.png -m 125 --expectedFromGrid=${exp_quantile} --rRelAcc 0.005 --rAbsAcc 0.0005  --adaptiveToys 1 -T 500"
combine -M HybridNew -H AsymptoticLimits -d $cardname --LHCmode LHC-limits --plot=limit_scan_card_${exp_quantile}.png -m 125 --expectedFromGrid=${exp_quantile} --rRelAcc 0.005 --rAbsAcc 0.0005  --adaptiveToys 1 -T 500

cd ..


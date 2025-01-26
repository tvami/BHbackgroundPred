# !/bin/bash

cd /home/users/dazhang/works/phaseSpace/BlackHoleSearch/CMSSW_14_1_0_pre4/src
cmsenv
source twoD-env/bin/activate
cd -

cardname=../card.txt

echo "combine -M HybridNew -H AsymptoticLimits -d $cardname --LHCmode LHC-limits --plot=limit_scan_card_0.5.png -m 125 --expectedFromGrid=0.16 --rRelAcc 0.005 --rAbsAcc 0.0005  --adaptiveToys 1 -T 500"
combine -M HybridNew -H AsymptoticLimits -d $cardname --LHCmode LHC-limits --plot=limit_scan_card_0.16.png -m 125 --expectedFromGrid=0.16 --rRelAcc 0.005 --rAbsAcc 0.0005  --adaptiveToys 1 -T 500

cd ..


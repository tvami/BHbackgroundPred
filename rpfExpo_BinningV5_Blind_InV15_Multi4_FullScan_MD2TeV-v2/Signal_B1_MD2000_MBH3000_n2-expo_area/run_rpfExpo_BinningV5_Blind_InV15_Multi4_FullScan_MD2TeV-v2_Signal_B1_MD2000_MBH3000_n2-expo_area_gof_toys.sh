#!/bin/bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
xrdcp root://cmseos.fnal.gov//store/user/tvami/CMSSW_14_1_0_pre4_env.tgz env_tarball.tgz
export SCRAM_ARCH=el8_amd64_gcc12
scramv1 project CMSSW CMSSW_14_1_0_pre4
tar -xzf env_tarball.tgz
rm env_tarball.tgz

mkdir tardir; cp rpfExpo_BinningV5_Blind_InV15_Multi4_FullScan_MD2TeV-v2_Signal_B1_MD2000_MBH3000_n2-expo_area_gof_toys_input.tgz tardir/; cd tardir
tar -xzvf rpfExpo_BinningV5_Blind_InV15_Multi4_FullScan_MD2TeV-v2_Signal_B1_MD2000_MBH3000_n2-expo_area_gof_toys_input.tgz
rm rpfExpo_BinningV5_Blind_InV15_Multi4_FullScan_MD2TeV-v2_Signal_B1_MD2000_MBH3000_n2-expo_area_gof_toys_input.tgz
cp -r * ../CMSSW_14_1_0_pre4/src/
cd ../
cd CMSSW_14_1_0_pre4/src/; eval `scramv1 runtime -sh`
cd rpfExpo_BinningV5_Blind_InV15_Multi4_FullScan_MD2TeV-v2/Signal_B1_MD2000_MBH3000_n2-expo_area
echo $*
$*
cd $CMSSW_BASE/src/

tar -czvf rpfExpo_BinningV5_Blind_InV15_Multi4_FullScan_MD2TeV-v2_Signal_B1_MD2000_MBH3000_n2-expo_area_gof_toys_output_${CONDOR_ID}.tgz rpfExpo_BinningV5_Blind_InV15_Multi4_FullScan_MD2TeV-v2/Signal_B1_MD2000_MBH3000_n2-expo_area/higgsCombine_gof_toys.GoodnessOfFit.mH120.*.root
cp rpfExpo_BinningV5_Blind_InV15_Multi4_FullScan_MD2TeV-v2_Signal_B1_MD2000_MBH3000_n2-expo_area_gof_toys_output_${CONDOR_ID}.tgz $CMSSW_BASE/../

import ROOT
import os
import tdrstyle

ROOT.gROOT.SetBatch(True)
# tdrstyle.setTDRStyle()
ROOT.gStyle.SetOptFit(0)
# ROOT.gStyle.SetOptStat(0);

# unit pb
crossSectionArray_QCD = {
    # "QCD_HT50to100.root" : 187700000.0,  # +-1639000
    # "QCD_HT100to200.root" : 23500000.0,  # +-207400
    # "QCD_HT200to300.root" : 1552000.0,  # +-14450.0
    # "QCD_HT300to500" : 321100.0,  # +-2968.0
    # "QCD_HT500to700" : 30250.0,  # +-284.0
    "QCD_HT700to1000" : 6398.0,  # +-59.32
    "QCD_HT1000to1500" : 1122.0,  # +- 10.41
    "QCD_HT1500to2000" : 109.4,  # +-1.006
    "QCD_HT2000toInf" : 21.74, # +-0.2019
}

# unit pb
crossSectionArray_blackmax = {
    "BlackHole_B1_MD2000_MBH3000_n2" : 89.4228,
    "BlackHole_B1_MD2000_MBH4000_n2" : 21.474,
    "BlackHole_B1_MD2000_MBH5000_n2" : 4.79294,
    "BlackHole_B1_MD2000_MBH6000_n2" : 0.952668,
    "BlackHole_B1_MD2000_MBH7000_n2" : 0.151634,
    "BlackHole_B1_MD2000_MBH8000_n2" : 0.017859,
    "BlackHole_B1_MD2000_MBH9000_n2" : 0.00137232,
    "BlackHole_B1_MD2000_MBH10000_n2" : 0.000056915,
    "BlackHole_B1_MD2000_MBH11000_n2" : 0.000000830986,
    "BlackHole_B1_MD3000_MBH4000_n2" : 6.78799,
    "BlackHole_B1_MD3000_MBH5000_n2" : 1.55122,
    "BlackHole_B1_MD3000_MBH6000_n2" : 0.301522,
    "BlackHole_B1_MD3000_MBH7000_n2" : 0.0486405,
    "BlackHole_B1_MD3000_MBH8000_n2" : 0.00584229,
    "BlackHole_B1_MD3000_MBH9000_n2" : 0.000454481,
    "BlackHole_B1_MD3000_MBH10000_n2" : 0.000018391,
    "BlackHole_B1_MD3000_MBH11000_n2" : 0.000000276788,
    "BlackHole_B1_MD4000_MBH5000_n2" : 0.675984,
    "BlackHole_B1_MD4000_MBH6000_n2" : 0.135296,
    "BlackHole_B1_MD4000_MBH7000_n2" : 0.0218575,
    "BlackHole_B1_MD4000_MBH8000_n2" : 0.00263422,
    "BlackHole_B1_MD4000_MBH9000_n2" : 0.000205028,
    "BlackHole_B1_MD4000_MBH10000_n2" : 0.00000823413,
    "BlackHole_B1_MD4000_MBH11000_n2" : 0.000000124564,
    "BlackHole_B1_MD5000_MBH6000_n2" : 0.0697818,
    "BlackHole_B1_MD5000_MBH7000_n2" : 0.0116312,
    "BlackHole_B1_MD5000_MBH8000_n2" : 0.00137388,
    "BlackHole_B1_MD5000_MBH9000_n2" : 0.000109127,
    "BlackHole_B1_MD5000_MBH10000_n2" : 0.00000439053,
    "BlackHole_B1_MD5000_MBH11000_n2" : 0.000000066559,
    "BlackHole_B1_MD6000_MBH7000_n2" : 0.00677405,
    "BlackHole_B1_MD6000_MBH8000_n2" : 0.000826004,
    "BlackHole_B1_MD6000_MBH9000_n2" : 0.0000650319,
    "BlackHole_B1_MD6000_MBH10000_n2" : 0.00000260528,
    "BlackHole_B1_MD6000_MBH11000_n2" : 0.0000000396912,
    "BlackHole_B1_MD7000_MBH8000_n2" : 0.000525429,
    "BlackHole_B1_MD7000_MBH9000_n2" : 0.0000418709,
    "BlackHole_B1_MD7000_MBH10000_n2" : 0.00000169923,
    "BlackHole_B1_MD7000_MBH11000_n2" : 0.0000000256018,
    "BlackHole_B1_MD8000_MBH9000_n2" : 0.000028304,
    "BlackHole_B1_MD8000_MBH10000_n2" : 0.0000011523,
    "BlackHole_B1_MD8000_MBH11000_n2" : 0.0000000174306,
    "BlackHole_B1_MD9000_MBH10000_n2" : 0.000000826779,
    "BlackHole_B1_MD9000_MBH11000_n2" : 0.0000000125184,
}

def make_output_rootfile(h_PASS, h_FAIL, sample, out_dir):
    # save the histograms to root file
    if sample.find("BlackHole") != -1:
        signal_name = sample.split("BlackHole_")[-1]
        filename = f"BH_Signal_{signal_name}.root"
    elif sample == "QCD":
        filename = "BH_FakeData.root"
    elif sample == "data":
        filename = "BH_Data.root"
    
    if not os.path.exists(f"{out_dir}/"):
        os.makedirs(f"{out_dir}/")
    
    output = ROOT.TFile(f"{out_dir}/{filename}", "RECREATE")
    h_PASS.GetXaxis().SetTitle("ST [GeV]")
    h_PASS.GetYaxis().SetTitle("Multiplicity")
    h_PASS.Write("hpass")
    h_FAIL.GetXaxis().SetTitle("ST [GeV]")
    h_FAIL.GetYaxis().SetTitle("Multiplicity")
    h_FAIL.Write("hfail")
    output.Close()


if __name__ == '__main__':
     
    xmin = 2000
    xmax = 13000 #8000
    SVM_score_cut = 0.63
    PASS = f"SVM_score >= {SVM_score_cut}"
    FAIL = f"SVM_score <  {SVM_score_cut}"
    # PASS = f"SVM_score >= 0.5 && SVM_score <= 0.63"
    # FAIL = f"SVM_score < 0.5"
    N = 5
    sample = "data"  # QCD, signal, data
    lumi = 137.62 * 1000  # 96.14 * 1000 # 59.8 * 1000 # unit pb^-1
    outDir = "./histograms_for_2DAlphabet_v10"
    blind = False
    
    if sample == "QCD":
    
        sample_types = ["QCD_HT700to1000", "QCD_HT1000to1500", "QCD_HT1500to2000", "QCD_HT2000toInf"]
        
        hists_PASS = []
        hists_FAIL = []
        Ngen = {}
        
        for sample_type in sample_types:
            rootfile_dir = "/home/users/dazhang/works/phaseSpace/BlackHoleSearch/PhaseSpaceOT/EventClassification/eval/condor_QCD_new/{}/".format(sample_type)
            
            hist_PASS = ROOT.TH2F(f"Hist_PASS_{sample_type}", "ST vs Multiplicity 2D Hist", int((xmax-xmin)/50.), xmin, xmax, 20, 0, 20)
            hist_FAIL = ROOT.TH2F(f"Hist_FAIL_{sample_type}", "ST vs Multiplicity 2D Hist", int((xmax-xmin)/50.), xmin, xmax, 20, 0, 20)

            tchain = ROOT.TChain("Events")
            for rootfile in os.listdir(rootfile_dir):
                if rootfile.endswith(".root") and rootfile.find(f"geq{int(N+1)}Objects") != -1:
                    tchain.Add(os.path.join(rootfile_dir, rootfile))
            
            Ngen[sample_type] = tchain.GetEntries()
            
            tchain.Draw(f"Multiplicity:ST >> Hist_PASS_{sample_type}",f"{PASS}")
            tchain.Draw(f"Multiplicity:ST >> Hist_FAIL_{sample_type}",f"{FAIL}")
            
            hists_PASS.append(hist_PASS)
            hists_FAIL.append(hist_FAIL)
    
        # Scale the histograms to xs
        for i, sample_type in enumerate(sample_types):
            
            hist_PASS = None
            for h in hists_PASS:
                name = h.GetName()
                if name.find(sample_type) != -1:
                    hist_PASS = h
                    break
            hist_FAIL = None
            for h in hists_FAIL:
                name = h.GetName()
                if name.find(sample_type) != -1:
                    hist_FAIL = h
                    break
            
            if hist_PASS is None or hist_FAIL is None:
                print(f"Error: {sample_type} cannot find the histograms")
                exit()
            
            xs = crossSectionArray_QCD[sample_type]
            ngen = Ngen[sample_type]
            hist_PASS.Scale(xs * lumi / ngen)
            hist_FAIL.Scale(xs * lumi / ngen)
            
        
        hist_PASS = None
        for h in hists_PASS:
            if hist_PASS is None:
                hist_PASS = h.Clone("hpass")
            else:
                hist_PASS.Add(h) 
        
        hist_FAIL = None
        for h in hists_FAIL:
            if hist_FAIL is None:
                hist_FAIL = h.Clone("hfail")
            else:
                hist_FAIL.Add(h)
                
        make_output_rootfile(hist_PASS, hist_FAIL, sample, outDir)
    
    elif sample == "signal":
        
        signal_dir = "/home/users/dazhang/works/phaseSpace/BlackHoleSearch/PhaseSpaceOT/EventClassification/eval/condor_signal_new"
        sample_types = [sample_type for sample_type in os.listdir(signal_dir) if os.path.isdir(os.path.join(signal_dir, sample_type))]
        
        for sample_type in sample_types:
            rootfile_dir = os.path.join(signal_dir, sample_type)
            
            hist_PASS = ROOT.TH2F(f"Hist_PASS_{sample_type}", "ST vs Multiplicity 2D Hist", int((xmax-xmin)/50.), xmin, xmax, 20, 0, 20)
            hist_FAIL = ROOT.TH2F(f"Hist_FAIL_{sample_type}", "ST vs Multiplicity 2D Hist", int((xmax-xmin)/50.), xmin, xmax, 20, 0, 20)
            
            tchain = ROOT.TChain("Events")
            for rootfile in os.listdir(rootfile_dir):
                if rootfile.endswith(".root") and rootfile.find(f"geq{int(N+1)}Objects") != -1:
                    tchain.Add(os.path.join(rootfile_dir, rootfile))
            
            ngen = tchain.GetEntries()
            
            tchain.Draw(f"Multiplicity:ST >> Hist_PASS_{sample_type}",f"{PASS}")
            tchain.Draw(f"Multiplicity:ST >> Hist_FAIL_{sample_type}",f"{FAIL}")
            
            hist_PASS.Scale(crossSectionArray_blackmax[sample_type] * lumi / ngen)
            hist_FAIL.Scale(crossSectionArray_blackmax[sample_type] * lumi / ngen)
            
            make_output_rootfile(hist_PASS, hist_FAIL, sample_type, outDir)

    elif sample == "data":
        data18_dir     = "/home/users/dazhang/works/phaseSpace/BlackHoleSearch/PhaseSpaceOT/EventClassification/eval/condor_data18"
        data16_dir     = "/home/users/dazhang/works/phaseSpace/BlackHoleSearch/PhaseSpaceOT/EventClassification/eval/condor_data16_110424"
        data16post_dir = "/home/users/dazhang/works/phaseSpace/BlackHoleSearch/PhaseSpaceOT/EventClassification/eval/condor_data16post_111224"
        data17_dir     = "/home/users/dazhang/works/phaseSpace/BlackHoleSearch/PhaseSpaceOT/EventClassification/eval/condor_data17_111224"
        
        hist_PASS = ROOT.TH2F(f"Hist_PASS_{sample}", "ST vs Multiplicity 2D Hist", int((xmax-xmin)/50.), xmin, xmax, 20, 0, 20)
        hist_FAIL = ROOT.TH2F(f"Hist_FAIL_{sample}", "ST vs Multiplicity 2D Hist", int((xmax-xmin)/50.), xmin, xmax, 20, 0, 20)
        
        tchain = ROOT.TChain("Events")
        # List of directories to process
        directories = [data18_dir, data16_dir, data16post_dir, data17_dir]
        # Loop over each directory
        for data_dir in directories:
            for rootfile in os.listdir(data_dir):
                if rootfile.endswith(".root") and rootfile.find(f"geq{int(N+1)}Objects") != -1:
                    tchain.Add(os.path.join(data_dir, rootfile))
        
        PASS_blind = PASS
        if blind:
            PASS_blind = f"{PASS} && ST < 4000"
        
        tchain.Draw(f"Multiplicity:ST >> Hist_PASS_{sample}",f"{PASS_blind}")
        tchain.Draw(f"Multiplicity:ST >> Hist_FAIL_{sample}",f"{FAIL}")
        
        make_output_rootfile(hist_PASS, hist_FAIL, sample, outDir)
        

    
    
    
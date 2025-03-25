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
    # "QCD_HT700to1000" : 6398.0,  # +-59.32
    # "QCD_HT1000to1500" : 1122.0,  # +- 10.41
    "QCD_HT1500to2000" : 109.4,  # +-1.006
    "QCD_HT2000toInf" : 21.74, # +-0.2019
}

# unit pb
crossSectionArray_signals = {
    "Sphaleron_thr8500_pNCS0p5" : 28.3304 * 1e-3,
    "Sphaleron_thr8750_pNCS0p5" : 14.5121 * 1e-3,
    "Sphaleron_thr9000_pNCS0p5" : 7.11033 * 1e-3,  # 0.01005
    "Sphaleron_thr9250_pNCS0p5" : 3.41194 * 1e-3,
    "Sphaleron_thr9500_pNCS0p5" : 1.55813 * 1e-3, 
}


def make_output_rootfile(hists, sample, out_dir):
    # save the histograms to root file
    if sample.find("Sphaleron") != -1:
        signal_name = sample.split("Sphaleron_")[-1]
        filename = f"Sphaleron_Signal_{signal_name}.root"
    elif sample == "QCD":
        filename = "Sphaleron_FakeData.root"
    elif sample == "data":
        filename = "Sphaleron_Data.root"
    
    if not os.path.exists(f"{out_dir}/"):
        os.makedirs(f"{out_dir}/")
    
    output = ROOT.TFile(f"{out_dir}/{filename}", "RECREATE")
    
    for h in hists:
        h.GetXaxis().SetTitle("ST [GeV]")
        h.GetYaxis().SetTitle("Multiplicity")
        h.Write()
    output.Close()

def scale_add_hists_QCD(hists, Ngen, lumi, histname):
    for h in hists:
        name = h.GetName()
        xs = crossSectionArray_QCD["_".join(name.split("_")[2:4])]
        sample_type = "_".join(name.split("_")[2:4])
        ngen = Ngen[sample_type]
        h.Scale(xs * lumi / ngen)
    hist_add = None
    for h in hists:
        if hist_add is None:
            hist_add = h.Clone(histname)
        else:
            hist_add.Add(h) 
    return hist_add

if __name__ == '__main__':
    
    nModel = 1
    nExtra = 2
     
    xmin = 2000
    xmax = 13000 #8000
    SVM_score_cut = 0.63
    SVM_score_up = 0.7
    SVM_score_down = 0.5
    
    # PASS = f"SVM_score >= {SVM_score_cut}"
    # FAIL = f"SVM_score <  {SVM_score_cut}"
    # PASS_SVM_up = f"SVM_score >= {SVM_score_up}"
    # FAIL_SVM_up = f"SVM_score <  {SVM_score_up}"
    # PASS_SVM_down = f"SVM_score >= {SVM_score_down}"
    # FAIL_SVM_down = f"SVM_score <  {SVM_score_down}"
    
    PASS = f"SVM_score >= {SVM_score_cut} && Sphericity > 0.1"
    FAIL = f"SVM_score <  {SVM_score_cut} && Sphericity > 0.1"
    PASS_SVM_up = f"SVM_score >= {SVM_score_up} && Sphericity > 0.1"
    FAIL_SVM_up = f"SVM_score <  {SVM_score_up} && Sphericity > 0.1"
    PASS_SVM_down = f"SVM_score >= {SVM_score_down} && Sphericity > 0.1"
    FAIL_SVM_down = f"SVM_score <  {SVM_score_down} && Sphericity > 0.1"
    
    # PASS = f"SVM_score >= 0.5 && SVM_score <= 0.63 && Sphericity > 0.1"
    # FAIL = f"SVM_score < 0.5 && Sphericity > 0.1"
    # PASS_SVM_up = f"SVM_score >= {SVM_score_up} && Sphericity > 0.1"
    # FAIL_SVM_up = f"SVM_score <  {SVM_score_up} && Sphericity > 0.1"
    # PASS_SVM_down = f"SVM_score >= {SVM_score_down} && Sphericity > 0.1"
    # FAIL_SVM_down = f"SVM_score <  {SVM_score_down} && Sphericity > 0.1"
    
    N = 5
    sample = "signal"  # QCD, signal, data
    lumi = 137.62 * 1000   # 137.62 * 1000  # 96.14 * 1000 # 59.8 * 1000 unit pb^-1
    outDir = "./histograms_for_2DAlphabet_v20"
    blind = False
    
    if sample == "QCD":
    
        sample_types = ["QCD_HT1500to2000", "QCD_HT2000toInf"]
        
        hists_PASS = []
        hists_FAIL = []
        hists_PASS_SVM_up = []
        hists_FAIL_SVM_up = []
        hists_PASS_SVM_down = []
        hists_FAIL_SVM_down = []
        Ngen = {}
        
        for sample_type in sample_types:
            rootfile_dir = "/home/users/dazhang/works/phaseSpace/BlackHoleSearch/PhaseSpaceOT/EventClassification/eval/blackmax_BH{}_n{}/condor_QCD_new/{}/".format(nModel,nExtra,sample_type)
            
            hist_PASS = ROOT.TH2F(f"Hist_PASS_{sample_type}", "ST vs Multiplicity 2D Hist", int((xmax-xmin)/50.), xmin, xmax, 20, 0, 20)
            hist_FAIL = ROOT.TH2F(f"Hist_FAIL_{sample_type}", "ST vs Multiplicity 2D Hist", int((xmax-xmin)/50.), xmin, xmax, 20, 0, 20)
            hist_PASS_up = ROOT.TH2F(f"Hist_PASS_{sample_type}_SVM_up", "ST vs Multiplicity 2D Hist", int((xmax-xmin)/50.), xmin, xmax, 20, 0, 20)
            hist_FAIL_up = ROOT.TH2F(f"Hist_FAIL_{sample_type}_SVM_up", "ST vs Multiplicity 2D Hist", int((xmax-xmin)/50.), xmin, xmax, 20, 0, 20)
            hist_PASS_down = ROOT.TH2F(f"Hist_PASS_{sample_type}_SVM_down", "ST vs Multiplicity 2D Hist", int((xmax-xmin)/50.), xmin, xmax, 20, 0, 20)
            hist_FAIL_down = ROOT.TH2F(f"Hist_FAIL_{sample_type}_SVM_down", "ST vs Multiplicity 2D Hist", int((xmax-xmin)/50.), xmin, xmax, 20, 0, 20)
            
            tchain = ROOT.TChain("Events")
            for rootfile in os.listdir(rootfile_dir):
                if rootfile.endswith(".root") and rootfile.find(f"geq{int(N+1)}Objects") != -1:
                    tchain.Add(os.path.join(rootfile_dir, rootfile))
            
            Ngen[sample_type] = tchain.GetEntries()
            
            tchain.Draw(f"Multiplicity:ST >> Hist_PASS_{sample_type}",f"{PASS}")
            tchain.Draw(f"Multiplicity:ST >> Hist_FAIL_{sample_type}",f"{FAIL}")
            tchain.Draw(f"Multiplicity:ST >> Hist_PASS_{sample_type}_SVM_up",f"{PASS_SVM_up}")
            tchain.Draw(f"Multiplicity:ST >> Hist_FAIL_{sample_type}_SVM_up",f"{FAIL_SVM_up}")
            tchain.Draw(f"Multiplicity:ST >> Hist_PASS_{sample_type}_SVM_down",f"{PASS_SVM_down}")
            tchain.Draw(f"Multiplicity:ST >> Hist_FAIL_{sample_type}_SVM_down",f"{FAIL_SVM_down}")
            
            hists_PASS.append(hist_PASS)
            hists_FAIL.append(hist_FAIL)
            hists_PASS_SVM_up.append(hist_PASS_up)
            hists_FAIL_SVM_up.append(hist_FAIL_up)
            hists_PASS_SVM_down.append(hist_PASS_down)
            hists_FAIL_SVM_down.append(hist_FAIL_down)
    
        # Scale the histograms to xs
        hist_PASS = scale_add_hists_QCD(hists_PASS, Ngen, lumi, 'hpass')
        hist_FAIL = scale_add_hists_QCD(hists_FAIL, Ngen, lumi, 'hfail')
        hist_PASS_SVM_up = scale_add_hists_QCD(hists_PASS_SVM_up, Ngen, lumi, "hpass_SVMsyst_up")
        hist_FAIL_SVM_up = scale_add_hists_QCD(hists_FAIL_SVM_up, Ngen, lumi, "hfail_SVMsyst_up")
        hist_PASS_SVM_down = scale_add_hists_QCD(hists_PASS_SVM_down, Ngen, lumi, "hpass_SVMsyst_down")
        hist_FAIL_SVM_down = scale_add_hists_QCD(hists_FAIL_SVM_down, Ngen, lumi, "hfail_SVMsyst_down")
                
        make_output_rootfile([hist_PASS, hist_PASS_SVM_up, hist_PASS_SVM_down, hist_FAIL, hist_FAIL_SVM_up, hist_FAIL_SVM_down], sample, outDir)
        # make_output_rootfile([hist_PASS, hist_FAIL], sample, outDir)
    
    elif sample == "signal":
        
        signal_dir = "/home/users/dazhang/works/phaseSpace/BlackHoleSearch/PhaseSpaceOT/EventClassification/eval/blackmax_BH{}_n{}/condor_sphaleron".format(nModel, nExtra)
        sample_types = [sample_type for sample_type in os.listdir(signal_dir) if os.path.isdir(os.path.join(signal_dir, sample_type)) and sample_type.find("pNCS0p5") != -1]
        
        for sample_type in sample_types:
            print(f">> making histograms for {sample_type}")
            
            rootfile_dir = os.path.join(signal_dir, sample_type)
            
            hist_PASS = ROOT.TH2F(f"Hist_PASS_{sample_type}", "ST vs Multiplicity 2D Hist", int((xmax-xmin)/50.), xmin, xmax, 20, 0, 20)
            hist_FAIL = ROOT.TH2F(f"Hist_FAIL_{sample_type}", "ST vs Multiplicity 2D Hist", int((xmax-xmin)/50.), xmin, xmax, 20, 0, 20)
            hist_PASS_SVM_up = ROOT.TH2F(f"Hist_PASS_{sample_type}_SVM_up", "ST vs Multiplicity 2D Hist", int((xmax-xmin)/50.), xmin, xmax, 20, 0, 20)
            hist_FAIL_SVM_up = ROOT.TH2F(f"Hist_FAIL_{sample_type}_SVM_up", "ST vs Multiplicity 2D Hist", int((xmax-xmin)/50.), xmin, xmax, 20, 0, 20)
            hist_PASS_SVM_down = ROOT.TH2F(f"Hist_PASS_{sample_type}_SVM_down", "ST vs Multiplicity 2D Hist", int((xmax-xmin)/50.), xmin, xmax, 20, 0, 20)
            hist_FAIL_SVM_down = ROOT.TH2F(f"Hist_FAIL_{sample_type}_SVM_down", "ST vs Multiplicity 2D Hist", int((xmax-xmin)/50.), xmin, xmax, 20, 0, 20)
            
            tchain = ROOT.TChain("Events")
            for rootfile in os.listdir(rootfile_dir):
                if rootfile.endswith(".root") and rootfile.find(f"geq{int(N+1)}Objects") != -1:
                    tchain.Add(os.path.join(rootfile_dir, rootfile))
            
            ngen = tchain.GetEntries()
            print(f"ngen: {ngen}")
            
            tchain.Draw(f"Multiplicity:ST >> Hist_PASS_{sample_type}",f"{PASS}")
            tchain.Draw(f"Multiplicity:ST >> Hist_FAIL_{sample_type}",f"{FAIL}")
            tchain.Draw(f"Multiplicity:ST >> Hist_PASS_{sample_type}_SVM_up",f"{PASS_SVM_up}")
            tchain.Draw(f"Multiplicity:ST >> Hist_FAIL_{sample_type}_SVM_up",f"{FAIL_SVM_up}")
            tchain.Draw(f"Multiplicity:ST >> Hist_PASS_{sample_type}_SVM_down",f"{PASS_SVM_down}")
            tchain.Draw(f"Multiplicity:ST >> Hist_FAIL_{sample_type}_SVM_down",f"{FAIL_SVM_down}")
            
            hist_PASS.Scale(crossSectionArray_signals[sample_type] * lumi / ngen)
            hist_FAIL.Scale(crossSectionArray_signals[sample_type] * lumi / ngen)
            hist_PASS_SVM_up.Scale(crossSectionArray_signals[sample_type] * lumi / ngen)
            hist_FAIL_SVM_up.Scale(crossSectionArray_signals[sample_type] * lumi / ngen)
            hist_PASS_SVM_down.Scale(crossSectionArray_signals[sample_type] * lumi / ngen)
            hist_FAIL_SVM_down.Scale(crossSectionArray_signals[sample_type] * lumi / ngen)
            
            hist_PASS.SetName(f"hpass")
            hist_FAIL.SetName(f"hfail")
            hist_PASS_SVM_up.SetName(f"hpass_SVMsyst_up")
            hist_FAIL_SVM_up.SetName(f"hfail_SVMsyst_up")
            hist_PASS_SVM_down.SetName(f"hpass_SVMsyst_down")
            hist_FAIL_SVM_down.SetName(f"hfail_SVMsyst_down")
            
            make_output_rootfile([hist_PASS, hist_PASS_SVM_up, hist_PASS_SVM_down, hist_FAIL, hist_FAIL_SVM_up, hist_FAIL_SVM_down], sample_type, outDir)
            # make_output_rootfile([hist_PASS, hist_FAIL], sample_type, outDir)

    elif sample == "data":
        data18_dir     = "/home/users/dazhang/works/phaseSpace/BlackHoleSearch/PhaseSpaceOT/EventClassification/eval/blackmax_BH1_n2/condor_data18"
        data16_dir     = "/home/users/dazhang/works/phaseSpace/BlackHoleSearch/PhaseSpaceOT/EventClassification/eval/blackmax_BH1_n2/condor_data16_110424"
        data16post_dir = "/home/users/dazhang/works/phaseSpace/BlackHoleSearch/PhaseSpaceOT/EventClassification/eval/blackmax_BH1_n2/condor_data16post_111224"
        data17_dir     = "/home/users/dazhang/works/phaseSpace/BlackHoleSearch/PhaseSpaceOT/EventClassification/eval/blackmax_BH1_n2/condor_data17_111224"
        
        hist_PASS = ROOT.TH2F(f"Hist_PASS_{sample}", "ST vs Multiplicity 2D Hist", int((xmax-xmin)/50.), xmin, xmax, 20, 0, 20)
        hist_FAIL = ROOT.TH2F(f"Hist_FAIL_{sample}", "ST vs Multiplicity 2D Hist", int((xmax-xmin)/50.), xmin, xmax, 20, 0, 20)
        hist_PASS_SVM_up = ROOT.TH2F(f"Hist_PASS_{sample}_SVM_up", "ST vs Multiplicity 2D Hist", int((xmax-xmin)/50.), xmin, xmax, 20, 0, 20)
        hist_FAIL_SVM_up = ROOT.TH2F(f"Hist_FAIL_{sample}_SVM_up", "ST vs Multiplicity 2D Hist", int((xmax-xmin)/50.), xmin, xmax, 20, 0, 20)
        hist_PASS_SVM_down = ROOT.TH2F(f"Hist_PASS_{sample}_SVM_down", "ST vs Multiplicity 2D Hist", int((xmax-xmin)/50.), xmin, xmax, 20, 0, 20)
        hist_FAIL_SVM_down = ROOT.TH2F(f"Hist_FAIL_{sample}_SVM_down", "ST vs Multiplicity 2D Hist", int((xmax-xmin)/50.), xmin, xmax, 20, 0, 20)
        
        tchain = ROOT.TChain("Events")
        # List of directories to process
        directories = [data18_dir, data16_dir, data16post_dir, data17_dir]
        # Loop over each directory
        for data_dir in directories:
            for rootfile in os.listdir(data_dir):
                if rootfile.endswith(".root") and rootfile.find(f"geq{int(N+1)}Objects") != -1:
                    tchain.Add(os.path.join(data_dir, rootfile))
        
        PASS_blind = PASS
        PASS_SVM_up_blind = PASS_SVM_up
        PASS_SVM_down_blind = PASS_SVM_down
        if blind:
            PASS_blind = f"{PASS} && ST < 4000"
            PASS_SVM_up_blind = f"{PASS_SVM_up} && ST < 4000"
            PASS_SVM_down_blind = f"{PASS_SVM_down} && ST < 4000"
        
        tchain.Draw(f"Multiplicity:ST >> Hist_PASS_{sample}",f"{PASS_blind}")
        tchain.Draw(f"Multiplicity:ST >> Hist_FAIL_{sample}",f"{FAIL}")
        tchain.Draw(f"Multiplicity:ST >> Hist_PASS_{sample}_SVM_up",f"{PASS_SVM_up_blind}")
        tchain.Draw(f"Multiplicity:ST >> Hist_FAIL_{sample}_SVM_up",f"{FAIL_SVM_up}")
        tchain.Draw(f"Multiplicity:ST >> Hist_PASS_{sample}_SVM_down",f"{PASS_SVM_down_blind}")
        tchain.Draw(f"Multiplicity:ST >> Hist_FAIL_{sample}_SVM_down",f"{FAIL_SVM_down}")
        
        hist_PASS.SetName(f"hpass")
        hist_FAIL.SetName(f"hfail")
        hist_PASS_SVM_up.SetName(f"hpass_SVMsyst_up")
        hist_FAIL_SVM_up.SetName(f"hfail_SVMsyst_up")
        hist_PASS_SVM_down.SetName(f"hpass_SVMsyst_down")
        hist_FAIL_SVM_down.SetName(f"hfail_SVMsyst_down")
        
        make_output_rootfile([hist_PASS, hist_PASS_SVM_up, hist_PASS_SVM_down, hist_FAIL, hist_FAIL_SVM_up, hist_FAIL_SVM_down], sample, outDir)
        # make_output_rootfile([hist_PASS, hist_FAIL], sample, outDir)
        

    
    
    
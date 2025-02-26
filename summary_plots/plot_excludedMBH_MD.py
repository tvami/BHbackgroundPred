import os
import ROOT
import numpy as np

ROOT.gROOT.SetBatch(True)


MD_list = np.linspace(2,9,8)
working_dir = '/home/users/dazhang/works/phaseSpace/BlackHoleSearch/CMSSW_14_1_0_pre4/src/'

MD_MBH_excluded = {}

for MD in MD_list:
    # limit_plot = os.path.join(working_dir, f'rpfExpo_BinningV5_Blind_InV16_Multi4_FullScan_MD{MD:.0f}TeV/limits_combine_137p6fb_signals_BH1_MD{(MD*1000):.0f}_BH.C')
    limit_plot = os.path.join(working_dir, f'rpfExpo_BinningV5_Blind_InV15_Multi4_FullScan_MD{MD:.0f}TeV/limits_combine_137p6fb_signals_BH1_MD{(MD*1000):.0f}_BH.C')
    ROOT.gROOT.ProcessLine('.x %s' % limit_plot)
    
    canvas = ROOT.gROOT.FindObject("climits")
    if not canvas:
        raise ValueError("Canvas not found!")
    
    # Search for TLatex objects in the canvas primitives
    latex_objects = []
    primitive_list = canvas.GetListOfPrimitives()

    for prim in primitive_list:
        # Check if the primitive is a TLatex object
        if isinstance(prim, ROOT.TLatex):
            latex_objects.append(prim)

    # Example: Print properties of the first TLatex object
    if latex_objects:
        first_latex = latex_objects[0]
        print("TLatex text:", first_latex.GetTitle())
        print("Position (x, y):", first_latex.GetX(), first_latex.GetY())
        print(first_latex.GetTitle().split())
        MD_MBH_excluded[MD] = float(first_latex.GetTitle().split()[0])
    else:
        print("No TLatex objects found in the canvas.")

# if MBH = 0, delete it
for MD in MD_list:
    if MD_MBH_excluded[MD] == -1:
        MD_MBH_excluded.pop(MD)

print(MD_MBH_excluded)
for key, value in MD_MBH_excluded.items():
    print(f"MD: {key} TeV, excluded MBH: {value} TeV")

# draw the excluded MBH vs MD in ROOT
canvas = ROOT.TCanvas("canvas", "canvas", 800, 600)
graph = ROOT.TGraph(len(MD_MBH_excluded), np.array(list(MD_MBH_excluded.keys())), np.array(list(MD_MBH_excluded.values())))
graph.SetTitle("Excluded MBH vs MD")
graph.GetXaxis().SetTitle("M_{D} [TeV]")
graph.GetYaxis().SetTitle("Excluded M_{BH}^{min} [TeV]")
graph.SetMarkerStyle(20)
graph.GetXaxis().SetRangeUser(1, 8);
graph.GetYaxis().SetRangeUser(6, 11);
graph.Draw("APL")
canvas.SaveAs("excludedMBH_MD_SVMOnly.pdf")
    
    

import os
import ROOT
import numpy as np
import tdrstyle
import ctypes


ROOT.gROOT.SetBatch(True)
tdrstyle.setTDRStyle()

line_colors = [ROOT.kBlack, ROOT.kRed, ROOT.kBlue, ROOT.kGreen, ROOT.kOrange, ROOT.kMagenta, ROOT.kCyan, ROOT.kYellow]

MD_list = np.linspace(2,9,8)
working_dir = '/home/users/dazhang/works/phaseSpace/BlackHoleSearch/CMSSW_14_1_0_pre4/src/'

graphs = []

for MD in MD_list:
    # limit_plot = os.path.join(working_dir, f'rpfExpo_BinningV5_Blind_InV16_Multi4_FullScan_MD{MD:.0f}TeV/limits_combine_137p6fb_signals_BH1_MD{(MD*1000):.0f}_BH.C')
    limit_plot = os.path.join(working_dir, f'rpfExpo_BinningV5_Blind_InV18_Multi4_FullScan_MD{MD:.0f}TeV_n6/limits_combine_137p6fb_signals_B1_n6_MD{(MD*1000):.0f}_BH.C')
    ROOT.gROOT.ProcessLine('.x %s' % limit_plot)
    
    canvas = ROOT.gROOT.FindObject("climits")
    if not canvas:
        raise ValueError("Canvas not found!")
    
    # Search for TGraph objects in the canvas primitives
    graph = []
    primitive_list = canvas.GetListOfPrimitives()

    for prim in primitive_list:
        # Check if the primitive is a TGraph object
        if isinstance(prim, ROOT.TGraph):
            graph.append(prim)

    # Example: Print properties of the first TLatex object
    if graph:
        first_graph = graph[0]
        print("Graph0 N:", first_graph.GetN())
        # get x and y values
        # x = first_graph.GetX()
        # y = first_graph.GetY()
        graphs.append(first_graph)
    else:
        print("No TGraph objects found in the canvas.")

# Draw graphs in a single canvas
can = ROOT.TCanvas("canvas", "canvas", 800, 600)
can.SetLogy()
can.SetGrid()

leg = ROOT.TLegend(0.6, 0.6, 0.9, 0.9)
leg.SetBorderSize(0)
leg.SetFillStyle(0)
leg.SetTextSize(0.03)

for i, graph in enumerate(graphs):
    graph.SetLineColor(line_colors[i])
    graph.SetLineWidth(2)
    leg.AddEntry(graph, f"MD = {MD_list[i]:.0f} TeV", "LP")
    if i == 0:
        graph.GetXaxis().SetTitle("M_{BH} [TeV]")
        graph.GetYaxis().SetTitle("Cross Section [pb]")
        graph.GetYaxis().SetRangeUser(1e-5, 0.05)
        graph.Draw("AL")
    else:
        graph.Draw("L same")
    # print the points
    print(f"MD: {MD_list[i]:.0f} TeV")
    for j in range(graph.GetN()):
        x = ctypes.c_double()
        y = ctypes.c_double()
        graph.GetPoint(j, x, y)
        print(f">> MBH: {x.value} TeV, xs: {y.value} pb")

leg.Draw()
can.SaveAs("xs_limits_B1_n6.pdf")

    
    

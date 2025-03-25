import os
import ROOT
import numpy as np

import matplotlib.pyplot as plt
import mplhep as hep
plt.style.use(hep.style.ROOT)

ROOT.gROOT.SetBatch(True)


MD_list = np.linspace(2,9,8)
working_dir = '/home/users/dazhang/works/phaseSpace/BlackHoleSearch/CMSSW_14_1_0_pre4/src/'

# list_dict_MD_MBHexcluded = []
dict_model = {}

for nModel in [1,2,3]:
    for nExtra in [2, 4, 6]:
        dict_MD_MBHexcluded = {}
        for MD in MD_list:
            if nModel == 1 and nExtra == 2:
                subdir = f'rpfExpo_BinningV5_Blind_InV16_Multi4_FullScan_MD{MD:.0f}TeV'
                filename = f'limits_combine_137p6fb_signals_BH1_MD{(MD*1000):.0f}_BH.C'
            else:
                subdir = f'rpfExpo_BinningV5_Blind_InV18_Multi4_FullScan_B{nModel}_n{nExtra}_MD{MD:.0f}TeV'
                filename = f'limits_combine_137p6fb_signals_B{nModel}_n{nExtra}_MD{(MD*1000):.0f}_BH.C'
            limit_plot = os.path.join(working_dir, subdir, filename)
            
            # Check if the file exists
            if not os.path.exists(limit_plot):
                dict_MD_MBHexcluded[MD] = -1
                continue
            
            # Load the limit plot canvas
            ROOT.gROOT.ProcessLine('.x %s' % limit_plot)
            # Get the canvas
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
                dict_MD_MBHexcluded[MD] = float(first_latex.GetTitle().split()[0])
            else:
                print("No TLatex objects found in the canvas.")
        dict_model[(nModel, nExtra)] = dict_MD_MBHexcluded

# if MBH = 0, delete it
for key, dict in dict_model.items():
    for MD in MD_list:
        if dict[MD] == -1:
            dict.pop(MD)

# print(list_dict_MD_MBHexcluded)
for key, dict_MD_MBHexcluded in dict_model.items():
    print("Model: {}, nExtra: {}".format(key[0], key[1]))
    for MD, MBHexcluded in dict_MD_MBHexcluded.items():
        print(f"MD = {MD}, MBH excluded = {MBHexcluded}")

print("-"*50)

# draw the excluded MBH vs MD in ROOT

# use matplt
fig, ax = plt.subplots(figsize=(10, 8))
# plt.tight_layout()
# for i, dict_MD_MBHexcluded in enumerate(list_dict_MD_MBHexcluded):
#     ax.plot(list(dict_MD_MBHexcluded.keys()), list(dict_MD_MBHexcluded.values()), label=f"B1, n = {(i+1)*2}", marker='o')

color = {1: 'g', 2: 'b', 3: 'r'}
marker = {1: 'o', 2: 's', 3: '^'}
line = {2: '-.', 4: '--', 6: '-'}

dict_lines = {}
for key, dict_MD_MBHexcluded in dict_model.items():
    l, = ax.plot(list(dict_MD_MBHexcluded.keys()), list(dict_MD_MBHexcluded.values()), label=f"B{key[0]}, n = {key[1]}", color=color[key[0]], marker=marker[key[0]], linestyle=line[key[1]])
    dict_lines[key] = l
ax.set_xlabel(r"$M_{D}$ [TeV]")
ax.set_ylabel(r"Excluded $M_{BH}^{min}$ [TeV]")
ax.grid(True, which='major', linestyle='--', linewidth=0.5)
# ax.legend()

# Create first legend (BlackMax models)
caption1 = [
    "Nonrotating, no graviton emission (B1)",
    "Rotating, no graviton emission (B2)",
    "Rotating, evergy/momentum loss (B3)"
]
legend1 = ax.legend([dict_lines[(1,6)], dict_lines[(2,6)], dict_lines[(3,6)]], caption1, loc='lower left', title="BlackMax", title_fontsize='x-small', fontsize='x-small')
legend1._legend_box.align = "left"
for line in legend1.get_lines():
    line.set_linestyle('')  # Remove line styles from the first legend
# Create second legend (n values)
caption2 = [
    "n = 6",
    "n = 4",
    "n = 2"
]
legend2 = ax.legend([dict_lines[(1,6)], dict_lines[(1,4)], dict_lines[(1,2)]], caption2, loc='lower right', title="", title_fontsize='x-small', fontsize='x-small')
for line in legend2.get_lines():
    line.set_color('k')  # Change the colors of the second legend
    line.set_marker('')  # Change the markers of the second legend

# Add the first legend back
ax.add_artist(legend1)

ax.set_xlim(1, 9)
ax.set_ylim(6, 11)
plt.savefig("excludedMBH_MD.pdf")


    
    

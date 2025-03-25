# unit pb
# Read in a csv file, the first column is the sample type, the 5th column is the cross-section
# make a dictionary with the sample type as the key and the cross-section as the value

dict_nModel_nDataset_blackmax = {
    1: 1,
    2: 2,
    3: 5
}
dict_nModel_nDataset_charybdis = {
    1: 2,
    2: 4,
    3: 8,
    4: 6,
    5: 10,
    6: 9
}

model = 'C'  # B or C
nModel = 6
nExtra = 6

filename = "BH_xs.csv" if model == 'B' else "BH_xs_charybdis.csv"
dict_nModel_nDataset = dict_nModel_nDataset_blackmax if model == 'B' else dict_nModel_nDataset_charybdis

crossSectionArray = {}
with open(filename, "r") as f:
    lines = f.readlines()
    for line in lines[1:]:
        line = line.strip().split(",")
        sample_type = line[0]
        nDataset = dict_nModel_nDataset[nModel]
        if sample_type.find(f"BlackHole_BH{nDataset}_") != -1:
            # sample type: BlackHole_BH1_MD-2000_MBH-3000_n-2_TuneCUETP8M1_13TeV-blackmax
            MDsplit = 'MD-' if model == 'B' else 'MD'
            MBHsplit = 'MBH-' if model == 'B' else 'MBH'
            nsplit = 'n-' if model == 'B' else '_n'
            MDval = int(sample_type.split(MDsplit)[1].split("_")[0])
            MBHval = int(sample_type.split(MBHsplit)[1].split("_")[0])
            nExtraval = int(sample_type.split(nsplit)[1].split("_")[0])
            key = "BlackHole_%s%d_MD%d_MBH%d_n%d" % (model, nModel, MDval, MBHval, nExtraval)
            cross_section = float(line[4])
            print("key: {}, cross_section: {}".format(key, cross_section))
            crossSectionArray[key] = cross_section

print(crossSectionArray)


print(nExtra)
for MD in [2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]:
    MBH_keys = [key for key in crossSectionArray.keys() if f"MD{MD}" in key and f"n{nExtra}" in key]
    print(MBH_keys)
    print("MD: ", MD)

    # Sort keys by MBH value
    sorted_keys = sorted(MBH_keys, 
                        key=lambda k: int(k.split("MBH")[1].split("_")[0]))

    # Generate signal names
    signal_names = [key.replace("BlackHole", "Signal") + "-expo_area"
                    for key in sorted_keys]

    # Extract masses
    masses = [int(key.split("MBH")[1].split("_")[0]) for key in sorted_keys]

    # Extract and format cross-sections
    def format_cross_section(x):
        formatted = "{0:.13f}".format(x).rstrip('0').rstrip('.')
        return formatted

    cross_sections = [format_cross_section(crossSectionArray[key]) 
                    for key in sorted_keys]

    # Write to file
    with open("signals_%s%s_n%s_MD%s.txt" % (model,nModel,nExtra,MD), "w") as f:
        # Write signal names
        f.write(", ".join(signal_names) + "\n")
        # Write masses
        f.write(", ".join(map(str, masses)) + "\n")
        # Write cross-sections twice
        f.write(", ".join(cross_sections) + "\n")
        f.write(", ".join(cross_sections))
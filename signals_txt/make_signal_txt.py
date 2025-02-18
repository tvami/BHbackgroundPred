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


for MD in [2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]:
    MBH_keys = [key for key in crossSectionArray_blackmax.keys() if f"MD{MD}" in key]

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

    cross_sections = [format_cross_section(crossSectionArray_blackmax[key]) 
                    for key in sorted_keys]

    # Write to file
    with open("signals_BH1_MD%s.txt" % MD, "w") as f:
        # Write signal names
        f.write(", ".join(signal_names) + "\n")
        # Write masses
        f.write(", ".join(map(str, masses)) + "\n")
        # Write cross-sections twice
        f.write(", ".join(cross_sections) + "\n")
        f.write(", ".join(cross_sections))
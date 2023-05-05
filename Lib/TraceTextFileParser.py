import statistics
import re
import pandas as pd
import openpyxl
import WireSharkBandwidthCalc

#reads a reformatted pcap text file and parses the payload data which is then written into an excel file
with open('/Users/Stump/Desktop/activity5plaintext.txt') as word_list:
    words = word_list.read().split(' ')
    hostData = []
    target = 'Len='
    target2 = 'Len:'
    length = 0
    i = 0
    for word in words:
        if target in word:
            host = word
            parsedLen = [int(s) for s in re.findall(r'\d+', word)]
            hostData.append(parsedLen)
            length += 1
        elif target2 in word:
            TLS = words[i+1]
            TLSrefined = [int(s) for s in re.findall(r'\d+', TLS)]
            hostData.append(TLSrefined)
        i+=1
    print(hostData)
    print(length)

    hostDataDF = pd.DataFrame(hostData)
    PacketNumberDF = pd.DataFrame(WireSharkBandwidthCalc.packetNumbers)
    print(PacketNumberDF)
    PacketFrameSizesDF = pd.DataFrame(WireSharkBandwidthCalc.totalPacketSizes)




    with pd.ExcelWriter("capture4info.xlsx", engine="openpyxl") as writer:
        hostDataDF.to_excel(writer, sheet_name="Sheet_1", index=False)
        PacketNumberDF.to_excel(writer,sheet_name="Sheet_1", startcol=2, startrow=1, index=False)
        PacketFrameSizesDF.to_excel(writer,sheet_name="Sheet_1", startcol=3, startrow=1, index=False)



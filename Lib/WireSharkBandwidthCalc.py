import pyshark
import datetime
import statistics
from statistics import mean

#utilizes the pyshark library to calculate the max, min, mean,
#and standard deviation of the bandwidth and packet size of a wireshark capture

#cap = pyshark.FileCapture('/Users/Stump/Desktop/capture2.pcapng', display_filter="ip.addr == 212.192.29.200")
cap = pyshark.FileCapture('/Users/Stump/Desktop/StreamingUDP.pcapng')
#capTimeRef = pyshark.FileCapture('/Users/Stump/Desktop/steamchat.pcapng')
firstPacket = cap[0]
timeStampRef = firstPacket.sniff_time # used to reference the first packet's sniff time in the capture
bandwidths = [] # contains calculated list of bandwidth usage per second
packetSizes = [] # used to calculate each individual bandwidth per second
totalPacketSizes = [] # used to populate each packet size with the corresponding packet number in excel
packetNumbers = [] # used to populate packet number column in excel

i = 0
k = 1.0

for packet in cap:

    packetNumber = packet.number
    packetNumbers.append(packetNumber)
    packet = cap[i]
    time = packet.sniff_time - timeStampRef
    floatTime = float(time.total_seconds())
    size = len(packet)
    packetSizes.append(size)
    totalPacketSizes.append(size)

    if floatTime > k :
        bandwidth = sum(packetSizes) / int(k)
        bandwidths.append(bandwidth)
        k += 1.0
        packetSizes = []

    i = i+1

print(packetNumbers) # list of packet numbers in ascending order

minPacketSize = min(totalPacketSizes)
maxPacketSize = max(totalPacketSizes)
avgPacketSize = mean(totalPacketSizes)
stdevPacketSize = statistics.pstdev(totalPacketSizes)

print('The Minimum Packet Size is:',minPacketSize)
print('The Maximum Packet Size is:',maxPacketSize)
print('The Average Packet Size is:',avgPacketSize)
print('The Standard Deviation of Packet Size is:',stdevPacketSize)

total = sum(bandwidths)
min = min(bandwidths)
max = max(bandwidths)
avg = mean(bandwidths)
stdev = statistics.pstdev(bandwidths)

print('The Total Bandwidth Usage Is:', total * 8, 'Mb/s')
print('The Min Bandwidth Usage Is:', min * 8, 'Mb/s' )
print('The Max Bandwidth Usage Is:', max * 8, 'Mb/s')
print('The Average Bandwidth Usage Is:', avg * 8, 'Mb/s')
print('The Standard Deviation for Bandwidth Usage Is:', stdev * 8, 'Mb/s')
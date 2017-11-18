"""
        PROBLEM
Each line of input represents a single packet. Each line will be formatted as X Y Z some_text, 
where X Y and Z are positive integer and some_text is an arbitrary string. X represents the 
message ID (ie which message this packet is a part of). Y represents the packet ID (ie the index 
of this packet in the message) (packets are zero-indexed, so the first packet in a message will 
have Y=0, the last packet in a message will have Y=Z-1). Z represents the total number of packets 
in the message.

        OUTPUT
Output each completed message, one line per packet. Messages should be outputted in the order in 
which they are completed.
"""
import collections

Packet = collections.namedtuple('Packet', ['mid', 'pid', 'tcount', 'msg'])

def make_packet(raw):
    raw_split = raw.split("  ")
    return Packet(raw_split[0], int(raw_split[2]), int(raw_split[3]), raw_split[4])

def print_packet(self):
    print self.mid + "  " + str(self.pid) + "  " + str(self.tcount) + "  " + self.msg

def packet_search():
    while True: 
        rawpckt = raw_input("> ")
        if rawpckt == "":
            break 
        yield make_packet(rawpckt)

def build_packets():
    built, completion_order = {}, []
    for pckt in packet_search():
        if pckt.mid not in built: 
            built[pckt.mid] = [""] * pckt.tcount

        built[pckt.mid][pckt.pid] = pckt

        if "" not in built[pckt.mid]:
            completion_order.append(built[pckt.mid])
    return completion_order
        

if __name__ == "__main__":
        for pckts in build_packets():
            for p in pckts:
                print_packet(p)
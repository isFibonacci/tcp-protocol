from pj2.simulator import sim
from pj2.simulator import to_layer_three
from pj2.event_list import evl
from pj2.packet import *
from pj2.circular_buffer import circular_buffer

class A:
    def __init__(self):
        # initialization of the state of A
        self.estimated_rtt = 30
        self.state = "WAIT_LAYER5"
        self.seq = 0
        self.lastPkt = None

    def A_input(self, pkt):
        # process the ACK, NACK from B 
        if pkt.checksum == pkt.get_checksum() and pkt.acknum == self.seq :
            self.state = "WAIT_LAYER5"
            self.seq = 0 if self.seq else 1
            evl.remove_timer()
        else :
            to_layer_three("A", self.lastPkt)

    def A_output(self, m):
        pkt = packet(seqnum=self.seq, payload=m)
        to_layer_three("A", pkt)
        evl.start_timer("A", self.estimated_rtt)
        self.state = "WAIT_ACK"
        self.lastPkt = pkt

    def A_handle_timer(self):
        # resend the packet as needed
        to_layer_three("A", self.lastPkt)
        evl.start_timer("A", self.estimated_rtt)


a = A()

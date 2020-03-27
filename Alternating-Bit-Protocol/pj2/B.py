from pj2.simulator import to_layer_five
from pj2.packet import send_ack

class B:
    def __init__(self):
        # initialization of the state of B
        self.seq = 0

    def B_input(self, pkt):
        if pkt.seqnum == self.seq and pkt.checksum == pkt.get_checksum() : 
            to_layer_five("1", pkt.payload.data)
            send_ack("B", self.seq)
            self.seq = 0 if pkt.seqnum else 1
        else :
            oldSeq = 0 if self.seq else 1
            send_ack("B", oldSeq)

    def B_output(self, m):
        return

    def B_handle_timer(self):
        return


b = B()

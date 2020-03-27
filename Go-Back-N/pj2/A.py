from pj2.simulator import sim
from pj2.simulator import to_layer_three
from pj2.event_list import evl
from pj2.packet import *
from pj2.circular_buffer import circular_buffer

class A:
    def __init__(self):
        # go back n, the initialization of A
        # Initialize the initial sequence number to 0.
        # You need to initialize the circular buffer, using "circular_buffer(max)". 
        # max is the number of the packets that the buffer can hold
        # You can set the estimated_rtt to be 30, which is used as a parameter when you call start_timer
    
        self.estimated_rtt = 30
        self.seq = 0
        self.nextSeq = 0
        self.windowSize = 8
        self.base = 0
        self.window = circular_buffer(self.windowSize)


    def A_input(self, pkt):
        # go back n, A_input
        # Verify that the packet is not corrupted
        # Update the circular buffer according to
        # the acknowledgement number using "pop()
        if pkt.checksum == pkt.get_checksum() :
            # remove all teh acknowledged ptk
            while self.base < pkt.acknum + 1 :
                self.window.pop()
                self.base += 1
        
            if self.base == self.nextSeq :
                evl.remove_timer()
            else :
                evl.start_timer("A", self.estimated_rtt)


    def A_output(self, m):
        # go back n, A_output
        # If the buffer is full, just drop the packet
        # Construct the packet based on the message. 
        # Make sure that the sequence number is correct
        # Send the packet and save it to the circular buffer using "push()" of circular_buffer
        # Set the timer using "evl.start_timer(entity, time)", and the time should be set to estimated_rtt. 
        # iMake sure that there is only one timer started in the event list
        
        # if not self.window.isfull() : 
        if self.nextSeq < self.base + self.windowSize :
            pkt = packet(seqnum=self.nextSeq, payload=m)
            # print(str(pkt.payload.data))
            self.window.push(pkt)
            to_layer_three("A", pkt)

            # if self.base == self.nextSeq : 
            evl.start_timer("A", self.estimated_rtt)
            self.nextSeq += 1

    def A_handle_timer(self):
        # go back n, A_handle_timer
        # Read all the sent packet that it is not acknowledged
        # using "read_all()" of the circular buffer and resend them
        # If you need to resend packets, set a timer after that

        for ptk in self.window.read_all() :
            if ptk.seqnum >= self.base :
                to_layer_three("A", ptk)
        
        evl.start_timer("A", self.estimated_rtt)


a = A()

## Overview
The transport-level code for implementing a simple reliable data transfer protocol. The programming interface provided a simulated hardware/software environment. 

## Compilation steps
1. install Python 3
2. go to the specific folder
- for Alternating-Bit-Protocol version :
```bash
$ cd Alternating-Bit-Protocol
```

```bash
$ python3 main.py
```

- for Go-Back-N version :
```bash
$ cd Go-Back-N
```

```bash
$ python3 main.py
```

## Test cases

- for Alternating-Bit-Protocol version :
In simulator.py set the following different parameters.

1. TEST CASE 1 :

PARAMETERS :
```python
self.lossprob = 0.3  
self.corruptprob = 0.5 
self.Lambda = 2000  
self.nsimmax = 27
```

RESULT :
```bash
data recieved：aaaaaaaaaaaaaaaaaaaa
data recieved：bbbbbbbbbbbbbbbbbbbb
data recieved：cccccccccccccccccccc
data recieved：dddddddddddddddddddd
data recieved：eeeeeeeeeeeeeeeeeeee
data recieved：ffffffffffffffffffff
data recieved：gggggggggggggggggggg
data recieved：hhhhhhhhhhhhhhhhhhhh
data recieved：iiiiiiiiiiiiiiiiiiii
data recieved：jjjjjjjjjjjjjjjjjjjj
data recieved：kkkkkkkkkkkkkkkkkkkk
data recieved：llllllllllllllllllll
data recieved：mmmmmmmmmmmmmmmmmmmm
data recieved：nnnnnnnnnnnnnnnnnnnn
data recieved：oooooooooooooooooooo
data recieved：pppppppppppppppppppp
data recieved：qqqqqqqqqqqqqqqqqqqq
data recieved：rrrrrrrrrrrrrrrrrrrr
data recieved：ssssssssssssssssssss
data recieved：tttttttttttttttttttt
data recieved：uuuuuuuuuuuuuuuuuuuu
data recieved：vvvvvvvvvvvvvvvvvvvv
data recieved：wwwwwwwwwwwwwwwwwwww
data recieved：xxxxxxxxxxxxxxxxxxxx
data recieved：yyyyyyyyyyyyyyyyyyyy
data recieved：zzzzzzzzzzzzzzzzzzzz
simulation end
```

2. TEST CASE 2 :

PARAMETERS :
```python
self.lossprob = 0.2
self.corruptprob = 0.1 
self.Lambda = 2000  
self.nsimmax = 23
```

RESULT :
```bash
data recieved：aaaaaaaaaaaaaaaaaaaa
data recieved：bbbbbbbbbbbbbbbbbbbb
data recieved：cccccccccccccccccccc
data recieved：dddddddddddddddddddd
data recieved：eeeeeeeeeeeeeeeeeeee
data recieved：ffffffffffffffffffff
data recieved：gggggggggggggggggggg
data recieved：hhhhhhhhhhhhhhhhhhhh
data recieved：iiiiiiiiiiiiiiiiiiii
data recieved：jjjjjjjjjjjjjjjjjjjj
data recieved：kkkkkkkkkkkkkkkkkkkk
data recieved：llllllllllllllllllll
data recieved：mmmmmmmmmmmmmmmmmmmm
data recieved：nnnnnnnnnnnnnnnnnnnn
data recieved：oooooooooooooooooooo
data recieved：pppppppppppppppppppp
data recieved：qqqqqqqqqqqqqqqqqqqq
data recieved：rrrrrrrrrrrrrrrrrrrr
data recieved：ssssssssssssssssssss
data recieved：tttttttttttttttttttt
data recieved：uuuuuuuuuuuuuuuuuuuu
data recieved：vvvvvvvvvvvvvvvvvvvv
simulation end
```

3. TEST CASE 3 :

PARAMETERS :
```python
self.lossprob = 0.4
self.corruptprob = 0.8 
self.Lambda = 2000  
self.nsimmax = 20
```

RESULT :
```bash
data recieved：aaaaaaaaaaaaaaaaaaaa
data recieved：bbbbbbbbbbbbbbbbbbbb
data recieved：cccccccccccccccccccc
data recieved：dddddddddddddddddddd
data recieved：eeeeeeeeeeeeeeeeeeee
data recieved：ffffffffffffffffffff
data recieved：gggggggggggggggggggg
data recieved：hhhhhhhhhhhhhhhhhhhh
data recieved：iiiiiiiiiiiiiiiiiiii
data recieved：jjjjjjjjjjjjjjjjjjjj
data recieved：kkkkkkkkkkkkkkkkkkkk
data recieved：llllllllllllllllllll
data recieved：mmmmmmmmmmmmmmmmmmmm
data recieved：nnnnnnnnnnnnnnnnnnnn
data recieved：oooooooooooooooooooo
data recieved：pppppppppppppppppppp
data recieved：qqqqqqqqqqqqqqqqqqqq
data recieved：rrrrrrrrrrrrrrrrrrrr
data recieved：ssssssssssssssssssss
simulation end
```

- for Go-Back-N version :
In simulator.py set the following different parameters.

1. TEST CASE 1 :

PARAMETERS :
```python
self.lossprob = 0.3  
self.corruptprob = 0.5 
self.Lambda = 2000  
self.nsimmax = 27
```

RESULT :
```bash
data recieved：aaaaaaaaaaaaaaaaaaaa
data recieved：bbbbbbbbbbbbbbbbbbbb
data recieved：cccccccccccccccccccc
data recieved：dddddddddddddddddddd
data recieved：eeeeeeeeeeeeeeeeeeee
data recieved：ffffffffffffffffffff
data recieved：gggggggggggggggggggg
data recieved：hhhhhhhhhhhhhhhhhhhh
data recieved：iiiiiiiiiiiiiiiiiiii
data recieved：jjjjjjjjjjjjjjjjjjjj
data recieved：kkkkkkkkkkkkkkkkkkkk
data recieved：llllllllllllllllllll
data recieved：mmmmmmmmmmmmmmmmmmmm
data recieved：nnnnnnnnnnnnnnnnnnnn
data recieved：oooooooooooooooooooo
data recieved：pppppppppppppppppppp
data recieved：qqqqqqqqqqqqqqqqqqqq
data recieved：rrrrrrrrrrrrrrrrrrrr
data recieved：ssssssssssssssssssss
data recieved：tttttttttttttttttttt
data recieved：uuuuuuuuuuuuuuuuuuuu
data recieved：vvvvvvvvvvvvvvvvvvvv
data recieved：wwwwwwwwwwwwwwwwwwww
data recieved：xxxxxxxxxxxxxxxxxxxx
data recieved：yyyyyyyyyyyyyyyyyyyy
data recieved：zzzzzzzzzzzzzzzzzzzz
simulation end
```

2. TEST CASE 2 :

PARAMETERS :
```python
self.lossprob = 0.2
self.corruptprob = 0.1 
self.Lambda = 2000  
self.nsimmax = 23
```

RESULT :
```bash
data recieved：aaaaaaaaaaaaaaaaaaaa
data recieved：bbbbbbbbbbbbbbbbbbbb
data recieved：cccccccccccccccccccc
data recieved：dddddddddddddddddddd
data recieved：eeeeeeeeeeeeeeeeeeee
data recieved：ffffffffffffffffffff
data recieved：gggggggggggggggggggg
data recieved：hhhhhhhhhhhhhhhhhhhh
data recieved：iiiiiiiiiiiiiiiiiiii
data recieved：jjjjjjjjjjjjjjjjjjjj
data recieved：kkkkkkkkkkkkkkkkkkkk
data recieved：llllllllllllllllllll
data recieved：mmmmmmmmmmmmmmmmmmmm
data recieved：nnnnnnnnnnnnnnnnnnnn
data recieved：oooooooooooooooooooo
data recieved：pppppppppppppppppppp
data recieved：qqqqqqqqqqqqqqqqqqqq
data recieved：rrrrrrrrrrrrrrrrrrrr
data recieved：ssssssssssssssssssss
data recieved：tttttttttttttttttttt
data recieved：uuuuuuuuuuuuuuuuuuuu
data recieved：vvvvvvvvvvvvvvvvvvvv
simulation end
```

3. TEST CASE 3 :

PARAMETERS :
```python
self.lossprob = 0.4
self.corruptprob = 0.8 
self.Lambda = 2000  
self.nsimmax = 20
```

RESULT :
```bash
data recieved：aaaaaaaaaaaaaaaaaaaa
data recieved：bbbbbbbbbbbbbbbbbbbb
data recieved：cccccccccccccccccccc
data recieved：dddddddddddddddddddd
data recieved：eeeeeeeeeeeeeeeeeeee
data recieved：ffffffffffffffffffff
data recieved：gggggggggggggggggggg
data recieved：hhhhhhhhhhhhhhhhhhhh
data recieved：iiiiiiiiiiiiiiiiiiii
data recieved：jjjjjjjjjjjjjjjjjjjj
data recieved：kkkkkkkkkkkkkkkkkkkk
data recieved：llllllllllllllllllll
data recieved：mmmmmmmmmmmmmmmmmmmm
data recieved：nnnnnnnnnnnnnnnnnnnn
data recieved：oooooooooooooooooooo
data recieved：pppppppppppppppppppp
data recieved：qqqqqqqqqqqqqqqqqqqq
data recieved：rrrrrrrrrrrrrrrrrrrr
data recieved：ssssssssssssssssssss
simulation end
```

## Data structure
- for Alternating-Bit-Protocol version :
  Not added, not uisng provided data structure

- for Go-Back-N version :
  Not added, uisng provided circle buffer

## Functions or methods
- for Alternating-Bit-Protocol version :
  
    In A.py : 

1. def __init__(self): # initialization of the state of A
2. def A_input(self, pkt): # process the ACK, NACK from B
3. def A_output(self, m): # send packet to the network
4. def A_handle_timer(self): # resend the packet as needed

    In B.py : 

5. def B_input(self, pkt): # process ptk from A
6. def __init__(self) : # initialization of the state of B

- for Go-Back-N version :
  
    In A.py : 

1. def __init__(self): # initialization of the state of A
2. def A_input(self, pkt): # process the ACK, NACK from B
3. def A_output(self, m): # send packet to the network
4. def A_handle_timer(self): # resend the packet as needed
    
    In B.py : 

5. def B_input(self, pkt): # process ptk from A
6. def __init__(self) : # initialization of the state of B
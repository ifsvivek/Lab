# Initialize the simulator
set ns [new Simulator]

# Open the trace and nam files
set nf [open lab2.nam w]
set f [open lab2.tr w]

# Set up tracing
$ns namtrace-all $nf
$ns trace-all $f

# Procedure to end the simulation
proc finish {} {
    global ns nf f
    $ns flush-trace
    close $nf
    close $f
    exec nam lab2.nam &
    exit 0
}

# Define the nodes
set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]
set n5 [$ns node]

# Label nodes for easier identification in NAM
$n0 label "Ping0"
$n1 label "Ping1"
$n2 label "R1"
$n3 label "R2"
$n4 label "Ping4"
$n5 label "Ping5"

# Set link colors
$ns color 1 Red
$ns color 2 Blue
$ns color 3 Green
$ns color 4 Orange

# Define duplex links between the nodes
$ns duplex-link $n0 $n2 1Mb 10ms DropTail
$ns duplex-link $n1 $n2 1Mb 10ms DropTail
$ns duplex-link $n2 $n3 0.4Mb 30ms DropTail
$ns duplex-link $n3 $n4 1Mb 10ms DropTail
$ns duplex-link $n3 $n5 1Mb 10ms DropTail

# Set up ping agents
set ping0 [new Agent/Ping]
$ns attach-agent $n0 $ping0

set ping1 [new Agent/Ping]
$ns attach-agent $n1 $ping1

set ping4 [new Agent/Ping]
$ns attach-agent $n4 $ping4

set ping5 [new Agent/Ping]
$ns attach-agent $n5 $ping5

# Create Null agents to receive packets
set null4 [new Agent/Null]
$ns attach-agent $n4 $null4

set null5 [new Agent/Null]
$ns attach-agent $n5 $null5

# Connect the ping agents to the Null agents
$ns connect $ping0 $null4
$ns connect $ping1 $null5

# Procedure to send ping packets periodically
proc SendPingPacket {} {
    global ns ping0 ping1
    set intervalTime 0.001
    set now [$ns now]
    $ns at [expr $now + $intervalTime] "$ping0 send"
    $ns at [expr $now + $intervalTime] "$ping1 send"
    $ns at [expr $now + $intervalTime] "SendPingPacket"
}

# Define the behavior when an agent receives a packet
Agent/Ping instproc recv {from rtt} {
    global seq
    $self instvar node_
    puts "The node [$node_ id] received an ACK from $from with RTT $rtt ms"
}

# Set classes for ping agents
$ping0 set Class_ 1
$ping1 set Class_ 2
$ping4 set Class_ 4
$ping5 set Class_ 5

# Schedule events
$ns at 0.01 "SendPingPacket"
$ns at 10.0 "finish"

# Run the simulation
$ns run

set ns[new Simulator]
set nf [open lab2.nam w]
set f [open lab2.tr w]
$ns namtrace-all $nf
$ns trace-all $f

proc finish {} {
    global ns nf f
    $ns flush-trace
    close $nf
    close $f
    exec nam lab2.nam &
    exit 0
}

set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]
set n5 [$ns node]

$n0 label "Ping0"
$n1 label "Ping1"
$n2 label "R1"
$n3 label "R2"
$n4 label "Ping4"
$n5 label "Ping5"

$ns color 1 Red
$ns color 2 Blue
$ns color 3 Green
$ns color 4 Orange

$ns duplex-link $n0 $n2 1Mb 10ms DropTail
$ns duplex-link $n1 $n2 1Mb 10ms DropTail
$ns duplex-link $n2 $n3 0.4Mb 30ms DropTail
$ns duplex-link $n3 $n4 1Mb 10ms DropTail
$ns duplex-link $n3 $n5 1Mb 10ms DropTail

set ping0[new Agent/Ping]
$ns attach-agent $n0 $ping0
set ping1[new Agent/Ping]
$ns attach-agent $n1 $ping1
set ping4[new Agent/Ping]
$ns attach-agent $n4 $ping4
set ping5[new Agent/Ping]
$ns attach-agent $n5 $ping5

$ns connect $ping0 $n4
$ns connect $ping1 $n5

proc SendPingPacket {}{
    global ns ping0 ping1
    set intervalTime 0.001
    set now[$ns now]
    $ns at [expr $now+$intervalTime] "$ping0 send"
    $ns at [expr $now+$intervalTime] "$ping1 send"
    $ns at [expr $now+$intervalTime] "SendPingPacket"    
}

Agent/Ping instproc recv {from rtt} {
    global seq
    $self instvar node_
    puts "The node [$node_ id] received a ACK from $from with RTT $rtt ms"
}

$ping0 set Class_ 1
$ping1 set Class_ 2
$ping4 set Class_ 4
$ping5 set Class_ 5

$ns at 0.01 "SendPingPacket"
$ns at 10.0 "finish"
$ns run
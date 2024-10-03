Begin{
    drop = 0;
}
{
    if($1 == "d"){
        drop++;
    }
}
END{
    print "Total number of %s packets dropped: %d", $5, drop;
}
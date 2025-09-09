    AREA SEARCH, CODE, READONLY
ENTRY
    LDR R0, =AVALUE
    MOV R1, #10
    MOV R2, #0X00000005
    MOV R4, #0

search_loop
    CMP R1, #0
    BEQ end_search
    LDR R3, [R0], #4
    CMP R1, R2
    BEQ element_found
    SUB R1, R1, #1
    B search_loop

element_found
    MOV R4, #1

end_search
    MOV R0, R4
    B .

    AREA DATA1, DATA, READWRITE
AVALUE
    DCD 0X00000001
    DCD 0X00000002
    DCD 0X00000003
    DCD 0X00000004
    DCD 0X00000005
    DCD 0X00000006
    DCD 0X00000007
    DCD 0X00000008
    DCD 0X00000009
    DCD 0X0000000A
    END
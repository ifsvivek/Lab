    AREA SearchArray, CODE, READONLY
    ENTRY

; Constants
ARRAY_START    EQU     0x40000000  ; Starting address of the array in memory
ARRAY_LENGTH   EQU     10          ; Length of the array (number of elements)
TARGET         EQU     0x00000008  ; Element to search for

; Registers
; r0 - current array element
; r1 - target element
; r2 - index
; r3 - array base address
; r4 - temporary register (not used in this version)
; r5 - array length

    LDR     r1, =TARGET             ; Load the target value into r1
    LDR     r3, =ARRAY_START        ; Load the base address of the array into r3
    MOV     r2, #0                  ; Initialize index to 0
    MOV     r5, #ARRAY_LENGTH       ; Load the array length into r5

Loop
    CMP     r2, r5                  ; Compare index with array length
    BEQ     NotFound                ; If index == array length, target not found
    LDR     r0, [r3, r2, LSL #2]    ; Load the current array element into r0
    CMP     r0, r1                  ; Compare current element with target
    BEQ     Found                   ; If equal, target found
    ADD     r2, r2, #1              ; Increment index
    B       Loop                    ; Repeat the loop

Found
    ; Target found
    MOV     r0, r2                  ; Move the index of the found element into r0
    B       End                     ; Jump to end of program

NotFound
    ; Target not found
    MOV     r0, #-1                 ; Move -1 into r0 to indicate not found

End
    ; Here, r0 will have the index of the found element or -1 if not found
    B       End                     ; End of program, infinite loop

    END
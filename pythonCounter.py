
b00=False
b00Bar = True
b01=False
b01Bar = True
b02=False
b02Bar = True
b03=False
b03Bar = True

b10=False
b10Bar = True
b11=False
b11Bar = True
b12=False
b12Bar = True
b13=False
b13Bar = True

b20=False
b20Bar = True
b21=False
b21Bar = True
b22=False
b22Bar = True
b23=False
b23Bar = True

b30=False
b30Bar = True
b31=False
b31Bar = True
b32=False
b32Bar = True
b33=False
b33Bar = True

b40=False
b40Bar = True
b41=False
b41Bar = True
b42=False
b42Bar = True
b43=False
b43Bar = True

pulse = True

while(not b41):
    pulse = not pulse
    
    #################################################
    ################       b0       #################
    #################################################

    #             rst
    b00    = not (b03   or b00Bar)
    #             st       
    b00Bar = not (pulse or b00   )

    b01    = not ( b03                or b01Bar)
    b01Bar = not ((b00 and not pulse) or b01   )

    b02    = not ( b03            or b02Bar)
    b02Bar = not ((b01 and pulse) or b02   )

    b03    = not ((b03 and not b02) or b03Bar)
    b03Bar = not ((b02 and not pulse) or b03 )


    #             rst
    b00    = not (b03   or b00Bar)
    #             st       
    b00Bar = not (pulse or b00   )

    b01    = not ( b03                or b01Bar)
    b01Bar = not ((b00 and not pulse) or b01   )

    b02    = not ( b03            or b02Bar)
    b02Bar = not ((b01 and pulse) or b02   )

    b03    = not ((b03 and not b02) or b03Bar)
    b03Bar = not ((b02 and not pulse) or b03 )


    #             rst
    b00    = not (b03   or b00Bar)
    #             st       
    b00Bar = not (pulse or b00   )

    b01    = not ( b03                or b01Bar)
    b01Bar = not ((b00 and not pulse) or b01   )

    b02    = not ( b03            or b02Bar)
    b02Bar = not ((b01 and pulse) or b02   )

    b03    = not ((b03 and not b02) or b03Bar)
    b03Bar = not ((b02 and not pulse) or b03 )

    #################################################
    ################       b1       #################
    #################################################
    #             rst
    b10    = not (b13 or b10Bar)
    #             st       
    b10Bar = not (b01 or b10   )

    b11    = not ( b13              or b11Bar)
    b11Bar = not ((b10 and not b01) or b11   )

    b12    = not ( b13          or b12Bar)
    b12Bar = not ((b11 and b01) or b12   )

    b13    = not ((b13 and not b12) or b13Bar)
    b13Bar = not ((b12 and not b01) or b13 )

    
    #             rst
    b10    = not (b13 or b10Bar)
    #             st       
    b10Bar = not (b01 or b10   )

    b11    = not ( b13              or b11Bar)
    b11Bar = not ((b10 and not b01) or b11   )

    b12    = not ( b13          or b12Bar)
    b12Bar = not ((b11 and b01) or b12   )

    b13    = not ((b13 and not b12) or b13Bar)
    b13Bar = not ((b12 and not b01) or b13 )
    
    #             rst
    b10    = not (b13 or b10Bar)
    #             st       
    b10Bar = not (b01 or b10   )

    b11    = not ( b13              or b11Bar)
    b11Bar = not ((b10 and not b01) or b11   )

    b12    = not ( b13          or b12Bar)
    b12Bar = not ((b11 and b01) or b12   )

    b13    = not ((b13 and not b12) or b13Bar)
    b13Bar = not ((b12 and not b01) or b13 )

    #################################################
    ################       b2       #################
    #################################################

    #             rst
    b20    = not (b23 or b20Bar)
    #             st       
    b20Bar = not (b11 or b20   )

    b21    = not ( b23              or b21Bar)
    b21Bar = not ((b20 and not b11) or b21   )

    b22    = not ( b23          or b22Bar)
    b22Bar = not ((b21 and b11) or b22   )

    b23    = not ((b23 and not b22) or b23Bar)
    b23Bar = not ((b22 and not b11) or b23 )
    
    #             rst
    b20    = not (b23 or b20Bar)
    #             st       
    b20Bar = not (b11 or b20   )

    b21    = not ( b23              or b21Bar)
    b21Bar = not ((b20 and not b11) or b21   )

    b22    = not ( b23          or b22Bar)
    b22Bar = not ((b21 and b11) or b22   )

    b23    = not ((b23 and not b22) or b23Bar)
    b23Bar = not ((b22 and not b11) or b23 )
    
    #             rst
    b20    = not (b23 or b20Bar)
    #             st       
    b20Bar = not (b11 or b20   )

    b21    = not ( b23              or b21Bar)
    b21Bar = not ((b20 and not b11) or b21   )

    b22    = not ( b23          or b22Bar)
    b22Bar = not ((b21 and b11) or b22   )

    b23    = not ((b23 and not b22) or b23Bar)
    b23Bar = not ((b22 and not b11) or b23 )


    #################################################
    ################       b3       #################
    #################################################

    #             rst
    b30    = not (b33   or b30Bar)
    #             st       
    b30Bar = not (b21 or b30   )

    b31    = not ( b33                or b31Bar)
    b31Bar = not ((b30 and not b21) or b31   )

    b32    = not ( b33            or b32Bar)
    b32Bar = not ((b31 and b21) or b32   )

    b33    = not ((b33 and not b32) or   b33Bar)
    b33Bar = not ((b32 and not b21) or b33 )

    #             rst
    b30    = not (b33   or b30Bar)
    #             st       
    b30Bar = not (b21 or b30   )

    b31    = not ( b33                or b31Bar)
    b31Bar = not ((b30 and not b21) or b31   )

    b32    = not ( b33            or b32Bar)
    b32Bar = not ((b31 and b21) or b32   )

    b33    = not ((b33 and not b32) or   b33Bar)
    b33Bar = not ((b32 and not b21) or b33 )

    #             rst
    b30    = not (b33   or b30Bar)
    #             st       
    b30Bar = not (b21 or b30   )

    b31    = not ( b33                or b31Bar)
    b31Bar = not ((b30 and not b21) or b31   )

    b32    = not ( b33            or b32Bar)
    b32Bar = not ((b31 and b21) or b32   )

    b33    = not ((b33 and not b32) or   b33Bar)
    b33Bar = not ((b32 and not b21) or b33 )

    #################################################
    ################       b4       #################
    #################################################

    #             rst
    b40    = not (b43   or b40Bar)
    #             st       
    b40Bar = not (b31 or b40   )

    b41    = not ( b43              or b41Bar)
    b41Bar = not ((b40 and not b31) or b41   )

    b42    = not ( b43          or b42Bar)
    b42Bar = not ((b41 and b31) or b42   )

    b43    = not ((b43 and not b42) or b43Bar)
    b43Bar = not ((b42 and not b31) or b43 )
    
    #             rst
    b40    = not (b43   or b40Bar)
    #             st       
    b40Bar = not (b31 or b40   )

    b41    = not ( b43              or b41Bar)
    b41Bar = not ((b40 and not b31) or b41   )

    b42    = not ( b43          or b42Bar)
    b42Bar = not ((b41 and b31) or b42   )

    b43    = not ((b43 and not b42) or b43Bar)
    b43Bar = not ((b42 and not b31) or b43 )
    
    #             rst
    b40    = not (b43   or b40Bar)
    #             st       
    b40Bar = not (b31 or b40   )

    b41    = not ( b43              or b41Bar)
    b41Bar = not ((b40 and not b31) or b41   )

    b42    = not ( b43          or b42Bar)
    b42Bar = not ((b41 and b31) or b42   )

    b43    = not ((b43 and not b42) or b43Bar)
    b43Bar = not ((b42 and not b31) or b43 )

    print("p: " + str(int(pulse)) + "\t" + str(int(b31)) + str(int(b21)) + str(int(b11)) + str(int(b01)) + str(int(pulse)))




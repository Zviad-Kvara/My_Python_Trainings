# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal 
# representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range 
# must be rounded to the closest valid value.
# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

# 255, 255, 255 --> "FFFFFF"
# 255, 255, 300 --> "FFFFFF"
# 0, 0, 0       --> "000000"
# 148, 0, 211   --> "9400D3"
def rgb(r, g, b):
    if 0 > r > 255 and 0 > g > 255 and 0 > b > 255:
        
    


print(rgb(255, 255, 255))      # "FFFFFF"
# print(rgb(255, 255, 300))      # "FFFFFF"
# print(rgb(0, 0, 0))            # "000000"
# print(rgb(148, 0, 211))        # "9400D3"
#
from moku.instruments import Oscilloscope

# Connect to your Moku by its ip address using Oscilloscope('192.168.###.###')
# force_connect will overtake an existing connection
osc = Oscilloscope('192.168.127.145', force_connect=True)
### Let's do the functional equivalent of the classic *IDN command ### 
idn = osc.serial_number()
prop = osc.describe()
print(osc)
print(idn)
print(prop)
try:
    # Set the span to from -1ms to 1ms i.e. trigger point centred
    osc.set_timebase(-1e-3, 1e-3)

    # Get and print a single frame  of data (time series
    # of voltage per channel)

except Exception as e:
    osc.relinquish_ownership()
    raise e
finally:
    # Close the connection to the Moku device
    # This ensures network resources are released correctly
    osc.relinquish_ownership()

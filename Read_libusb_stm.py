import usb1
import libusb1
import usb.core
import usb.util





def main():

    #find our device
    #dev = usb.core.find(idVendor=483, idProduct=5750)

    #was it found?
    #if dev is None:
     #   print('Device not found')
    #if dev is True:
     #   print('Device found')

   # Device_STM_Discovery = context.getByVendorIDAndProductID( 0x0483, 0x5750,skip_on_access_error=False, skip_on_error=False)
   # if Device_STM_Discovery is None:
   #     print('Device not found')
   # if Device_STM_Discovery is True:
   #     print('Device found')

#------------------------------------------------------------------------------------------------------------------------#
    context = usb1.USBContext()
    device_number = 0
    for device in context.getDeviceList(skip_on_error=True):
        print ('ID %04x:%04x' % (device.getVendorID(), device.getProductID()), '->'.join(str(x) for x in ['Bus %03i' % (device.getBusNumber(), )] + device.getPortNumberList()), 'Device', device.getDeviceAddress())
        Vendor_ID = device.getVendorID()
        Product_ID = device.getProductID()

        device_number = device_number + 1
        if Vendor_ID == 1155 and Product_ID == 22352:
            Device_interface = device_number
            print ('STM Discovery Board Found')
           # device_Handle = context.openByVendorIDAndProductID( 0x0483, 0x5750,skip_on_access_error=False, skip_on_error=False)

            device_Handle=device.open()
            if device_Handle == None:
                print ('Cannot open STM Discovery Board')
            else:
                print ('STM Discovery Board Opened')

    device_Handle.claimInterface(0)
    AFE_DATA = device_Handle.bulkRead(0x81, 64, timeout=3000)
    print (AFE_DATA)

    device_Handle.releaseInterface(0)
#---------------------------------------Find USB----------------------------------------------------------------------#
    #context = usb1.USBContext()
    '''
    STM_found = context.getByVendorIDAndProductID(1155, 22352, skip_on_access_error=False, skip_on_error=False)
    if STM_found == None:
        print ('STM Discovery Board Not Found')
    else:
        print ('STM Discovery Board Found')

'''

#---------------------------------------OPEN USB----------------------------------------------------------------------#
   # device_Handle = context.openByVendorIDAndProductID( 0x0483, 0x5750,skip_on_access_error=False, skip_on_error=False)
    #if device_Handle == None:
     #   print ('Cannot open STM Discovery Board')
    #else:
     #   print ('STM Discovery Board Opened')
#---------------------------------------Bulk transfer from STM to PC----------------------------------------------------------------------#
   # print (device_Handle.getEndpoint())
   # USBTransfer = usb1.USBTransfer()

    #USBDeviceHandle = usb1.USBDeviceHandle()
    #device_Handle.getTransfer(iso_packets=0)
    #device_Handle.getDevice()
    #device_Handle.getConfiguration()


    #print(Device_interface)

    #transfer_packet1 = device_Handle.getTransfer(iso_packets=1)
    #transfer_packet1.setIsochronous(endpoint=0x81, buffer_or_len=64, callback=None,user_data=None, timeout=0, iso_transfer_length_list=None)

    #transfer_packet1.submit()




   # USBTransfer = usb1.USBTransfer()
    #USBTransfer.__init__(device_handle, iso_packets, before_submit, after_completion)
    #USBTransfer.setBulk(0X04, 64, callback=None, user_data=None,timeout=0)
    #if USBTransfer.getActualLength() == 64:
    #USBTransfer.setIsochronous(0X04, 64, callback=None,user_data=None, timeout=0, iso_transfer_length_list=None)
   # AFE_DATA = USBTransfer.getEndpoint()




   # while True:
    #    context.handleEvents()



    #USBTransferHelper = usb1.USBTransferHelper()
    #USBTransferHelper.setEventCallback(self, TRANSFER_ERROR, callback)
if __name__ == '__main__':
    main()


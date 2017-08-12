#!/usr/bin/env python

# Copyright (C) 2017 Dominic Spill <dominicgs@gmail.com> 
#
# This library is free software; you can redistribute it and/or
#
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# 
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

from __future__ import print_function

import usb

class DeviceNotFoundError(IOError):
    """ Error indicating no FX2 device was found. """
    pass


class Fx2(object):

    def __init__(self, vendorid, productid, idx=0, verbose=1):
        self.verbose = verbose
        try:
            usbdevs = usb.core.find(find_all=True, idVendor=vendorid, idProduct=productid)
        except usb.core.USBError as e:
            # On some platforms, providing identifiers that don't match with any
            # real device produces a USBError/Pipe Error. We'll convert it into a
            # DeviceNotFoundError.
            if e.errno == LIBUSB_PIPE_ERROR:
                raise DeviceNotFoundError()
            else:
                raise e

        for i, dev in enumerate(usbdevs):
            if i == idx:
                self.device = dev
                break
        else:
            raise DeviceNotFoundError()

    def write_to_ram(self, address, data):
        xfer_size = 1204
        while data:
            try:
                rv = self.device.ctrl_transfer(0x40, 0xA0, address, 0,
                                               data[:xfer_size])
            except usb.core.USBError as e:
                print("Request failed with error: %s" % e)
                return
            if rv:
                print("wrote %d bytes" % rv)
            else:
                print("Error: %d" % ret)
                return
            data = data[xfer_size:]
            address += xfer_size

    def reset_device(self):
        if self.verbose:
            print("Resetting device")
        self.write_to_ram(0xe600, [0x01])

    def run_firmware(self):
        if self.verbose:
            print("Running firmware")
        self.write_to_ram(0xe600, [0x00])

    def write_firmware(self, firmware):
        self.reset_device()
        if self.verbose:
            print("Loading firmware of length: ", len(firmware))
        self.write_to_ram(0, firmware)
        self.run_firmware()

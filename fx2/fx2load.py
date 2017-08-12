#!/usr/bin/env python

# Copyright (C) 2009 Ubixum, Inc. 
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


import argparse
import fx2

def vid_pid(x):
    return int(x, 16)

def main():
    parser = argparse.ArgumentParser(description="A tool for updating fx2 device firmware")
    parser.add_argument('-v', dest='vendorid', metavar='<VendorID>', default=0x04b4,
                        type=vid_pid, help="Vendor ID of device")
    parser.add_argument('-p', dest='productid', metavar='<ProductID>', default=0x8613,
                        type=vid_pid, help="Product ID of device")
    parser.add_argument('-f', dest='firmware', metavar='<filename>',
                        type=str, help="Firmware file to write", required=True)
    args = parser.parse_args()

    device = fx2.Fx2(args.vendorid, args.productid)

    with open(args.firmware) as f:
        data = f.read()
        device.write_firmware(data)

if __name__ == "__main__":
    main()

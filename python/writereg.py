#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-2.0-or-later

from periphery import I2C
import argparse
import gsi2c

def main():
    parser = argparse.ArgumentParser(description="I2C write",prog="write")
    parser.add_argument('-r', dest='register', metavar='register', type=lambda x: int(x,0), required=True, help='register address')
    parser.add_argument('-s', dest='size', metavar='reg size', type=lambda x: int(x,0), default=8,help='register size',choices=[8,16,32])
    parser.add_argument('-d',  dest='writedata', metavar='data', type=lambda x: int(x,0),  required=True, help='data value: 1 2 0x01 0x23 etc ..')
    parser.add_argument('-i', dest='iic', metavar='iic',type=int, default=0, help='i2c bus 0 or 1')
    args = parser.parse_args()

    if args.iic == 0:
        gsi2c.i2c = I2C("/dev/links/csi0_i2c")
    elif args.iic == 1:
        gsi2c.i2c = I2C("/dev/links/csi1_i2c")
    else:
        print("wrong i2c bus!\n")
        return


    if args.size == 8:
        gsi2c.write8(args.register,args.writedata)
        print("0x%02X = 0x%02X"%(args.register,args.writedata))
    if args.size == 16:
        gsi2c.write16(args.register,args.writedata)
        print("0x%04X = 0x%04X"%(args.register,args.writedata))
    if args.size == 32:
        gsi2c.write32(args.register,args.writedata)
        print("0x%04X = 0x%08X"%(args.register,args.writedata))

if __name__ == "__main__":
    main()

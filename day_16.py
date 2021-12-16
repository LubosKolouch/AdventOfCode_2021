#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Advent of Code 2021 Day 16 """

import numpy as np


class AllPackets:
    def __init__(self, in_file: str):
        with open(in_file, "r") as my_file:
            self.packet_str = my_file.readline().strip()

        self.packet = "{0:04b}".format(int(self.packet_str, 16))

        packet_length = len(self.packet) % 4
        padding = (4 - packet_length) % 4
        self.packet = "0" * padding + self.packet

        self.packets = []
        self.pos = 0

    def process_all_packets(self):
        """ Load all packets list """

        while self.pos < len(self.packet):
            next_packet = Packet(packet_str=self.packet, pos=self.pos)
            next_packet.decode_packet()
            self.pos = next_packet.pos
            self.packets.append(next_packet)

        total_sum = 0
        for next_packet in self.packets:

            try:
                total_sum += next_packet.version_sum
            except TypeError:
                pass
        return total_sum, self.packets[0].values


class Packet:
    """ Day 16 AoC """
    def __init__(self, packet_str: str, pos: int):
        self.packet = packet_str
        self.version_sum = 0
        self.pos = pos
        self.values = np.empty(0, dtype=int)
        self.sub_packets = []

    def decode_packet(self):

        try:
            packet_version = int(self.packet[self.pos:self.pos + 3], 2)
            self.version_sum = packet_version
        except ValueError:
            self.pos += 3
            return

        self.pos += 3
        try:
            packet_type = int(self.packet[self.pos:self.pos + 3], 2)
        except ValueError:
            return
        self.pos += 3

        if packet_type == 4:
            # literal packet
            temp_value = ""
            while 1:
                next_num = self.packet[self.pos:self.pos + 5]

                temp_value += next_num[1:]

                self.pos += 5
                if next_num[0] == '0':
                    self.values = np.append(self.values, int(temp_value, 2))
                    break

        else:
            # operator
            type_id = self.packet[self.pos]
            self.pos += 1

            if type_id == '0':

                subpacket_length = self.packet[self.pos:self.pos + 15]
                subpacket_length = int(subpacket_length, 2)
                self.pos += 15

                next_pos = self.pos + subpacket_length

                while self.pos < next_pos:
                    next_packet = Packet(packet_str=self.packet, pos=self.pos)
                    next_packet.decode_packet()
                    self.values = np.append(self.values, next_packet.values)
                    self.version_sum += next_packet.version_sum
                    self.sub_packets.append(next_packet)
                    self.pos = next_packet.pos
            else:
                subpacket_count = int(self.packet[self.pos:self.pos + 11], 2)
                self.pos += 11

                for i in range(subpacket_count):
                    next_packet = Packet(packet_str=self.packet, pos=self.pos)
                    next_packet.decode_packet()
                    self.values = np.append(self.values, next_packet.values)
                    self.version_sum += next_packet.version_sum

                    self.sub_packets.append(next_packet)
                    self.pos = next_packet.pos

        if packet_type == 0:
            self.values = np.sum(self.values)

        elif packet_type == 1:
            self.values = np.product(self.values)

        elif packet_type == 2:
            self.values = np.min(self.values)

        elif packet_type == 3:
            self.values = np.max(self.values)

        elif packet_type == 5:
            self.values = 1 if self.values[0] > self.values[1] else 0

        elif packet_type == 6:
            self.values = 1 if self.values[0] < self.values[1] else 0

        elif packet_type == 7:
            self.values = 1 if self.values[0] == self.values[1] else 0


def test_day_16():
    """ Run the tests """

    packets = AllPackets("input16_test8")
    version, value = packets.process_all_packets()
    assert version == 14
    assert value == 3


# packets = AllPackets("input16_test7")
# assert packets.process_all_packets() == 23


def main():
    """ Run the exercise """
    packets = AllPackets("input16")
    version, value = packets.process_all_packets()
    print(version)
    print(value)


if __name__ == "__main__":
    main()

def analize_ipv6_packet(hex_packet):
    enter = 0
    ipv6_header = {
        "version": hex(0),
        "flow_label": hex(0),
        "traffic_class": hex(0), 
        "next_header": hex(0),
        "hop_limit": hex(0),
        "source": hex(0),
        "destination": hex(0),
    }

    for i in range(len(hex_packet)):
        if hex_packet[i] == 0x86 and hex_packet[i+1] == 0xDD:

            ipv6_header["version"] = str(hex_packet[i+2])
            ipv6_header["flow_label"] = str(" ".join(hex_packet[i+3:i+4]))
            ipv6_header["traffic_class"] = str(" ".join(hex_packet[i+5:i+6]))
            
            #8-bit 
            ipv6_header["next_header"] = str(hex_packet[i+7])
            
            #8-bit
            ipv6_header["hop_limit"] = str(hex_packet[i+8])
            
            #128-bit
            ipv6_header["source"] = str(" ".join(hex_packet[i+9:i+16]))
            
            #128-bit
            ipv6_header["destination"] = str(" ".join(f'{hex_packet[i+17:i+24]}' for n in))
            break

    return ipv6_header

packet= [0x86, 0xDD, 0x60, 0x00, 0x00, 0x00, 0x00, 0x10, 0x11, 0x40,
          0x20, 0x01, 0x0d, 0xb8, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00, 0x01, 0x20, 0x01, 0x0d, 0xb8, 0x00, 0x00, 0x00, 0x00,
          0x00, 0x00, 0x00, 0x02]
result = analize_ipv6_packet(packet)
print(result)
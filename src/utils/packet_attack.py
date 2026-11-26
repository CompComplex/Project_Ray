import socket
import struct

def send_packet(target_ip, target_port, source_ip):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        packet_payload = struct.pack("!4s", bytes(source_ip, "utf-8"))
        sock.sendto(packet_payload, (target_ip,target_port))
        sock.close()
    except Exception as e:
        print(f"Error sending packet: {e}")

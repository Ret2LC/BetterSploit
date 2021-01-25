import subprocess as sub
import argparse


class Enumeration(object):
    def __init__(self, file_for_results):
        self.file_for_results = file_for_results

    def enumeration_start(self):
        investigate_sockets = sub.check_output("ss -r -a -e", shell=True)
        look_at_processes = sub.check_output("ps aux", shell=True)
        cpu = sub.check_output("lscpu", shell=True)
        usb = sub.check_output("lsusb", shell=True)
        block_devices = sub.check_output("lsblk", shell=True)
        pci_devices = sub.check_output("lspci", shell=True)
        File_System_Information = sub.check_output("sudo fdisk -l", shell=True)
        memory_information = sub.check_output("sudo dmidecode -t memory", shell=True)
        bios = sub.check_output("sudo dmidecode -t bios", shell=True)
        system = sub.check_output("sudo dmidecode -t system", shell=True)
        processor = sub.check_output("sudo dmidecode -t processor", shell=True)
        hardware_dump = sub.check_output("sudo dmidecode", shell=True)
        with open(self.file_for_results, "w") as file:
            file.write("SOCKET INFORMATION: \n" + investigate_sockets.decode() + 
            "\n\n\n" + "RUNNING PROCESSES: \n" + look_at_processes.decode() +
            "\n\n\n" + "CPU INFO: \n" + cpu.decode() +
            "\n\n\n" + "USB INFORMATION: \n" + usb.decode() + 
            "\n\n\n" + "BLOCK DEVICES: \n" + block_devices.decode() +
            "\n\n\n" + "PCI DEVICES: \n" + pci_devices.decode() +
            "\n\n\n" + "FILE SYSTEM INFORMATION: \n" + File_System_Information.decode() + 
            "\n\n\n" + "MEMORY INFORMATION: \n" + memory_information.decode() + 
            "\n\n\n" + "BIOS INFORMATION: \n" + bios.decode() +
            "\n\n\n" + "SYSTEM INFORMATION: \n" + system.decode() +
            "\n\n\n" + "PROCESSOR INFORMATION: \n" + processor.decode() + 
            "\n\n\n" + "HARDWARE DUMP: \n" + hardware_dump.decode())
            file.close()


parser = argparse.ArgumentParser()
parser.add_argument("--enumerate", metavar="FILE.txt", type=str, help="enumerate the system and save to a file")

args = parser.parse_args()
if __name__ == "__main__":
    send = Enumeration(file_for_results=args.enumerate)
    send.enumeration_start()
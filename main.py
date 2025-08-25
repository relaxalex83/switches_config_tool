import subprocess
from netmiko import ConnectHandler
from threading import Thread
from tqdm import tqdm
import tabulate
import getpass
import numpy as np
from colorama import Fore, Style, init

# Initialize colorama
init()

# Start Disable Cisco
def disable_10_50_2_13_cisco(switch_ip, username, password, secret, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='cisco_ios', username=username, password=password, secret=secret)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.13dis.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def disable_10_50_2_15_cisco(switch_ip, username, password, secret, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='cisco_ios', username=username, password=password, secret=secret)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.15dis.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def disable_10_50_2_16_cisco(switch_ip, username, password, secret, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='cisco_ios', username=username, password=password, secret=secret)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.16dis.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def disable_10_50_2_17_cisco(switch_ip, username, password, secret, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='cisco_ios', username=username, password=password, secret=secret)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.17dis.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def disable_10_50_2_18_cisco(switch_ip, username, password, secret, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='cisco_ios', username=username, password=password, secret=secret)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.18dis.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def disable_10_50_2_19_cisco(switch_ip, username, password, secret, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='cisco_ios', username=username, password=password, secret=secret)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.19dis.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def disable_10_50_2_20_cisco(switch_ip, username, password, secret, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='cisco_ios', username=username, password=password, secret=secret)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.20dis.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def disable_10_50_2_22_cisco(switch_ip, username, password, secret, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='cisco_ios', username=username, password=password, secret=secret)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.22dis.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def disable_10_50_2_24_cisco(switch_ip, username, password, secret, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='cisco_ios', username=username, password=password, secret=secret)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.24dis.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def disable_10_50_2_25_cisco(switch_ip, username, password, secret, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='cisco_ios', username=username, password=password, secret=secret)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.25dis.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def disable_10_50_2_26_cisco(switch_ip, username, password, secret, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='cisco_ios', username=username, password=password, secret=secret)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.26dis.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def disable_10_50_2_27_cisco(switch_ip, username, password, secret, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='cisco_ios', username=username, password=password, secret=secret)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.27dis.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def disable_10_50_2_29_cisco(switch_ip, username, password, secret, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='cisco_ios', username=username, password=password, secret=secret)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.29dis.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def disable_10_50_2_30_cisco(switch_ip, username, password, secret, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='cisco_ios', username=username, password=password, secret=secret)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.30dis.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def disable_10_50_2_32_cisco(switch_ip, username, password, secret, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='cisco_ios', username=username, password=password, secret=secret)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.32dis.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def disable_10_50_2_33_cisco(switch_ip, username, password, secret, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='cisco_ios', username=username, password=password, secret=secret)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.33dis.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def disable_10_50_2_35_cisco(switch_ip, username, password, secret, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='cisco_ios', username=username, password=password, secret=secret)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.35dis.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def disable_10_50_2_70_cisco(switch_ip, username, password, secret, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='cisco_ios', username=username, password=password, secret=secret)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.70dis.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def disable_10_50_2_71_cisco(switch_ip, username, password, secret, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='cisco_ios', username=username, password=password, secret=secret)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.71dis.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)
# End Disable Cisco

# Start Enable Cisco
def enable_10_50_2_13_cisco(switch_ip, username, password, secret, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='cisco_ios', username=username, password=password, secret=secret)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.13en.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def enable_10_50_2_15_cisco(switch_ip, username, password, secret, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='cisco_ios', username=username, password=password, secret=secret)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.15en.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def enable_10_50_2_16_cisco(switch_ip, username, password, secret, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='cisco_ios', username=username, password=password, secret=secret)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.16en.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def enable_10_50_2_17_cisco(switch_ip, username, password, secret, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='cisco_ios', username=username, password=password, secret=secret)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.17en.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def enable_10_50_2_18_cisco(switch_ip, username, password, secret, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='cisco_ios', username=username, password=password, secret=secret)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.18en.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def enable_10_50_2_19_cisco(switch_ip, username, password, secret, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='cisco_ios', username=username, password=password, secret=secret)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.19en.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def enable_10_50_2_20_cisco(switch_ip, username, password, secret, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='cisco_ios', username=username, password=password, secret=secret)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.20en.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def enable_10_50_2_22_cisco(switch_ip, username, password, secret, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='cisco_ios', username=username, password=password, secret=secret)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.22en.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def enable_10_50_2_24_cisco(switch_ip, username, password, secret, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='cisco_ios', username=username, password=password, secret=secret)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.24en.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def enable_10_50_2_25_cisco(switch_ip, username, password, secret, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='cisco_ios', username=username, password=password, secret=secret)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.25en.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def enable_10_50_2_26_cisco(switch_ip, username, password, secret, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='cisco_ios', username=username, password=password, secret=secret)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.26en.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def enable_10_50_2_27_cisco(switch_ip, username, password, secret, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='cisco_ios', username=username, password=password, secret=secret)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.27en.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def enable_10_50_2_29_cisco(switch_ip, username, password, secret, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='cisco_ios', username=username, password=password, secret=secret)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.29en.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def enable_10_50_2_30_cisco(switch_ip, username, password, secret, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='cisco_ios', username=username, password=password, secret=secret)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.30en.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def enable_10_50_2_32_cisco(switch_ip, username, password, secret, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='cisco_ios', username=username, password=password, secret=secret)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.32en.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def enable_10_50_2_33_cisco(switch_ip, username, password, secret, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='cisco_ios', username=username, password=password, secret=secret)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.33en.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def enable_10_50_2_35_cisco(switch_ip, username, password, secret, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='cisco_ios', username=username, password=password, secret=secret)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.35en.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def enable_10_50_2_70_cisco(switch_ip, username, password, secret, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='cisco_ios', username=username, password=password, secret=secret)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.70en.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def enable_10_50_2_71_cisco(switch_ip, username, password, secret, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='cisco_ios', username=username, password=password, secret=secret)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.71en.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)
# End Enable Cisco

# Start Disable H3C
def disable_10_50_2_60_H3C(switch_ip, username, password, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='hp_comware', username=username, password=password)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.60dis.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def disable_10_50_2_153_H3C(switch_ip, username, password, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='hp_comware', username=username, password=password)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.153dis.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def disable_10_50_2_106_H3C(switch_ip, username, password, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='hp_comware', username=username, password=password)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.106dis.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def disable_10_50_2_51_H3C(switch_ip, username, password, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='hp_comware', username=username, password=password)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.51dis.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def disable_10_50_2_52_H3C(switch_ip, username, password, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='hp_comware', username=username, password=password)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.52dis.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def disable_10_50_2_181_H3C(switch_ip, username, password, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='hp_comware', username=username, password=password)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.181dis.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)
# End Disable H3C

# Start Enable H3C
def enable_10_50_2_60_H3C(switch_ip, username, password, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='hp_comware', username=username, password=password)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.60en.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def enable_10_50_2_153_H3C(switch_ip, username, password, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='hp_comware', username=username, password=password)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.153en.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def enable_10_50_2_106_H3C(switch_ip, username, password, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='hp_comware', username=username, password=password)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.106en.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def enable_10_50_2_51_H3C(switch_ip, username, password, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='hp_comware', username=username, password=password)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.51en.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def enable_10_50_2_52_H3C(switch_ip, username, password, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='hp_comware', username=username, password=password)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.52en.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)

def enable_10_50_2_181_H3C(switch_ip, username, password, pbar):
    try:
        net_connect = ConnectHandler(ip=switch_ip, device_type='hp_comware', username=username, password=password)
        net_connect.enable()
        output = net_connect.send_config_from_file('City17/10.50.2.181en.txt')
        net_connect.disconnect()
    except:
        print(f"{Fore.RED}Не удалось подключиться к указанному IP адресу: {switch_ip}{Style.RESET_ALL}")
        pbar.update(1)
        return

    pbar.update(1)
# End Enable H3C

# Start connect to cisco disable
def KLG_cisco_disable():
        username = input(f"{Fore.YELLOW}Enter Username: {Style.RESET_ALL}")
        password = "your password"
        secret = "your secret"
        with open("ip_list_KLG_cisco.txt", "r") as f:
            ip_list = f.read().splitlines()

        pbar = tqdm(total=len(ip_list), desc="🔗 Подключение к коммутаторам")

        threads = []
        for switch_ip in ip_list:
            if switch_ip == '10.50.2.13':
                t = Thread(target=disable_10_50_2_13_cisco, args=(switch_ip, username, password, secret, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.15':
                t = Thread(target=disable_10_50_2_15_cisco, args=(switch_ip, username, password, secret, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.16':
                t = Thread(target=disable_10_50_2_16_cisco, args=(switch_ip, username, password, secret, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.17':
                t = Thread(target=disable_10_50_2_17_cisco, args=(switch_ip, username, password, secret, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.18':
                t = Thread(target=disable_10_50_2_18_cisco, args=(switch_ip, username, password, secret, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.19':
                t = Thread(target=disable_10_50_2_19_cisco, args=(switch_ip, username, password, secret, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.20':
                t = Thread(target=disable_10_50_2_20_cisco, args=(switch_ip, username, password, secret, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.22':
                t = Thread(target=disable_10_50_2_22_cisco, args=(switch_ip, username, password, secret, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.24':
                t = Thread(target=disable_10_50_2_24_cisco, args=(switch_ip, username, password, secret, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.25':
                t = Thread(target=disable_10_50_2_25_cisco, args=(switch_ip, username, password, secret, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.26':
                t = Thread(target=disable_10_50_2_26_cisco, args=(switch_ip, username, password, secret, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.27':
                t = Thread(target=disable_10_50_2_27_cisco, args=(switch_ip, username, password, secret, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.29':
                t = Thread(target=disable_10_50_2_29_cisco, args=(switch_ip, username, password, secret, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.30':
                t = Thread(target=disable_10_50_2_30_cisco, args=(switch_ip, username, password, secret, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.32':
                t = Thread(target=disable_10_50_2_32_cisco, args=(switch_ip, username, password, secret, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.33':
                t = Thread(target=disable_10_50_2_33_cisco, args=(switch_ip, username, password, secret, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.35':
                t = Thread(target=disable_10_50_2_35_cisco, args=(switch_ip, username, password, secret, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.70':
                t = Thread(target=disable_10_50_2_70_cisco, args=(switch_ip, username, password, secret, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.71':
                t = Thread(target=disable_10_50_2_71_cisco, args=(switch_ip, username, password, secret, pbar))
                threads.append(t)
                t.start()

        for t in threads:
            t.join()
        pbar.close()
# End connect to cisco disable

# Start connect to cisco enable
def KLG_cisco_enable():
        username = input(f"{Fore.YELLOW}Enter Username: {Style.RESET_ALL}")
        password = "your password"
        secret = "your secret"
        with open("ip_list_KLG_cisco.txt", "r") as f:
            ip_list = f.read().splitlines()

        pbar = tqdm(total=len(ip_list), desc="🔗 Подключение к коммутаторам")

        threads = []
        for switch_ip in ip_list:
            if switch_ip == '10.50.2.13':
                t = Thread(target=enable_10_50_2_13_cisco, args=(switch_ip, username, password, secret, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.15':
                t = Thread(target=enable_10_50_2_15_cisco, args=(switch_ip, username, password, secret, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.16':
                t = Thread(target=enable_10_50_2_16_cisco, args=(switch_ip, username, password, secret, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.17':
                t = Thread(target=enable_10_50_2_17_cisco, args=(switch_ip, username, password, secret, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.18':
                t = Thread(target=enable_10_50_2_18_cisco, args=(switch_ip, username, password, secret, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.19':
                t = Thread(target=enable_10_50_2_19_cisco, args=(switch_ip, username, password, secret, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.2':
                t = Thread(target=enable_10_50_2_2_cisco, args=(switch_ip, username, password, secret, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.20':
                t = Thread(target=enable_10_50_2_20_cisco, args=(switch_ip, username, password, secret, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.22':
                t = Thread(target=enable_10_50_2_22_cisco, args=(switch_ip, username, password, secret, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.24':
                t = Thread(target=enable_10_50_2_24_cisco, args=(switch_ip, username, password, secret, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.25':
                t = Thread(target=enable_10_50_2_25_cisco, args=(switch_ip, username, password, secret, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.26':
                t = Thread(target=enable_10_50_2_26_cisco, args=(switch_ip, username, password, secret, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.27':
                t = Thread(target=enable_10_50_2_27_cisco, args=(switch_ip, username, password, secret, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.29':
                t = Thread(target=enable_10_50_2_29_cisco, args=(switch_ip, username, password, secret, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.30':
                t = Thread(target=enable_10_50_2_30_cisco, args=(switch_ip, username, password, secret, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.32':
                t = Thread(target=enable_10_50_2_32_cisco, args=(switch_ip, username, password, secret, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.33':
                t = Thread(target=enable_10_50_2_33_cisco, args=(switch_ip, username, password, secret, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.35':
                t = Thread(target=enable_10_50_2_35_cisco, args=(switch_ip, username, password, secret, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.70':
                t = Thread(target=enable_10_50_2_70_cisco, args=(switch_ip, username, password, secret, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.71':
                t = Thread(target=enable_10_50_2_71_cisco, args=(switch_ip, username, password, secret, pbar))
                threads.append(t)
                t.start()

        for t in threads:
            t.join()
        pbar.close()
# End connect to cisco enable

# Start connect to H3C disable
def KLG_H3C_disable():
        username = input(f"{Fore.YELLOW}Enter Username: {Style.RESET_ALL}")
        password = "your password"
        with open("ip_list_KLG_H3C.txt", "r") as f:
            ip_list = f.read().splitlines()

        pbar = tqdm(total=len(ip_list), desc="🔗 Подключение к коммутаторам")

        threads = []
        for switch_ip in ip_list:
            if switch_ip == '10.50.2.60':
                t = Thread(target=disable_10_50_2_60_H3C, args=(switch_ip, username, password, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.153':
                t = Thread(target=disable_10_50_2_153_H3C, args=(switch_ip, username, password, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.106':
                t = Thread(target=disable_10_50_2_106_H3C, args=(switch_ip, username, password, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.51':
                t = Thread(target=disable_10_50_2_51_H3C, args=(switch_ip, username, password, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.52':
                t = Thread(target=disable_10_50_2_52_H3C, args=(switch_ip, username, password, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.181':
                t = Thread(target=disable_10_50_2_181_H3C, args=(switch_ip, username, password, pbar))
                threads.append(t)
                t.start()

        for t in threads:
            t.join()
        pbar.close()
# End connect to H3C disable

# Start connect to H3C enable
def KLG_H3C_enable():
        username = input(f"{Fore.YELLOW}Enter Username: {Style.RESET_ALL}")
        password = "your secret"
        with open("ip_list_KLG_H3C.txt", "r") as f:
            ip_list = f.read().splitlines()

        pbar = tqdm(total=len(ip_list), desc="🔗 Подключение к коммутаторам")

        threads = []
        for switch_ip in ip_list:
            if switch_ip == '10.50.2.60':
                t = Thread(target=enable_10_50_2_60_H3C, args=(switch_ip, username, password, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.153':
                t = Thread(target=enable_10_50_2_153_H3C, args=(switch_ip, username, password, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.106':
                t = Thread(target=enable_10_50_2_106_H3C, args=(switch_ip, username, password, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.51':
                t = Thread(target=enable_10_50_2_51_H3C, args=(switch_ip, username, password, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.52':
                t = Thread(target=enable_10_50_2_52_H3C, args=(switch_ip, username, password, pbar))
                threads.append(t)
                t.start()
            if switch_ip == '10.50.2.181':
                t = Thread(target=enable_10_50_2_181_H3C, args=(switch_ip, username, password, pbar))
                threads.append(t)
                t.start()

        for t in threads:
            t.join()
        pbar.close()
# End connect to H3C enable

#Menu
def main():
    print(f"{Fore.CYAN}Быстрое Выключение | Включение 802.1X на коммутаторах{Style.RESET_ALL}")
    
    main_menu = f'Выберете действие:\n' \
                f'\t{Style.RESET_ALL}1. Выключить 802.1X {Style.BRIGHT + Fore.YELLOW}в City17 (Cisco)\n' \
                f'\t{Style.RESET_ALL}2. Выключить 802.1X {Style.BRIGHT + Fore.YELLOW}в City17 (H3C)\n' \
                f'\t{Style.RESET_ALL}11. Включить 802.1X {Style.BRIGHT + Fore.YELLOW}в City17 (Cisco)\n' \
                f'\t{Style.RESET_ALL}12. Включить 802.1X {Style.BRIGHT + Fore.YELLOW}в City17 (H3C)\n'
    while True:
        print(Style.RESET_ALL + main_menu)
        choice = input(f'{Style.RESET_ALL}Ваш выбор: ')

        if choice == '1':
            print(Fore.YELLOW + Style.BRIGHT + '\nВыключить 802.1X в City17 (Cisco)')
            KLG_cisco_disable()

        if choice == '2':
            print(Fore.YELLOW + Style.BRIGHT + '\nВыключить 802.1X в City17 (H3C)')
            KLG_H3C_disable()

        if choice == '11':
            print(Fore.YELLOW + Style.BRIGHT + '\nВключить 802.1X в City17 (Cisco)')
            KLG_cisco_enable()

        if choice == '12':
            print(Fore.YELLOW + Style.BRIGHT + '\nВключить 802.1X в City17 (H3C)')
            KLG_H3C_enable()

        else:
            pass
        input(f'{Style.RESET_ALL}Для продолжения нажмите {Style.BRIGHT + Fore.YELLOW}ENTER ')
        
if __name__ == "__main__":
    main()

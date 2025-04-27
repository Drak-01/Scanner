import socket
import sys
import getopt
import time



# Variables globales
target_host = ""
target_port = 0
list_ports = []
enble_service = False
detect_OS_val = False

def usage():
    print("Manuel.")
    print("")
    
    print("Usage: python scan.py -t target_host -p 80")
    print("  Scan le port 80 (HTTP) sur l'hôte cible.")
    print("")
    
    print("Usage: python scan.py -t target_host -p 4000")
    print("  Scanner les 4000 premiers ports ouverts sur l'hôte cible.")
    print("")
    
    print("Usage: python scan.py -t target_host -p 100-200")
    print("  Scanner les ports de 100 à 200 sur l'hôte cible.")
    print("")
    
    print("Usage: python scan.py -t target_host -p 1-65535")
    print("  Scanner tous les ports de 1 à 65535 sur l'hôte cible.")
    print("")
    
    print("Usage: python scan.py -t target_host1 target_host2")
    print("  Scanner plusieurs hôtes cibles.")
    print("")
    
    print("Usage: python scan.py -h")
    print("  Afficher cette aide.")
    print("")
    
    sys.exit(0)

def scan_port(target, port):
    global list_ports
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))
        if result == 0:
            serv_res = ''
            if enble_service:  # Use the correct variable name
                serv_res = service(sock, port)
            print(f"Port {port} is open with service: {serv_res}")

        sock.close()
        time.sleep(0.1)
    except socket.error as e:
        pass

def scan_ports(target):
    global list_ports
    if len(list_ports) == 1 :
        scan_port(target, list_ports[0])
    else:
        for port in list_ports:
            scan_port(target,port)

def liste_ports(port_range):
    global list_ports
    if len(port_range) == 1:
        list_ports.append(int(port_range[0]))
    else:
        for i in range(int(port_range[0]),int(port_range[1]),1):
            list_ports.append(i)

def service(sock, port): 
    try:
        res = socket.getservbyport(port)
        return res
    except:
        return "Unknown Service"

def detecte_System(): #gethostname(),
    try:
        pass
    except:
        pass

"""
def detect_os(target): #getfqdn()
    try:
        print("*"*50)
        print("Detection of os")
        print("*"*50)
        nm = nmap.PortScanner()
        nm.scan(target,arguments='-O')
        
        if target in nm.all_hosts():
            print(f"Result of detect OS:")

            if 'osmatch' in nm[target]:
                os_info = nm[target]['osmatch']
                print(f"OS detect :: {os_info[0]['name']} (probable : {os_info[0]['accuracy']}%)")
            else:
                print(f"Impossible to detect OS")
    except:
        pass

"""

def detect_inter_Reseau(): # if_nameindex()
    pass

def main():
    global target_host, target_port,enble_service,detect_OS_val
    
    if not len(sys.argv[1:]):
        usage()

    try:
        options, actions = getopt.getopt(sys.argv[1:], "ht:p:s:o", ["help", "target", "port", "service", "OS"])
    except getopt.GetoptError as err:
        print(f"Erreur : {err}")
        usage()

    for option, action in options:
        if option in ("-h", "--help"):
            usage()
        elif option in ("-t", "--target"):
            target_host = action
        elif option in ("-p", "--port"):
            target_port = action.split("-",1)
        elif option in ("-s", "--service"):
            enble_service = True
        elif option in ("-o", "--OS"):
            detect_OS_val = True
        else:
            usage()

    if not target_host:
        print("Erreur : Vous devez spécifier une cible avec l'option -t.")
        sys.exit(1)

    if not target_port:
        print("Erreur : Vous devez spécifier un port ou une plage de ports avec l'option -p.")
        sys.exit(1)

    # Convertir target_port en une liste de ports
    liste_ports(target_port)

    print(f"[*] Scanning Target : {target_host} !!!")
    print("="*50,"SCANNER","="*50, end='\n')

    # Lancer le scan des ports
    scan_ports(target_host)

    

if __name__ == "__main__":
    main()
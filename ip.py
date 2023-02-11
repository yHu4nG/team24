import ifaddr

adapters = ifaddr.get_adapters(include_unconfigured=True)

for adapter in adapters:
        print("IPs of network adapter " + adapter.nice_name)
        for ip in adapter.ips:
            if ip.is_IPv4:
                addr = ip.ip.split(".")
                addr[len(addr) - 1] = "51"
                addr1 = ".".join(addr)
                print("IPv4: " + addr1)
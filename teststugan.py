import psutil
#https://psutil.readthedocs.io/en/latest/

def get_memory_usage():
    print("--- Startar undersökning av get_memory_usage ---")
    
    memory_info = psutil.virtual_memory()
    print(f"1. Rådata från psutil: {memory_info}")
    
    total_bytes = memory_info.total
    print(f"2. Värdet för 'total' i bytes: {total_bytes}")
    
    total_gb_unrounded = total_bytes / (1024**3)
    print(f"3. Resultat efter division (före avrundning): {total_gb_unrounded}")

    total_gb = round(total_gb_unrounded, 2)
    print(f"4. Slutgiltigt värde för total_gb (efter avrundning): {total_gb}")
    
    used_gb = round(memory_info.used / (1024**3), 2)
    percent_used = memory_info.percent
    
    print("--- Undersökning klar ---")
    return percent_used, used_gb, total_gb

get_memory_usage()

#Siffrorna är i bytes och för att få det till gigabyte då måste jag dividera med 1024^3.
#Beräkning: 6973997056 / (1024 * 1024 * 1024) = 6,4950408,,,
#Använd avrundning "round(summan, 2)" 2 alltså till 2 decimaler och då får vi = 6,50 GB

def get_memory_usage():
    print("--- Startar undersökning av get_memory_usage ---")
    
    memory_info = psutil.virtual_memory()
    print(f"1. Rådata från psutil: {memory_info}")
    
    total_bytes = memory_info.total
    print(f"2. Värdet för 'total' i bytes: {total_bytes}")
    
    total_gb_unrounded = total_bytes / (1024**3)
    print(f"3. Resultat efter division (före avrundning): {total_gb_unrounded}")

    total_gb = round(total_gb_unrounded, 2)
    print(f"4. Slutgiltigt värde för total_gb (efter avrundning): {total_gb}")
    
    used_gb = round(memory_info.used / (1024**3), 2)
    percent_used = memory_info.percent
    
    print("--- Undersökning klar ---")
    return percent_used, used_gb, total_gb

get_memory_usage()
# main.py - TESTVERSION

from system_info import get_cpu_usage, get_memory_usage, get_disk_usage
from alarm import Alarm

def view_alarms(alarms_list):

    print("\n\n=============== STARTAR UNDERSÖKNING av view_alarms ===============")
    
    # Jag kollar vad funktionen fick för "ingrediens". Jag vill se exakt hur listan ser ut när den kommer in.
    print(f"1. Funktionen tog emot listan. Den innehåller just nu: {alarms_list}")
    
    # Här kollar jag om listan är tom. "not alarms_list" blir "True" om listan är tom.
    print(f"\n2. Kollar om listan är tom. Resultatet av 'not alarms_list' är: {not alarms_list}")
    if not alarms_list:
        # Om listan var tom, körs denna kod.
        print("   -> Listan är tom, skriver ut meddelande och hoppar till slutet.")
        print("No alarms have been configured yet.")
    else:
        # Om listan INTE var tom, körs istället denna kod.
        print("   -> Listan är inte tom, fortsätter till sortering.")
        
        # Innan jag sorterar, skapar jag en tillfällig, mer lättläst version av listan bara för att kunna skriva ut den snyggt.
        # [f"{a.alarm_type}-{a.threshold}%" for a in alarms_list] är en snabb loop som skapar en ny lista med textsträngar.
        readable_list_before = [f"{a.alarm_type}-{a.threshold}%" for a in alarms_list]
        print(f"\n3. Lista FÖRE sortering: {readable_list_before}")
        
        # Här sker själva sorteringen. sorted() skapar en NY lista som är sorterad.
        # 'key=lambda alarm: alarm.alarm_type' är instruktionen: "Sortera baserat på varje objekts alarm_type-egenskap".
        sorted_alarms = sorted(alarms_list, key=lambda alarm: alarm.alarm_type)
        
        # Jag skapar en till lättläst lista, nu från den sorterade versionen, för att bevisa att sorteringen fungerade.
        readable_list_after = [f"{a.alarm_type}-{a.threshold}%" for a in sorted_alarms]
        print(f"4. Lista EFTER sortering: {readable_list_after}")
        
        # Nu är det dags att loopa igenom den sorterade listan och skriva ut den snyggt, rad för rad.
        print("\n5. Startar for-loopen med enumerate för att skriva ut varje larm...")
        for index, alarm in enumerate(sorted_alarms, start=1):
            # "enumerate" ger mig ett räknenummer (index) och ett alarm-objekt (alarm) för varje varv.
            
            # Detta block upprepas för varje larm i listan.
            print(f"\n   --- Loop-varv {index} ---")
            print(f"   - Index från enumerate: {index}")
            print(f"   - Alarm-objekt för detta varv: {alarm}") # Visar den råa representationen av objektet
            print(f"   - Plockar ut alarm.alarm_type: {alarm.alarm_type}") # Plockar ut en egenskap från objektet
            print(f"   - Plockar ut alarm.threshold: {alarm.threshold}") # Plockar ut den andra egenskapen
            print(f"   -> Skriver ut den formaterade raden: '{index}. {alarm.alarm_type} alarm {alarm.threshold}%'")
            
    # Detta är bara en slutrubrik för att göra min utskrift tydlig.
    print("\n=============== UNDERSÖKNING av view_alarms KLAR ================")
    input("\nTryck Enter för att fortsätta test-sekvensen...")


def create_alarm_menu(alarms_list):
    
    print("\n\n============= STARTAR UNDERSÖKNING av create_alarm_menu =============")
    # Jag kollar hur listan ser ut precis när funktionen startar.
    print(f"1. Innehåll just nu: {alarms_list}")

    alarm_type = "CPU"
    print(f"2. Jag låtsas att användaren valde typ: '{alarm_type}'")
    
    # Här pausar jag och ber den som kör testet att mata in ett värde.
    threshold_input = input(f"TEST: Sätt larm-tröskel för {alarm_type} (1-100): ")
    # Jag sparar texten som användaren skrev i variabeln 'threshold_input'.
    print(f"3. Användaren matade in texten: '{threshold_input}'")
    
    # Nu börjar valideringen. Först, en kontroll: "Består texten bara av siffror?". .isdigit() ger True eller False.
    print(f"4. Kollar om '{threshold_input}' bara innehåller siffror. Resultat av .isdigit(): {threshold_input.isdigit()}")
    if threshold_input.isdigit():
        # Om .isdigit() var True, omvandlar jag texten (str) till ett heltal (int). "80" blir 80.
        threshold = int(threshold_input)
        print(f"5. Texten omvandlad till heltalet: {threshold}")
        
        # Nu kollar jag om talet är inom det giltiga intervallet 1-100.
        print(f"6. Kollar om {threshold} är mellan 1 och 100. Resultat: {1 <= threshold <= 100}")
        if 1 <= threshold <= 100:
            # Om alla kontroller passerades, är det dags att skapa mitt larm-objekt.
            print("\n7. Allt är korrekt! Nu skapar jag ett Alarm-objekt från min klass/ritning...")
            # Detta är raden där jag använder min 'Alarm'-klass för att skapa en instans/objekt.
            new_alarm = Alarm(alarm_type=alarm_type, threshold=threshold)
            print(f"   -> Objektet skapat i minnet: {new_alarm}") # Visar den råa representationen
            print(f"   -> Objektets typ: {new_alarm.alarm_type}") # Visar en av dess egenskaper
            print(f"   -> Objektets tröskel: {new_alarm.threshold}") # Visar den andra egenskapen
            
            # Nu lägger jag till det nyskapade objektet i listan jag fick från början.
            print(f"\n8. Lägger till objektet i listan med .append()...")
            alarms_list.append(new_alarm)
            # Jag skriver ut listan igen för att bevisa att objektet nu ligger där.
            print(f"9. Listans innehåll NU: {alarms_list}")
            
            print(f"\nSuccess: Alarm for {alarm_type} Usage set to {threshold}%.")
        else:
            # Detta körs om siffran var för hög eller för låg.
            print("   -> FEL: Siffran var utanför 1-100.")
    else:
        # Detta körs om .isdigit() var False.
        print("   -> FEL: Input var inte bara siffror.")

    # Slutrubrik
    print("============ UNDERSÖKNING av create_alarm_menu KLAR =============")


# STEG 1: Jag skapar en tom lista. Detta simulerar "alarms = []"" från "main_menu".
test_larm_lista = []
print(f"\nTom larm-lista skapad: {test_larm_lista}")

# STEG 2: Jag anropar view_alarms och skickar med den tomma listan.
# Jag vill testa att funktionen kan hantera en tom lista korrekt.
view_alarms(test_larm_lista)

# STEG 3: Jag anropar create_alarm_menu och skickar med listan.
# Funktionen kommer att lägga till ett larm i min `test_larm_lista`.
create_alarm_menu(test_larm_lista)

# STEG 4: Jag anropar create_alarm_menu IGEN, och skickar med SAMMA lista.
# Nu testar jag att lägga till ett andra larm. Listan är inte längre tom.
create_alarm_menu(test_larm_lista) 

# STEG 5: Jag anropar view_alarms igen.
# Nu skickar jag med listan som innehåller två larm, för att testa sorteringen och utskriftsloopen.
view_alarms(test_larm_lista)

# Slutmarkör
print("\n--- Testsekvens klar ---")
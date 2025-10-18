# ---------- ENGLISH ----------
# System Monitor (A Python Monitoring Application)

A simple console- and GUI-based application written in Python to monitor system resources (CPU, memory, disk) on a computer. The application allows the user to set up custom alarms and can send email notifications when these alarms are triggered.

## Features

* **Monitoring:** Displays current usage of CPU, RAM, and Hard Drive (root partition).
* **Alarm Management:**
    * Create percentage-based alarm thresholds for CPU, memory, and disk.
    * View a list of all active alarms, sorted by type.
    * Delete individual alarms.
    * Alarms are saved persistently in `alarms.json` between sessions.
* **Active Monitoring Mode:** A mode where the system is checked against active alarms every 5 seconds.
* **Email Notifications:** Sends an email via SendGrid when an alarm is triggered (only one email per trigger until the value normalizes).
* **Logging:** Creates a timestamped log file for each run, recording important events.
* **Graphical User Interface (GUI):** A simple Tkinter window displaying real-time system status updates (launched from the console menu).
* **Console Menu:** A text-based menu for interacting with all features.

## Installation and Setup

To run this application, you need Python 3 installed. Then follow these steps:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/DesignDeployer/system_monitor.git](https://github.com/DesignDeployer/system_monitor.git)
    cd system_monitor
    ```

2.  **Create and Activate Virtual Environment:**
    Using a virtual environment is strongly recommended.
    ```bash
    # Create the environment (run once)
    python -m venv venv

    # Activate the environment (run each time you open a new terminal)
    # On Windows with Git Bash:
    source venv/Scripts/activate
    # On Windows with cmd/PowerShell:
    # .\venv\Scripts\activate
    # On macOS/Linux:
    # source venv/bin/activate
    ```

3.  **Install Dependencies:**
    Install the required Python packages.
    ```bash
    pip install psutil sendgrid
    ```
    *(Tkinter is included in standard Python installations)*

4.  **Configure Email (SendGrid):**
    For email notifications to work, you need a free SendGrid account and an API key.
    * Create an account at [sendgrid.com](https://sendgrid.com).
    * Verify your "Single Sender Identity" (your email address).
    * Create an API key under **Settings -> API Keys**.
    * Create a file in the project root directory named `config.py`.
    * Add the following to `config.py`, replacing the placeholder values with your own:
        ```python
        # config.py
        SENDGRID_API_KEY = "YOUR_SENDGRID_API_KEY_HERE"
        FROM_EMAIL = "your-verified-sender@email.com"
        TO_EMAIL = "email-to-send-alerts-to@email.com"
        ```
    * **IMPORTANT:** Add `config.py` to your `.gitignore` file to avoid committing your secret API key to GitHub:
        ```gitignore
        # .gitignore (add to the bottom)
        config.py
        ```

## How to Run the Application

Once you have followed the installation steps and your virtual environment is **active**, start the application from your terminal:

```bash
python main.py



# ---------- SWEDISH ----------
# System Monitor (Övervakningsapplikation i Python)

En enkel konsol- och GUI-baserad applikation skriven i Python för att övervaka systemresurser (CPU, minne, disk) på en dator. Applikationen tillåter användaren att sätta upp anpassade larm och kan skicka e-postaviseringar när dessa larm utlöses.

## Funktioner

* **Övervakning:** Visar aktuell användning av CPU, RAM-minne och Hårddisk (rotpartitionen).
* **Larmhantering:**
    * Skapa procentuella larmgränser för CPU, minne och disk.
    * Visa en lista över alla aktiva larm, sorterade efter typ.
    * Ta bort enskilda larm.
    * Larm sparas permanent i `alarms.json` mellan körningar.
* **Aktivt Övervakningsläge:** Ett läge där systemet kontrolleras var 5:e sekund mot aktiva larm.
* **E-postaviseringar:** Skickar ett mejl via SendGrid när ett larm utlöses (endast ett mejl per utlösning tills värdet normaliserats).
* **Loggning:** Skapar en tidsstämplad loggfil för varje körning som registrerar viktiga händelser.
* **Grafiskt Gränssnitt (GUI):** Ett enkelt Tkinter-fönster som visar realtidsuppdateringar av systemstatus (startas från konsolmenyn).
* **Konsolmeny:** En textbaserad meny för att interagera med alla funktioner.

## Installation och Setup

För att köra denna applikation behöver du Python 3 installerat. Följ sedan dessa steg:

1.  **Klona Repositoriet:**
    ```bash
    git clone [https://github.com/DesignDeployer/system_monitor.git](https://github.com/DesignDeployer/system_monitor.git)
    cd system_monitor
    ```

2.  **Skapa och Aktivera Virtuell Miljö:**
    Det är starkt rekommenderat att använda en virtuell miljö.
    ```bash
    # Skapa miljön (körs en gång)
    python -m venv venv

    # Aktivera miljön (körs varje gång du öppnar en ny terminal)
    # På Windows med Git Bash:
    source venv/Scripts/activate
    # På Windows med cmd/PowerShell:
    # .\venv\Scripts\activate
    ```

3.  **Installera Beroenden:**
    Installera de Python-paket som krävs.
    ```bash
    pip install psutil sendgrid
    ```
    *(Tkinter är inbyggt i standard Python-installationer)*

4.  **Konfigurera E-post (SendGrid):**
    För att e-postaviseringar ska fungera behöver du ett gratis SendGrid-konto och en API-nyckel.
    * Skapa ett konto på [sendgrid.com](https://sendgrid.com).
    * Verifiera din "Single Sender Identity" (din e-postadress).
    * Skapa en API-nyckel under **Settings -> API Keys**.
    * Skapa en fil i projektmappen som heter `config.py`.
    * Lägg till följande i `config.py` och ersätt med dina egna värden:
        ```python
        # config.py
        SENDGRID_API_KEY = "DIN_SENDGRID_API_NYCKEL_HÄR"
        FROM_EMAIL = "din-verifierade-avsändar@email.com"
        TO_EMAIL = "email-att-skicka-larm-till@email.com"
        ```
    * **VIKTIGT:** Lägg till `config.py` i din `.gitignore`-fil för att undvika att ladda upp din hemliga API-nyckel till GitHub:
        ```gitignore
        # .gitignore (lägg till längst ner)
        config.py
        ```

## Hur man Kör Applikationen

När du har följt installationsstegen och din virtuella miljö är **aktiv**, starta programmet från terminalen:

```bash
python main.py
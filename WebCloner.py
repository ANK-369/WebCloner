import os
import subprocess
import sys

class Colors:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def print_banner():
    banner = r"""
  __      __      ___.  _________.__                    
 /  \    /  \ ____\_ |__ \_  ___/|  |    ____   ____   ___________ 
 \   \/\/   // __ \| __ \/    \   |  |  /  _ \ /    \_/ __ \_ __ \
  \        /\  ___/| \_\ \     \__|  |_(  <_> )   |  \  ___/|  | \/
   \__/\  /  \___  >___  /\______  /____/\____/|___|  /\___  >__|   
        \/       \/    \/       \/                 \/     \/       
"""
    print(f"{Colors.CYAN}{banner}{Colors.ENDC}")
    print(f"{Colors.GREEN}{Colors.BOLD}     ANdualem Koriya [ANK369]{Colors.ENDC}")
    print(f"{Colors.GREEN}     https://github.com/ANK-369/WebCloner.git{Colors.ENDC}")
    print(f"{Colors.CYAN}===================================================================={Colors.ENDC}")

def clone_website(user_input):
    clean_url = user_input.replace('https://', '').replace('http://', '').replace('www.', '').rstrip('/')
    website_dir = clean_url.split('/')[0]
    url = f"https://{clean_url}"

    # 1. መጀመሪያ ፎልደሩን እንፍጠር
    if not os.path.exists(website_dir):
        os.makedirs(website_dir)
    
    # 2. ወደዛ ፎልደር እንግባ
    os.chdir(website_dir)

    print(f"{Colors.GREEN}[+] በመቅዳት ላይ: {url}{Colors.ENDC}")
        
    # 3. የwget ትዕዛዝ (prefix አያስፈልገውም፣ ምክንያቱም ቀድመን ወደ ፎልደሩ ገብተናል)
    command = [
        "wget", "--recursive", "--no-clobber", "--page-requisites",
        "--html-extension", "--convert-links", "--no-parent",
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "--tries=2", "--timeout=10", url
    ]
    
    subprocess.run(command, capture_output=True, text=True)
    
    # 4. አሁን wget ፋይሎችን የፈጠረበትን (Domain name) ፎልደር እናገኛለን
    # ስለዚህ አንድ ደረጃ ወደ ውስጥ እንገባለን
    if os.path.exists(website_dir):
        os.chdir(website_dir)
        
    print(f"{Colors.GREEN}[+] ሰርቨሩ በ http://localhost:8000 ተጀምሯል{Colors.ENDC}")
    try:
        subprocess.run(["php", "-S", "localhost:8000"])
    except KeyboardInterrupt:
        print(f"\n{Colors.WARNING}[!] ሰርቨሩ ቆሟል።{Colors.ENDC}")

if __name__ == "__main__":
    try:
        print_banner()
        url = input(f"{Colors.GREEN}{Colors.BOLD}የድረ-ገጽ ሊንክ ያስገቡ: {Colors.ENDC}").strip()
        if url:
            clone_website(url)
    except KeyboardInterrupt:
        print(f"\n\n{Colors.WARNING}[!] ፕሮግራሙ በተጠቃሚው ተቋርጧል።{Colors.ENDC}")
        sys.exit(0)
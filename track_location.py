import phonenumbers
from test import number

from phonenumbers import geocoder

pepnumbers= phonenumbers.phrase(number)
location= geocoder.description_for_number(pepnumbers,'en')
print(location)

from phonenumbers import carrier

service_num= phonenumbers.phrase(number)
service_pro= carrier.name_for_number(service_num, 'en')
print(service_pro)

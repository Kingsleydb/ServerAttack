import os

word = 'suh'
while True:
    word += 'h'
    os.system('curl --data "username=' + word + '&lat=5&lng=9" https://secret-ocean-43823.herokuapp.com/submit')


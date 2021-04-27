
# How to get live internet speed in windows using python language.
![getInterbetSpeedLiveOutput](https://user-images.githubusercontent.com/50065404/116193775-7f993700-a74d-11eb-9095-4acb2deef350.PNG)


## This is very simple and no any special coding skills required.

## Before understanding this concept , we need to learn how to it work internally.
      
      In windows having a network packets.
             network packets :  In networking, a packet is a small segment of a larger message. Data sent over computer networks*, such as the Internet, is divided into     packets. These packets are then recombined by the computer or device that receives them.

            Suppose Alice is writing a letter to Bob, but Bob's mail slot is only wide enough to accept envelopes the size of a small index card. Instead of writing her letter on normal paper and then trying to stuff it through the mail slot, Alice divides her letter into much shorter sections, each a few words long, and writes these sections out on index cards. She delivers the group of cards to Bob, who puts them in order to read the whole message.

            This is similar to how packets work on the Internet. Suppose a user needs to load an image. The image file does not go from a web server to the user's computer in one piece. Instead, it is broken down into packets of data, sent over the wires, cables, and radio waves of the Internet, and then reassembled by the user's computer into the original photo.

## netstat command used in code.
  
   So guys, here I used " netstat -e " command inside run method. If you dry run in your terminal yout get output like this :
   
   ![netstat-e](https://user-images.githubusercontent.com/50065404/116194589-a7d56580-a74e-11eb-9d44-5f1bd819fe67.PNG)
  
   In this above image your see bytes (recived or sent ) :
            so this is the current data of our network speed (speed is nothing but , it is data recived or sent in persecond).

## now we understand our code.

  so as we seen output from above command , data recived or sent in bytes, so we have need convert bytes to kilo bytes. By dividing by 1024(This is standard value of 1kb ). 
  Inside the code, I minus previus value to new value , because windows adding old bytes to new bytes like this (1+3+5 = 9), to calculate total data recived or sent overthe network. But we wants to find speed so, that's why we are dividing previous value to fresh recived value.
  
### Run is method which is imported from subprocess module. 
  Actully, Run is method which read output from terminal as string. 
    
##### Author : Pawan kushwah
##### Profession : software engineer
##### Language : Python, javascript(side language)
##### framework : Django, Django Rest framework, electron,express.
##### version control : Gitlab, Github.
##### contact info >  pawankushwah850@gmail.com

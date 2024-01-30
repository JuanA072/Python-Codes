import pandas as pd
import numpy as np
import matplotlib.pyplot as plt #library import
import re #import the re data












                rvs = ['''I’ve seen a lot of bad reviews for this phone based on issues with the seller. Granted, some of those reviews say it took a few weeks for the problems to appear so I’ll edit this if that happens, but wow was I happy with what I got. Not only did it come with a charger (there’s some debate on that in other reviews), but it even had a clear bumper case. That was neither expected nor necessary but I appreciated it (I bought a Unicorn Beetle case which I have used and loved before on other phones). There wasn’t a scratch on this phone and it started working right away for me. The battery seems to be holding up fine. All in all I’d say this seems like a steal. If it self destructs on me in the next few weeks I’ll update this. UPDATE: It's been a few months and a trip overseas since I wrote that initial review, and it remains a solid decision I'm very happy with.''', '''This phone looks and performs great like it's brand new. Not one scratch. The phone came with a screen protector and a charger. I was surprised as other reviews said they did not get one. For $269, I feel like this was a steal, compared to other listings. Hopefully nothing goes wrong with the phone later. But with the Amazon 90 day guarantee I'm a little more at ease about possible return. Never bought a refurbished phone before. Not sure what to expect. As far as my order, I am happy with it.''',


'''Don't listen to bad reviews! My phone arrived in great condition. There are no scratches on the glass, and there is no visible wear and tear on the case. It works perfectly. I inserted my carrier-provided SIM card in the SIM tray and it was immediately available on AT&T's network. A SIM tray key was included in the box along with protective plastic covers for the screen. A charging cable and standard outlet plug were also included in the box. This version of the iPhone does not have a headphone jack. I did not receive a headphone insert in the box, but (#1) I don't need one as all of my headphones are Bluetooth and (#2) I don't know if Apple included this in the original packaging so this is just a courtesy note for potential buyers of the iPhone 7, not a complaint. The seller contacted me after I received my phone to make sure I was happy with the purchase and I am.''',
'''Love this phone! I am so glad I bought a refurbished one. I took it to the Apple store just in case to do a diagnostics on it and said that it was refurbished and bought through Amazon, and Apple checked it and said everything is great. Very happy with my purchase.''',
'''First, seller did a great job and I think I got a good price for an iPhone 7, I just think ALL CELL PHONES are way way way too expensive. When a Cell phone costs more than a good laptop computer that is too expensive. Second all Smart phones have bad battery life. Apple's iPhones are no exception. There is a mode on the iPhone 7 to allow for an extended battery life setting. But I see no difference between the extended setting and the normal setting. I do not use my phone except for emergencies so I would expect the phone to last 5-6 days between charging, but I am averaging 3-4 days between charging. I am having an issue that the WiFi doesn't see both of my wireless networks (dual band router). Seller tried to help but Apple's support said if it sees a network that's all they care about. Phone appears to be working fine and so far I am happy with it.''', '''Received prompt delivery of the phone. I inserted my 'sim card' and the phone was functional with no issues and I could make and receive calls right away, so far so good. I received the phone which is cosmetically in very good condition and I am quite happy with my purchase with exception of two minor issues which I believe someone could provide me guidance to resolve or trouble shoot.''',


'''Overall, the phone isn't too bad for the price. It came already scratched up, overheats more than a normal iPhone (I've had tons of iPhones). The delivery process of just getting the phone was pretty stressful, I'm a month and half in using the iPhone and I called customer service to see if they could replace my iphone because it got to the point where my hands feel the burning from the phone... the lady was so unhelpful, bland and kind of rude. The return proccess would be such a hassle and leave me phoneless so I decided to keep the phone instead. All the functions work fine, it's just that the iphone started heating up the moment I got it. I don't usually write reviews no matter how good or bad a product is, but I've never received such bad service from a company, especially amazon sellers. I'm basically stuck with the phone, or be phoneless. I would recommend the phone, but just know there will definitely some things you need to deal with. HAVE A NICE DAY TO WHOEVER IS READING :)''',
'''The iPhone 7 I purchased was "certified refurbished" and labeled as "new" quality but doesn't work. The phone looks great, but when I first turned it on it was in a restart loop. This was a bad sign to begin with, but I gave it the benefit of the doubt and connected it to my computer. When I finally got it to restore to factory settings, the screen started glitching to the point where there was nothing to stop it, and if it did get to the startup screen, it was non-responsive.''',
'''Initially I was happy with the phone. It looked great physically and had no signs of wear and tear. However, the battery health was lower than I wanted; the phone said the battery health was 88%. However, I knew from the ad, that it could ship with as low as 85%, so I can't complain too much about that. The biggest issue with the phone that was an absolute deal breaker was that it frequently crashed and closed apps on me. Other times it would freeze up. Imagine having an emergency and having to make a phone call, only to find out that your phone decided to freeze up?! I have a family, so that's completely unacceptable. The phone also seemed to have connectivity issues and would not connect well with my wifi. It was slower than my other devices on my wifi and would sometimes freeze up. With the problems that I was having, I'm thinking it was a bad main board or "motherboard". The seller was MobileSpree. I contacted them and asked for an exchange. They refused to do an exchange and said my only option was to return it. I returned it with the shipping label provided by Amazon. However, even after 5 days of having the phone back, they would not refund my money. I had to get Amazon involved to get a refund. Overall, don't buy. It was a waste of time and money and a hassle to get refunded.''',
'''Be cautious - if you have ANY issues at all, return phone immediately. We got one for my daughter, paid $244 and it didn’t last 4 months. Seller will not replace/return as it is past 90 days. She had intermittent issues with service connections shortly after receiving the phone. When it finally stopped connecting at all and we had it checked at the AT&T store, they told us it was an internal issue with the SIM card brackets that connects to the mother board. Basically causing a fatal error and cannot get any service connection. I contacted the seller and received the generic “past the 90 day warranty” so there is nothing they will do about it. We may try to have it repaired, but the repair shop is looking at $100 to inspect and possibly repair, if it can be repaired. I guess that’s our expensive mistake, but at least we can warn others.''']





         feel = ["Positive", "Positive", "Positive", "Positive", "Positive", "Positive", "Negative", "Negative", "Negative", "Negative"]


    stuff = pd.DataFrame({"text":train_reviews, "feel":train_sentiment})
class B:




    def __init__(self):
        self.fs = None
        self.ps = None
        self.ks = None




    def train(self, bow, ins, cs): #data is sent through and read / determines what fits
        self.ks = bow
        self.ps = {}
        df = self.get(bagOfWords, ins, classes)
        self.fs = df
        cl = len(cs)
        cs = set(cs)







                                    for c in cs:
            tmp = {}
            tmp_df = df[(df["Outcome"]==c)]
            cnt = len(tmp_df)



            for w in bow:
                cr = tmp_df[tmp_df[w]==1]
                tmp[w] = (len(cr)/cnt)
            tmp[c] = cnt/cl
            self.ps[c] = tmp





















    def get(self,bow, ins, cs):
        stuff = []
        for i in bow:
            stuff.append(i)
        stuff.append("Outcome")
        res = []
        for i in range(len(ins)):
            tmp=[]
            ins = ins[i].lower()
            c = cs[i]
            for w in bow:













                if re.search(w.lower(), ins) != None:
                    tmp.append(1)
                else:
                    tmp.append(0)
            tmp.append(c)
            res.append(tmp)
        df = pd.DataFrame(res, columns = stuff)
        return df














                            def fetch(self, ex):
        probs = []
        detected = []
        p = 1
        n = 1










        for i in self.keys:
            if re.search(i.lower(),ex.lower()):
                p *= self.probs["Positive"][i]
                n *= self.probs["Negative"][i]
        p *= self.probs["Positive"]["Positive"]
        n *= self.probs["Negative"]["Negative"]
        o = ''











        if n > p:
            o = ("Negative")
        elif n < p:
            o = ("Positive")
        else:
            o =("Equal outcome")
        df = pd.DataFrame([[p, n, o]], columns = ["Positive", "Negative", "Outcome"])
        return df








cs = ["Positive","Positive","Positive","Positive","Positive","Positive","Negative","Negative","Negative","Negative"]
boq = ['Happy', 'Great', 'Bad', 'Return']
use = B()
use.trainClassifier(boq, rvs, cs)

print(model.fetch("  THE PHONEphone arrivSed in pretty decent condition. The front screen was scratDSch-free and the display is great, but there is a long scratch on the bGack of the phone. This doesn't bother me much because I always have a case on my phone. However, the issue with this phone is that the cellular signal won't work; the device detects the sim but the signal is bad. Apparently this is an issue with some iPhone 7 models, but the any free of charge repair is not valid because the phone is coming from a third party seller. After speaking with Apple, Verizon (my mobile carrier), AND Amazon, I've reached the conclusion that the issue is with the phone. I've tried everything to troubleshoot, but I will unfortunately have to return the item and get another one."))
print(use.fetch("iPhone 7 Black came in excellent condition. Like new. No scratches or scuffs. Works gFreat. Was happy for couple months until phone sFtarted to develop issues with hearing callers and vs versa. Callers can’t hear me and I can’t hear callers, the sound is bad. Checked settings . Disabled WiFi calling. Hard reset phone. Updated iOS. Happens randomly. Suspect possible known defects on iPhone 7 with audio IC chips. I want to return the phone but I’m waiting to se for a month"))
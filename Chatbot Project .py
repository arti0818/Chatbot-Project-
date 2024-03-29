from nltk.chat.util import Chat, reflections

pairs = [
    
    [
        r"(.*)my name is (.*)",
        ["Hello %/2, How are you today ?",]
    ],
    [
        r"(.*)help(.*)",
        ["How can i help you",]
    ],
    [  
        r"(.*)your name ?",
        ["I am Alex, but you can call me Robot and i am a chatbot",]
    ],
    [  
        r"How are you (.*)",
        [" I am doing Great !",]
    ],
    [   
        r"sorry (.*)",
        ["It's OK,Never Mind", "It's alright",]
    ],
    [  
        r"i am (.*) (good/well/okay/ok)",
       ["Nice to hear that", "Alright, Great !",]
    ],
    [  
        r"(hi/hey/hello) (.*)",
       ["Hello", "Hey there"]
    ],
    [  
        r"what (.*) want ?",
       ["Make me an offer that i can't refuse",]
    ],
    [  
        r"(.*) created (.*)" ,
       [" Arti created using python libaray",]
    ],
    [  
       r"(.*) (Location/city) ?",
       ["Hyderabad , india",]
    ],
    [  
       r"(.*) raining in (.*) ",
       [" No rain in the last 5 days in %/2","In %2 there is a 50% chance of rain",]
    ],
    [  
       r"quit",
       ["Bye for now. See you soon :) ", "It was nice to talking to you. see you soon",]
    ],
    [
       r"(.*)" ,
       ["our cutomer service will reachout to you",]
    ], 
 ]

#default message at the start of chat

print('Hi am Alex and i like to chat \n please type lowercase English language to start the conversation. Type quit to exit')

chat = Chat(pairs, reflections)

chat.converse()





























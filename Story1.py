from Getter import *

def story1(debug= False):
	if debug: print "--In story1 function--"
	
	friend1 = getWord("A Name: ". debug)
    item1 = getWord("Enter a item: ", debug)
    description1 = getWord("Enter a description: ", debug)
	
	out = ""
	out += "One day me and my friend, " + friend1
    out += ", went for a walk. We found a " + item1
    out += ". " + friend1 + "said it was very " + description1
	out += "Wow it's sooo big, isn't it? " 
    
    
    
	return out 

#HTML generally allows optional attributes to be expressed as part of 
#an opening tag. The general form used is <name attribute1 = “value1” 
#attribute2 = “value2”>. Write function that checks whether tags or 
#matched properly, even when an opening tag may include one or 
#more attributes.

import stack_functions
def tagMatch(S,string):
	for str in string:
		if str=='<':
			S.stackPush(str)
		elif str=='>':
			if str=='>' and S.stackLength()==0:
				print("The tags are not properly matched in:"+string)
				exit()
			else:
				S.stackPop()
		else:
			continue
	if S.stackLength()==0:
		print("The tags are properly matched in: "+string)
	else:
		print("The tags are not properly matched in: "+string)
stack1=stack_functions.LimitedStack()
string1='</span><span class="pun">&gt;&gt;&gt;</span><span class="pln"> </span><span'
string2='<name1 color = "blue" size = “big”><name2 color = "green">'
tagMatch(stack1,string1)
# lambda response:"END" in response["content"]
#list
a = ["prabhu", "sara"]
b = [1,2]

if "prabhu" in a:
    print("yes")
else:
    print("no")

if 3 in b:
    print("yes")
else:
    print("no")

prabhu=["END","BYE"]

if "END" in prabhu:
    print("sara terminated agent")
else:
    print("no")

#prabhu: agent response
response = {
        "content":"END qwidfhweif qafhwi",
        "name" :"prabhu",
        "age" : 25
    }

lambda response:"END" in response["content"]
# response["name"]
# response["age"]
## lambda response:"END" in response["content"] wriet detaily
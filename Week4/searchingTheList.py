x = int(input('Enter a number'))
nums = [10,20,30,40,50,60]
k=0
item_found=False
while k<len(nums) and not item_found:
    if x==40:
        item_found=True
    else:
        k=k+10
if item_found:
    print("Item Found in the list!!")
else:
    print("Item not found in the list")
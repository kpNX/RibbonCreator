from PIL import Image
import os

ribbon_lst = os.listdir('./ribbon')

ribbon_total = int(input("How many ribbon do you want to assign : "))

rack = []

i = 0
print(ribbon_lst)
while i < ribbon_total :
	selected_ribbon = input("Which ribbon do you want to put on the rack : ")
	selected_medal = int(input("How many medals : "))
	rack.append(selected_ribbon)
	rack.append(selected_medal)
	i = i+1

print(rack)
ribbon_len = len(rack)//2
print(ribbon_len)

if ribbon_len <= 4 :
	row = 1
else :
	row = divmod(ribbon_len, 4)
	if row[1] > 0 :
		row = row[0] + 1

print(row)

if ribbon_len >= 4 :
	column = 4
else :
	column = ribbon_len

background = Image.new("RGBA", (105*column, 30*row), (255, 0, 0, 0))

i = 0
j = 0
y = 30 * (row-1)
x = 0

while i < ribbon_len :
	if i % 4 == 0 and column >= 4 and i != 0:
		x = 0
		y = y - 30
		j = 0
		#check how many left
		comparator = ribbon_len - i
		if comparator < 4 :
			if comparator == 1 :
				x = 157
			elif comparator == 2 :
				x = 105
				j = j + 1
			elif comparator == 3 :
				x = 35
				j = j + 1
	
	ribbon = Image.open('./ribbon'+"/"+str(rack[i*2])+'.png', 'r')
	medal = Image.open('./medal'+"/"+str(rack[i*2+1])+'_medal.png', 'r')
	overlay = Image.open('./overlay/RibbonOverlay.png', 'r')
	print(x,y)
	background.paste(ribbon, (x, y), ribbon)
	background.paste(overlay, (x, y), overlay)
	background.paste(medal, (x, y), medal)
	ribbon.close()
	medal.close()
	overlay.close()
	
	i = i + 1
	j = j + 1
	x = x + 105

background.save("ribbon_rack.png","PNG")
os.startfile("ribbon_rack.png")
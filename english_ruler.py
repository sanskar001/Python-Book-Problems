# This is  python program to understand the concept of  recursion.
# This is program to making kind of english ruler.

# This is function defination for drawing the tick lines.

def draw_line(tick_length,label = ' '):
    line = '-' * tick_length
    line = line + " " + label
    print(line)

# This is key function for drawing the sub ticks or drawing interval between the main points.

def draw_interval(center_tick_length):

    if center_tick_length>0:
        draw_interval(center_tick_length-1)
        draw_line(center_tick_length)
        draw_interval(center_tick_length-1)


# This is function for drawing the english ruler.

def draw_ruler(number_of_inches,max_tick_length):
    draw_line(max_tick_length,"0")
    for i in range(1,number_of_inches+1):
        draw_interval(max_tick_length-1)
        draw_line(max_tick_length,str(i))
    

number_of_inches = 3   # for number of incehes shown over the english ruler.
max_length = 4         # for taking the maximum length of tick.

draw_ruler(number_of_inches,max_length)
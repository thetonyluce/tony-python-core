'''
--------------------------------------------------------
                99 BOTTLES OF BEER LYRICS
--------------------------------------------------------

https://www.reddit.com/r/beginnerprojects/comments/19kxre/project_99_bottles_of_beer_on_the_wall_lyrics/

-- GOAL --
Create a program that prints out every line to the song
"99 bottles of beer on the wall." This should be a pretty simple program,
so to make it a bit harder, here are some rules to follow.

-- RULES --
1) If you are going to use a list for all of the numbers,
    do not manually type them all in. Instead, use a built in function.
2) Besides the phrase "take one down," you may not type in any
    numbers/names of numbers directly into your song lyrics.
3) Remember, when you reach 1 bottle left, the word "bottles" becomes singular.
4) Put a blank line between each verse of the song.

'''
for i in range(99, 1, -1):

    if i == 2:
        print(str(i) + " bottles of beer on the wall" + ", " + str(i) + " bottles of beeeeer!")
        print("You take one down, pass it around, " + str(i - 1) + " bottle of beer on the wall.")

    elif i == 1:
        print(str(i) + " bottle of beer on the wall" + ", " + str(i) + " bottle of beeeeer!")
        print("You take one down, pass it around, " + str(i - 1) + " bottle of beer on the wall.")

    else:
        print(str(i) + " bottles of beer on the wall" + ", " + str(i) + " bottles of beeeeer!")
        print("You take one down, pass it around, " + str(i - 1) + " bottles of beer on the wall.")

    print("And we're done.")

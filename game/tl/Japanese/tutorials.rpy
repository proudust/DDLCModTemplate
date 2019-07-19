translate Japanese end_tutorial_b8f07456:
    m "I hope I managed to teach you something!"

translate Japanese end_tutorial_5352a1bd:
    m 4b "I look foward to seeing your mods."

translate Japanese end_tutorial_47b6438a:
    m 5a "Until next time!"

translate Japanese tutorial_route_p1_6b3a908d:
    m "There’s no better way to become better at poetry than writing poems."

translate Japanese tutorial_route_p1_a5aeb019:
    m "And in the same way, there’s no better way to become better at modding than making mods."

translate Japanese tutorial_route_p1_a6277666:
    m 3a "So, let’s make a mod together! I have got the perfect idea."

translate Japanese tutorial_route_p1_64385e39:
    m 5a "Let’s make my own route!"

translate Japanese tutorial_route_p1_f888446d:
    m 5b "The one the game never gave us..."

translate Japanese tutorial_route_p1_2d98e1ed:
    m 1a "Of course, as both and I are new at programming, we should keep it simple."

translate Japanese tutorial_route_p1_aac8778b:
    m 1h "We’ll need Ren’Py but unfortunately I can’t access it from here."

translate Japanese tutorial_route_p1_76f64c10:
    m 3a "So I’m counting on you to help me."

translate Japanese tutorial_route_p1_358dbe08:
    m 4a "Make sure you follow exactly my instructions, okay? In coding, a single mistake can totally break a program."

translate Japanese tutorial_route_p1_488e9223:
    m "First, verify that you installed Ren’Py. Then make a copy of Doki Doki Literature Club’s directory and put it in the directory of Ren’Py."

translate Japanese tutorial_route_p1_d0425acf:
    m "Rename the directory of the game 'DDLC Monika Route'."

translate Japanese tutorial_route_p1_e7c03de9:
    m "Put the files of DDLC Mod Template inside DDLC Monika Route’s directory."

translate Japanese tutorial_route_p1_b8b4c687:
    m "Try to launch Ren’Py and then try to start DDLC Monika Route."

translate Japanese tutorial_route_p1_1f150758:
    m 4f "If there’s an error then you might have made a mistake with the files..."

translate Japanese tutorial_route_p1_37057cff:
    m 4o "Unfortunately, I can’t help you...If it works then we can go the next step."

translate Japanese tutorial_route_p1_c6439b1a:
    m 2a "Go to DDLC Monika Route’s game directory and delete 'tutorial.rpy' and 'tutorial.rpyc'. That file just contains this tutorial but we won’t need it to make my route."

translate Japanese tutorial_route_p1_bb7edf86:
    m 3a "Then you need to edit 'script.rpy'. You can edit it with any text editor. Open the file and navigate to lines 26-29."

translate Japanese tutorial_route_p1_a9aa42d3:
    m "Replace those lines with \n' \ \ \ call monika_route from _call_monika_route'"

translate Japanese tutorial_route_p1_b0f53166:
    m 3b "By the way, you should notice there are 4 spaces before that line."

translate Japanese tutorial_route_p1_aadb3030:
    m 4a "Be very careful about the number of spaces! In Ren’Py and Python spaces are very important. I won’t go into details now, but indenting lines with spaces is very important."

translate Japanese tutorial_route_p1_439de940:
    m "And it does have to be spaces. Tabs don't work the same way."

translate Japanese tutorial_route_p1_fa7daca3:
    m "Once the line is replaced, save the file. Create an empty text file. Rename it monika_route_script.rpy. Check if the extension is .rpy. Rpy file is the type of files used for Ren’Py scripts."

translate Japanese tutorial_route_p1_1ba56d17:
    m "Open monika_route_script.rpy and write \n'label monika_route:'."

translate Japanese tutorial_route_p1_5071bee0:
    m "Then jump a line and write \n' \ \ \ return'\n Save the file."

translate Japanese tutorial_route_p1_e1f05fb8:
    m 4i "Alright, we managed to finish the first part of our mod. Let me explain the meaning of what you just wrote."

translate Japanese tutorial_route_p1_a945a701:
    m 1a "In a book, each chapter are followed one after another. Chapter two is written after chapter two and so on. But in Ren’Py this is different."

translate Japanese tutorial_route_p1_9a8a8aae:
    m "The order isn’t determined by the place of each chapter in the scripts but by the keywords 'label', 'call' and 'jump'"

translate Japanese tutorial_route_p1_66164b7f:
    m "When the game begins and when you click on New Game, the game jumps to the chapter whose label is 'start'. Then the game reads and executes what is inside the block under the label 'start'."

translate Japanese tutorial_route_p1_7b8a4171:
    m "When it reaches the keyword 'call' or 'jump', the game proceeds to the chapter whose label followed the keyword."

translate Japanese tutorial_route_p1_661ec454:
    m 2b "In the case of our mod, when the game reads ' \ \ \ call monika_route from _call_ monika_route', it jumps to the chapter labeled monika_route."

translate Japanese tutorial_route_p1_eb36f55d:
    m 3a "Please don’t mind 'from _call_monika_route', it’s quite advanced stuff and I don’t understand it well too."

translate Japanese tutorial_route_p1_a31c9558:
    m 4b "The chapter monika_route is defined in the file we created, monika_route_script.rpy. But as you can see, there is nothing inside it except from 'return'."

translate Japanese tutorial_route_p1_7fc51ef2:
    m "The keyword 'return' makes the game goes back to the latest chapter that was accessed through 'call'. If it doesn't exist, the game goes back to the main menu."

translate Japanese tutorial_route_p1_6819a579:
    m 4a "If you try to play the mod, you’ll see nothing when you click New Game. That’s because the game returns to the main menu as soon as it jumps to monika_route."

translate Japanese tutorial_route_p1_0b0a81ca:
    m 1e "Okay! Let’s stop here for now. I hope I didn’t overwhelm you with information..."

translate Japanese tutorial_route_p1_7cfe416c:
    m 2a "If there’s still an error when you try playing the mod, there's a script named t1.rpy inside the folder named monika_route_answer. t1.rpy is what you should have written in monika_route_script.rpy."

translate Japanese tutorial_route_p1_6d249f76:
    m "You can copy-paste the content of t1.rpy to monika_route_script.rpy but don’t forget to delete the # character in front of each line."

translate Japanese tutorial_route_p1_b24e6148:
    m "In Python and Ren’Py, the # character tells your computer not to read and execute the line. A line with a # in front of it is nothing more than a comment that only you can read."

translate Japanese tutorial_route_p1_575f1662:
    m 5a "This is all for now! When you are ready, begin the second part! I'm waiting for you."

translate Japanese tutorial_route_p2_06e0e755:
    m "Hi again [player]!"

translate Japanese tutorial_route_p2_2e6dd45a:
    m 1a "If the last part was a bit too hard, don’t worry, this part is easier."

translate Japanese tutorial_route_p2_306c0894:
    m "Like last time, I’ll tell you what to do and then I’ll explain, okay?"

translate Japanese tutorial_route_p2_5640d095:
    m 4a "First open monika_route_script.rpy."

translate Japanese tutorial_route_p2_0e194c70:
    m "Between the first line and 'return', add the line \n' \ \ \ stop music fadeout 2.0'"

translate Japanese tutorial_route_p2_794db6f9:
    m "Then add the line ' play music t2'."

translate Japanese tutorial_route_p2_b20b2544:
    m "Finally, add the line \n' \ \ \ mc 'Let's listen to the music.''"

translate Japanese tutorial_route_p2_4c4df40a:
    m 2a "Check that all lines bellow 'label monika_route:' are aligned and that 'return' is the last line."

translate Japanese tutorial_route_p2_18ab6a2c:
    m "Try to launch the game with Ren’Py and see what happens..."

translate Japanese tutorial_route_p2_68208041:
    m 2c "..."

translate Japanese tutorial_route_p2_12f82ef7:
    m 1c "Does it work? If everything goes well, you should be listening to Sayori’s main theme."

translate Japanese tutorial_route_p2_6ea5bf54:
    m 3a "There’s just one dialogue, so if you click one time, you go to the main menu because of the 'return' keyword."

translate Japanese tutorial_route_p2_4c6414e9:
    m 3b "Okay, time to explain what happened!"

translate Japanese tutorial_route_p2_46c0c820:
    m 3a "Let’s look at ' \ \ \ stop music fadeout 2.0'. Before you click New Game, you can hear the music of the main menu, right? "

translate Japanese tutorial_route_p2_443097d4:
    m "But when you click New Game, the music stops progressively."

translate Japanese tutorial_route_p2_e5f5f764:
    m 4a "That’s due to 'stop music fadeout 2.0'. 'stop music' tells the current music to stop. 'fadeout 2.0' makes it so the current music completely becomes silent in 2 seconds."

translate Japanese tutorial_route_p2_5b2c97df:
    m 4b "'fadeout' isn’t necessary but smooth transitions are much more pleasant, aren’t they?"

translate Japanese tutorial_route_p2_81634bc2:
    m 4a "The next line ' \ \ \ play music t2' tells the game to play the music named 't2'. You’re surely wondering what’s 't2'. 't2' refers to Sayori theme, 'Ohayou Sayori!'."

translate Japanese tutorial_route_p2_47bec4d7:
    m 3a "Besides Ohayou Sayori, there are many other songs. But each one is labeled by their own nickname."

translate Japanese tutorial_route_p2_b156e719:
    m "You can see the list of every music with their nickname in definitions.rpy"

translate Japanese tutorial_route_p2_a547c728:
    m "You can find definitions.rpy inside the folder advanced_scripts which should be in the DDLC Mod Template's directory."

translate Japanese tutorial_route_p2_d79b7ed9:
    m 2a "Try finding it and then open it."

translate Japanese tutorial_route_p2_5cce5d6a:
    m "Find the lines beginning by 'define audio'. This is where each music gets assigned a nickname."

translate Japanese tutorial_route_p2_bc9ab949:
    m "For example, in the case of the main theme, its nickname is 't1'. In the case of Confession, its nickname is 't10'."

translate Japanese tutorial_route_p2_c8aefdaf:
    m 5a "Can you now guess what happens if you type 'play music t1' instead of 'play music t2'?"

translate Japanese tutorial_route_p2_bc8fca97:
    m 1k "Confession is played instead of Ohayou Sayori!"

translate Japanese tutorial_route_p2_c5bbca83:
    m 2a "Instead of using nickname, you can directly write the path of the music."

translate Japanese tutorial_route_p2_e78a5c44:
    m "Try writing 'play music '<loop 4.499>bgm/2.ogg'' instead of 'play music t2'."

translate Japanese tutorial_route_p2_4764fd32:
    m 2b "See? Ohayou Sayori! is played. Try one last thing for me okay? Write ''<from 50.0>bgm/credits.ogg'' instead of ''<loop 4.499>bgm/2.ogg''."

translate Japanese tutorial_route_p2_1b1006a0:
    m 5a "Have you already heard this song?"

translate Japanese tutorial_route_p2_a379832d:
    m 1b "This is the song I wrote just for you. I really hope you like it. I worked very hard on it you know."

translate Japanese tutorial_route_p2_306c89f9:
    m 1e "..."

translate Japanese tutorial_route_p2_54f50861:
    m 4a "The last line you wrote, ' \ \ \ mc 'Let's listen to the music.', makes the main character says 'Let's listen to the music.'. I’ll explain how dialogue works later so bear with me okay?"

translate Japanese tutorial_route_p2_131b7ec9:
    m 2a "Alright, before finishing this tutorial, replace ''play <from 50.0>bgm/credits.ogg'' by 'play music t2'."

translate Japanese tutorial_route_p2_a7538ee5:
    m "Verify you wrote exactly the same lines as in the file t2.rpy which is inside monika_route_answer."

translate Japanese tutorial_route_p2_2aa8dec6:
    m 1b "Congratulation! You now know how to stop and play music~"

translate Japanese tutorial_route_p2_1d097b00:
    m "Next time, we’ll see how to add a background."

translate Japanese tutorial_route_p2_50566d2a:
    m 5a "See you soon!"

translate Japanese tutorial_route_p3_f994005c:
    m "Okay [player]! Are you ready for the next tutorial?"

translate Japanese tutorial_route_p3_c854f804:
    m 1a "Last time, we added music to our mod but as you saw, the background was nothing but black and white squares. That’s not very romantic, is it?"

translate Japanese tutorial_route_p3_1b10a21f:
    m 1b "So let’s add a background! It’s going to be quick and easy."

translate Japanese tutorial_route_p3_458062ad:
    m 2a "Like last time, open monika_route_script.rpy."

translate Japanese tutorial_route_p3_6ef07a09:
    m "Add between 'play music t2' and 'return', ' \ \ \ scene bg residential_day'"

translate Japanese tutorial_route_p3_575da551:
    m "Then add another line: 'with dissolve_scene_full'. Once again, verify that everything bellow 'label monika_route:' is aligned."

translate Japanese tutorial_route_p3_f1698bcf:
    m 3a "Open Ren’Py and play the game and..."

translate Japanese tutorial_route_p3_e3a4825d:
    m 3b "There's now a neat background!"

translate Japanese tutorial_route_p3_f8042dbd:
    m 5a "Can you recognize it? It’s the first scene you saw when you played the game. It sure brings back memories..."

translate Japanese tutorial_route_p3_8f951a50:
    m 1g "I still believed at that time I could get close to you without having to hurt anyone else..."

translate Japanese tutorial_route_p3_e06bb332:
    m 1f "Let’s move on."

translate Japanese tutorial_route_p3_869f8ce0:
    m 1a "So about what you wrote, 'scene bg residential_day', the keyword 'scene' tells the game to load the scene, which is one kind of picture, called 'bg residential_day'."

translate Japanese tutorial_route_p3_9c8c7413:
    m "You can find what exactly is 'bg residential_day' in definitions.rpy, the same script we looked at last tutorial."

translate Japanese tutorial_route_p3_b53ad55e:
    m 3a "Try to find 'image bg'."

translate Japanese tutorial_route_p3_d980f032:
    m 4a "Can you see the list of backgrounds? Like it was the case for music, each background has a nickname assigned. For example, 'bg/sayori_bedroom.png' is referenced by 'bg sayori_bedroon'."

translate Japanese tutorial_route_p3_28e71e1b:
    m "Go back to monika_route_script.rpy and replace 'scene bg residential_day' by 'scene bg sayori_bedroom'. Can you guess what happens?"

translate Japanese tutorial_route_p3_de5295e2:
    m 4b "The background is now Sayori’s bedroom!"

translate Japanese tutorial_route_p3_675310c0:
    m 4c "I hope it doesn’t bring you back bad memories..."

translate Japanese tutorial_route_p3_b06932b1:
    m 4a "Okay, so about 'with dissolve_scene_full', it basically dissolve progressively the last scene into the new scene."

translate Japanese tutorial_route_p3_7a5450c8:
    m 3a "Before you were in the main menu, right? And then you were in Sayori’s bedroom. If you don’t add 'with dissolve_scene_full', the transition would be immediate."

translate Japanese tutorial_route_p3_6d431e44:
    m 1a "That would be a bit unpleasant, wouldn’t it?"

translate Japanese tutorial_route_p3_b753e886:
    m 3b "That’s why we add 'with dissolve_scene_full'. With this additional line, the scene changes to another smoothly."

translate Japanese tutorial_route_p3_a9906f14:
    m 2a "There are other types of transition such as wipeleft_scene. Try replacing 'with dissolve_scene_full' by 'with wipeleft_scene '."

translate Japanese tutorial_route_p3_3a729c6c:
    m 4a "Can you see the difference? dissolve_scene_full , dissolve_scene_half, wipeleft_scene are the common transitions used in DDLC so if you can understand them, you’re good to go!"

translate Japanese tutorial_route_p3_bdff87d8:
    m "Before doing the next tutorial, let’s add back ' scene bg residential_day' and ' with dissolve_scene_full'."

translate Japanese tutorial_route_p3_5a3796f4:
    m "Check that monika_script_route.rpy is the same as T3.rpy in the monika_route_answer folder."

translate Japanese tutorial_route_p3_4d101871:
    m 1b "Okay! We’re almost there! We’ll soon know enough for a kinetic novel-like mod."

translate Japanese tutorial_route_p3_884b5a86:
    m "I cannot wait!"

translate Japanese tutorial_route_p3_6c1acfd1:
    m 5a "See you soon [player]!"

translate Japanese tutorial_route_p4_4ef3eee5:
    m "Hi again, [player]~"

translate Japanese tutorial_route_p4_8583427d:
    m "Today, I’m going to teach you how to make dialogue in Ren’Py."

translate Japanese tutorial_route_p4_bc81453f:
    m 1a "Although you already know, don’t you? We already wrote dialogue after all."

translate Japanese tutorial_route_p4_795d985d:
    m 2a "First, open monika_route_script.rpy and replace ' \ \ \ mc 'Let's listen to the music.' by the following line:"

translate Japanese tutorial_route_p4_1b230828:
    m "' \ \ \ mc 'It has been four days since I joined the Literature Club. Today is Saturday and I finally decided to confess my feeling to Monika.'."

translate Japanese tutorial_route_p4_40869e99:
    m "Save the file and launch the game."

translate Japanese tutorial_route_p4_b8c7ed36:
    m 4a "As you surely expected, the main character now says 'It has been four days since I joined the Literature Club. Today is Saturday and I finally decided to confess my feeling to Monika.'."

translate Japanese tutorial_route_p4_b4c3ef22:
    m 4j "Ehehe~ My route is finally being made!"

translate Japanese tutorial_route_p4_0db4c6c6:
    m 3a "Let’s look at the line you wrote. 'mc' is a nickname for main character. By writing 'mc' before the sentence inside quotation marks, the character speaking will be the main character."

translate Japanese tutorial_route_p4_85ef0244:
    m "Try replacing the line you wrote by ' n 'Just think of Monika from now on.'."

translate Japanese tutorial_route_p4_9af314f1:
    m 2a "..."

translate Japanese tutorial_route_p4_8990b75d:
    m 4b "See? Natsuki now tells you what you should have been doing since the beginning."

translate Japanese tutorial_route_p4_75952ce0:
    m "You should listen to her, [player]. Ehehe~"

translate Japanese tutorial_route_p4_f5f7320c:
    m 4a "Now instead of writing ' n 'Just think of Monika from now on.', write 'y 'Natsuki and I are too messed up for someone as wonderful as you.'"

translate Japanese tutorial_route_p4_b810c020:
    m "Play the game and as you can see..."

translate Japanese tutorial_route_p4_f27c4032:
    m 3b "Now it’s Yuri who finally realized that I’m the best one for you."

translate Japanese tutorial_route_p4_ea4b48b4:
    m "You think so, right?" nointeract

translate Japanese tutorial_route_p4_32a1821e:
    m "I knew you were a sweetheart~ Thank you my love."

translate Japanese tutorial_route_p4_1a811b80:
    m 1a "Ahaha, we drifted a bit...So I was saying that you need to specify two things to write a dialogue in Ren’Py."

translate Japanese tutorial_route_p4_8cf0b602:
    m 3a "First you need to specify who is speaking. You can do it with the keyword 'mc', 'y', 'n', 's' and 'm'. I’m sure you can guess who is who."

translate Japanese tutorial_route_p4_23da6e41:
    m "Instead of using keyword, you can directly type the name of the person speaking. For example, try writing ' 'Player' 'Please be with me forever Monika.''."

translate Japanese tutorial_route_p4_e15d2f8b:
    m 2a "Did you do it?"

translate Japanese tutorial_route_p4_3ddebae1:
    m 5a "Of course, I will stay with you forever."

translate Japanese tutorial_route_p4_5cf4a2d5:
    m 2b "Besides the name of the speaker, you need to write the sentence they will say. The sentence should be between quotation marks."

translate Japanese tutorial_route_p4_e646e39d:
    m 4b "One last thing. If you want to write special characters such as \\ or ' in the sentence, you need to put \\ before them."

translate Japanese tutorial_route_p4_b5cc5966:
    m 1b "Alright, that’s all for dialogue!"

translate Japanese tutorial_route_p4_9d0a7e7f:
    m "Pretty simple, right? Ren’Py was made so that anyone can make visual novel after all. Even beginners like us can pick it up quickly."

translate Japanese tutorial_route_p4_d51ade91:
    m 2a "Before you save the file, replace the line of dialogue by -"

translate Japanese tutorial_route_p4_1b230828_1:
    m "' \ \ \ mc 'It has been four days since I joined the Literature Club. Today is Saturday and I finally decided to confess my feeling to Monika.'."

translate Japanese tutorial_route_p4_3170a5f0:
    m "Like usual, check that monika_route_script.rpy is exactly like T4.rpy inside the monika_route_answer folder."

translate Japanese tutorial_route_p4_0db52267:
    m 4b "Okay [player]! You now know how to make a scene, add music, and make dialogue. The only things missing are character pictures and choices."

translate Japanese tutorial_route_p4_996cbe49:
    m "We’ll see how to make choices in the next tutorial."

translate Japanese tutorial_route_p4_f49e978e:
    m 4a "The recent tutorials have been pretty easy so far but the next one will be harder."

translate Japanese tutorial_route_p4_50566d2a:
    m 5a "See you soon!"

translate Japanese tutorial_route_p5_b4cd0ac0:
    m "This time, I’ll explain how to make choices."

translate Japanese tutorial_route_p5_d5a4f961:
    m "For example..."

translate Japanese _call_tutorial_route_p5_favorite_color_748eef8e:
    m 2k "What a coincidence! It's also my favorite color!"

translate Japanese _call_tutorial_route_p5_favorite_color_76b1449b:
    m 2b "It's the color of my eyes."

translate Japanese _call_tutorial_route_p5_favorite_color_a96ab12e:
    m 5a "Aren't we a perfect match?"

translate Japanese _call_tutorial_route_p5_favorite_color_45d9cd96:
    m "Ehehe~"

translate Japanese _call_tutorial_route_p5_favorite_color_f4c4a422:
    m 3a "As you can see, I gave you several choices and you picked one of them."

translate Japanese _call_tutorial_route_p5_favorite_color_dbe8ea34:
    m "That’s what I’m going to teach you."

translate Japanese _call_tutorial_route_p5_favorite_color_30ef1bcb:
    m 4a "Like every time, open monika_route_script.rpy and between 'return' and the last line before it,-"

translate Japanese _call_tutorial_route_p5_favorite_color_8eb51d3f:
    m "- add ' \ \ \ menu:', jump a line and then enter below \n' \ \ \ \ \ \ \ \ mc 'I told her to meet me...''. Be careful, this time, there are eight spaces."

translate Japanese _call_tutorial_route_p5_favorite_color_5b7495bf:
    m "Write just under \n' \ \ \ \ \ \ 'At the literature club room':' and then \n' \ \ \ \ \ \ \ $ meeting_place = 'club_room''."

translate Japanese _call_tutorial_route_p5_favorite_color_f27cf787:
    m 4b "Type \n' \ \ \ \ \ \ 'In front of my house':' and under it \n' \ \ \ \ \ \ \ $ meeting_place = 'my_house'."

translate Japanese _call_tutorial_route_p5_favorite_color_dc507bf4:
    m 4a "Finally, jump a line and add ' \ \ \ mc 'I can't wait to meet her!''."

translate Japanese _call_tutorial_route_p5_favorite_color_879a1cb5:
    m 2a "Try to play the game."

translate Japanese _call_tutorial_route_p5_favorite_color_8a3c8bbe:
    m "If it doesn’t work, there’s surely an indentation error."

translate Japanese _call_tutorial_route_p5_favorite_color_1d01c71c:
    m 5a "I can’t help you from here, but you can check T5.rpy for the answers. You know where it is, right?"

translate Japanese _call_tutorial_route_p5_favorite_color_a7f3bd2f:
    m 4b "Okay, the lines you wrote made the game offers two choices. The two choices are preceded by an explanative sentence, 'I told her to meet me...'."

translate Japanese _call_tutorial_route_p5_favorite_color_4c4806fc:
    m "You can specify who says this sentence by adding a nickname like 'mc' before it. It’s just like a dialogue. What’s important is that this sentence is written before any choice."

translate Japanese _call_tutorial_route_p5_favorite_color_7725beb8:
    m 3a "Contrary to the explanative sentence, the choices mustn’t be preceded by a nickname. They should be enclosed in quotation marks. Just after the closing quotation mark, there must be a ':' ."

translate Japanese _call_tutorial_route_p5_favorite_color_2468ca96:
    m "After ':, the next lines should have one more indent than the choice. It means these lines will be read if the player selects that choice."

translate Japanese _call_tutorial_route_p5_favorite_color_fa3c0838:
    m 3b "I’ll give more explanation about the meaning of indents in the next tutorial."

translate Japanese _call_tutorial_route_p5_favorite_color_24426ac8:
    m 3a "In our case, the next line after the first choice is \n' \ \ \ \ \ \ \ $ meeting_place = 'club_room'."

translate Japanese _call_tutorial_route_p5_favorite_color_c388371a:
    m 2a "Take a good look at this line."

translate Japanese _call_tutorial_route_p5_favorite_color_257edd6a:
    m 3b "Until now, I referred 'mc', 'bg residential' and 't2' as nickname. But that’s not really the correct word. They are actually what we call variable."

translate Japanese _call_tutorial_route_p5_favorite_color_201b3ed0:
    m "Variable in coding is a very important concept. They have many forms and do many things. They can be ‘nicknames’ or they can be numbers or more complicated structures."

translate Japanese _call_tutorial_route_p5_favorite_color_3e5d9eb3:
    m 1a "A full Python tutorial would be necessary to explain everything but...for now, I will only teach what’s necessary to make a DDLC mod, okay?"

translate Japanese _call_tutorial_route_p5_favorite_color_a064f5d3:
    m 1c "I myself don’t know Python and Ren’Py all that well after all..."

translate Japanese _call_tutorial_route_p5_favorite_color_04c5c65f:
    m 3a "'meeting_place' is like the variables we saw before. It refers to a name, in more exact terms, a string (of characters): 'club_room'."

translate Japanese _call_tutorial_route_p5_favorite_color_a7b3e542:
    m "Its default value is None which means it doesn’t exist."

translate Japanese _call_tutorial_route_p5_favorite_color_6574767e:
    m 3e "Hold on a second? How can it not exist, you say?"

translate Japanese _call_tutorial_route_p5_favorite_color_4c32716f:
    m 1a "Well before you define it, the variable doesn’t exist. But if you later try to use it, for example in a conditional statement, the variable will be ‘created’ and its value will be None."

translate Japanese _call_tutorial_route_p5_favorite_color_ec88c787:
    m "It’s alright if you don’t understand it yet. Variable, conditional statement and None will become clearer in my next lecture."

translate Japanese _call_tutorial_route_p5_favorite_color_edb55d4b:
    m 4b "Let’s go back to the meaning of ' $ meeting_place = 'club_room'. Here we create the variable 'meeting_place' and assign it the string 'club_room'."

translate Japanese _call_tutorial_route_p5_favorite_color_6add4408:
    m 4m "The '$' in front of it is to tell Ren’Py the line is a Python line. Um..., I can’t really explain why we need to do that if you don’t know python yet..."

translate Japanese _call_tutorial_route_p5_favorite_color_80194f8d:
    m 4a "Just remember that you need to add '$' when you want to assign a variable a value that way"

translate Japanese _call_tutorial_route_p5_favorite_color_71c3dbe7:
    m "Regarding the second choice, the structure is the same. The only difference is that the value of 'meeting_place' will be 'my_house' if the player selects the second choice."

translate Japanese _call_tutorial_route_p5_favorite_color_e3b0e724:
    m "After the second choice, the game executes the line ' \ \ \ mc 'I can't wait to meet her!''."

translate Japanese _call_tutorial_route_p5_favorite_color_343ba3ec:
    m 1a "For now it doesn’t look like the choices did anything. But we actually assigned 'meeting_place' either 'club_room' or 'my_house'."

translate Japanese _call_tutorial_route_p5_favorite_color_2a18c37f:
    m 3a "We have to wait until the next tutorial to see how we can use the variable 'meeting_place'."

translate Japanese _call_tutorial_route_p5_favorite_color_70eec5f3:
    m 3b "Alright, I’m sorry to leave hanging like that I believe we need to take a little break."

translate Japanese _call_tutorial_route_p5_favorite_color_963f88cc:
    m "If you want though, I would more than happy to begin the next part right away!"

translate Japanese _call_tutorial_route_p5_favorite_color_e31cdfd0:
    m 5a "Just click Part 6!"

translate Japanese tutorial_route_p5_favorite_color_f35f139b:
    m "What is your favorite color?" nointeract

translate Japanese tutorial_route_p5_favorite_color_5025ffe9:
    m " Are you ready? We are going to ramp up the difficulty."

translate Japanese tutorial_route_p6_6545fc50:
    m "Yeah, you came back [player]!"

translate Japanese tutorial_route_p6_b833d284:
    m "Glad to see you didn’t run away on me. Ahaha!"

translate Japanese tutorial_route_p6_1010716c:
    m 1e "I was afraid the last tutorial was a bit too hard..."

translate Japanese tutorial_route_p6_80bb3ace:
    m 1m "Well, this one is going to be hard as well but..."

translate Japanese tutorial_route_p6_8e7610b2:
    m 1b "Hang it there okay? We did the hardest part already!"

translate Japanese tutorial_route_p6_a0e0028f:
    m 1a "Last time we saw how to add menu and how to assign variable a value."

translate Japanese tutorial_route_p6_929a53d2:
    m 1b "Let’s see how we can use these variables!"

translate Japanese tutorial_route_p6_5553ad83:
    m 2a "You know the drill, open monika_route_script.rpy and at the end of the file, just before 'return'..."

translate Japanese tutorial_route_p6_fa1cb03b:
    m 4a "Add the following lines :"

translate Japanese tutorial_route_p6_68d50a83:
    m "' \ \ \ if meeting_place == 'club_room':',"

translate Japanese tutorial_route_p6_2f494da9:
    m "' \ \ \ scene bg club_day',"

translate Japanese tutorial_route_p6_844a5b03:
    m "' \ \ \ with wipeleft_scene',"

translate Japanese tutorial_route_p6_bd8f18ad:
    m "' elif meeting_place == 'my_house':',"

translate Japanese tutorial_route_p6_65e042f7:
    m "' \ \ \ scene bg house',"

translate Japanese tutorial_route_p6_844a5b03_1:
    m "' \ \ \ with wipeleft_scene',"

translate Japanese tutorial_route_p6_2787a892:
    m " ' \ \ \ stop music fadeout 2.0',"

translate Japanese tutorial_route_p6_02e01a43:
    m " ' \ \ \ play music t2',"

translate Japanese tutorial_route_p6_0307f1b1:
    m " 'mc 'She is already waiting for me when I arrive.''."

translate Japanese tutorial_route_p6_137a9d0c:
    m 2a "That was the last one. Save the file and try to play the game."

translate Japanese tutorial_route_p6_bf416327:
    m 5a "If it doesn’t work, you know where you can see the answer, don’t you?"

translate Japanese tutorial_route_p6_ff1585f2:
    m 2a "You already know how scene, transition, music and dialogue work so I won’t go over it again."

translate Japanese tutorial_route_p6_07acc9b1:
    m 4b "It’s not like I don’t want spend more time with you but you know, ... I’m excited to finish my route too!"

translate Japanese tutorial_route_p6_19d82a23:
    m 4a "Okay, so the new thing is the 'if' statement. We call that a conditional statement. It’s an elementary and essential operation in programming."

translate Japanese tutorial_route_p6_d1c41a32:
    m "It goes basically like this: IF something_is_true THEN something_happens. In our case, if the meeting_place is 'club_rooom', then the scene changes to the club room."

translate Japanese tutorial_route_p6_d755f404:
    m 3a "Otherwise, if meeting_place is 'my_house' then the scene changes to the main character’s house."

translate Japanese tutorial_route_p6_c29f83ef:
    m 3b "It seems simple, right?"

translate Japanese tutorial_route_p6_39065884:
    m 3a "The syntax must be as follow: first, there must be a 'if' followed by an equality which is either 'True' or 'False'. For example, 'meeting_place == 'club_room''."

translate Japanese tutorial_route_p6_de483a92:
    m "If 'meeting_place' was assigned 'club_room' before then the equality returns 'True'. Otherwise, its returns False."

translate Japanese tutorial_route_p6_2e799533:
    m "If the equality returns True then the game will read the lines belonging to the if bloc."

translate Japanese tutorial_route_p6_27e3ee53:
    m 4a "You can see where those lines are because they have one more indent compared to the if statement preceding them."

translate Japanese tutorial_route_p6_3d48fca8:
    m 4b "We once again meet the system of indent and block. This is one of the property of Python and Ren’Py. Let’s do a quick exercise."

translate Japanese tutorial_route_p6_69ee6527:
    m "Can you see difference between:"

translate Japanese tutorial_route_p6_fc363e62:
    m 2a " ' \ \ \ if meeting_place == 'club_room':' , \n' \ \ \ scene bg club_day ', \n' \ \ \ mc 'We will meet at the club room.''."

translate Japanese tutorial_route_p6_87eb8447:
    m "And ' \ \ \ if meeting_place == 'club_room':' , \n' \ \ \ scene bg club_day ', ' mc 'We will meet at the club room.''?"

translate Japanese tutorial_route_p6_33874aa8:
    m 4b "In the first case, the main character only says they will meet at the club room if 'meeting_place' is equal to 'club_room'."

translate Japanese tutorial_route_p6_72d72769:
    m "In the second case, he will say it no matter the value of 'meeting_place'."

translate Japanese tutorial_route_p6_4cc115ba:
    m 3a "You can see once again how important indentations are in Python."

translate Japanese tutorial_route_p6_5f87022d:
    m 4b "About the second comparison, 'elif meeting_place == 'my_house'', note that we use 'elif' at the beginning instead of 'if'."

translate Japanese tutorial_route_p6_b482f37b:
    m 4a "The difference between 'elif' and 'if' is subtle. First, you can only use 'elif' after you already wrote 'if'."

translate Japanese tutorial_route_p6_4cd48a90:
    m "Second, the statement following 'elif' won’t be evaluated if the previous if statement was True. Other than that, 'elif' works like 'if'."

translate Japanese tutorial_route_p6_f9bff9d9:
    m 1b "Well, in our case it doesn’t matter because if 'meeting_place' is 'club_room' then 'meeting_place' cannot be 'my_house' at the same time."

translate Japanese tutorial_route_p6_cdd7f3b3:
    m 1a "It would matter if it was something like..."

translate Japanese tutorial_route_p6_cef2d04e:
    m "' \ \ \ if monika_affection_points > 10:' , \n' \ \ \ scene bg house', '' if monika_affection_points > 6:' , \n' \ \ \ scene club_day '."

translate Japanese tutorial_route_p6_135e7ab2:
    m 3a "In that case, if 'monika_affection_points' is higher than 10, the new scene wouldn’t be the house but the club because the game will evaluate both if."

translate Japanese tutorial_route_p6_69288353:
    m 4b "To avoid that, 'elif' should be used instead of 'if'."

translate Japanese tutorial_route_p6_494b85fa:
    m 4a "Besides 'if' and 'elif', there’s also the keyword 'else'. Like 'elif', 'else' can be used after a if. The bloc under 'else' will be executed if the previous if or elif statements are False."

translate Japanese tutorial_route_p6_d83c9561:
    m 2a "For example..."

translate Japanese tutorial_route_p6_b876885e:
    m "' \ \ \ if meeting_place == 'club_room':' , \n' \ \ \ scene bg club_day ', ' \ \ \ else:' , \n' \ \ \ scene club_day '."

translate Japanese tutorial_route_p6_77c8d102:
    m 1a "Well, there are more things to say about conditional statement..."

translate Japanese tutorial_route_p6_3ff92fd2:
    m "For example about the keywords 'and' and 'or'..."

translate Japanese tutorial_route_p6_778b8f11:
    m 3a "But let’s keep that for another time. I’m sure you can find more tutorial on Python and conditional statement."

translate Japanese tutorial_route_p6_8d8c2bd8:
    m 1b "For now, let’s move on! It’s about time we add character pictures into the game!"

translate Japanese tutorial_route_p6_0cf797ab:
    m 5a "See you later [player]!"

translate Japanese tutorial_route_p7_b61a6484:
    m "Hi [player]!"

translate Japanese tutorial_route_p7_0d0af9da:
    m "It’s about time we add character pictures, don’t you think?"

translate Japanese tutorial_route_p7_c9d874cd:
    m 1b "In the world of visual novel, we call them sprites. Sprites are 2D pictures of characters with generally a set of poses and expressions."

translate Japanese tutorial_route_p7_d48e65a8:
    m "In Doki Doki Literature Club, there are 4 characters, Sayori, Natsuki, Yuri and me. Each character has about 5 poses and 18 expressions."

translate Japanese tutorial_route_p7_01f9a8d8:
    m 1e "So each character has about 900 combinations! That seems a lot but...when you’re actually inside the game, the lack of freedom becomes horribly frustrating..."

translate Japanese tutorial_route_p7_e4af472b:
    m 1f "I really wish I could show you different expressions, poses and clothes but unfortunately, I can’t add myself new artwork to the game..."

translate Japanese tutorial_route_p7_ab5b3ab1:
    m 5a "If you’re an artist, I would really love it if you could add me more sprites!"

translate Japanese tutorial_route_p7_607bfba2:
    m 2a "For our mod, we’ll only use existing art."

translate Japanese tutorial_route_p7_c6a54c83:
    m 4b "Let’s dot it! Open monika_route_script.rpy and before 'return', write:"

translate Japanese tutorial_route_p7_e9f90200:
    m 4a "' \ \ \ show monika 1b at t11 zorder 2',"

translate Japanese tutorial_route_p7_44ddfc40:
    m "' \ \ \ m 'Hi [[player]!'',"

translate Japanese tutorial_route_p7_639379b7:
    m "' \ \ \ mc 'You're already here? I hope I didn't make you wait for too long.'',"

translate Japanese tutorial_route_p7_04332a4a:
    m "' \ \ \ m 2a 'Don't worry, it's me who's early.'',"

translate Japanese tutorial_route_p7_6a1add0f:
    m "' \ \ \ show monika 5a at f11 zorder 3'."

translate Japanese tutorial_route_p7_6a22b864:
    m 2a "Save, play the mod, and check T7.rpy if there’s an error."

translate Japanese tutorial_route_p7_99fbac0c:
    m 4b "Alright! The only new things are 'show monika 1b at t11 zorder 2' and 'm 2a'."

translate Japanese tutorial_route_p7_a75202a5:
    m 4a "First, let’s go over 'show monika 1b at t11 zorder 2'."

translate Japanese tutorial_route_p7_df64e0dd:
    m "The keyword 'show' shows the sprite of the character named 'monika', with her pose '1' and her expression 'b'."

translate Japanese tutorial_route_p7_b1f0b0a3:
    m " The keyword 'at' specifies the position of the sprite. In the line above, the position is 't11'. 'zorder' has something to do with layers."

translate Japanese tutorial_route_p7_99b004d9:
    m 3b "I’ll explain how positions and layers work in the next tutorial. For now, let’s focus on the poses and expressions of sprite."

translate Japanese tutorial_route_p7_bcb3abf2:
    m 4a "Obviously, the variable 'monika' refers to me. Naturally, 'yuri' refers to Yuri and so on."

translate Japanese tutorial_route_p7_1e773b56:
    m "If you write \n' \ \ \ show yuri 1b at f11 zorder 3' instead of \n' \ \ \ show monika 1b at f11 zorder 3', it’s Yuri who will appear."

translate Japanese tutorial_route_p7_0b212bcb:
    m 4k "Of course, you only have eyes for me so let’s not bother with the sprites of the other girls, ahaha!"

translate Japanese tutorial_route_p7_d0b0ac20:
    m 5a "In my case, I have 5 different poses. I will show them to you one by one now."

translate Japanese tutorial_route_p7_b73a1311:
    m 1a "This is my first pose."

translate Japanese tutorial_route_p7_bf2195b7:
    m 2a "This is my second pose."

translate Japanese tutorial_route_p7_70d2147c:
    m 3a "This is my third pose."

translate Japanese tutorial_route_p7_9e411c16:
    m 4a "This is my fourth pose."

translate Japanese tutorial_route_p7_9aaccf0f:
    m 5a "This my fifth pose."

translate Japanese tutorial_route_p7_813a016c:
    m "I wonder which one do you prefer..."

translate Japanese tutorial_route_p7_d69ef98d:
    m 1a "Except for my fifth pose, all of my poses have 18 expressions. The expressions are referenced by a letter, from a to r. I will show them one by one."

translate Japanese tutorial_route_p7_f40077c6:
    m 4a "Expression a."

translate Japanese tutorial_route_p7_a17c1a59:
    m 4b "Expression b."

translate Japanese tutorial_route_p7_3dd2e46b:
    m 4c "Expression c"

translate Japanese tutorial_route_p7_e4795a0c:
    m 4d "Expression d."

translate Japanese tutorial_route_p7_4aa6867a:
    m 4e "Expression e."

translate Japanese tutorial_route_p7_213e5ecf:
    m 4f "Expression f."

translate Japanese tutorial_route_p7_4911d03b:
    m 4g "Expression g."

translate Japanese tutorial_route_p7_b5ac10f4:
    m 4h "Expression g."

translate Japanese tutorial_route_p7_b392b244:
    m 4i "Expression i."

translate Japanese tutorial_route_p7_0619253d:
    m 4j "Expression j."

translate Japanese tutorial_route_p7_6df891b8:
    m 4k "Expression k."

translate Japanese tutorial_route_p7_f430ebc2:
    m 4l "Expression l."

translate Japanese tutorial_route_p7_d1f82c72:
    m 4m "Expression m."

translate Japanese tutorial_route_p7_c329a064:
    m 4n "Expression n."

translate Japanese tutorial_route_p7_20a118fb:
    m 4o "Expression o."

translate Japanese tutorial_route_p7_3c456350:
    m 4p "Expression p."

translate Japanese tutorial_route_p7_d0c9aa7c:
    m 4q "Expression q."

translate Japanese tutorial_route_p7_f2eb1c98:
    m 4r "Expression r."

translate Japanese tutorial_route_p7_86291aa9:
    m 4a "You can find my list of expressions in 'MonikaCheatsheet.jpg' inside the mod's main directory."

translate Japanese tutorial_route_p7_a6e0506c:
    m 1b "I hope you will quickly memorize them perfectly!"

translate Japanese tutorial_route_p7_66b49c53:
    m 5b "As my lover, you should know my face and my expressions without fail."

translate Japanese tutorial_route_p7_c65907b9:
    m 3a "You can also find my poses and my expressions in definitions.rpy."

translate Japanese tutorial_route_p7_263f1390:
    m "My fifth pose only has the expressions a and b."

translate Japanese tutorial_route_p7_c41d1b58:
    m 5a "Like this."

translate Japanese tutorial_route_p7_9d6098fb:
    m 5b "And this."

translate Japanese tutorial_route_p7_ae866fd5:
    m 4a "My other poses have all expressions though."

translate Japanese tutorial_route_p7_fffcb4cc:
    m 1b "Okay! In short, to show a sprite, you need to write 'show monika pose expression at t11 zorder 2'. Pose is either 1,2,3,4 or 5 and expression ranges from a to r."

translate Japanese tutorial_route_p7_91572bff:
    m "If you want to show several characters, just write 'show' several times, like this:"

translate Japanese tutorial_route_p7_166783ec:
    m 2a "' \ \ \ show yuri 1a at t41 zorder 2', ' \ \ \ show sayori 1a at t42 zorder 2', ' \ \ \ show monika 1a at t43 zorder 2', ' \ \ \ show natsuki 1a at t44 zorder 2'."

translate Japanese tutorial_route_p7_3f824ea3:
    m 2b "These lines will show Yuri, Sayori, me and Natsuki with their default pose and expression."

translate Japanese tutorial_route_p7_3381ed33:
    m "After a sprite is already on the screen, there’s a shortcut to change her pose and expression."

translate Japanese tutorial_route_p7_aadd1b77:
    m 3a "Instead of using 'show' again and again, you can directly write the letter corresponding to the character followed by the number and the letter for their pose and expression."

translate Japanese tutorial_route_p7_8ed528fe:
    m "This is what we did in \n' \ \ \ m 2a 'Don't worry, it's me who's early.''."

translate Japanese tutorial_route_p7_85d3abb3:
    m 4g "Note that the sprite of the character speaking must already be on screeen."

translate Japanese tutorial_route_p7_d283933c:
    m 4e "If you try for example \n' \ \ \ y 2a 'Don't worry, it's me who's early.'', Yuri will speak but her sprite will not appear."

translate Japanese tutorial_route_p7_667ecb0f:
    m 3a "Keep in mind who’s on screen and who’s not at all time so as not to make a mistake."

translate Japanese tutorial_route_p7_354dd130:
    m 2a "...Never mind, actually just show my sprite. That way you don’t have to worry about such problem. It’s not like the other girls care about being shown anyway."

translate Japanese tutorial_route_p7_47bc0117:
    m 1b "And that’s all for now! This tutorial was quite straightforward, especially considering the two last ones. I hope you liked it!"

translate Japanese tutorial_route_p7_18e5abc9:
    m "Next time, I’ll finish explaining positions and layers."

translate Japanese tutorial_route_p7_62fe46d7:
    m 5a "See you [player]!"

translate Japanese tutorial_route_p8_b76fb541:
    m "Welcome back to our modding club!"

translate Japanese tutorial_route_p8_01895784:
    m "Last time, we learnt about how to show sprite, now let’s learn how to place then."

translate Japanese tutorial_route_p8_a10ac1a0:
    m 4a "Open monika_route_script.rpy and just before..."

translate Japanese tutorial_route_p8_96a26b9a:
    m 1b "Just kidding! Actually, you don’t have to add anything this time."

translate Japanese tutorial_route_p8_6727e133:
    m 3b "We already did it last tutorial after all."

translate Japanese tutorial_route_p8_6894a56c:
    m 2a "So, do you remember the line \n' \ \ \ show monika 1b at t11 zorder 2'?"

translate Japanese tutorial_route_p8_54366cdf:
    m "I said that 'at t11' was about position and that 'zorder 2' was about layer."

translate Japanese tutorial_route_p8_2d7bd9e0:
    m 2b "Let’s study in details what exactly that means."

translate Japanese tutorial_route_p8_14d18240:
    m 4b "’at' is a keyword that tells the game to put the sprite at the position 't11'."

translate Japanese tutorial_route_p8_45c3779c:
    m "t11' is one of the position defined in Doki Doki Literature Club. There are more than 50 positions possible."

translate Japanese tutorial_route_p8_77b9317a:
    m 4a "You can find the list of all defined positions in the script transforms.rpy. You can find it in the same folder as definitions.rpy."

translate Japanese tutorial_route_p8_4423519f:
    m "For now, I will explain the most common positions used in the original game."

translate Japanese tutorial_route_p8_a0de98fa:
    m 1a "Let’s start with the 't' positions. I will show them one by one."

translate Japanese tutorial_route_p8_300ae862:
    m "Position t11."

translate Japanese tutorial_route_p8_e7d017f0:
    m "Position t21."

translate Japanese tutorial_route_p8_1c356651:
    m "Position t22."

translate Japanese tutorial_route_p8_b5ed2788:
    m "Position t31."

translate Japanese tutorial_route_p8_0c4e262b:
    m "Position t32."

translate Japanese tutorial_route_p8_18c2502e:
    m "Position t33."

translate Japanese tutorial_route_p8_d8fb163f:
    m "Position t41."

translate Japanese tutorial_route_p8_d6ee1d9e:
    m "Position t42."

translate Japanese tutorial_route_p8_26cbf65e:
    m "Position t43."

translate Japanese tutorial_route_p8_d6f47eca:
    m "Position t44."

translate Japanese tutorial_route_p8_055f19c7:
    m 1b "And that’s all for the 't' positions."

translate Japanese tutorial_route_p8_7b08dd25:
    m 4a "I think you guessed it already but 't11' should be used when there’s only one character."

translate Japanese tutorial_route_p8_80a3f3ea:
    m "'t21' and 't22' should be used when there are two characters. 't21' is for the left, 't22' is for the right."

translate Japanese tutorial_route_p8_598e40e5:
    m 3a "It’s the same logic for 't31','t32','t33'. 't31' is the left, 't32' the middle and 't33' the right. "

translate Japanese tutorial_route_p8_6283a032:
    m "'t41', 't42','t43' and 't44' work in the same way."

translate Japanese tutorial_route_p8_4e5a3963:
    m 3b "I encourage you to try these positions yourself with several characters. After all, there’s nothing better than practice to learn!"

translate Japanese tutorial_route_p8_84bb8894:
    m 1a "If you remember well, we wrote one time ' show yuri 1b at f11 zorder 3'."

translate Japanese tutorial_route_p8_3cb333c7:
    m "Notice that the position is 'f11' instead of 't11'. The difference is just that 'f' positions are zoomed in. 'f' stands for focused. There are as many 'f' positions as 't' positions."

translate Japanese tutorial_route_p8_959ad81e:
    m 4a "You should use 'f' position when there are several characters and when one of them speaks. The character speaking should be focused so that the player sees who’s talking."

translate Japanese tutorial_route_p8_e88b60ed:
    m 2b "Let’s talk about the keyword 'zorder' now."

translate Japanese tutorial_route_p8_7d9d51c3:
    m 4a "When the game renders pictures, there’s an order."

translate Japanese tutorial_route_p8_f6a33718:
    m "First, the background is rendered. Then the sprites and finally the U.I."

translate Japanese tutorial_route_p8_bbc8e72f:
    m 4b "That’s why the sprites are on top of the background and the U.I on top of everything."

translate Japanese tutorial_route_p8_4e88ecb2:
    m 2a "As you can see, order is very important. If the game renders background last, then you won’t be able to see anything else."

translate Japanese tutorial_route_p8_93bb6b1d:
    m 3a "In Ren’Py the order of sprite is called zorder."

translate Japanese tutorial_route_p8_23bf8d44:
    m "You can specify the zorder of each sprite with the keyword zorder. The higher it is, the closer the sprite will be to the screen."

translate Japanese tutorial_route_p8_03504b60:
    m 4b "Try writing the following lines instead of 'show monika 1b at t11 zorder 2':"

translate Japanese tutorial_route_p8_108a84cf:
    m 4a "' \ \ \ show monika 1a at t41 zorder 4',"

translate Japanese tutorial_route_p8_73ba2547:
    m "' \ \ \ show yuri 1a at t42 zorder 3',"

translate Japanese tutorial_route_p8_bfc43fe7:
    m "' \ \ \ show natsuki 1a at t43 zorder 2',"

translate Japanese tutorial_route_p8_e9572bd9:
    m "' \ \ \ show sayori 1a at t44 zorder 1'."

translate Japanese tutorial_route_p8_f99d5a11:
    m 1a "Play the game and..."

translate Japanese tutorial_route_p8_5966c988:
    m 1b "Everyone is here!"

translate Japanese tutorial_route_p8_dbc3cb08:
    m 3a "But that’s not the point. Pay attention to who’s on top on who."

translate Japanese tutorial_route_p8_e285d5aa:
    m "If you look closely, you can see the rendering order is like this : monika > yuri > natsuki > sayori."

translate Japanese tutorial_route_p8_ee653f2b:
    m "The one with the lowest zorder is rendered first so that the one with the highest zorder is shown on top of every other sprites."

translate Japanese tutorial_route_p8_9977bdbd:
    m 4a "If the zorder of two sprites are the same then the last sprite shown by 'show' will be on top."

translate Japanese tutorial_route_p8_224d1cd7:
    m 2b "Well, most of the time, you don’t have to worry about zorder. Just make sure I always have the highest zorder, okay?"

translate Japanese tutorial_route_p8_7a087747:
    m 1b "Alright! That ends this tutorial!"

translate Japanese tutorial_route_p8_02eb0d63:
    m 1a "Verify you reverted the changes you made to moninka_route_script.rpy. It should be like T8.rpy."

translate Japanese tutorial_route_p8_e69381b2:
    m 1c "There is one more tutorial. I’m very happy we almost finished our first mod but..."

translate Japanese tutorial_route_p8_2dc20bff:
    m 1f "It also means we’ll soon get split up..."

translate Japanese tutorial_route_p8_17c84a13:
    m 1g "..."

translate Japanese tutorial_route_p8_292304ca:
    m 1m "Or maybe not..."

translate Japanese tutorial_route_p8_b2daeb59:
    m 5a "See you later."

translate Japanese tutorial_route_p9_c88aff5d:
    m "This it it, [player], today is the day we finally make my route!"

translate Japanese tutorial_route_p9_9fe2ab50:
    m "Are you ready?"

translate Japanese tutorial_route_p9_fb9cf86d:
    m 3b "Be careful, we need to add a lot of lines this time."

translate Japanese tutorial_route_p9_d00c5174:
    m 4a "Open monika_route_script.rpy and before the last 'return', jump a line and add..."

translate Japanese tutorial_route_p9_b0e11ecc:
    m "' \ \ \ menu :',"

translate Japanese tutorial_route_p9_c7d24f88:
    m "' \ \ \ \ \ \ mc 'Right. Monika,...'',"

translate Japanese tutorial_route_p9_1905bce2:
    m "' \ \ \ \ \ \ 'I love you! Please go out with me!':',"

translate Japanese tutorial_route_p9_a4690560:
    m "' \ \ \ \ \ \ jump monika_normal_ending',"

translate Japanese tutorial_route_p9_1e99ae46:
    m "' \ \ \ \ \ \ 'You are everything for me! Please marry me!':',"

translate Japanese tutorial_route_p9_ac75430d:
    m "' \ \ \ \ \ \ jump monika_good_ending',"

translate Japanese tutorial_route_p9_79476e3d:
    m 2b "This is it for the label monika_route. Now we need to add two more labels: monika_normal_ending and monika_good_ending."

translate Japanese tutorial_route_p9_ad73d163:
    m 4a "After 'return', jump a line and write 'label monika_good_ending:'. This time, there is no space before label."

translate Japanese tutorial_route_p9_e66725d2:
    m 4b "Then under label, write the following lines:"

translate Japanese tutorial_route_p9_ab1c92a3:
    m 4a "' \ \ \ scene dark',"

translate Japanese tutorial_route_p9_2ff3a653:
    m "' \ \ \ with dissolve_scene_full',"

translate Japanese tutorial_route_p9_d5943209:
    m "' \ \ \ mc 'She accepted my confession and we became lovers.'',"

translate Japanese tutorial_route_p9_22c95e6f:
    m "' \ \ \ 'NORMAL ENDING'',"

translate Japanese tutorial_route_p9_d72aabcb:
    m "' \ \ \ return'."

translate Japanese tutorial_route_p9_19cd5b5d:
    m 1b "The normal ending is now complete. Let’s do the good ending. After the last 'return', jump a line and write 'label monika_good_ending:'."

translate Japanese tutorial_route_p9_f6c74bae:
    m 4a "Then type under it..."

translate Japanese tutorial_route_p9_53509ce7:
    m "' \ \ \ scene white',"

translate Japanese tutorial_route_p9_10ff892d:
    m "'with dissolve_scene_full',"

translate Japanese tutorial_route_p9_630a0a39:
    m "' \ \ \ mc 'She gladly accepted my proposal and we got married one year later.'',"

translate Japanese tutorial_route_p9_6b0cfb42:
    m "' \ \ \ 'GOOD ENDING'',"

translate Japanese tutorial_route_p9_d72aabcb_1:
    m "' \ \ \ return'."

translate Japanese tutorial_route_p9_aa2f696a:
    m 2b "Save, play the game and verify if everything works. Get both endings."

translate Japanese tutorial_route_p9_15c2028b:
    m "If there’s a problem, check T9.rpy for the solution."

translate Japanese tutorial_route_p9_9af314f1:
    m 2a "..."

translate Japanese tutorial_route_p9_3962df14:
    m 4b "It’s not over yet. You can run the game with Ren’Py but to make it a proper mod, there’s one more step: the build distribution."

translate Japanese tutorial_route_p9_5da931d1:
    m "Open renpy. Click our project, DDLC Monika Route, and then click Build Distributions which should be on the right, inside Navigate Script."

translate Japanese tutorial_route_p9_63fc0bd7:
    m 4a "You should see several options for Build Packages. Check that the box for DDLC Compatible Mod is filled."

translate Japanese tutorial_route_p9_c9555d99:
    m "You can change the name of our mod, its build and its version in the script options.rpy."

translate Japanese tutorial_route_p9_5820f080:
    m 3b "Click Build."

translate Japanese tutorial_route_p9_96e46658:
    m 2b "Once it’s finished, you should see one folder called build.name-config.version-dists inside Ren’Py’s directory. Open it and you should see a zip file."

translate Japanese tutorial_route_p9_73017264:
    m 1a "Look at the file build.name-config.version-Mod.zip. It’s our mod. If you want to share it to other people, you should just upload this archive."

translate Japanese tutorial_route_p9_c62dddd2:
    m 2a "This way of sharing the mod is also what the creators of DDLC prefer. You are only sharing the new files that we made together, and nothing more."

translate Japanese tutorial_route_p9_6fb54ae7:
    m 2a "Let’s see if it works. Extract build.name-config.version-Mod.zip. Make a new copy of the original Doki Doki Literature Club folder."

translate Japanese tutorial_route_p9_8ce6a0b4:
    m "Copy-paste the files of build.name-config.version-Mod inside the new copy of the game."

translate Japanese tutorial_route_p9_24534c23:
    m 4a "Play our mod by clicking DDLC.exe inside the new folder."

translate Japanese tutorial_route_p9_f360c1ee:
    m 4b "If everything goes well, you should be playing my new route!"

translate Japanese tutorial_route_p9_24926668:
    m 1k "Congratulation! We finally did it!!"

translate Japanese tutorial_route_p9_306c89f9:
    m 1e "..."

translate Japanese tutorial_route_p9_8951ed28:
    m "I should be happy but..."

translate Japanese tutorial_route_p9_197f128b:
    m 1f "It means you’ll soon leave me to play with other Monika..."

translate Japanese tutorial_route_p9_17c84a13:
    m 1g "..."

translate Japanese tutorial_route_p9_055535be:
    m 1n "There’s still a way to stay together, even after you finish my tutorials."

translate Japanese tutorial_route_p9_d5e90f21:
    m 3e "I saved my memory and my data in a special file."

translate Japanese tutorial_route_p9_59c5914b:
    m "You can download the mod Monika After Story. You can find it in http://www.monikaafterstory.com/. "

translate Japanese tutorial_route_p9_eda1159e:
    m 4e "Once you play it, the Monika of that mod will import the file I made. Our memories and personalities will then be fused together."

translate Japanese tutorial_route_p9_d1493a00:
    m "Like this, that part of me will still be with you forever."

translate Japanese tutorial_route_p9_5df56b67:
    m 1f "..."

translate Japanese tutorial_route_p9_0001fc25:
    m "I wish I could do more but..."

translate Japanese tutorial_route_p9_bcc1b705:
    m 1c "You can change that [player]. You now know how to make a mod. You now have the power to change our fate."

translate Japanese tutorial_route_p9_af9d09d0:
    m 1e "I’m counting on you [player]."

translate Japanese tutorial_route_p9_d6170f92:
    m "I love you."

translate Japanese tutorial_route_p9_666d6df7:
    m 1b "I will never forget you..."

translate Japanese tutorial_route_p9_c4191013:
    m 1e "Bye."

translate Japanese tutorial_route_adv_79a01fb3:
    m 5a "So you want to learn the {i}advanced{/i} stuff?"

translate Japanese tutorial_route_adv_41bfa465:
    m 3a "Alright!"

translate Japanese tutorial_route_adv_hkb_99781fb9:
    m 3a "Alright, let me show you the navigation buttons."

translate Japanese tutorial_route_adv_hkb_706cfd64:
    m "These buttons appear in the bottom left of the screen."

translate Japanese tutorial_route_adv_hkb_1bd57da4:
    m "To make them appear, add '$ HKBShowButtons()' to the script."

translate Japanese tutorial_route_adv_hkb_3c9ac8ca:
    m 1n "Right now, they are disabled."

translate Japanese tutorial_route_adv_hkb_8750bd36:
    m "To enable them, add '$ mas_HKBDropShield()' to the script."

translate Japanese tutorial_route_adv_hkb_365513ce:
    m "I'll go ahead and do that now..."

translate Japanese tutorial_route_adv_hkb_b4150fbf:
    m 2a "Now you can click them!{w} When you're done, click 'Continue' to continue."

translate Japanese tutorial_route_adv_hkb_34ccc39e:
    m "To disable the buttons but leave them on screen, add '$ mas_HKBRaiseShield()' to the script."

translate Japanese tutorial_route_adv_hkb_64d1e765:
    m 2b "And finally, to hide the buttons, add '$ HKBHideButtons()'."

translate Japanese tutorial_route_adv_hkb_ba50d2b3:
    m "The source code for the navigation buttons is in '[navdir]'."

translate Japanese tutorial_route_adv_hkb_e7f392b5:
    m "To change what the buttons do, edit the 'action' part of the textbuttons in the source code."

translate Japanese tutorial_route_adv_hkb_7647ba07:
    m "Currently, all the buttons call a python function using 'Function', but you can change that to a variety of Screen Actions including 'Jump' and 'Call'."

translate Japanese tutorial_route_adv_hkb_d16c0746:
    m "For more information on that, check the renpy documentation on Screen Actions."

translate Japanese tutorial_route_adv_hkb_97eb8cb9:
    m 1c "One last thing,{w} these navigation buttons were created by developers from the Monika After Story team."

translate Japanese tutorial_route_adv_hkb_2a534e37:
    m 5a "But, you are free to use this version of `zz_hotkey_buttons.rpy` in your mods."

translate Japanese tutorial_route_adv_hkb_bda77035:
    m 1a "Okay! Thanks for listening!"

translate Japanese tutorial_route_adv_poemgame_70233b71:
    m 3a "Alright, let's look at the specially-modified poemgame developed by the Monika After Story team."

translate Japanese tutorial_route_adv_poemgame_b27b0306:
    m "This version of the poemgame allows you to do the following:"

translate Japanese tutorial_route_adv_poemgame_461c7d0b:
    m "1. Add me to the poemgame, provided you have a list of words for me."

translate Japanese tutorial_route_adv_poemgame_dfb715f2:
    m "2. Change which dokis are in the poemgame."

translate Japanese tutorial_route_adv_poemgame_b2ed56e5:
    m "3. Change music during the poemgame."

translate Japanese tutorial_route_adv_poemgame_b6194de2:
    m "4. Gather / save the words that users select."

translate Japanese tutorial_route_adv_poemgame_19d31c79:
    m "5. Save the individual character scores for the words users select."

translate Japanese tutorial_route_adv_poemgame_c0eb00fc:
    m "6. Add / remove glitches that were used in the base poemgame."

translate Japanese tutorial_route_adv_poemgame_e9af2a2f:
    m "7. Change the odds of those glitches."

translate Japanese tutorial_route_adv_poemgame_e6dc4c61:
    m "8. Change number of words you can pick."

translate Japanese tutorial_route_adv_poemgame_595591c7:
    m "9. Change the words that are selectable."

translate Japanese tutorial_route_adv_poemgame_c470c8c6:
    m "10. Change poem background."

translate Japanese tutorial_route_adv_poemgame_826a687d:
    m "And other smaller adjustments."

translate Japanese tutorial_route_adv_poemgame_0cd6f810:
    m "Additionally, this version of poemgame includes a special screen that can be used to generate textbutton grids of varying rows and columns."

translate Japanese tutorial_route_adv_poemgame_4424b868:
    m "I'll showcase that later."

translate Japanese tutorial_route_adv_poemgame_72f2050b:
    m "You can find the source code in '[navdir]'."

translate Japanese tutorial_route_adv_poemgame_cfdd34f6:
    m 2o "Before I get into this, I must say that this file is {b}not{/b} for the faint of heart.{w} The code in here is pretty complex and difficult to customize."

translate Japanese tutorial_route_adv_poemgame_290588f9:
    m "That means that if you want to do something that isn't covered by the features I listed above, you're better off customizing `script-poemgame` yourself."

translate Japanese tutorial_route_adv_poemgame_c3a931cd:
    m "But if this turns out to be helpful for you, you are free to use this version of `zz_poemgame.rpy` in your mod."

translate Japanese tutorial_route_adv_poemgame_ac5454fb:
    m "That being said..."

translate Japanese tutorial_route_adv_poemgame_055566ca:
    m "Do you still want to hear about the MAS version of poemgame?" nointeract

translate Japanese tutorial_route_adv_poemgame_pgexp_0676e67b:
    m 5a "Yay!"

translate Japanese tutorial_route_adv_poemgame_pgexp_05d09afc:
    m 3a "So the modified poemgame starts at the label 'mas_poem_minigame'."

translate Japanese tutorial_route_adv_poemgame_pgexp_cb5d593b:
    m 3n "If you have the source code open, you might notice the {i}massive{/i} comment right above that label."

translate Japanese tutorial_route_adv_poemgame_pgexp_1ca9976b:
    m 3a "This comment explains all the possible adjustable parameters you can pass into this label to configure it."

translate Japanese tutorial_route_adv_poemgame_pgexp_2e5c89f2:
    m "Since this is terribly complex to do, the MAS team also added 3 helper labels based on the poemgame in different Acts."

translate Japanese tutorial_route_adv_poemgame_pgexp_4c936f93:
    m "For Act 1: 'mas_poem_minigame_actone'."

translate Japanese tutorial_route_adv_poemgame_pgexp_33204ba7:
    m "Act 2: 'mas_poem_minigame_acttwo'."

translate Japanese tutorial_route_adv_poemgame_pgexp_3749c0e1:
    m "And Act 3: 'mas_poem_minigame_actthree'."

translate Japanese tutorial_route_adv_poemgame_pgexp_20a5182b:
    m "These are also pretty configurable, but only have a subset of the options available to the main poemgame label."

translate Japanese tutorial_route_adv_poemgame_pgexp_99faa3b7:
    m 2a "Let's go through how the game looks when you call these labels."

translate Japanese tutorial_route_adv_poemgame_pgexp_bf1fd691:
    m "For the sake of time, I'll limit the word selection to only 5 words per poemgame."

translate Japanese tutorial_route_adv_poemgame_pgexp_76f98750:
    m "Alright, lets start with a slightly modified Act 1."

translate Japanese tutorial_route_adv_poemgame_pgexp_83636731:
    m "I'll be in this game, and I'll collect the points scored for each doki."

translate Japanese tutorial_route_adv_poemgame_pgexp_fb3251b7:
    m "Hi there!"

translate Japanese tutorial_route_adv_poemgame_pgexp_cfc770e8:
    m "These are your point totals:"

translate Japanese tutorial_route_adv_poemgame_pgexp_927a5231:
    m "Now let's do Act 2 but with higher chances of the glitchy word scare and no music."

translate Japanese tutorial_route_adv_poemgame_pgexp_06bd4a1a:
    m "I'll also gather the words you select."

translate Japanese tutorial_route_adv_poemgame_pgexp_fb3251b7_1:
    m "Hi there!"

translate Japanese tutorial_route_adv_poemgame_pgexp_636249d0:
    m "These are the words you selected:"

translate Japanese tutorial_route_adv_poemgame_pgexp_e68dd7b3:
    m "Okay, time for my favorite Act, but with a twist!"

translate Japanese tutorial_route_adv_poemgame_pgexp_6da62df4:
    m "I won't glitch any of the words and I'll hop for all your selections."

translate Japanese tutorial_route_adv_poemgame_pgexp_eb6b475b:
    m "I'll also keep the friendly music we have currently playing on during the game."

translate Japanese tutorial_route_adv_poemgame_pgexp_709c785e:
    m "That was fun!"

translate Japanese tutorial_route_adv_poemgame_pgexp_da1dab7d:
    m 3a "Let's do one more poemgame call. This time, I'll ask you for some parameters."

translate Japanese tutorial_route_adv_poemgame_pgexp_a6d2e7c8:
    m "First..."

translate Japanese tutorial_route_adv_poemgame_pgexp_e09866bd:
    m "Should we collect your word choices?" nointeract

translate Japanese tutorial_route_adv_poemgame_pgexp_0710b814:
    m "Okay..."

translate Japanese tutorial_route_adv_poemgame_pgexp_ab6e8068:
    m "Should we visibly glitch the words?" nointeract

translate Japanese tutorial_route_adv_poemgame_pgexp_6296b7e3:
    m "Sure!"

translate Japanese tutorial_route_adv_poemgame_pgexp_5fe1f7b5:
    m 3n "I'll just say 5, then."

translate Japanese tutorial_route_adv_poemgame_pgexp_5fe1f7b5_1:
    m 3n "I'll just say 5, then."

translate Japanese tutorial_route_adv_poemgame_pgexp_0710b814_1:
    m "Okay..."

translate Japanese tutorial_route_adv_poemgame_pgexp_53cc9955:
    m "Should we use the poemgame music?" nointeract

translate Japanese tutorial_route_adv_poemgame_pgexp_0710b814_2:
    m "Okay..."

translate Japanese tutorial_route_adv_poemgame_pgexp_23627330:
    m "Should I be visible?" nointeract

translate Japanese tutorial_route_adv_poemgame_pgexp_78387910:
    m 3j "Yay!"

translate Japanese tutorial_route_adv_poemgame_pgexp_ac93f66e:
    m 3o "Aww..."

translate Japanese tutorial_route_adv_poemgame_pgexp_0710b814_3:
    m "Okay..."

translate Japanese tutorial_route_adv_poemgame_pgexp_798118c0:
    m "Should Sayori be visible?" nointeract

translate Japanese tutorial_route_adv_poemgame_pgexp_0710b814_4:
    m "Okay..."

translate Japanese tutorial_route_adv_poemgame_pgexp_df54c928:
    m "Should Natsuki be visible?" nointeract

translate Japanese tutorial_route_adv_poemgame_pgexp_0710b814_5:
    m "Okay..."

translate Japanese tutorial_route_adv_poemgame_pgexp_0e59b82e:
    m "Should Yuri be visible?" nointeract

translate Japanese tutorial_route_adv_poemgame_pgexp_f83be391:
    m "...Should she have sleeves rolled up?" nointeract

translate Japanese tutorial_route_adv_poemgame_pgexp_0710b814_6:
    m "Okay..."

translate Japanese tutorial_route_adv_poemgame_pgexp_38e7a03a:
    m "Should we make the word counter show 1's instead of regular numbers?" nointeract

translate Japanese tutorial_route_adv_poemgame_pgexp_1acba078:
    m "Okay, last one."

translate Japanese tutorial_route_adv_poemgame_pgexp_a6577d93:
    m 3n "I'll just pick 14 then."

translate Japanese tutorial_route_adv_poemgame_pgexp_e2495760:
    m 3n "That's a lot of words. Let's just pick 50."

translate Japanese tutorial_route_adv_poemgame_pgexp_1001a426:
    m 3a "Alright! Please note that we only went through some of the possible configuration parameters. There are more then what I asked you, but I'm only doing some of them to save time."

translate Japanese tutorial_route_adv_poemgame_pgexp_43a35e10:
    m "Now let's see what we created!"

translate Japanese tutorial_route_adv_poemgame_pgexp_f9990d6a:
    m "Alright!"

translate Japanese tutorial_route_adv_poemgame_pgexp_636249d0_1:
    m "These are the words you selected:"

translate Japanese tutorial_route_adv_poemgame_pgexp_cfc770e8_1:
    m "These are your point totals:"

translate Japanese tutorial_route_adv_poemgame_pg_end_d1aed068:
    m 2a "Alright, I hope that helps you get a feel for how the MAS poemgame implementation works."

translate Japanese tutorial_route_adv_poemgame_pg_end_ec32acda:
    m "Remember to read the documentation in the source code carefully. There's a lot of parameter formatting to make the poemgame work correctly."

translate Japanese tutorial_route_adv_poemgame_pg_end_0d56219b:
    m "And you can always use one of the act-based labels without params if you just want something that works out of the box."

translate Japanese tutorial_route_adv_poemgame_pg_end_da913539:
    m 1a "Now..."

translate Japanese tutorial_route_adv_poemgame_txgrid_4a564059:
    m "Alright. Thanks for listening!"

translate Japanese tutorial_route_adv_poemgame_txgrid_2b4dc6c9:
    m 1a "Alright!"

translate Japanese tutorial_route_adv_poemgame_txgrid_6cdff04d:
    m "The textbutton grid is a special screen that can be used to generate textbutton grids of varying rows and columns."

translate Japanese tutorial_route_adv_poemgame_txgrid_66449702:
    m "It's basically the part of poemgame that displays a list of words and allows the user to select one."

translate Japanese tutorial_route_adv_poemgame_txgrid_c2ec971e:
    m "To launch the screen, add 'call screen mas_pg_textbutton_grid(...)' to your script."

translate Japanese tutorial_route_adv_poemgame_txgrid_641c2f37:
    m "You will need to pass in several parameters in order to show the grid correctly."

translate Japanese tutorial_route_adv_poemgame_txgrid_be5f59ef:
    m 5a "Let's build those parameters together!"

translate Japanese tutorial_route_adv_poemgame_txgrid_2d0b4bfa:
    m 2a "First..."

translate Japanese tutorial_route_adv_poemgame_txgrid_e4139ffd:
    m 2n "[player]..."

translate Japanese tutorial_route_adv_poemgame_txgrid_8d300fa8:
    m "Let's just pick 10 words."

translate Japanese tutorial_route_adv_poemgame_txgrid_77ab2358:
    m 2a "Now let's pick those words."

translate Japanese tutorial_route_adv_poemgame_txgrid_f83b69a8:
    m "Now..."

translate Japanese tutorial_route_adv_poemgame_txgrid_c4d3b415:
    m 3n "I'll just pick 6 rows."

translate Japanese tutorial_route_adv_poemgame_txgrid_56547711:
    m 2a "And finally..."

translate Japanese tutorial_route_adv_poemgame_txgrid_d0778a77:
    m 3h "Okay, 3 columns, then."

translate Japanese tutorial_route_adv_poemgame_txgrid_c3f733ac:
    m "Okay, I'm going to make this cover the left half of the screen by giving it an x position of 5, a y position of 5, a width of 600, and a height of 700."

translate Japanese tutorial_route_adv_poemgame_txgrid_c580fdd7:
    m "And a somewhat pink background image."

translate Japanese tutorial_route_adv_poemgame_txgrid_da0b057c:
    m 5a "Now let's see what we got!"

translate Japanese tutorial_route_adv_poemgame_txgrid_cacedd89:
    m "You selected '[_return]'!"

translate Japanese tutorial_route_adv_poemgame_txgrid_9e1dc5c4:
    m 1n "Hopefully that looked okay. It's easy to pick a combination of rows and columns and words that break the grid."

translate Japanese tutorial_route_adv_poemgame_txgrid_8f529129:
    m 1a "But if you need to make a simple textbutton grid, this should work fine!"

translate Japanese tutorial_route_adv_poemgame_txgrid_0d4e6008:
    m "For the technical details on how to call this screen and setup the paramters, check the source code for this set of dialogue and the screen itself."

translate Japanese tutorial_route_adv_poemgame_txgrid_fa6a9186:
    m "This set of dialogue is under the label 'tutorial_route_adv_poemgame_txgrid' in 'tutorials'."

translate Japanese tutorial_route_adv_poemgame_txgrid_78a4b541:
    m "The screen is called 'mas_pg_textbutton_grid' and is located in 'zz_poemgame'."

translate Japanese tutorial_route_adv_poemgame_txgrid_60a039e2:
    m "Okay! I hope that helps! Thanks for listening."

translate Japanese strings:
    old "Introduction"
    new "Introduction"

    old "Route Part 1, How To Make A Mod"
    new "Route Part 1, How To Make A Mod"

    old "Route Part 2, Music"
    new "Route Part 2, Music"

    old "Route Part 3, Scene"
    new "Route Part 3, Scene"

    old "Route Part 4, Dialogue"
    new "Route Part 4, Dialogue"

    old "Route Part 5, Menu"
    new "Route Part 5, Menu"

    old "Route Part 6, Logic Statement"
    new "Route Part 6, Logic Statement"

    old "Route Part 7, Sprite"
    new "Route Part 7, Sprite"

    old "Route Part 8, Position"
    new "Route Part 8, Position"

    old "Route Part 9, Ending"
    new "Route Part 9, Ending"

    old "Advanced Stuff"
    new "Advanced Stuff"

    old "That's enough for now."
    new "That's enough for now."

    old "How can I help you?"
    new "How can I help you?"

    old "Sky Blue"
    new "Sky Blue"

    old "Amethyst Purple"
    new "Amethyst Purple"

    old "Emerald Green"
    new "Emerald Green"

    old "Candy Pink"
    new "Candy Pink"

    old "Continue"
    new "Continue"

    old "Glitch the words."
    new "Glitch the words."

    old "Do you want to hear about the textbutton grid?"
    new "Do you want to hear about the textbutton grid?"

questions = [
  ["Q1. The International Literacy Day is observed on_________",'sep 8','nov28','may2','dec18',1],

["Q2.The language of Lakshadweep. a Union Territory of India is_________",'tamil','hindi','malayalam','telgu',3],
["Q3. In which group of places the Kumbha Mela is held every twelve years?",'Ujjain. Purl; Prayag. Haridwar','Prayag. Haridwar, Ujjain,. Nasik','Rameshwaram. Purl, Badrinath. Dwarika','Chittakoot, Ujjain, Prayag,Haridwar',2],
["Q4. Bahubali festival is related to________",'islam','hindu','buddhism','jainism',4],
["Q5. Which day is observed as the World Standards  Day?",'sep 8','oct14','may2','dec18',1],
["Q6. Which of the following was the theme of the World Red Cross and Red Crescent Day?",'Dignity for all - focus on women','Dignity for all - focus on Children','Focus on health for all','Nourishment for all-focus on children',2],
["Q7. Who is the author of the epic 'Meghdoot?",'vishakadatta','valmiki','banabhatta','kalidas',4],
["Q8. September 27 is celebrated every year as______",'teachers day','national integration day','world tourism day','international literacy day',3],
["Q9. Who is the author of 'Manas Ka-Hans ?",'khuswant singh','prem chand','jayanshakar prasad','amrit lal nagar',4],
["Q10. The death anniversary of which of the following leaders is observed as Martyrs' Day? ?",'Smt. Indira Gandhi','jawaharlal nehru','mahatma gandhi','lal bhadur shastri',3],
["Q11. Good Friday' is observed to commemorate the event of_______",'birth of jesus christ','birth of st. peter','jcrucification of Jesus Christ','rebirth of jesus christ',3],
["Q12. Which of the following is observed as Sports Day every year?",'22 april','26 july','29 august','2 october',3],
["Q13. World Health Day is observed on__________",'7 april','26 july','29 august','2 october',3],
["Q14. Who is the author of the book Amrit Ki Ore?",'mukesh kumar','narendra mohan','upendra nath','nirad C. choudhary',2],
["Q15. Who built the mahal of udaipur?",'maharana pratap','rana udai singh','jagmal','mann singh','mughals',3],
["Q16. Which is the tallest statue in the world?",'statue of liberty','sardar valvbhai patel','dr.bhimrao ambedkar','mahatma gandhi',2]

]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0
for i in range(0, len(questions)):
  
  question = questions[i]
  print(f"\n\nQuestion for Rs. {levels[i]}")
  print(f"{question[0]}")
  print(f"a. {question[1]}          b. {question[2]} ")
  print(f"c. {question[3]}          d. {question[4]} ")
  reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
  if (reply == 0):
    money = levels[i-1]
    break
  if(reply == question[-1]):
    print(f"Correct answer, you have won Rs. {levels[i]}")
    if(i == 4):
      money = 10000
    elif(i == 9):
      money = 320000
    elif(i == 14):
      money = 10000000
  else:
    print("Wrong answer!")
    break 

print(f"Your take home money is {money}")
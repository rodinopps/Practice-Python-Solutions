while True:
  p1 = input("R, P or S? ")
  p2 = input("R, P or S? ")
  
  if p1 == "S" and p2 == "P":
    print("Player 1 has won. ")
    break
  elif p1 == "S" and p2 == "R":
    print("Player 2 has won. ")
    break
  elif p1 == "S" and p2 == "S":
    print("Draw. Try again. ")

  elif p1 == "R" and p2 == "S":
    print("Player 1 has won. ")
    break
  elif p1 == "R" and p2 == "R":
    print("Draw. Try again. ")
  elif p1 == "R" and p2 == "P":
    print("Player 2 has won. ")
    break

  elif p1 == "P" and p2 == "P":
    print("Draw. Try again. ")
  elif p1 == "P" and p2 == "R":
    print("Player 1 has won. ")
    break
  elif p1 == "P" and p2 == "S":
    print("Player 2 has won. ")
    break

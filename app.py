from random import seed
from random import random
import random
PLAYER_SHOULD_SWITCH, PLAYER_SHOULD_NOT_SWITCH = (True, False)

def set_game():
  doors = [False, False, True]
  random.shuffle(doors)
  sr = random.SystemRandom()
  first_choice_index = sr.randrange(len(doors))
  first_choice = doors[first_choice_index]

  def switch_choice(first_choice, reavealed_door):
    new_choice = None
    for i, val in enumerate(doors):
      if i is not first_choice and i is not reavealed_door:
        new_choice = i
    return new_choice
  return doors, switch_choice, first_choice_index

def play(player_should_switch):
  doors, switch_choice, first_choice_index = set_game()
  win = False

  for i, val in enumerate(doors):
    if i != first_choice_index and val == False:
      reavealed_door_index = i
      break
  if (player_should_switch):
    first_choice_index = switch_choice(first_choice_index, reavealed_door_index)

  if doors[first_choice_index] == True:
    win = True
  return win

def simulate(n, player_should_switch):
  wins = 0
  losses = 0
  for i in range(n):
    result = play(player_should_switch)
    if result == True:
      wins += 1
    else:
      losses += 1
  ratio = wins/n
  return ratio

simulations = 10000

result_with_switch = simulate(simulations, PLAYER_SHOULD_SWITCH)
result_without_switch = simulate(simulations, PLAYER_SHOULD_NOT_SWITCH)

print("Result with switching: {0}%\nResult without switching: {1}".format(result_with_switch, result_without_switch))

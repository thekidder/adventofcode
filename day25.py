def transform_subject(subject, loop_size):
  val = 1
  for i in range(loop_size):
    val = transform_iteration(subject, val)
  return val

def transform_iteration(subject, val):
  val *= subject
  val = val % 20201227
  return val

def guess_loop_size(door_public_key, card_public_key):
  val = 1
  for i in range(1, 10000000):
    val = transform_iteration(7, val)
    if val == door_public_key:
      return i, None
    elif val == card_public_key:
      return None, i
  return None, None

def run(card_key, door_key):
  door_loop_size, card_loop_size = guess_loop_size(door_key, card_key)
  print(door_loop_size, card_loop_size)
  if card_loop_size is not None:
    print(transform_subject(door_key, card_loop_size))
  if door_loop_size is not None:
    print(transform_subject(card_key, door_loop_size))




# run(5764801, 17807724) # ex
run(12090988, 240583) # problem
import random

basic_notes = ['A', 'Bb', 'B', 'C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'G#']
style_list = [ 'Major', 'Minor']

# whole, whole, half, whole, whole, whole, half
major_progression = { 1: { 'key': 'Major', 'index': 0 }, # root
                      2: { 'key': 'Minor', 'index': 2 }, #   ii
                      3: { 'key': 'Minor', 'index': 4 }, #  iii
                      4: { 'key': 'Major', 'index': 5 }, #   IV
                      5: { 'key': 'Major', 'index': 7 }, #    V
                      6: { 'key': 'Minor', 'index': 9 }, #   vi
                      7: { 'key': 'Dimin', 'index': 11 } #  vii <d>
                     }

# whole, half, whole, whole, half, whole, whole
minor_progression = { 1: { 'key': 'Minor', 'index': 0 },
                      2: { 'key': 'Dimin', 'index': 2 },
                      3: { 'key': 'Major', 'index': 3 },
                      4: { 'key': 'Minor', 'index': 5 },
                      5: { 'key': 'Major', 'index': 7 },
                      6: { 'key': 'Major', 'index': 8 },
                      7: { 'key': 'Major', 'index': 10}
                    }

def choose_root():
  return random.choice(basic_notes)

def choose_style():
  return random.choice(style_list)

def make_numerical_prog():
  chord_set = set()
  while len(chord_set) < 3:
    chord_set.add(random.randint(2,7))
  chord_prog = list(chord_set)
  random.shuffle(chord_prog)
  chord_prog.insert(0, 1)
  return chord_prog

def make_new(a_list, root):
  index = ''
  try:
    index = basic_notes.index(root)
  except ValueError as e:
    print('index fail')
    exit()

  a_list = a_list[index:] + a_list[0:index]
  return(a_list)


def make_progression():
  style = choose_style()
  root = choose_root()
  numerical_prog = make_numerical_prog()

  result = f'The key is in {root} {style}.\n'
  result += f'The chord progression is as follows:\n'
  notes = make_new(basic_notes, root)

  if style == 'Major':
    for num in numerical_prog:
      result += f"{notes[major_progression[num]['index']]} {major_progression[num]['key']} "
  else:
    for num in numerical_prog:
      result += f"{notes[minor_progression[num]['index']]} {minor_progression[num]['key']} "

  print(result)

if __name__ == '__main__':
  make_progression()

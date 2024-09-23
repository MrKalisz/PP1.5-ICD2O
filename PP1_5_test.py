import os.path
import sys
import PP1_5

def test_q1_1(capsys):

  try:
    exists = os.path.exists("PP1_5.py")
    assert exists
  except:
    sys.exit()

  input_values = [5]
  
  def mock_input(s):
    print(s, end='')
    return input_values.pop(0)
  PP1_5.input = mock_input
  
  PP1_5.q1()
  captured = capsys.readouterr()
  assert captured.out == "Input an integer: 8\n"

def test_q1_2(capsys):

  try:
    exists = os.path.exists("PP1_5.py")
    assert exists
  except:
    sys.exit()

  input_values = [15]
  
  def mock_input(s):
    print(s, end='')
    return input_values.pop(0)
  PP1_5.input = mock_input
  
  PP1_5.q1()
  captured = capsys.readouterr()
  assert captured.out == "Input an integer: 18\n"

def test_q2_1(capsys):

  try:
    exists = os.path.exists("PP1_5.py")
    assert exists
  except:
    sys.exit()

  input_values = [123.2]
  
  def mock_input(s):
    print(s, end='')
    return input_values.pop(0)
  PP1_5.input = mock_input

  PP1_5.q2()
  captured = capsys.readouterr()
  assert captured.out == "Input a number: 125.24\n"

def test_q2_2(capsys):

  try:
    exists = os.path.exists("PP1_5.py")
    assert exists
  except:
    sys.exit()

  input_values = [1]
  
  def mock_input(s):
    print(s, end='')
    return input_values.pop(0)
  PP1_5.input = mock_input

  PP1_5.q2()
  captured = capsys.readouterr()
  assert captured.out == "Input a number: 16.0\n"

def test_q3_1(capsys):

  try:
    exists = os.path.exists("PP1_5.py")
    assert exists
  except:
    sys.exit()

  input_values = [15.2]
  
  def mock_input(s):
    print(s, end='')
    return input_values.pop(0)
  PP1_5.input = mock_input

  PP1_5.q3()
  captured = capsys.readouterr()
  assert captured.out == "Input a radius: 725.4656\n"

def test_q3_2(capsys):

  try:
    exists = os.path.exists("PP1_5.py")
    assert exists
  except:
    sys.exit()

  input_values = [5]
  
  def mock_input(s):
    print(s, end='')
    return input_values.pop(0)
  PP1_5.input = mock_input

  PP1_5.q3()
  captured = capsys.readouterr()
  assert captured.out == "Input a radius: 78.5\n"

def test_q4_1(capsys):

  try:
    exists = os.path.exists("PP1_5.py")
    assert exists
  except:
    sys.exit()

  input_values = [32.2]
  
  def mock_input(s):
    print(s, end='')
    return input_values.pop(0)
  PP1_5.input = mock_input

  PP1_5.q4()
  captured = capsys.readouterr()
  assert captured.out == "Input a number: 386\n"

def test_q4_2(capsys):

  try:
    exists = os.path.exists("PP1_5.py")
    assert exists
  except:
    sys.exit()

  input_values = [0.05]
  
  def mock_input(s):
    print(s, end='')
    return input_values.pop(0)
  PP1_5.input = mock_input

  PP1_5.q4()
  captured = capsys.readouterr()
  assert captured.out == "Input a number: 0\n"

def test_q5_1(capsys):

  try:
    exists = os.path.exists("PP1_5.py")
    assert exists
  except:
    sys.exit()

  input_values = [10]
  
  def mock_input(s):
    print(s, end='')
    return input_values.pop(0)
  PP1_5.input = mock_input

  PP1_5.q5()
  captured = capsys.readouterr()
  assert captured.out == "Input an integer: Your number + 5 is 15\n"

def test_q5_2(capsys):

  try:
    exists = os.path.exists("PP1_5.py")
    assert exists
  except:
    sys.exit()

  input_values = [-5]
  
  def mock_input(s):
    print(s, end='')
    return input_values.pop(0)
  PP1_5.input = mock_input


  PP1_5.q5()
  captured = capsys.readouterr()
  assert captured.out == "Input an integer: Your number + 5 is 0\n"

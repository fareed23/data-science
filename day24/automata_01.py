{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Input string rejected\n"
     ]
    }
   ],
   "source": [
    "states = ['q0', 'q1', 'q2']\n",
    "\n",
    "def accept_re1(input_str):\n",
    "  \n",
    "  current_state = 'q0'\n",
    "  \n",
    "  for symbol in input_str:\n",
    "    if current_state == 'q0':\n",
    "      if symbol == '0':\n",
    "        current_state = 'q1'\n",
    "      else:\n",
    "        return False\n",
    "\n",
    "    elif current_state == 'q1':\n",
    "      if symbol == '.':\n",
    "        current_state = 'q2'\n",
    "      else:\n",
    "        return False\n",
    "\n",
    "    elif current_state == 'q2':\n",
    "      if symbol in ['0', '1']:\n",
    "        current_state = 'q2'\n",
    "      else:\n",
    "        return False\n",
    "\n",
    "  return current_state == 'q2'\n",
    "\n",
    "input_str = input(\"Enter input string: \")\n",
    "if accept_re1(input_str):\n",
    "  print(\"Input string accepted\") \n",
    "else:\n",
    "  print(\"Input string rejected\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

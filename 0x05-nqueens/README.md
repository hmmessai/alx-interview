# 0x05. N Queens

The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.

Usage:
- nqueens N
- If the user called the program with the wrong number of arguments, prints Usage: nqueens N, followed by a new line, and exit with the status 1
- where N must be an integer greater or equal to 4
- If N is not an integer, prints N must be a number, followed by a new line, and exits with the status 1
- If N is smaller than 4, prints N must be at least 4, followed by a new line, and exits with the status 1
- The program prints every possible solution to the problem

Format: 
```
	ubuntu@ubuntu:~/0x05-nqueens$ ./0-nqueens.py 4
	
	[[0, 1], [1, 3], [2, 0], [3, 2]]
	[[0, 2], [1, 0], [2, 3], [3, 1]]
```

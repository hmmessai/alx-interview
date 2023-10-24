# 0x04. UTF-8 Validation

UTF-8 is a variable-length character encoding standard used for electronic communication. Defined by the Unicode Standard, the name is derived from Unicode (or Universal Coded Character Set) Transformation Format – 8-bit.

UTF-8 is capable of encoding all 1,112,064 valid character code points in Unicode using one to four one-byte (8-bit) code units. Code points with lower numerical values, which tend to occur more frequently, are encoded using fewer bytes. It was designed for backward compatibility with ASCII: the first 128 characters of Unicode, which correspond one-to-one with ASCII, are encoded using a single byte with the same binary value as ASCII, so that valid ASCII text is valid UTF-8-encoded Unicode as well.

In this project I tried to come up with the solution of the utf8 validation problem and create a method that determines if a given data set represents a valid utf-8 encoding.

### Files

- [0-validate_utf8.py](./0-validate_utf8.py): Contains a method that checks if a given data(list of numbers which are supposed to represent utf8 character) is a valid UTF-8 encoding or not.
	- hello

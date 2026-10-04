# Password Strength Checker

A Python tool that rates password strength using entropy, character variety,
pattern detection, common-word detection and a common-password list.

## Features
- Length and character-type checks
- Entropy calculation (bits)
- Detects repeating characters, low variety and keyboard/number sequences
- Detects common words with leetspeak tricks (P@ssw0rd, Welcome@2024)
- Checks against the 10k most common passwords (optional file)

## How to run
python checker.py
python test_passwords.py

## Privacy
Passwords are never stored or sent anywhere. Use dummy passwords only.

## Bugs I found and fixed
- "aaaaaaaaaaaa" was rated Medium. Fixed by penalizing low character variety.
- "P@ssw0rd" and "Welcome@2024" were rated too high. Fixed with
  leetspeak normalization and a common-words check.
- Test results went from 12/14 to 14/14.

## Limitations / future work
- Entropy is an estimate, not a guarantee
- The common-words list is small
- Could add a breach check (Have I Been Pwned API)

## What I learned
I learned about the word "ENTROPY" that means its about both strengh, length and character variety. Ater that 
2) Bug: aaaaaaaaaaaa took medium rating, because tool doesnot see the variety. Also I put unique character to clear this mistake.
3) Pattern attacks: P@ssw0rd and Welcome@2024 according to mathematics its seem to be strong but from the attackers POV its not. They know this trick before we know. 
4) Testing: When I test these 14 passwords then I checked together with the help of AI the bugs seems immedietly (12/14 to 14/14).
5) Design: Put both files LOGIC (checker.py) and TESTING in different files so that I don't write the code again.
6) Git: Install this GIT by my own and do everything individually at the very first time.
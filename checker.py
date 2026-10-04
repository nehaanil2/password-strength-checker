import math
import os
import re
from getpass import getpass


def load_common_passwords(path="10k-most-common.txt"):
    if not os.path.exists(path):
        return set()
    with open(path, encoding="utf-8", errors="ignore") as f:
        return {line.strip().lower() for line in f if line.strip()}

COMMON = load_common_passwords()


def calculate_entropy(password):
    pool = 0
    if re.search(r"[a-z]", password):
        pool += 26
    if re.search(r"[A-Z]", password):
        pool += 26
    if re.search(r"\d", password):
        pool += 10
    if re.search(r"[^a-zA-Z0-9]", password):
        pool += 32
    if pool == 0:
        return 0.0
    return len(password) * math.log2(pool)


def has_repeating(password):
    return bool(re.search(r"(.)\1{2,}", password))


def has_sequence(password):
    rows = ["abcdefghijklmnopqrstuvwxyz", "0123456789",
            "qwertyuiop", "asdfghjkl", "zxcvbnm"]
    p = password.lower()
    for row in rows:
        for i in range(len(row) - 3):
            chunk = row[i:i + 4]
            if chunk in p or chunk[::-1] in p:
                return True
    return False


def check_password(password):
    feedback = []
    entropy = calculate_entropy(password)

    if len(password) < 8:
        feedback.append("Kam se kam 8 characters rakho (12+ better hai).")
    elif len(password) < 12:
        feedback.append("12 ya usse zyada characters rakho.")

    if not re.search(r"[a-z]", password):
        feedback.append("Lowercase letters add karo.")
    if not re.search(r"[A-Z]", password):
        feedback.append("Uppercase letters add karo.")
    if not re.search(r"\d", password):
        feedback.append("Numbers add karo.")
    if not re.search(r"[^a-zA-Z0-9]", password):
        feedback.append("Special symbol (@, #, !) add karo.")
    if len(set(password)) < len(password) / 2:
        entropy -= 15
        feedback.append("Bahut kam unique characters hain, variety badhao.")
    if has_repeating(password):
        entropy -= 10
        feedback.append("Repeating characters (aaa, 111) avoid karo.")
    if has_sequence(password):
        entropy -= 10
        feedback.append("Sequences (1234, abcd, qwerty) avoid karo.")
    if password.lower() in COMMON:
        entropy = min(entropy, 10)
        feedback.append("Ye common passwords list mein hai! Bilkul use mat karo.")

    entropy = max(entropy, 0)

    if entropy < 40:
        rating = "Weak"
    elif entropy < 60:
        rating = "Medium"
    else:
        rating = "Strong"

    return {"rating": rating, "entropy": round(entropy, 1), "feedback": feedback}


if __name__ == "__main__":
    pw = getpass("Password daalo (dummy password use karo): ")
    result = check_password(pw)
    print(f"\nRating : {result['rating']}")
    print(f"Entropy: {result['entropy']} bits")
    for tip in result["feedback"]:
        print(f" - {tip}")

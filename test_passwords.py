from checker import check_password

# (password, jo rating honi chahiye)
TESTS = [
    ("123456", "Weak"),
    ("password", "Weak"),
    ("abc", "Weak"),
    ("qwerty123", "Weak"),
    ("abcd1234", "Weak"),
    ("11111111", "Weak"),
    ("aaaaaaaaaaaa", "Weak"),
    ("P@ssw0rd", "Weak"),
    ("Hello123", "Medium"),
    ("Summer2024", "Medium"),
    ("Welcome@2024", "Medium"),
    ("Zx9#kLm2$vQp7!", "Strong"),
    ("MyDog$Loves2Run!", "Strong"),
    ("correcthorsebatterystaple", "Strong"),
]

print(f"{'Password':<28}{'Expected':<10}{'Got':<10}{'Entropy':<10}Status")
print("-" * 68)

passed = 0
for pw, expected in TESTS:
    r = check_password(pw)
    ok = r["rating"] == expected
    passed += ok
    status = "OK" if ok else "MISMATCH"
    print(f"{pw:<28}{expected:<10}{r['rating']:<10}{r['entropy']:<10}{status}")

print(f"\n{passed}/{len(TESTS)} tests pass hue")
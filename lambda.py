
def increment(x):
    return x + 1

print(f"",increment(5))


# lambda creation:
increment_v2 = lambda x : x + 1

print(increment_v2(10))


full_name = lambda name, last_name: f"Champ's name: '{name} {last_name}'"

print(full_name("Leonel", "Messi"))
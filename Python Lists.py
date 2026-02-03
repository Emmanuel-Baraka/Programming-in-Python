#EMMANUEL BARAKA
# BSCIT-05-0113/2024
names = []
unique_names = []

# Collecting names
while True:
    entry = input("Enter a name (type 'stop' to end): ").strip()
    if entry.lower() == 'stop':
        break
    names.append(entry)

# Removing duplicates manually
for name in names:
    if name not in unique_names:
        unique_names.append(name)

# Sort the final list
unique_names.sort()

print(f"Total entered: {len(names)}")
print(f"Final sorted list: {unique_names}")

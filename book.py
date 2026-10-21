import json, csv


books = [{"title": f"B{i}", "author": f"A{i}", "genre": "Sci" if i % 2 == 0 else "Fic", "year": 2000 + i} for i in range(1, 16)]
json.dump(books, open("lib.json", "w"))
data = json.load(open("lib.json"))


fiction = [b for b in data if b["genre"] == "Fic"]
counts = {"Sci": sum(1 for b in data if b["genre"] == "Sci"), "Fic": sum(1 for b in data if b["genre"] == "Fic")}


writer = csv.writer(open("catalogue.csv", "w", newline=""))
writer.writerow(["title", "author", "genre", "year"])
writer.writerows(sorted([list(b.values()) for b in data], key=lambda x: x[3]))

print(counts)


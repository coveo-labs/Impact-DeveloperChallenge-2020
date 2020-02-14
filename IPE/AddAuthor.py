import random

authorfield="author"

people=["Eric Stoltz",
"Alex Winter",
"Cathy Schulman",
"Alice Trueman",
"Evan Glodell",
"Jon Keeyes",
"Christopher Ray",
"Malik Barnhardt",
"Ash Christian",
"Michael Lindgren",
"Tony Randel",
"Ted Field",
"Barbie Castro",
"Paulo Branco",
"Karan Johar",
"Peter Bose",
"Jonas Allen",
"Douglas Urbanski",
"Allan Loeb",
"Priyanka Chopra",
"Neal H. Moritz",
"Joe Roth",
"Vin Diesel",
"Ram Charan",
"Roger Corman",
"Arthur Harari",
"James Arama",
"Patrick Kong",
"Sophia Paul",
"Elijah Wood",
"Ashley Springer",
"Charles Band",
"Courtney Solomon",
"Peter Bergen",
"Pharrell Williams"]

authorname=''.join(map(str,random.sample(people,  1)))

log('Author set to: '+authorname)

document.add_meta_data({
        "author": authorname
    })

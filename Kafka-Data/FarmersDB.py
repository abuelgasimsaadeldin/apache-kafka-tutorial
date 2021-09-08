import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd="skymind",
    database="farmers")

mycursor = db.cursor()

# mycursor.execute("CREATE DATABASE farmers")

data = [("Jordan", "0162360942", "jordan@gmail.com", "Penang", "jordanfarm", "wheat"),
        ("James", "0162460962", "jam@gmail.com", "Sabah", "jamfarm", "orange"),
        ("Hellen", "016236242", "hel@gmail.com", "Sarawak", "helfarm", "apple"),
        ("Jorge", "0162362342", "jor@gmail.com", "Selangor", "jorfarm", "grape"),
        ("Alien", "0162310942", "alien@gmail.com", "Terengganu", "alienfarm", "banana"),
        ("Baboo", "0162360942", "bab@gmail.com", "Kota Kinabalu", "babfarm", "strawberry"),
        ("Holls", "0162330942", "hol@gmail.com", "Kuching", "holfarm", "mango"),
        ("Jennifer", "0132360942", "jen@gmail.com", "Shah Alam", "jenfarm", "honey"),
        ("Ali", "0162360842", "ali@gmail.com", "Terengganu", "alifarm", "comb"),
        ("Zack", "0162399942", "zac@gmail.com", "Johor", "zacfarm", "wheat"),
        ("Drake", "0162550942", "drake@gmail.com", "Kedah", "drakefarm", "marshmallow"),
        ("Josh", "0162360332", "josh@gmail.com", "Kelantan", "joshfarm", "grapes"),
        ("Mans", "0162362242", "mans@gmail.com", "Malacca", "mansfarm", "strawberry"),
        ("Mus", "0162360911", "mus@gmail.com", "Negeri Sembilan", "musfarm", "mushroom"),
        ("Muh", "0162360332", "muhd@gmail.com", "Pahang", "muhdfarm", "cannabis"),
        ("Bash", "0162388942", "bash@gmail.com", "Penang", "bashfarm", "grapes"),
        ("Cat", "0162440942", "cat@gmail.com", "Perak", "catfarm", "durian"),
        ("Dog", "0162363542", "dog@gmail.com", "Perlis", "dogfarm", "mangosteen"),
        ("Hassan", "0162320942", "has@gmail.com", "Sabah", "hasfarm", "banana"),
        ("Jim", "0162360966", "jim@gmail.com", "Sarawak", "jimfarm", "apple"),
        ("Zakari", "0162360942", "zak@gmail.com", "Slangor", "zakfarm", "starfruit"),
        ("Zul", "0162360972", "zul@gmail.com", "Terengganu", "zulfarm", "orange"),
        ("Reem", "0162363942", "reem@gmail.com", "Penang", "reemfarm", "honeycomb"),
        ("Jelly", "0162370942", "jel@gmail.com", "Perak", "jelfarm", "vegetables"),
        ("Squid", "0162369942", "squi@gmail.com", "Perlis", "squifarm", "lettuce"),
        ("Sharifah", "0163360942", "sharif@gmail.com", "Sabah", "shariffarm", "starfruit"),
        ("Zulkifli", "0162460942", "zulkif@gmail.com", "Sarawak", "zulkiffarm", "rambutan"),
        ("Ahmad", "0162360972", "ahm@gmail.com", "Selangor", "ahmfarm", "mango"),
        ("Honda", "0162360922", "hond@gmail.com", "Terengganu", "hondfarm", "wheat"),
        ("Imran", "0162360982", "imran@gmail.com", "Pahang", "imranfarm", "banana"),
        ("Saleh", "0162360949", "sal@gmail.com", "Negeri Sembilan", "salfarm", "marshmallow"),
        ("Fathi", "0162360944", "fathi@gmail.com", "Malacca", "fathifarm", "lettuce"),
        ("Jimmy", "0162360942", "jim@gmail.com", "Kelantan", "jimfarm", "sunflower"),
        ("Mike", "0162360946", "mike@gmail.com", "Kedah", "mikefarm", "durian"),
        ("London", "0162360972", "lond@gmail.com", "Johor", "londfarm", "apple"),
        ("Fox", "0162360941", "fox@gmail.com", "Terengganu", "foxfarm", "honey"),
        ("Heyman", "0162320942", "heey@gmail.com", "Selangor","heeyfarm", "wheat"),
        ("Watida", "0162363942", "wat@gmail.com", "Sarawak", "watfarm", "mangosteen"),
        ("Summayah", "0162340942", "sum@gmail.com", "Sabah", "sumfarm", "lettuce"),
        ("Ala", "0162360945", "ala@gmail.com", "Perlis", "alafarm", "cucumber"),
        ("Alice", "0162360947", "alice@gmail.com", "Perak", "alicefarm", "coconat"),
        ("Amanda", "0162360842", "amanda@gmail.com", "Penang", "amandafarm", "wheat"),
        ("Jennifer", "0162369942", "jen@gmail.com", "Pahang", "jenfarm", "strawberry"),
        ("Muhammad", "0162100942", "muh@gmail.com", "Negeri Sembilan","muhfarm", "mushroom"),
        ("Fatih", "0162361142", "fatih@gmail.com", "Malacca", "fatihfarm", "tomato"),
        ("Bobby", "0162312942", "bob@gmail.com", "Kelantan", "bobfarm", "yoghurt"),
        ("Michael", "0162313942", "mich@gmail.com", "Kedah", "michfarm", "mushroom"),
        ("Sum", "0162360142", "sum@gmail.com", "Johor", "sumfarm", "mango"),
        ("Jalal", "0162160942", "jal@gmail.com", "Penang", "jalfarm", "durian"),
        ("Peterson", "0162200942", "pet@gmail.com", "Selangor", "petfarm", "cannabis")]

# mycursor.execute("CREATE TABLE farmers(farmerID int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), phone INT UNSIGNED, email VARCHAR(50), address VARCHAR(50), farm VARCHAR(50), crops VARCHAR(50))")

# mycursor.executemany("INSERT INTO farmers(name, phone, email, address, farm, crops) VALUES (%s,%s,%s,%s,%s,%s)", data)

# db.commit()

mycursor.execute("SELECT * FROM farmers")

# mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)
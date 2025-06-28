import random
playlists = {
    "romantic": [
        ("Tum Mile", "Pritam"),
        ("Raabta", "Arijit Singh"),
        ("Tera Ban Jaunga", "Akhil Sachdeva"),
        ("Tujh Mein Rab Dikhta Hai", "Roop Kumar Rathod"),
        ("Pee Loon", "Mohit Chauhan"),
        ("Shayad", "Arijit Singh"),
        ("Tum Se Hi", "Mohit Chauhan"),
        ("Jeene Laga Hoon", "Atif Aslam"),
        ("Bekhayali", "Sachet–Parampara"),
        ("Dil Diyan Gallan", "Atif Aslam"),
        ("Kaun Tujhe", "Palak Muchhal"),
        ("Janam Janam", "Arijit Singh"),
        ("Hasi Ban Gaye", "Ami Mishra"),
        ("Sun Saathiya", "Priya Saraiya"),
        ("Raat Bhar", "Arijit Singh"),
        ("Muskurane", "Arijit Singh"),
        ("Pal", "Arijit Singh"),
        ("Hamari Adhuri Kahani", "Arijit Singh"),
        ("Gerua", "Arijit Singh"),
        ("Zaalima", "Arijit Singh")
    ],
    "sad": [
        ("Channa Mereya", "Arijit Singh"),
        ("Tujhe Kitna Chahne Lage", "Arijit Singh"),
        ("Agar Tum Saath Ho", "Alka Yagnik, Arijit Singh"),
        ("Phir Le Aaya Dil", "Rekha Bhardwaj"),
        ("Tadap Tadap", "KK"),
        ("Humdard", "Arijit Singh"),
        ("Kal Ho Naa Ho", "Sonu Nigam"),
        ("Kabira", "Tochi Raina"),
        ("Bhula Dena", "Mustafa Zahid"),
        ("Judaai", "Arijit Singh"),
        ("Yaad Piya Ki Aane Lagi", "Neha Kakkar"),
        ("Hamari Adhuri Kahani", "Arijit Singh"),
        ("Woh Lamhe Woh Baatein", "Atif Aslam"),
        ("Main Rahoon Ya Na Rahoon", "Armaan Malik"),
        ("Tujhse Naraz Nahi Zindagi", "Lata Mangeshkar"),
        ("Zaroori Tha", "Rahat Fateh Ali Khan"),
        ("Tera Yaar Hoon Main", "Arijit Singh"),
        ("Mann Bharrya", "B Praak"),
        ("Teri Mitti", "B Praak"),
        ("Darmiyaan", "Shafqat Amanat Ali")
    ],
    "party": [
        ("Kala Chashma", "Badshah"),
        ("Nashe Si Chadh Gayi", "Arijit Singh"),
        ("Kar Gayi Chull", "Badshah"),
        ("Bom Diggy Diggy", "Zack Knight"),
        ("Aankh Marey", "Neha Kakkar"),
        ("London Thumakda", "Labh Janjua"),
        ("High Rated Gabru", "Guru Randhawa"),
        ("Saturday Saturday", "Indeep Bakshi"),
        ("Dil Chori", "Yo Yo Honey Singh"),
        ("Morni Banke", "Guru Randhawa"),
        ("Abhi Toh Party Shuru Hui Hai", "Badshah"),
        ("Tamma Tamma Again", "Badshah"),
        ("She Move It Like", "Badshah"),
        ("Naach Meri Rani", "Guru Randhawa"),
        ("Lungi Dance", "Yo Yo Honey Singh"),
        ("DJ Waley Babu", "Badshah"),
        ("Proper Patola", "Diljit Dosanjh"),
        ("Urvashi", "Yo Yo Honey Singh"),
        ("Gallan Goodiyan", "Various Artists"),
        ("The Breakup Song", "Arijit Singh")
    ],
    "lofi": [
        ("Tera Zikr (LoFi)", "Darshan Raval"),
        ("Choo Lo (LoFi)", "The Local Train"),
        ("Safar (LoFi)", "Mohit Chauhan"),
        ("Tum Ho (LoFi)", "Mohit Chauhan"),
        ("Ek Tarfa (LoFi)", "Darshan Raval"),
        ("Kesariya (LoFi)", "Arijit Singh"),
        ("Aabaad Barbaad (LoFi)", "Arijit Singh"),
        ("Rihaayi De (LoFi)", "A R Rahman"),
        ("Tere Bina (LoFi)", "AR Rahman"),
        ("Kya Mujhe Pyar Hai (LoFi)", "KK"),
        ("Tera Ban Jaunga (LoFi)", "Lo-fi Flip"),
        ("Phir Mohabbat (LoFi)", "Lo-fi Touch"),
        ("Apna Bana Le (LoFi)", "Lo-fi India"),
        ("Raabta (LoFi)", "Lo-fi Remix"),
        ("Mann Mera (LoFi)", "Gajendra Verma"),
        ("Zaroori Tha (LoFi)", "Lo-fi India"),
        ("Dil Diyan Gallan (LoFi)", "Lo-fi Edition"),
        ("Channa Mereya (LoFi)", "Lo-fi India"),
        ("Iktara (LoFi)", "Lo-fi Dreams"),
        ("Shayad (LoFi)", "Lo-fi India")
    ],
    "sufi_fusion": [
        ("Kun Faya Kun", "AR Rahman"),
        ("Tera Yaar Hoon Main", "Arijit Singh"),
        ("Maula Mere Maula", "Roop Kumar Rathod"),
        ("Mora Saiyaan", "Fuzön"),
        ("Khwaja Mere Khwaja", "AR Rahman"),
        ("Tu Jaane Na", "Atif Aslam"),
        ("Tose Naina", "Arijit Singh"),
        ("Iktara", "Kavita Seth"),
        ("Alvida", "KK"),
        ("Yeh Honsla", "Shafqat Amanat Ali"),
        ("Saiyaan", "Kailash Kher"),
        ("Teri Deewani", "Kailash Kher"),
        ("Piya Re", "Aalap Desai"),
        ("Allah Ke Bande", "Kailash Kher"),
        ("Aarambh Hai Prachand", "Piyush Mishra"),
        ("Rabba", "Kailash Kher"),
        ("Noor E Khuda", "Adnan Sami"),
        ("Ali Maula", "Salim-Sulaiman"),
        ("O Re Piya", "Rahat Fateh Ali Khan"),
        ("Madari", "Vishal Dadlani & Sonu Kakkar")
    ]
}

# Quiz: Each answer points to one vibe
questions = [
    {
        "q": "1. Which one are you more likely to play on a lonely night?",
        "options": {
            "a": ("Channa Mereya", "sad"),
            "b": ("Kun Faya Kun", "sufi_fusion"),
            "c": ("Tum Mile", "romantic"),
            "d": ("Tera Zikr (LoFi)", "lofi")
        }
    },
    {
        "q": "2. You’re at a wedding. What’s your jam?",
        "options": {
            "a": ("London Thumakda", "party"),
            "b": ("Morni Banke", "party"),
            "c": ("Tujh Mein Rab Dikhta Hai", "romantic"),
            "d": ("Yeh Honsla", "sufi_fusion")
        }
    },
    {
        "q": "3. Pick a song to cry in the rain to:",
        "options": {
            "a": ("Agar Tum Saath Ho", "sad"),
            "b": ("Tum Ho (LoFi)", "lofi"),
            "c": ("Kal Ho Naa Ho", "sad"),
            "d": ("Kabira", "sad")
        }
    },
    {
        "q": "4. Choose a chill weekend song:",
        "options": {
            "a": ("Choo Lo (LoFi)", "lofi"),
            "b": ("Iktara", "sufi_fusion"),
            "c": ("Bekhayali", "romantic"),
            "d": ("Kar Gayi Chull", "party")
        }
    },
    {
        "q": "5. What’s your go-to genre?",
        "options": {
            "a": ("Sufi + fusion", "sufi_fusion"),
            "b": ("Bollywood romance", "romantic"),
            "c": ("Dard bhare geet", "sad"),
            "d": ("Party banger", "party")
        }
    }
]

def take_quiz():
    print("\n🎶 Desi Vibe Quiz — Pick a, b, c or d\n")
    scores = {}
    answered_songs = set()

    for q in questions:
        print(q["q"])
        for key, (name, _) in q["options"].items():
            print(f"  {key}) {name}")
        ans = input("Your choice: ").strip().lower()

        if ans in q["options"]:
            song_name, vibe = q["options"][ans]
            scores[vibe] = scores.get(vibe, 0) + 1
            answered_songs.add(song_name)
        else:
            print("Skipped invalid input.")

    if not scores:
        print("\nNo valid answers given. Try again!")
        exit()

    # Get top vibe
    top_vibe = max(scores, key=scores.get)
    return top_vibe, answered_songs

def show_playlist(vibe, answered_songs):
    print(f"\n🎧 Your Hindi Music Vibe: {vibe.replace('_', ' ').title()}")
    print("🔥 Recommended Playlist:\n")

    available_songs = [s for s in playlists.get(vibe, []) if s[0] not in answered_songs]
    if not available_songs:
        print("No more songs available excluding answers.")
        return

    sampled = random.sample(available_songs, min(10, len(available_songs)))
    for song, artist in sampled:
        print(f"- {song} by {artist}")

    rating = input("\n📅 Rate this playlist out of 10: ").strip()
    try:
        rating = int(rating)
        if rating < 5:
            print("\n🚀 Improving your vibe score for better suggestions next time!")
            scores = {v: 0 for v in playlists.keys()}
            for song in answered_songs:
                for category, songs in playlists.items():
                    if any(song == s[0] for s in songs):
                        scores[category] -= 1
            previous_vibes = set()
            while True:
                new_vibe = max(scores, key=scores.get)
                if new_vibe in previous_vibes:
                    print("\n❌ No better vibe could be determined.")
                    break
                previous_vibes.add(new_vibe)
                print(f"\n🤖 Recalculating your vibe... New vibe: {new_vibe.title()}")
                show_playlist(new_vibe, answered_songs)
                again = input("\nWould you like to rate and regenerate again? (y/n): ").strip().lower()
                if again != 'y':
                    break
                rating = input("\n📅 Rate this new playlist out of 10: ").strip()
                try:
                    rating = int(rating)
                    if rating >= 5:
                        break
                except ValueError:
                    break
    except ValueError:
        print("Invalid rating input. Skipping feedback.")

if __name__ == "__main__":
    vibe, answered = take_quiz()
    show_playlist(vibe, answered)

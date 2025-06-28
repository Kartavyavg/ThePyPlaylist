# 🎶 The PyPlaylist Recommendation Model

A Python-based Hindi song recommendation system that uses a simple quiz to understand your current mood and generate a personalized playlist. This project brings together emotion-driven logic and music curation in a clean terminal interface.

---

## 📌 Features

* 🧠 **Mood-Based Quiz**: 5 curated questions to determine your vibe.
* 🎧 **Genre Mapping**: Includes 5 core vibes—romantic, sad, party, lofi, sufi-fusion.
* 🔁 **Rating Loop**: Users can rate the playlist. If unsatisfied (<5), the model recalibrates and shows a new vibe.
* 🎲 **Smart Playlist Generator**: Excludes already suggested songs to keep recommendations fresh.
* 🎶 **Handpicked Hindi Songs**: Each vibe contains 20+ real Hindi tracks with artists.
* 🧹 **Lightweight**: Single-file `.py` script, no external dependencies required.

---

## 🛠️ How It Works

1. **User takes a quiz** with MCQ-style questions.
2. Each answer points to a vibe (like 'sad' or 'party').
3. Scores are tallied to determine the dominant vibe.
4. A playlist of 10 unseen songs from that vibe is shown.
5. User rates the playlist:

   * If score >= 5: session ends.
   * If score < 5: playlist is improved with alternative vibe suggestions.

---

## 🧪 Example Output

```bash
🎶 Desi Vibe Quiz — Pick a, b, c or d

1. Which one are you more likely to play on a lonely night?
  a) Channa Mereya
  b) Kun Faya Kun
  c) Tum Mile
  d) Tera Zikr (LoFi)
...

🎧 Your Hindi Music Vibe: Sad
🔥 Recommended Playlist:
- Agar Tum Saath Ho by Alka Yagnik, Arijit Singh
- Judaai by Arijit Singh
...

📅 Rate this playlist out of 10: 4
🚀 Improving your vibe score for better suggestions next time!
🤖 Recalculating your vibe... New vibe: Lofi
```

---

## 🧱 Tech Stack

* Python 3.x
* Standard Library Only

---

## ⚠️ Limitations

* ❌ Not real-time or ML-based — static rule-based logic.
* ❌ Song dataset is manually curated (expandable though).
* ❌ No GUI or web interface yet.
* ❌ Quiz responses can skew results with random input.

---

## 📦 Future Improvements

* 🧠 Add NLP-based mood detection from text input.
* 🌐 Integrate Spotify API or YouTube Music API.
* 📊 Use pandas to load large `.csv` or `.json` song databases.
* 🌈 Web version (Flask/React) or mobile app for wider use.

---

## 🤝 Contributing

Pull requests, new vibes, or additional curated songs are always welcome! Drop your playlist ideas or suggestions in the Issues section.

---

## 👤 Author

**Kartavya V Gupta** — Developer, Designer, Dreamer 🌟

---

## 📄 License

This project is open-source and free to use under the MIT License.

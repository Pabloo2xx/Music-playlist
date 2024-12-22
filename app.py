from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

playlist = []

@app.route("/")
def home():
    """Homepage to display the playlist."""
    return render_template("index.html", playlist=playlist)

@app.route("/add", methods=["POST"])
def add_song():
    """Add a song to the playlist."""
    song_name = request.form.get("song_name")
    artist_name = request.form.get("artist_name")

    if song_name and artist_name:
        playlist.append({"name": song_name, "artist": artist_name})

    return redirect(url_for("home"))

@app.route("/remove/<int:song_index>", methods=["POST"])
def remove_song(song_index):
    """Remove a song from the playlist by index."""
    if 0 <= song_index < len(playlist):
        playlist.pop(song_index)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)

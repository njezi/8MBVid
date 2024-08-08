# 8MBVid
A simple Flask app to compress videos to 8MB, perfect for uploading files on Discord.\
This is an alternative to https://8mb.video/

# Features
- Compress videos to a maximum of 8MB
- Built with Flask for easy deployment and integration
- Upload and compress videos through a user-friendly web interface
- Files are automatically removed after 5 minutes to save space

# How to use
1. Clone this repository
```
git clone https://github.com/njezi/8MBVid
cd 8MBVid
```
2. Install and add FFmpeg to PATH
3. Install Flask
```
pip install flask
```
4. Run `app.py`
```
python3 app.py
```
5. Go to `http://127.0.0.1:5000/` and start using the tool.

# System Requirements
You don't need a very strong device, but I suggest using something that has a good CPU,
otherwise you may need to wait a long time for one video to compress.

# TODO
- [x] Optimize File Cleanup
- [ ] Make managing settings easier
- [ ] Add an option to change output file size
- [ ] Make the UI look better
- [ ] Improve Compression Settings

# Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or improvements.
pyinstaller --onedir --windowed --add-binary "ffmpeg:ffmpeg" yd-ui.py
hdiutil create -volname "yd-ui" -srcfolder dist/yd-ui.app -srcfolder dist/yd-ui -ov -format UDZO dist/yd-ui.dmg
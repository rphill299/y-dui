pyinstaller --onedir --windowed --add-binary "ffmpeg:ffmpeg" main.py
hdiutil create -volname "y-dui" -srcfolder dist/main.app -srcfolder dist/main -ov -format UDZO dist/y-dui.dmg
#!/bin/bash

APP_NAME="personnel-management-system"
VERSION="1.0.0"
APPDIR="build/AppDir"
mkdir -p $APPDIR/usr/bin

# Copy app
cp app.py $APPDIR/usr/bin/$APP_NAME
echo -e '#!/bin/bash\npython3 /usr/bin/$APP_NAME' > $APPDIR/AppRun
chmod +x $APPDIR/AppRun

# Create desktop entry
mkdir -p $APPDIR/usr/share/applications
cat <<EOF > $APPDIR/usr/share/applications/$APP_NAME.desktop
[Desktop Entry]
Name=Personnel Management System
Exec=AppRun
Icon=app
Type=Application
Categories=Utility;
EOF

# Download appimagetool if not present
if [ ! -f ./appimagetool ]; then
    wget https://github.com/AppImage/AppImageKit/releases/latest/download/appimagetool-x86_64.AppImage -O appimagetool
    chmod +x appimagetool
fi

# Build AppImage
./appimagetool $APPDIR build/$APP_NAME-$VERSION.AppImage
echo "AppImage created at build/$APP_NAME-$VERSION.AppImage"

#!/bin/bash

APP_NAME="personnel-management-system"
VERSION="1.0.0"
BUILD_DIR="build/$APP_NAME-$VERSION"
DEB_DIR="$BUILD_DIR/DEB"
APPIMG_DIR="$BUILD_DIR/AppImage"

# Clean build dir
rm -rf $BUILD_DIR
mkdir -p $DEB_DIR/opt/$APP_NAME
mkdir -p $DEB_DIR/DEBIAN

# Copy app files
cp -r app.py requirements.txt $DEB_DIR/opt/$APP_NAME
echo '#!/bin/bash\npython3 /opt/$APP_NAME/app.py' > $DEB_DIR/opt/$APP_NAME/start.sh
chmod +x $DEB_DIR/opt/$APP_NAME/start.sh

# Create control file
cat <<EOF > $DEB_DIR/DEBIAN/control
Package: $APP_NAME
Version: $VERSION
Architecture: all
Maintainer: ParaCryptid Team
Description: Secure Personnel Management System for field and remote ops.
EOF

# Build .deb
dpkg-deb --build $DEB_DIR build/$APP_NAME-$VERSION.deb

# AppImage build placeholder
mkdir -p $APPIMG_DIR
cp app.py $APPIMG_DIR/
echo "AppImage build coming soon..."

echo "Build complete. Files in build/"

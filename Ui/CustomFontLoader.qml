// CustomFontLoader.qml

import QtQuick

// Load your custom font from a resource path
FontLoader {
    id: customFontLoader
    source: "qrc:/fonts/helvetica-bold-3-2_ufonts.com.ttf"
}

Label {
    text: "Hello Custom Font!"
    font.family: customFontLoader.name // Use the name from the FontLoader
    font.pointSize: 18
}


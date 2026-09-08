/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/

import QtQuick
import QtQuick.Controls

Item {
    id: root
    width: 1920
    height: 1080

    Pane {
        id: pane
        x: 705
        y: 419
        width: 200
        height: 200

        TextArea {
            id: textArea
            x: -12
            y: -12
            width: 120
            height: 59
            text: "Appearance"
            font.italic: true
            font.family: "Segoe UI"
            placeholderText: qsTr("Text Area")
        }
    }
}

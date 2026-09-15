import QtQuick
import QtQuick.Layouts
import Ui

// Title + subtitle used at the top of each page.
ColumnLayout {
    id: root

    property string title: ""
    property string subtitle: ""

    spacing: 2

    Text {
        text: root.title
        font: Constants.largeFont
        color: Constants.textColor
    }

    Text {
        visible: root.subtitle.length > 0
        text: root.subtitle
        font: Constants.smallFont
        color: Constants.mutedTextColor
        wrapMode: Text.WordWrap
        Layout.fillWidth: true
    }
}

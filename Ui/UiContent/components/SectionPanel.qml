import QtQuick
import QtQuick.Layouts
import Ui

// Plain bordered box used to group related controls (filters, settings, etc.).
Rectangle {
    id: root

    default property alias content: contentColumn.children
    property string title: ""

    color: "transparent"
    border.width: 1
    border.color: Constants.borderColor
    implicitHeight: contentColumn.implicitHeight + Constants.spacingM * 2

    ColumnLayout {
        id: contentColumn
        anchors.fill: parent
        anchors.margins: Constants.spacingM
        spacing: Constants.spacingS

        Text {
            visible: root.title.length > 0
            text: root.title
            font.family: Constants.font.family
            font.pixelSize: Constants.font.pixelSize
            font.bold: true
            color: Constants.textColor
        }
    }
}

import QtQuick
import QtQuick.Layouts
import Ui

// Left-hand navigation list. Emits `destinationSelected(index)` when the
// user picks a different page.
Rectangle {
    id: root

    property var destinations: []
    property int currentIndex: 0

    signal destinationSelected(int index)

    color: Constants.backgroundColor
    border.width: 1
    border.color: Constants.borderColor

    ColumnLayout {
        anchors.fill: parent
        anchors.margins: Constants.spacingM
        spacing: Constants.spacingS

        Repeater {
            model: root.destinations

            delegate: Text {
                required property var modelData
                required property int index

                Layout.fillWidth: true
                text: modelData
                font.family: Constants.font.family
                font.pixelSize: Constants.font.pixelSize
                font.bold: root.currentIndex === index
                color: Constants.textColor

                MouseArea {
                    anchors.fill: parent
                    cursorShape: Qt.PointingHandCursor
                    onClicked: root.destinationSelected(index)
                }
            }
        }

        Item { Layout.fillHeight: true }
    }
}

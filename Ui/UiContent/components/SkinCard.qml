import QtQuick
import QtQuick.Layouts
import Ui

// Row for displaying a single skin, with a small preview image alongside
// the text details. Takes plain properties rather than a backend model
// object, so it can be used with static design-time data. `imageSource`
// is optional - leave it unset to show an empty placeholder box.
Rectangle {
    id: root

    property string skinName: "Skin Name"
    property string weaponName: "Weapon"
    property string wear: "Field-Tested"
    property string rarity: "Mil-Spec"
    property url imageSource: ""

    implicitWidth: 240
    implicitHeight: Math.max(contentRow.implicitHeight, 40) + Constants.spacingM * 2
    color: "transparent"
    border.width: 1
    border.color: Constants.borderColor

    RowLayout {
        id: contentRow
        anchors.fill: parent
        anchors.margins: Constants.spacingM
        spacing: Constants.spacingM

        Rectangle {
            id: imageBox
            Layout.preferredWidth: 40
            Layout.preferredHeight: 40
            Layout.alignment: Qt.AlignTop
            color: Constants.surfaceColor
            border.width: 1
            border.color: Constants.borderColor
            clip: true

            Image {
                anchors.fill: parent
                anchors.margins: 2
                source: root.imageSource
                fillMode: Image.PreserveAspectFit
                visible: root.imageSource.toString().length > 0
            }
        }

        ColumnLayout {
            Layout.fillWidth: true
            spacing: 2

            Text {
                Layout.fillWidth: true
                text: root.weaponName
                font: Constants.smallFont
                color: Constants.mutedTextColor
                elide: Text.ElideRight
            }

            Text {
                Layout.fillWidth: true
                text: root.skinName
                font: Constants.font
                color: Constants.textColor
                elide: Text.ElideRight
            }

            Text {
                Layout.fillWidth: true
                text: root.wear + " · " + root.rarity
                font: Constants.smallFont
                color: Constants.mutedTextColor
                elide: Text.ElideRight
            }
        }
    }
}

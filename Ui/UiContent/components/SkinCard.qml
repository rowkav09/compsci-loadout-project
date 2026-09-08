import QtQuick
import QtQuick.Layouts
import Ui

// Plain row for displaying a single skin. Takes plain properties rather
// than a backend model object, so it can be used with static design-time
// data.
Rectangle {
    id: root

    property string skinName: "Skin Name"
    property string weaponName: "Weapon"
    property string wear: "Field-Tested"
    property string rarity: "Mil-Spec"

    implicitWidth: 220
    implicitHeight: contentColumn.implicitHeight + Constants.spacingM * 2
    color: "transparent"
    border.width: 1
    border.color: Constants.borderColor

    ColumnLayout {
        id: contentColumn
        anchors.fill: parent
        anchors.margins: Constants.spacingM
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

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/

import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import Ui
import "../components"

Item {
    id: root
    width: 1920
    height: 1080

    property var loadoutResults: []

    function findSkin(weaponName, finishName) {
        var results = skinsController.search(weaponName, finishName, "", "")
        return results.length > 0 ? results[0] : {}
    }

    Component.onCompleted: loadoutResults = [
        findSkin("AK-47", "Redline"),
        findSkin("M4A4", "Asiimov"),
        findSkin("Desert Eagle", "Blaze"),
        findSkin("Karambit", "Doppler")
    ]

    ScrollView {
        anchors.fill: parent
        contentWidth: availableWidth
        clip: true

        ColumnLayout {
            width: parent.width
            spacing: Constants.spacingL

            RowLayout {
                Layout.fillWidth: true
                Layout.margins: Constants.spacingL

                PageHeader {
                    title: "Loadout Generator"
                    subtitle: "Randomly generate a full loadout from the local skins dataset."
                    Layout.fillWidth: true
                }

                Button {
                    text: "Generate Loadout"
                    font: Constants.font
                    background: Rectangle {
                        color: Constants.surfaceColor
                        border.color: Constants.borderColor
                        radius: Constants.radius
                    }
                }
            }

            SectionPanel {
                Layout.fillWidth: true
                Layout.leftMargin: Constants.spacingL
                Layout.rightMargin: Constants.spacingL
                title: "Filters"

                RowLayout {
                    Layout.fillWidth: true
                    spacing: Constants.spacingM

                    ComboBox {
                        Layout.preferredWidth: 160
                        model: ["Any Rarity", "Mil-Spec", "Restricted", "Classified", "Covert"]
                        font: Constants.font
                        background: Rectangle {
                            color: Constants.surfaceColor
                            border.color: Constants.borderColor
                            radius: Constants.radius
                        }
                    }

                    ComboBox {
                        Layout.preferredWidth: 160
                        model: ["Any Wear", "Factory New", "Minimal Wear", "Field-Tested", "Well-Worn", "Battle-Scarred"]
                        font: Constants.font
                        background: Rectangle {
                            color: Constants.surfaceColor
                            border.color: Constants.borderColor
                            radius: Constants.radius
                        }
                    }

                    Item { Layout.fillWidth: true }
                }
            }

            Flow {
                Layout.fillWidth: true
                Layout.leftMargin: Constants.spacingL
                Layout.rightMargin: Constants.spacingL
                Layout.bottomMargin: Constants.spacingL
                spacing: Constants.spacingM

                Repeater {
                    model: root.loadoutResults

                    delegate: SkinCard {
                        weaponName: modelData.weapon_name || "Unknown weapon"
                        skinName: modelData.name || "Unknown skin"
                        wear: ["Field-Tested", "Well-Worn", "Factory New", "Factory New"][index]
                        rarity: modelData.rarity || "Unknown"
                        imageSource: modelData.image || ""
                    }
                }
            }
        }
    }
}

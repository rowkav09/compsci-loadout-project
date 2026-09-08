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

// Design-time layout only: the loadout slots below use static sample data
// and are not wired to the skins repository / controller yet.
Item {
    id: root
    width: 1920
    height: 1080

    ListModel {
        id: sampleLoadout

        ListElement { weaponName: "AK-47"; skinName: "Redline"; wear: "Field-Tested"; rarity: "Classified" }
        ListElement { weaponName: "M4A4"; skinName: "Asiimov"; wear: "Well-Worn"; rarity: "Covert" }
        ListElement { weaponName: "Desert Eagle"; skinName: "Blaze"; wear: "Factory New"; rarity: "Restricted" }
        ListElement { weaponName: "Karambit"; skinName: "Doppler"; wear: "Factory New"; rarity: "Covert" }
    }

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
                    }

                    ComboBox {
                        Layout.preferredWidth: 160
                        model: ["Any Wear", "Factory New", "Minimal Wear", "Field-Tested", "Well-Worn", "Battle-Scarred"]
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
                    model: sampleLoadout

                    delegate: SkinCard {
                        weaponName: model.weaponName
                        skinName: model.skinName
                        wear: model.wear
                        rarity: model.rarity
                    }
                }
            }
        }
    }
}
